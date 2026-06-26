# Real-time Assessment (A + B)

This package adds two assessment modes:

A) Questionnaire-based screening (PHQ-9, GAD-7, DASS-21)
B) Behavior-inference signals (audio, video, typing, cognitive tests)

Disclaimer: This is a supportive, non-diagnostic tool. It does not replace
professional medical advice.

## Quick demo

Run the demo to see the combined scoring pipeline:

```
python src/realtime/cli_demo.py
```

## Package layout

- questionnaire.py: validated scale scoring
- audio_features.py: audio signal heuristics (accepts extracted features)
- video_features.py: facial and gaze heuristics (accepts extracted features)
- typing_features.py: typing rhythm heuristics
- cognitive_tests.py: reaction-time and error heuristics
- fusion.py: combine signals into final scores
- runtime.py: orchestrator for a single assessment payload
- sample_payloads.py: sample inputs for demos
