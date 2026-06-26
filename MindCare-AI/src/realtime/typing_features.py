from typing import Dict


def typing_stress_score(features: Dict[str, float]) -> float:
    cpm = features.get("chars_per_min", 200.0)
    backspace = features.get("backspace_ratio", 0.05)
    pause = features.get("pause_ratio", 0.1)

    speed_score = min(max((260 - cpm) * 0.2, 0.0), 30.0)
    backspace_score = min(max(backspace * 200, 0.0), 40.0)
    pause_score = min(max((pause - 0.1) * 200, 0.0), 30.0)

    return float(min(speed_score + backspace_score + pause_score, 100.0))


def typing_depression_score(features: Dict[str, float]) -> float:
    cpm = features.get("chars_per_min", 200.0)
    pause = features.get("pause_ratio", 0.1)

    speed_score = min(max((220 - cpm) * 0.25, 0.0), 60.0)
    pause_score = min(max((pause - 0.1) * 200, 0.0), 40.0)

    return float(min(speed_score + pause_score, 100.0))
