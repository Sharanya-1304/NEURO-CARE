from .runtime import assess
from .sample_payloads import SAMPLE_PAYLOAD


def main() -> None:
    result = assess(SAMPLE_PAYLOAD)
    print("Real-time assessment demo")
    print("===========================")
    print(f"Depression score: {result['depression_score']}")
    print(f"Stress score: {result['stress_score']}")
    print(f"Anxiety score: {result['anxiety_score']}")
    print(f"Flags: {', '.join(result['flags']) if result['flags'] else 'none'}")
    print(result["disclaimer"])


if __name__ == "__main__":
    main()
