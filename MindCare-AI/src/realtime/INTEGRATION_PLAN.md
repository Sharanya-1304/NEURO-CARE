# Integration Plan (Real-time Assessment)

This plan plugs A (questionnaire) and B (behavior inference) into the project.

## A) Questionnaire pipeline

1. Collect PHQ-9, GAD-7, DASS-21 items.
2. Score with questionnaire.py.
3. Store summary and severity tags.

## B) Behavior-inference pipeline

1. Audio: extract pitch/energy/rate/pause (librosa or torchaudio).
2. Video: extract emotions and gaze metrics (mediapipe/deepface).
3. Typing: capture timing and backspaces (frontend JS).
4. Cognitive: reaction-time tasks (frontend JS).

## Fusion

- Weighted fusion in runtime.py.
- Track trends over time in a small datastore (CSV or SQLite).

## Ethics

- Always show the disclaimer before results.
- Provide escalation links for high-risk flags.
