# HealthConnect Clinic — Data Analytics

AnalystLab Africa Experience Lab — piste Data Analytics — Semaines 5 à 8.

## Dataset

- `HealthConnect_Appointment_Data.csv` — 5 000 rendez-vous, 18 colonnes, 1 696 patients uniques (48,5 % No-Show · 46,3 % Attended · 5,3 % Cancelled)
- `HealthConnect_Appointment_Data_cleaned_S6.csv` — version dérivée avec imputation médiane (distance, waiting_time)

## Structure du repo

```
├── data/
│   ├── HealthConnect_Appointment_Data.csv
│   └── HealthConnect_Appointment_Data_cleaned_S6.csv
├── dashboard/
│   └── HealthConnect_Dashboard.pbix
├── notebooks/
│   └── risk_score_modeling_S7.ipynb      # tests prédictifs (régression logistique, arbre, random forest)
├── reports/
│   ├── HealthConnect_Semaine5_DataAnalytics.docx
│   ├── HealthConnect_Semaine6_DataAnalytics.docx
│   ├── HealthConnect_Semaine7_DataAnalytics.docx
│   └── HealthConnect_Semaine8_DataAnalytics.docx
└── README.md
```

*(adapter les noms de dossiers à l'organisation réelle du repo)*

## Démarche analytique

| Semaine | Étape |
|---|---|
| S5 | Nettoyage, EDA, 5 KPI (DAX), dashboard Power BI 1 page, 5 premiers insights business |
| S6 | Construction d'un score de risque combiné (délai > 30j, antécédent, distance > 20km, absence de rappel), imputation médiane, correction d'une visualisation trompeuse |
| S7 | Test du score dans un modèle de classification (régression logistique), comparaison avec les 4 facteurs séparés, extension (arbre, random forest) |
| S8 | Intégration finale, collaboration cross-track documentée, package de décision complet |

## KPI finaux

| Indicateur | Valeur |
|---|---|
| Taux de no-show global | 48,5 % |
| Taux de rappel envoyé | 72,7 % |
| No-show avec antécédent / sans | 55,4 % / 43,5 % |
| Délai moyen de réservation | 29,6 jours |
| Distance moyenne à la clinique | 10,1 km |

## Findings clés

- Le **délai de réservation** est le facteur le plus déterminant : 24,8 % de no-show à 0-3 jours contre 60,5 % à 30 jours et plus.
- Effet de seuil au-delà de **20 km** de distance (57,8 % de no-show).
- Le **SMS** reste le canal de rappel le plus efficace, mais pèse le moins dans le modèle prédictif.
- Le **score de risque combiné** présente un gradient net (31,4 % → 71,1 % selon le nombre de facteurs), utile pour la segmentation dashboard.

## Modèles testés (S7)

| Approche | Accuracy | AUC | Recall |
|---|---|---|---|
| Score de risque seul (régression logistique) | 59,8 % | 0,616 | 48,8 % |
| 4 facteurs séparés (régression logistique) | 61,7 % | 0,644 | 64,0 % |
| Variables brutes (12 colonnes) | — | 0,672 | 59,5 % |
| Random forest (profondeur 8, variables brutes) | 75,8 % (train) / 61,4 % (test) | — | — |

**Conclusion :** le score agrégé est utile pour la priorisation opérationnelle, mais les 4 facteurs séparés sont recommandés pour la modélisation prédictive (meilleur recall).

## Limites

- Échantillon à 4 facteurs de risque simultanés trop faible pour conclure (n = 22).
- Un sous-groupe de no-show échappe aux 4 facteurs actuels (angle mort identifié via l'analyse des faux négatifs).
- Aucune validation croisée reçue de la piste Data Science au moment de la clôture S8.
- Modèle de test exploratoire, non représentatif du modèle final de prédiction.

## Stack technique

Power BI · DAX · Python (scikit-learn) · SQL Server

## Auteur

**Fortuné Assouan** — Bac+2 Information Systems, Lomé Business School
[LinkedIn](https://linkedin.com/in/fortuné-assouan-a29561a7) · [Portfolio](https://fortuneassouan.vercel.app)

---
*AnalystLab Africa Experience Lab.*
