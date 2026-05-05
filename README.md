# AI Requirement Traceability Checker

![CI](https://github.com/Aria-Yao6688/ai-requirement-traceability-checker/actions/workflows/ci.yml/badge.svg)
## Overview

This project implements an AI-assisted requirement traceability checker for systems engineering workflows. It analyzes requirement datasets and identifies missing links between requirements, design, verification, and test cases.

The goal is to improve traceability coverage and support quality assurance in engineering projects.

---

## Features

- Detect missing design links
- Detect missing verification methods
- Detect missing test cases
- Compute traceability coverage
- Generate summary reports

---

## Project Structure
```
ai-requirement-traceability-checker/
│
├── src/
│ └── traceability_checker.py
│
├── tests/
│ └── test_traceability_checker.py
│
├── data/
│ └── sample_requirements.csv
│
├── .github/workflows/
│ └── ci.yml
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Aria-Yao6688/ai-requirement-traceability-checker.git
cd ai-requirement-traceability-checker
pip install -r requirements.txt
```
## Usage

Run the traceability checker:
```python
from src.traceability_checker import load_requirements, check_traceability

df = load_requirements("data/sample_requirements.csv")
report = check_traceability(df)

print(report)
```
## Testing

Run tests using:

```bash
pytest
```
Continuous integration is configured using GitHub Actions.
## Results

The system identifies incomplete traceability and calculates coverage metrics, helping engineers detect gaps early in the development lifecycle.
## Reflection

This project demonstrates how AI-assisted coding tools can accelerate development while maintaining engineering rigor. Challenges included debugging CI pipelines and ensuring consistent project structure. Integrating automated testing and CI improved reliability and reproducibility.
## Author

Aria Yao
