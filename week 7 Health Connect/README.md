# HealthConnect Clinic — Semaine 7 (Piste Data Analytics)

**Programme :** AnalystLab Africa Experience Lab
**Projet :** HealthConnect Clinic Experience Lab
**Semaine :** 7 — Testing, Refinement & End-to-End Validation
**Auteur :** Fortuné Assouan

## Objectif de la semaine

Semaine 7 n'est pas une nouvelle analyse : c'est le test, la validation et l'affinement de ce qui a été produit en Semaine 6 (score de risque combiné de no-show). Aucune donnée nouvelle, aucun nouvel indicateur — uniquement des tests sur l'existant.

## Contenu de ce dossier

```
Semaine7/
├── README.md
├── Semaine7_DataAnalytics_Testing_Refinement.docx   → rapport principal
├── data/
│   └── HealthConnect_Appointment_Data_cleaned_S6.csv → données de S6, réutilisées telles quelles
├── scripts/
│   ├── reconstruction_risk_score.py                  → tests 1, 3, 5 (reconstruction, stabilité, segments)
│   ├── test_modeles_classification.py                → tests 2, 4, 6, 7 (modèles, importance des facteurs)
│   └── extension_data_science.py                     → tests 8 à 12 (algorithmes, surapprentissage, erreurs, fuite)
├── evidence/
│   ├── camembert_avant.png                            → dashboard avant correction (S6)
│   ├── camembert_apres.png                            → dashboard après correction (S6, vérifié en S7)
│   └── extension_charts.png                           → surapprentissage + profil des faux négatifs
└── communication/
    └── message_data_science.png                       → message envoyé au HC-POD (collaboration cross-track)
```

## Principaux résultats (voir le rapport pour le détail complet)

- Le score de risque combiné (S6) est **stable et reproductible** : 31,4 % → 71,1 % de no-show selon le nombre de facteurs présents.
- Dans un modèle de classification, les **4 facteurs pris séparément surpassent le score agrégé** en recall (64,0 % vs 48,8 %) — le score reste utile pour le dashboard, pas pour un modèle prédictif.
- Un modèle plus complexe (random forest, variables brutes) montre un **surapprentissage net** : 75,8 % en entraînement contre 61,4 % en test.
- Une partie des no-show échappe aux 4 facteurs de risque connus, même après réception d'un rappel — **angle mort documenté** pour la Semaine 8.
- Le graphique "No-Show by History" (camembert → colonnes) a été corrigé et vérifié dans Power BI Desktop.

## Différence avec la Semaine 6

| Semaine 6 | Semaine 7 |
|---|---|
| Construction du score de risque | Test et validation de ce score |
| Analyse exploratoire | Analyse d'erreurs et de robustesse |
| Correction manuelle du dashboard | Vérification de cette correction |

## Collaboration cross-track (HC-POD)

Piste collaborée : **Data Science**. Message envoyé avec les résultats du test "score agrégé vs facteurs séparés" et une question directe sur leur propre approche de modélisation. Réponse en attente à la date de rédaction — voir section 6 du rapport principal pour le détail complet et la procédure de suivi.

## À faire avant la Semaine 8

- Documenter la réponse de Data Science dès réception.
- Explorer l'angle mort identifié sur les faux négatifs (patients sans facteur de risque connu).
