"""Learnova data loading utilities."""

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_profiles():
    return pd.read_csv(DATA_DIR / "learner_profiles.csv")

def load_activity():
    return pd.read_csv(DATA_DIR / "learner_activity.csv")

def load_assessments():
    return pd.read_csv(DATA_DIR / "assessments.csv")

def load_resources():
    return pd.read_csv(DATA_DIR / "resources.csv")

if __name__ == "__main__":
    print("Profiles:", load_profiles().shape)
    print("Activity:", load_activity().shape)
    print("Assessments:", load_assessments().shape)
    print("Resources:", load_resources().shape)
