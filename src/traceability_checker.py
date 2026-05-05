import pandas as pd


def load_requirements(file_path):
    return pd.read_csv(file_path)


def check_traceability(df):
    report = {}

    report["missing_design"] = df[df["Design"].isna()]
    report["missing_verification"] = df[df["Verification"].isna()]
    report["missing_test_case"] = df[df["TestCase"].isna()]

    total = len(df)
    complete = df.dropna().shape[0]

    report["coverage"] = complete / total if total > 0 else 0

    return report


def generate_summary(report):
    summary = f"""
Traceability Report

Missing Design Links: {len(report["missing_design"])}
Missing Verification Methods: {len(report["missing_verification"])}
Missing Test Cases: {len(report["missing_test_case"])}

Coverage: {report["coverage"]*100:.2f}%
"""
    return summary
