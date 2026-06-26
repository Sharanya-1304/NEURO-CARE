from typing import Dict, List, Tuple


def score_phq9(items: List[int]) -> int:
    if len(items) != 9:
        raise ValueError("PHQ-9 requires 9 items")
    return int(sum(items))


def score_gad7(items: List[int]) -> int:
    if len(items) != 7:
        raise ValueError("GAD-7 requires 7 items")
    return int(sum(items))


def score_dass21(items: List[int]) -> Tuple[int, int, int]:
    if len(items) != 21:
        raise ValueError("DASS-21 requires 21 items")
    # Indices are 0-based for depression, anxiety, stress subscales
    depression_idx = [2, 4, 9, 12, 15, 16, 20]
    anxiety_idx = [1, 3, 6, 8, 14, 18, 19]
    stress_idx = [0, 5, 7, 10, 11, 13, 17]
    depression = sum(items[i] for i in depression_idx)
    anxiety = sum(items[i] for i in anxiety_idx)
    stress = sum(items[i] for i in stress_idx)
    return int(depression), int(anxiety), int(stress)


def phq9_severity(score: int) -> str:
    if score <= 4:
        return "minimal"
    if score <= 9:
        return "mild"
    if score <= 14:
        return "moderate"
    if score <= 19:
        return "moderately_severe"
    return "severe"


def gad7_severity(score: int) -> str:
    if score <= 4:
        return "minimal"
    if score <= 9:
        return "mild"
    if score <= 14:
        return "moderate"
    return "severe"


def dass21_severity(score: int, scale: str) -> str:
    # Simplified cutoffs for demonstration
    if scale == "depression":
        if score <= 4:
            return "normal"
        if score <= 6:
            return "mild"
        if score <= 10:
            return "moderate"
        if score <= 13:
            return "severe"
        return "extremely_severe"
    if scale == "anxiety":
        if score <= 3:
            return "normal"
        if score <= 5:
            return "mild"
        if score <= 7:
            return "moderate"
        if score <= 9:
            return "severe"
        return "extremely_severe"
    if score <= 7:
        return "normal"
    if score <= 9:
        return "mild"
    if score <= 12:
        return "moderate"
    if score <= 16:
        return "severe"
    return "extremely_severe"


def questionnaire_features(phq9: int, gad7: int, dass21: Dict[str, int]) -> Dict[str, float]:
    return {
        "phq9": float(phq9),
        "gad7": float(gad7),
        "dass21_depression": float(dass21["depression"]),
        "dass21_anxiety": float(dass21["anxiety"]),
        "dass21_stress": float(dass21["stress"]),
    }
