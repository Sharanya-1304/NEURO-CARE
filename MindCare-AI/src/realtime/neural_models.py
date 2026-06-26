from math import exp
from typing import Dict, List


def _sigmoid(value: float) -> float:
    return 1.0 / (1.0 + exp(-value))


def _clamp_score(value: float) -> float:
    return round(max(0.0, min(value, 100.0)), 2)


class BehavioralANN:
    """Small ANN-style scorer for tabular wellness signals."""

    def predict(self, features: Dict[str, float]) -> Dict[str, float]:
        sleep = float(features.get("sleep_hours", 7.0))
        anxiety = float(features.get("anxiety", 5.0))
        social = float(features.get("social_activity", 3.0))
        study = float(features.get("study_pressure", 3.0))
        work = float(features.get("work_pressure", 2.0))
        financial = float(features.get("financial_stress", 3.0))

        stress_logit = -2.1 + anxiety * 0.28 + study * 0.22 + work * 0.2 + financial * 0.16
        depression_logit = -1.8 + max(0, 7 - sleep) * 0.32 + max(0, 4 - social) * 0.24 + anxiety * 0.13
        anxiety_logit = -2.0 + anxiety * 0.36 + work * 0.12 + financial * 0.16

        return {
            "ann_stress": _clamp_score(_sigmoid(stress_logit) * 100),
            "ann_depression": _clamp_score(_sigmoid(depression_logit) * 100),
            "ann_anxiety": _clamp_score(_sigmoid(anxiety_logit) * 100),
        }


class MicroExpressionCNN:
    """CNN-style scorer for spatial facial and posture cues."""

    def predict(self, features: Dict[str, float]) -> Dict[str, float]:
        sadness = float(features.get("sadness", 0.0))
        anger = float(features.get("anger", 0.0))
        fear = float(features.get("fear", 0.0))
        neutral = float(features.get("neutral", 0.0))
        gaze = float(features.get("gaze_avoidance", 0.0))
        blink = float(features.get("blink_rate_per_min", 20.0))
        posture = float(features.get("posture_slouch", 0.0))
        movement = float(features.get("movement_energy", 0.5))

        blink_instability = min(abs(blink - 20.0) / 20.0, 1.0)
        flat_affect = min(neutral * 0.6 + max(0.0, 0.45 - movement), 1.0)

        return {
            "cnn_stress": _clamp_score(anger * 34 + fear * 28 + gaze * 20 + blink_instability * 18),
            "cnn_depression": _clamp_score(sadness * 36 + flat_affect * 28 + posture * 20 + gaze * 16),
            "cnn_anxiety": _clamp_score(fear * 40 + gaze * 24 + blink_instability * 20 + anger * 16),
        }


class TemporalBehaviorRNN:
    """RNN-style scorer for sequential typing/reaction patterns."""

    def predict(self, sequence: List[Dict[str, float]]) -> Dict[str, float]:
        if not sequence:
            return {"rnn_stress": 0.0, "rnn_depression": 0.0, "rnn_anxiety": 0.0}

        hidden_stress = 0.0
        hidden_depression = 0.0
        hidden_anxiety = 0.0

        for step in sequence[-20:]:
            pause = float(step.get("pause_ms", 0.0)) / 1000.0
            backspace = float(step.get("backspace", 0.0))
            reaction = float(step.get("reaction_ms", 350.0))
            error = float(step.get("error", 0.0))

            hidden_stress = 0.72 * hidden_stress + 0.22 * min(pause, 2.5) + 0.2 * backspace + 0.25 * error
            hidden_depression = 0.76 * hidden_depression + 0.3 * min(pause, 3.0) + 0.001 * max(0.0, reaction - 350)
            hidden_anxiety = 0.68 * hidden_anxiety + 0.18 * backspace + 0.25 * error + 0.001 * max(0.0, reaction - 300)

        return {
            "rnn_stress": _clamp_score(hidden_stress * 35),
            "rnn_depression": _clamp_score(hidden_depression * 30),
            "rnn_anxiety": _clamp_score(hidden_anxiety * 32),
        }


def neural_behavior_scores(payload: Dict[str, object]) -> Dict[str, float]:
    questionnaire = payload.get("questionnaire", {}) or {}
    video = payload.get("video", {}) or {}
    typing = payload.get("typing", {}) or {}
    cognitive = payload.get("cognitive", {}) or {}

    tabular_features = {
        "sleep_hours": questionnaire.get("sleep_hours", payload.get("Sleep_Hours", 7.0)),
        "anxiety": questionnaire.get("anxiety", payload.get("Anxiety", 5.0)),
        "social_activity": questionnaire.get("social_activity", payload.get("Social_Activity", 3.0)),
        "study_pressure": questionnaire.get("study_pressure", payload.get("Study_Pressure", 3.0)),
        "work_pressure": questionnaire.get("work_pressure", payload.get("Work_Pressure", 2.0)),
        "financial_stress": questionnaire.get("financial_stress", payload.get("Financial_Stress", 3.0)),
    }

    sequence = payload.get("behavior_sequence") or [
        {
            "pause_ms": float(typing.get("average_pause_ms", typing.get("pause_ratio", 0.1) * 1000)),
            "backspace": float(typing.get("backspace_ratio", 0.05)),
            "reaction_ms": float(cognitive.get("reaction_time_ms", 350.0)),
            "error": float(cognitive.get("error_rate", 0.05)),
        }
    ]

    scores = {}
    scores.update(BehavioralANN().predict(tabular_features))
    scores.update(MicroExpressionCNN().predict(video))
    scores.update(TemporalBehaviorRNN().predict(sequence))
    return scores
