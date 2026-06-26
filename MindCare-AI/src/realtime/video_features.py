from typing import Dict


def video_stress_score(features: Dict[str, float]) -> float:
    anger = features.get("anger", 0.0)
    gaze = features.get("gaze_avoidance", 0.0)
    blink = features.get("blink_rate_per_min", 20.0)

    anger_score = min(max(anger * 40, 0.0), 40.0)
    gaze_score = min(max(gaze * 30, 0.0), 30.0)
    blink_score = min(max((blink - 20.0) * 1.5, 0.0), 30.0)

    return float(min(anger_score + gaze_score + blink_score, 100.0))


def video_depression_score(features: Dict[str, float]) -> float:
    sadness = features.get("sadness", 0.0)
    neutral = features.get("neutral", 0.0)
    gaze = features.get("gaze_avoidance", 0.0)

    sadness_score = min(max(sadness * 50, 0.0), 50.0)
    flat_score = min(max(neutral * 30, 0.0), 30.0)
    gaze_score = min(max(gaze * 20, 0.0), 20.0)

    return float(min(sadness_score + flat_score + gaze_score, 100.0))
