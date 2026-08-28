# HealthConnect — Analyse des rendez-vous et prédiction des absences

## À propos

HealthConnect Clinic est une clinique fictive confrontée à un taux élevé d'absences aux rendez-vous (no-shows). Ce projet explore comment les données peuvent aider à comprendre ce phénomène et à identifier des leviers d'action.

**Question centrale :** comment utiliser les données pour réduire les rendez-vous manqués et améliorer l'expérience des patients ?

## Jeu de données

`HealthConnect_Appointment_Data.csv` — 5 000 rendez-vous, 18 variables : démographie du patient, détails de réservation, historique d'absences, envoi de rappels, distance à la clinique, temps d'attente, et issue du rendez-vous (`Attended` / `No-Show` / `Cancelled`).


### Compréhension du problème et qualité des données
- Exploration du dataset et revue du dictionnaire de données
- Contrôle qualité complet (doublons, valeurs manquantes, cohérence des dates, valeurs aberrantes, cohérence des catégories, équilibre de la variable cible)
- Formulation de 5 questions business et identification de 5 KPI potentiels
- Définition de l'approche d'analyse pour la suite du projet

**Constat clé :** taux de no-show de 48,5 %, quasiment égal au taux de présence (46,3 %).

### Prochaines étapes
- Nettoyage des valeurs manquantes restantes (~2 % sur distance et temps d'attente)
- Calcul des KPI identifiés
- Construction d'un premier tableau de bord Power BI

## Utilisation

```bash
pip install pandas
jupyter notebook week4-healthconnect/HealthConnect_Semaine4_Notebook.ipynb
```

## Stack technique

`Python` (pandas) · `Power BI` (DAX) · `SQL` · `Jupyter Notebook`
