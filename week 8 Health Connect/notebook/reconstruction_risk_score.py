"""
HealthConnect - Semaine 7 - Piste Data Analytics
Tests 1, 3 et 5 : reconstruction du risk_score, stabilite, validite par segment.

Entree : HealthConnect_Appointment_Data_cleaned_S6.csv
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

DATA_PATH = "HealthConnect_Appointment_Data_cleaned_S6.csv"


def load_and_build_risk_score(path=DATA_PATH):
    """Charge les donnees et reconstruit les 4 facteurs binaires + le risk_score (0-4)."""
    df = pd.read_csv(path)
    df["no_show"] = (df["appointment_outcome"] == "No-Show").astype(int)

    df["f_delay"] = (df["booking_lead_days"] > 30).astype(int)
    df["f_antecedent"] = (df["previous_no_shows"] > 0).astype(int)
    df["f_distance"] = (df["distance_to_clinic_km"] > 20).astype(int)
    df["f_no_reminder"] = (df["reminder_sent"] == "No").astype(int)

    df["risk_score"] = (
        df["f_delay"] + df["f_antecedent"] + df["f_distance"] + df["f_no_reminder"]
    )
    return df


def test_1_reconstruction(df):
    """Test 1 : le gradient reconstruit doit correspondre a celui documente en S6
    (31,4% -> 71,1% de no-show, n=370 / 7,4% du volume, pour 3 facteurs)."""
    print("=== Test 1 : reconstruction du risk_score ===")
    summary = df.groupby("risk_score")["no_show"].agg(["mean", "count"])
    summary["pct_volume"] = summary["count"] / len(df) * 100
    print(summary.round(4))
    print()


def test_3_stability(df, seeds=(1, 42, 99)):
    """Test 3 : stabilite du risk_score comme predicteur unique sur plusieurs
    decoupages aleatoires differents (regression logistique)."""
    print("=== Test 3 : stabilite sur 3 decoupages aleatoires ===")
    X = df[["risk_score"]]
    y = df["no_show"]
    for seed in seeds:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=seed, stratify=y
        )
        model = LogisticRegression()
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        proba = model.predict_proba(X_test)[:, 1]
        acc = accuracy_score(y_test, pred)
        auc = roc_auc_score(y_test, proba)
        print(f"seed={seed} : accuracy={acc:.3f} | AUC={auc:.3f}")
    print()


def test_5_segment_validity(df, min_n=50):
    """Test 5 : le gradient du risk_score doit rester croissant a l'interieur
    de chaque segment de type de rendez-vous (pas un artefact d'un seul type)."""
    print("=== Test 5 : validite du gradient par segment (appointment_type) ===")
    for atype in df["appointment_type"].unique():
        sub = df[df["appointment_type"] == atype]
        if len(sub) < min_n:
            continue
        g = sub.groupby("risk_score")["no_show"].agg(["mean", "count"])
        print(f"\n-- {atype} (n={len(sub)}) --")
        print(g.round(4))


if __name__ == "__main__":
    data = load_and_build_risk_score()
    test_1_reconstruction(data)
    test_3_stability(data)
    test_5_segment_validity(data)
