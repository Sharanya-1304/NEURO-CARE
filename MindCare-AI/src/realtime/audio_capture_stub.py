"""Audio capture placeholder.

This file outlines where real-time audio capture should go.
Use a separate service or frontend recording and send features to backend.
"""


def extract_audio_features_stub() -> dict:
    # Replace with real feature extraction in production.
    return {
        "pitch_mean_hz": 150.0,
        "energy_rms": 0.06,
        "speech_rate_wpm": 120.0,
        "pause_ratio": 0.18,
    }
