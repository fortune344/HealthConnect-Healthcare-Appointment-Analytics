# HealthConnect Clinic — Data Analytics — Semaine 5

Projet réalisé dans le cadre du programme **AnalystLab Africa — Experience Lab**.

**Problématique du projet :** comment HealthConnect Clinic peut-elle utiliser la donnée et l'IA pour réduire les rendez-vous manqués (no-show) et améliorer l'accompagnement des patients ?

**Stagiaire :** Fortuné Assouan — Piste Data Analytics

---

## Fichiers de la semaine

| Fichier | Description |
|---|---|
| `HealthConnect_Appointment_Data.csv` | Jeu de données source (5000 rendez-vous, 18 colonnes, 1696 patients uniques). |
| `healthConnectClinicDashboard.pbix` | Dashboard Power BI Semaine 5. |
| `HealthConnect_Semaine5_DataAnalytics.docx` | Rapport complet de la semaine. |

## Objectif de la semaine

Préparer le jeu de données et produire une première analyse exploratoire du no-show.

## Travail réalisé

- Nettoyage et préparation du jeu de données
- Analyse exploratoire (EDA)
- 5 KPI calculés via des mesures DAX dans Power BI :
  - Taux de No-Show global : **48,5 %**
  - Taux de rappel envoyé : **72,7 %**
  - No-show avec antécédent : **55,4 %** vs **43,5 %** sans antécédent
  - Délai moyen de réservation : **29,6 jours**
  - Distance moyenne à la clinique : **10,1 km**
- Dashboard Power BI (1 page) : 5 cartes KPI + 5 graphiques comparatifs + filtres interactifs (type de rendez-vous, âge, genre)
- Au moins 5 insights business, dont :
  - Le délai de réservation est le facteur individuel le plus déterminant (24,8 % à 0-3j → 60,5 % à 30j+)
  - Effet de seuil de la distance au-delà de 20 km
  - Le SMS est le canal de rappel le plus efficace

## Limite identifiée

~2 % de valeurs manquantes sur `distance_to_clinic_km` et `waiting_time_minutes` ; imputation par la médiane recommandée mais application dans le modèle final non confirmée à ce stade.

## Suite prévue (Semaine 6)

Approfondir les facteurs de risque combinés, valider les KPI, intégrer avec la piste Data Science.
