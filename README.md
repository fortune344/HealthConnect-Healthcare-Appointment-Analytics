# HealthConnect — Dashboard Power BI des rendez-vous et des absences

## À propos

**HealthConnect Clinic** est une clinique fictive confrontée à un taux élevé d'absences aux rendez-vous (*no-shows*).

Après l'analyse exploratoire et l'identification des principaux enjeux business réalisées lors du **Week 4**, ce projet poursuit l'analyse à travers la conception d'un **tableau de bord interactif avec Power BI**.

L'objectif est de transformer les données de rendez-vous en indicateurs et visualisations permettant aux responsables de la clinique de mieux comprendre les facteurs associés aux absences et de faciliter la prise de décision.

**Question centrale :** comment utiliser la Business Intelligence pour mieux comprendre les rendez-vous manqués et identifier les facteurs associés au No-Show ?

---

##  Continuité avec le Week 4

Ce dashboard constitue la suite directe du projet réalisé lors du **Week 4 — Analyse des rendez-vous et prédiction des absences**.

Lors du Week 4, le travail portait principalement sur :

* la compréhension du problème business ;
* l'exploration du dataset ;
* le contrôle de la qualité des données ;
* l'identification des variables importantes ;
* la formulation des questions business ;
* la définition des KPI à suivre.

Le **Week 5** consiste à transformer ces analyses en un outil de **Business Intelligence interactif** permettant d'explorer les résultats plus facilement.

---

##  Jeu de données

Le projet utilise le dataset :

`HealthConnect_Appointment_Data.csv`

Le jeu de données contient **5 000 rendez-vous** et **18 variables** couvrant notamment :

* les caractéristiques démographiques des patients ;
* les détails de réservation ;
* l'historique des absences ;
* l'envoi de rappels ;
* la distance entre le patient et la clinique ;
* le temps d'attente ;
* le type de rendez-vous ;
* l'issue du rendez-vous.

La variable cible principale est l'issue du rendez-vous :

`Attended` / `No-Show` / `Cancelled`

---

##  Objectifs du dashboard

Le tableau de bord a été conçu pour permettre de :

1. Suivre les principaux indicateurs liés aux rendez-vous.
2. Mesurer le taux global de No-Show.
3. Analyser les facteurs associés aux absences.
4. Comparer les comportements selon les profils de patients.
5. Étudier l'impact potentiel des rappels.
6. Analyser le délai entre la réservation et le rendez-vous.
7. Examiner la relation entre la distance et les absences.
8. Identifier les catégories de rendez-vous présentant les taux de No-Show les plus élevés.

---

##  KPI principaux

Le dashboard permet notamment de suivre :

| KPI                     | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| **Reminder Rate**       | Pourcentage de rendez-vous ayant reçu un rappel                      |
| **No-Show Rate**        | Pourcentage de rendez-vous non honorés                               |
| **Repeat No-Show Rate** | Taux de No-Show chez les patients ayant déjà un historique d'absence |
| **Average Lead Time**   | Délai moyen entre la réservation et le rendez-vous                   |
| **Average Distance**    | Distance moyenne entre le patient et la clinique                     |

Ces indicateurs permettent d'obtenir rapidement une vision globale de la situation et de suivre les facteurs potentiellement associés aux absences.

---

##  Analyses réalisées

### 1. Analyse du No-Show

Le dashboard permet d'observer le taux de No-Show et de comparer les rendez-vous honorés et non honorés.

### 2. Analyse du délai de réservation

Le délai entre la réservation et la date du rendez-vous est analysé afin d'identifier son éventuelle relation avec le taux d'absence.

### 3. Historique des absences

L'analyse prend en compte l'existence d'un précédent No-Show afin d'identifier les patients présentant un risque récurrent d'absence.

### 4. Analyse de la distance

La distance entre le patient et la clinique est regroupée en catégories afin d'étudier son association avec les absences.

### 5. Analyse des rappels

Les différents canaux de rappel sont comparés afin d'observer leur association avec le comportement des patients.

### 6. Analyse du type de rendez-vous

Les taux de No-Show sont comparés selon les différents types de rendez-vous.

### 7. Segmentation

Les données peuvent être explorées selon différents profils, notamment :

* groupe d'âge ;
* genre ;
* type de rendez-vous ;
* historique de No-Show ;
* canal de rappel.

---

##  Fonctionnalités du dashboard

Le rapport Power BI comprend :

* des cartes KPI ;
* des graphiques interactifs ;
* des analyses comparatives ;
* des filtres dynamiques ;
* des segmentations par profil patient ;
* des visualisations permettant d'identifier les facteurs associés au No-Show.

L'utilisateur peut ainsi passer d'une **vue globale** à une analyse plus détaillée des différents segments.

---

##  Stack technique

* **Power BI** — Business Intelligence et visualisation
* **Power Query** — préparation et transformation des données
* **DAX** — création des mesures et KPI
* **Python / Pandas** — exploration et analyse initiale des données
* **Jupyter Notebook** — analyse exploratoire


##  Utilisation

### Prérequis

Pour consulter ou modifier le dashboard :

* Microsoft Power BI Desktop

Pour reproduire l'analyse exploratoire :

* Python
* Pandas
* Jupyter Notebook

### Ouvrir le dashboard

Ouvrir le fichier :

```text
week5-healthconnect/data/healthConnectClinicDashboard.pbix
```

avec **Power BI Desktop**.

Pour reproduire l'analyse du Week 4 :

```bash
pip install pandas
jupyter notebook week4-healthconnect/analyse/HealthConnect_Semaine4_Notebook.ipynb
```

---

##  Insights et valeur business

L'utilisation de Power BI permet de transformer les résultats de l'analyse en un outil directement exploitable par les responsables de la clinique.

Le dashboard peut notamment aider à :

* identifier les profils présentant davantage de No-Shows ;
* suivre l'évolution des indicateurs clés ;
* comprendre les facteurs associés aux rendez-vous manqués ;
* améliorer les stratégies de rappel ;
* optimiser la gestion des créneaux médicaux ;
* prendre des décisions basées sur les données.

L'objectif final est de contribuer à la **réduction des rendez-vous manqués**, à une meilleure utilisation des ressources médicales et à l'amélioration de l'expérience des patients.

---

