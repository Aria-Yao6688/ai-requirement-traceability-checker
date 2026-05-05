from src.traceability_checker import load_requirements, check_traceability

def test_traceability():
    df = load_requirements("data/sample_requirements.csv")
    report = check_traceability(df)

    assert report["coverage"] < 1
    assert len(report["missing_design"]) > 0
    assert len(report["missing_verification"]) > 0
    assert len(report["missing_test_case"]) > 0
