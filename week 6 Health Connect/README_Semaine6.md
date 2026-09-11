# HealthConnect Clinic — Data Analytics — Semaine 6

Projet réalisé dans le cadre du programme **AnalystLab Africa — Experience Lab**.

**Stagiaire :** Fortuné Assouan — Piste Data Analytics

---

## Fichiers de la semaine

| Fichier | Description |
|---|---|
| `HealthConnect_Appointment_Data_cleaned_S6.csv` | Fichier dérivé : imputation médiane appliquée (`distance_to_clinic_km`, `waiting_time_minutes`), `reminder_channel` manquant recodé, + 4 variables de risque binaires et un score de risque cumulé (`risk_score`, 0-4). Ne remplace pas le fichier source. |
| `healthConnectClinicDashboard_S6.pbix` | Dashboard corrigé : graphique « No-Show by History » passé en barres (au lieu d'un camembert), recoloré selon la charte du reste du dashboard. |
| `HealthConnect_Semaine6_DataAnalytics.docx` | Rapport complet de la semaine (transition, intégration, analyse avancée, cross-track, limites, résumé). |

## Objectif de la semaine

Ne pas refaire l'EDA ni le dashboard de la Semaine 5 : approfondir les résultats, valider leur robustesse, et intégrer concrètement avec une autre piste du projet.

## Corrections apportées depuis la Semaine 5

- L'imputation par la médiane, recommandée mais jamais confirmée comme appliquée, a été effectivement mise en œuvre dans un fichier dérivé séparé.
- Le graphique « No-Show by History » était resté en camembert alors que le rapport S5 expliquait l'avoir écarté (comparaison de deux taux indépendants, pas de parts d'un tout) → remplacé par un graphique à colonnes, recoloré selon la logique du reste du dashboard (corail au-dessus de la moyenne globale, teal en dessous).

## Validation

Les 5 KPI de la Semaine 5 recalculés sur les données corrigées restent tous stables.

## Nouvelle analyse : score de risque combiné

4 indicateurs binaires (délai de réservation > 30 jours, antécédent de no-show, distance > 20 km, absence de rappel) combinés en un score cumulé de 0 à 4 :

| Facteurs cumulés | Rendez-vous | Taux de No-Show |
|---|---|---|
| 0 | 1 013 | 31,4 % |
| 1 | 2 125 | 44,9 % |
| 2 | 1 470 | 59,3 % |
| 3 | 370 | 71,1 % |
| 4 (n=22, échantillon faible) | 22 | 68,2 % |

Découverte complémentaire : l'antécédent de no-show a un effet **gradient** (43,5 % → 53,5 % → 59,4 % → 67,9 % selon le nombre d'antécédents), pas un simple effet de seuil — `previous_no_shows` devrait être gardé en valeur continue plutôt qu'en indicateur binaire pour un futur modèle.

## Intégration cross-track

Stage mené en autonomie (pas de coéquipier réel sur la piste Data Science) : l'intégration a été documentée en produisant un livrable réellement exploitable — le fichier dérivé et ses variables de risque — plutôt qu'un échange simulé. Détails complets dans le rapport, section 4.

## Limites

- Score à 4 facteurs cumulés basé sur un échantillon restreint (n=22), à interpréter avec prudence.
- Associations statistiques, non des relations de cause à effet.
- Jeu de données fictif et anonymisé.

## Suite prévue (Semaine 7)

Tester le `risk_score` comme variable dans un modèle de classification simple, vérifier la stabilité du score sur un sous-échantillon de validation.
