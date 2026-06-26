from typing import Dict, List


def weighted_fusion(scores: Dict[str, float], weights: Dict[str, float]) -> float:
    total_weight = sum(weights.values()) or 1.0
    total = 0.0
    for key, weight in weights.items():
        total += scores.get(key, 0.0) * weight
    return total / total_weight


def build_flags(depression: float, stress: float, anxiety: float) -> List[str]:
    flags = []
    if depression >= 70.0:
        flags.append("high_depression_risk")
    if stress >= 70.0:
        flags.append("high_stress")
    if anxiety >= 70.0:
        flags.append("high_anxiety")
    return flags
