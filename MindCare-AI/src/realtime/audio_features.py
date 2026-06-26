from typing import Dict


def audio_stress_score(features: Dict[str, float]) -> float:
    pitch = features.get("pitch_mean_hz", 150.0)
    energy = features.get("energy_rms", 0.05)
    rate = features.get("speech_rate_wpm", 120.0)
    pause = features.get("pause_ratio", 0.15)

    # Heuristic scoring in 0..100
    pitch_score = min(max((pitch - 120) * 0.2, 0.0), 20.0)
    energy_score = min(max((0.2 - energy) * 200, 0.0), 20.0)
    rate_score = min(max((rate - 110) * 0.2, 0.0), 20.0)
    pause_score = min(max((pause - 0.12) * 200, 0.0), 40.0)

    return float(min(pitch_score + energy_score + rate_score + pause_score, 100.0))


def audio_depression_score(features: Dict[str, float]) -> float:
    energy = features.get("energy_rms", 0.05)
    rate = features.get("speech_rate_wpm", 120.0)
    pause = features.get("pause_ratio", 0.15)

    energy_score = min(max((0.15 - energy) * 300, 0.0), 50.0)
    rate_score = min(max((120 - rate) * 0.5, 0.0), 30.0)
    pause_score = min(max((pause - 0.15) * 200, 0.0), 20.0)

    return float(min(energy_score + rate_score + pause_score, 100.0))
