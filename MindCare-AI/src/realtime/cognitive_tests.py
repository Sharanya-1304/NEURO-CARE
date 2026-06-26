from typing import Dict


def cognitive_stress_score(features: Dict[str, float]) -> float:
    rt = features.get("reaction_time_ms", 350.0)
    error = features.get("error_rate", 0.05)

    rt_score = min(max((rt - 300) * 0.2, 0.0), 60.0)
    err_score = min(max(error * 300, 0.0), 40.0)

    return float(min(rt_score + err_score, 100.0))


def cognitive_depression_score(features: Dict[str, float]) -> float:
    rt = features.get("reaction_time_ms", 350.0)
    error = features.get("error_rate", 0.05)

    rt_score = min(max((rt - 320) * 0.2, 0.0), 50.0)
    err_score = min(max(error * 200, 0.0), 50.0)

    return float(min(rt_score + err_score, 100.0))
