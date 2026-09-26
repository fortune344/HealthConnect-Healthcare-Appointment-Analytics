"""
HealthConnect - Semaine 7 - Piste Data Analytics
Tests 2, 4, 6 et 7 : le risk_score dans un modele de classification simple,
comparaison avec les facteurs separes, importance relative, continu vs binaire.

Entree : HealthConnect_Appointment_Data_cleaned_S6.csv
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split

DATA_PATH = "HealthConnect_Appointment_Data_cleaned_S6.csv"


def load_data(path=DATA_PATH):
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


def evaluate(X, y, label, seed=42):
    """Entraine une regression logistique et affiche les metriques de test."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed, stratify=y
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, pred)
    prec = precision_score(y_test, pred)
    rec = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    auc = roc_auc_score(y_test, proba)

    print(f"--- {label} (seed={seed}) ---")
    print(f"Accuracy={acc:.3f} | Precision={prec:.3f} | Recall={rec:.3f} | F1={f1:.3f} | AUC={auc:.3f}")
    print()
    return model


def test_2_risk_score_only(df):
    """Test 2 : le risk_score seul comme predicteur, compare a une prediction
    naive (toujours la classe majoritaire)."""
    print("=== Test 2 : risk_score seul vs baseline ===")
    y = df["no_show"]
    baseline = max(y.value_counts(normalize=True))
    print(f"Baseline (classe majoritaire) : {baseline:.3f}\n")
    evaluate(df[["risk_score"]], y, "risk_score seul")


def test_4_score_vs_facteurs(df):
    """Test 4 : risk_score agrege vs les 4 facteurs pris separement."""
    print("=== Test 4 : risk_score agrege vs facteurs separes ===")
    y = df["no_show"]
    evaluate(df[["risk_score"]], y, "risk_score agrege")
    evaluate(df[["f_delay", "f_antecedent", "f_distance", "f_no_reminder"]], y, "4 facteurs separes")


def test_6_importance_facteurs(df):
    """Test 6 : importance relative des 4 facteurs (coefficients / odds ratio)."""
    print("=== Test 6 : importance relative des 4 facteurs ===")
    X = df[["f_delay", "f_antecedent", "f_distance", "f_no_reminder"]]
    y = df["no_show"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    for name, coef in zip(X.columns, model.coef_[0]):
        print(f"  {name}: coef={coef:.3f} | odds ratio={np.exp(coef):.2f}")
    print()


def test_7_continu_vs_binaire(df, seeds=(1, 42, 99)):
    """Test 7 : previous_no_shows en continu vs antecedent en binaire
    (valide la recommandation de la Semaine 6)."""
    print("=== Test 7 : previous_no_shows continu vs f_antecedent binaire ===")
    y = df["no_show"]
    X_bin = df[["f_delay", "f_antecedent", "f_distance", "f_no_reminder"]]
    X_cont = df[["f_delay", "previous_no_shows", "f_distance", "f_no_reminder"]]

    for X, label in [(X_bin, "Binaire (f_antecedent)"), (X_cont, "Continu (previous_no_shows)")]:
        accs, recs, aucs = [], [], []
        for seed in seeds:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.25, random_state=seed, stratify=y
            )
            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, y_train)
            pred = model.predict(X_test)
            proba = model.predict_proba(X_test)[:, 1]
            accs.append(accuracy_score(y_test, pred))
            recs.append(recall_score(y_test, pred))
            aucs.append(roc_auc_score(y_test, proba))
        print(
            f"{label}: accuracy_moy={np.mean(accs):.3f} | recall_moy={np.mean(recs):.3f} | "
            f"AUC_moy={np.mean(aucs):.3f}"
        )
    print()


if __name__ == "__main__":
    data = load_data()
    test_2_risk_score_only(data)
    test_4_score_vs_facteurs(data)
    test_6_importance_facteurs(data)
    test_7_continu_vs_binaire(data)
