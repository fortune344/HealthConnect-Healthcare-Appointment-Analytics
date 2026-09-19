# HealthConnect Clinic — Semaine 7 

**Programme :** AnalystLab Africa Experience Lab
**Projet :** HealthConnect Clinic Experience Lab
**Semaine :** 7 — Testing, Refinement & End-to-End Validation


## Objectif de la semaine

Semaine 7 n'est pas une nouvelle analyse : c'est le test, la validation et l'affinement de ce qui a été produit en Semaine 6 (score de risque combiné de no-show). Aucune donnée nouvelle, aucun nouvel indicateur — uniquement des tests sur l'existant.


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


