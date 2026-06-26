from typing import Dict

from .audio_features import audio_depression_score, audio_stress_score
from .cognitive_tests import cognitive_depression_score, cognitive_stress_score
from .fusion import build_flags, weighted_fusion
from .neural_models import neural_behavior_scores
from .text_emotion import analyze_text_emotion
from .typing_features import typing_depression_score, typing_stress_score
from .video_features import video_depression_score, video_stress_score


def assess(payload: Dict[str, Dict[str, float]]) -> Dict[str, object]:
    # Questionnaire scores are treated as primary signals
    q = payload.get("questionnaire", {})
    phq9 = float(q.get("phq9", 0.0))
    gad7 = float(q.get("gad7", 0.0))
    dass_dep = float(q.get("dass21_depression", 0.0))
    dass_anx = float(q.get("dass21_anxiety", 0.0))
    dass_str = float(q.get("dass21_stress", 0.0))

    base_dep = min(phq9 * 3.5 + dass_dep * 3.0, 100.0)
    base_anx = min(gad7 * 4.0 + dass_anx * 3.0, 100.0)
    base_str = min(dass_str * 4.0, 100.0)

    audio = payload.get("audio", {})
    video = payload.get("video", {})
    typing = payload.get("typing", {})
    cognitive = payload.get("cognitive", {})
    text_signal = analyze_text_emotion(str(payload.get("journal_text", "")))
    neural_scores = neural_behavior_scores(payload)

    dep_scores = {
        "questionnaire": base_dep,
        "audio": audio_depression_score(audio) if audio else 0.0,
        "video": video_depression_score(video) if video else 0.0,
        "typing": typing_depression_score(typing) if typing else 0.0,
        "cognitive": cognitive_depression_score(cognitive) if cognitive else 0.0,
        "text": float(text_signal["depression_score"]),
        "neural": (
            neural_scores["ann_depression"]
            + neural_scores["cnn_depression"]
            + neural_scores["rnn_depression"]
        )
        / 3,
    }

    str_scores = {
        "questionnaire": base_str,
        "audio": audio_stress_score(audio) if audio else 0.0,
        "video": video_stress_score(video) if video else 0.0,
        "typing": typing_stress_score(typing) if typing else 0.0,
        "cognitive": cognitive_stress_score(cognitive) if cognitive else 0.0,
        "text": float(text_signal["stress_score"]),
        "neural": (
            neural_scores["ann_stress"]
            + neural_scores["cnn_stress"]
            + neural_scores["rnn_stress"]
        )
        / 3,
    }

    anx_scores = {
        "questionnaire": base_anx,
        "audio": audio_stress_score(audio) if audio else 0.0,
        "video": video_stress_score(video) if video else 0.0,
        "typing": typing_stress_score(typing) if typing else 0.0,
        "cognitive": cognitive_stress_score(cognitive) if cognitive else 0.0,
        "text": float(text_signal["anxiety_score"]),
        "neural": (
            neural_scores["ann_anxiety"]
            + neural_scores["cnn_anxiety"]
            + neural_scores["rnn_anxiety"]
        )
        / 3,
    }

    weights = {
        "questionnaire": 0.28,
        "audio": 0.12,
        "video": 0.18,
        "typing": 0.1,
        "cognitive": 0.1,
        "text": 0.12,
        "neural": 0.1,
    }

    depression = weighted_fusion(dep_scores, weights)
    stress = weighted_fusion(str_scores, weights)
    anxiety = weighted_fusion(anx_scores, weights)

    flags = build_flags(depression, stress, anxiety)

    return {
        "depression_score": round(depression, 2),
        "stress_score": round(stress, 2),
        "anxiety_score": round(anxiety, 2),
        "detail": {
            "depression": dep_scores,
            "stress": str_scores,
            "anxiety": anx_scores,
            "text_emotion": text_signal,
            "neural_models": neural_scores,
        },
        "flags": flags,
        "disclaimer": "This system is only for preliminary mental wellness assessment and not a medical diagnosis.",
    }
