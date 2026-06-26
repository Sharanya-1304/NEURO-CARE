from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class QuestionnaireScores:
    phq9: int
    gad7: int
    dass21_depression: int
    dass21_anxiety: int
    dass21_stress: int


@dataclass
class AudioFeatures:
    pitch_mean_hz: float
    energy_rms: float
    speech_rate_wpm: float
    pause_ratio: float


@dataclass
class VideoFeatures:
    sadness: float
    anger: float
    neutral: float
    gaze_avoidance: float
    blink_rate_per_min: float


@dataclass
class TypingFeatures:
    chars_per_min: float
    backspace_ratio: float
    pause_ratio: float


@dataclass
class CognitiveFeatures:
    reaction_time_ms: float
    error_rate: float


@dataclass
class AssessmentInput:
    questionnaire: QuestionnaireScores
    audio: Optional[AudioFeatures] = None
    video: Optional[VideoFeatures] = None
    typing: Optional[TypingFeatures] = None
    cognitive: Optional[CognitiveFeatures] = None


@dataclass
class AssessmentOutput:
    depression_score: float
    stress_score: float
    anxiety_score: float
    detail: Dict[str, float]
    flags: List[str]
