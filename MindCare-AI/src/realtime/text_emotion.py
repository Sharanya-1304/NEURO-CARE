from functools import lru_cache
from typing import Dict, List


NEGATIVE_TERMS = {
    "hopeless",
    "empty",
    "alone",
    "worthless",
    "tired",
    "exhausted",
    "sad",
    "numb",
    "anxious",
    "panic",
    "overwhelmed",
    "stressed",
    "crying",
    "burnout",
    "sleep",
    "can't focus",
}

POSITIVE_TERMS = {
    "calm",
    "okay",
    "better",
    "hopeful",
    "happy",
    "relaxed",
    "confident",
    "supported",
    "peaceful",
}


@lru_cache(maxsize=1)
def _load_huggingface_pipeline():
    try:
        from transformers import pipeline

        return pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None,
        )
    except Exception:
        return None


def _fallback_emotion(text: str) -> List[Dict[str, float]]:
    lowered = text.lower()
    negative_hits = sum(1 for term in NEGATIVE_TERMS if term in lowered)
    positive_hits = sum(1 for term in POSITIVE_TERMS if term in lowered)
    length_factor = min(len(text.split()) / 80, 1.0)

    sadness = min(0.15 + negative_hits * 0.12 + length_factor * 0.1, 0.95)
    fear = min(0.08 + ("anxious" in lowered or "panic" in lowered) * 0.35, 0.75)
    joy = min(0.12 + positive_hits * 0.16, 0.8)
    neutral = max(0.05, 1.0 - sadness - fear - joy)

    return [
        {"label": "sadness", "score": float(sadness)},
        {"label": "fear", "score": float(fear)},
        {"label": "joy", "score": float(joy)},
        {"label": "neutral", "score": float(neutral)},
    ]


def analyze_text_emotion(text: str) -> Dict[str, object]:
    if not text or not text.strip():
        return {
            "provider": "none",
            "emotions": [],
            "depression_score": 0.0,
            "stress_score": 0.0,
            "anxiety_score": 0.0,
            "summary": "No journal text provided.",
        }

    classifier = _load_huggingface_pipeline()
    provider = "huggingface" if classifier else "fallback"

    if classifier:
        raw = classifier(text[:1200])
        emotions = raw[0] if raw and isinstance(raw[0], list) else raw
    else:
        emotions = _fallback_emotion(text)

    normalized = {
        item["label"].lower(): float(item["score"])
        for item in emotions
        if "label" in item and "score" in item
    }

    sadness = normalized.get("sadness", normalized.get("sad", 0.0))
    fear = normalized.get("fear", normalized.get("anxiety", 0.0))
    anger = normalized.get("anger", 0.0)
    joy = normalized.get("joy", normalized.get("happy", 0.0))
    neutral = normalized.get("neutral", 0.0)

    depression_score = min((sadness * 70) + (neutral * 15) + max(0, 0.3 - joy) * 30, 100)
    stress_score = min((anger * 55) + (fear * 45) + (sadness * 25), 100)
    anxiety_score = min((fear * 75) + (anger * 20), 100)

    dominant = max(normalized.items(), key=lambda item: item[1])[0] if normalized else "neutral"

    return {
        "provider": provider,
        "emotions": emotions,
        "depression_score": round(float(depression_score), 2),
        "stress_score": round(float(stress_score), 2),
        "anxiety_score": round(float(anxiety_score), 2),
        "summary": f"Text signal suggests dominant emotion: {dominant}.",
    }
