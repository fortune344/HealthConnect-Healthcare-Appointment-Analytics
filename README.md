#  HealthConnect Clinic — Analyse des rendez-vous et prédiction du No-Show

Analyse de données pour réduire les rendez-vous manqués (*no-show*) et améliorer l'expérience des patients d'une clinique fictive, **HealthConnect Clinic**.

[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)](#-dashboard-power-bi)
[![Python](https://img.shields.io/badge/Python-scikit--learn%20%7C%20Pandas-3776AB?logo=python&logoColor=white)](#-stack-technique)
[![DAX](https://img.shields.io/badge/DAX-KPI%20%26%20mesures-yellow)](#-kpi-finaux)

---



##  Problématique

> Comment HealthConnect Clinic peut-elle utiliser la donnée et l'IA pour réduire les rendez-vous manqués (no-show) et améliorer l'accompagnement des patients ?

##  Structure du repo

```
HealthConnect-Healthcare-Appointment-Analytics/
├── Week 4 HealthConnect/       # Prise en main du dataset, qualité des données, questions business, KPI proposés
│   ├── analyse/                # Notebook d'exploration
│   ├── data/                   # Dataset source
│   └── report/                 # Rapport Semaine 4
│
├── week 5 Health Connect/      # EDA, 5 KPI (DAX), premier dashboard Power BI
│   ├── dashboard/               # .pbix + capture d'écran
│   ├── data/ · images/ · report/
│
├── week 6 Health Connect/      # Score de risque combiné, correction dashboard, intégration cross-track
│   ├── dashboard/ · data/ · images/ · report/
│
├── week 7 Health Connect/      # Test, validation et affinement du score de risque (S6)
│   ├── analyse/                 # Scripts Python : reconstruction du score, test de modèles de classification
│   ├── data/ · image/ · report/
│
├── week 8 Health Connect/      # Intégration finale, package de décision complet
│   ├── dashboard/ · data/ · notebook/ · report/
│
└── README.md
```

Chaque dossier de semaine contient son propre `README.md` détaillé.

##  Jeu de données

`HealthConnect_Appointment_Data.csv` — **5 000 rendez-vous**, **18 colonnes**, **1 696 patients uniques**, du 1er janvier 2025 au 30 juin 2026 (réservations remontant jusqu'à novembre 2024).

Répartition de la variable cible `appointment_outcome` :

| Issue | Part |
|---|---|
| No-Show | 48,5 % |
| Attended | 46,3 % |
| Cancelled | 5,3 % |

Contrôle qualité (S4) : aucun doublon, dates cohérentes, pas de valeurs aberrantes. Seuls points à traiter : `reminder_channel` vide quand aucun rappel n'est envoyé (à recoder en catégorie « Aucun », pas un vrai NaN), et ~2 % de valeurs manquantes sur `distance_to_clinic_km` et `waiting_time_minutes` (imputation médiane, appliquée en S6 dans `HealthConnect_Appointment_Data_cleaned_S6.csv`).

##  Démarche semaine par semaine

| Semaine | Étape |
|---|---|
| **S4** | Prise en main du dataset, contrôle qualité, questions business, proposition de KPI |
| **S5** | Nettoyage, EDA, 5 KPI calculés en DAX, dashboard Power BI (1 page), 5 premiers insights business |
| **S6** | Construction d'un **score de risque combiné**, imputation médiane, correction d'une visualisation trompeuse, intégration cross-track |
| **S7** | Test du score dans un modèle de classification, comparaison avec les 4 facteurs séparés, extension (arbre de décision, random forest) |
| **S8** | Intégration finale, collaboration cross-track documentée, package de décision complet |


##  KPI finaux

| Indicateur | Valeur |
|---|---|
| Taux de No-Show global | **48,5 %** |
| Taux de rappel envoyé | **72,7 %** |
| No-show avec antécédent / sans antécédent | **55,4 % / 43,5 %** |
| Délai moyen de réservation | **29,6 jours** |
| Distance moyenne à la clinique | **10,1 km** |

##  Findings clés

- **Délai de réservation** : facteur individuel le plus déterminant — **24,8 %** de no-show pour une réservation à 0-3 jours contre **60,5 %** au-delà de 30 jours.
- **Distance** : effet de seuil marqué au-delà de **20 km** (**57,8 %** de no-show).
- **Antécédent de no-show** : effet **gradient**, pas un simple seuil — 43,5 % → 53,5 % → 59,4 % → 67,9 % selon le nombre d'antécédents cumulés. `previous_no_shows` devrait donc être conservé en valeur continue plutôt qu'en indicateur binaire.
- **Canal de rappel** : le **SMS** reste le plus efficace sur le terrain, mais pèse le moins dans le modèle prédictif.
- **Score de risque combiné** (délai > 30j, antécédent, distance > 20 km, absence de rappel — de 0 à 4 facteurs) :

  | Facteurs cumulés | Rendez-vous | Taux de No-Show |
  |---|---|---|
  | 0 | 1 013 | 31,4 % |
  | 1 | 2 125 | 44,9 % |
  | 2 | 1 470 | 59,3 % |
  | 3 | 370 | 71,1 % |
  | 4 (échantillon faible, n=22) | 22 | 68,2 % |

##  Modèles testés (S7)

| Approche | Accuracy | AUC | Recall |
|---|---|---|---|
| Score de risque seul (régression logistique) | 59,8 % | 0,616 | 48,8 % |
| 4 facteurs séparés (régression logistique) | 61,7 % | 0,644 | **64,0 %** |
| Variables brutes (12 colonnes) | — | 0,672 | 59,5 % |
| Random forest (profondeur 8, variables brutes) | 75,8 % (train) / 61,4 % (test) — surapprentissage net | — | — |

**Conclusion :** le score agrégé reste utile pour la priorisation opérationnelle et la segmentation dans le dashboard, mais les **4 facteurs séparés sont recommandés pour un futur modèle prédictif** (meilleur recall).

##  Dashboard Power BI

Dashboard Power BI (1 page), construit en S5 et affiné en S6 :

- 5 cartes KPI
- 5 graphiques comparatifs (No-Show global, délai de réservation, historique, distance, canal de rappel)
- Filtres interactifs : type de rendez-vous, âge, genre
- Correction S6 : graphique « No-Show by History » passé de camembert à barres (comparaison de deux taux indépendants, pas des parts d'un tout), recoloré selon la charte du dashboard (corail au-dessus de la moyenne globale, teal en dessous)

Fichier : `week 8 Health Connect/dashboard/healthConnectClinicDashboard.pbix` (version la plus à jour) — à ouvrir avec **Power BI Desktop**.

##  Limites

- Dataset fictif et anonymisé : les résultats ne reflètent pas une vraie clinique.
- Échantillon à 4 facteurs de risque cumulés trop faible pour conclure (n = 22).
- Un sous-groupe de no-show échappe aux 4 facteurs de risque connus — angle mort identifié via l'analyse des faux négatifs.
- Corrélation ≠ causalité : d'autres facteurs non présents dans les données (revenu, moyen de transport...) peuvent expliquer certains liens observés.
- Aucune validation croisée reçue de la piste Data Science au moment de la clôture S8.
- Modèles de S7 exploratoires, non représentatifs d'un modèle final de production.

## 🛠 Stack technique

Power BI · DAX · Python (Pandas, scikit-learn) · Jupyter Notebook · SQL Server


---
*AnalystLab Africa Experience Lab.*
