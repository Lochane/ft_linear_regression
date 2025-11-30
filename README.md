# ft_linear_regression

Bien sûr ! Voici un **plan d’action complet** et détaillé pour ton programme `linear_regression.py`, qui entraîne ton modèle de régression linéaire **de A à Z**, avec toutes les étapes **dans l’ordre logique**, **sans solution** de code.

---

# ✅ Plan d’action pour `linear_regression.py`

📌 Objectif final : entraîner un modèle de régression linéaire à une variable (le kilométrage), trouver `theta0` et `theta1`, puis les sauvegarder.

---

## 🟦 1. Chargement des données

### 🎯 Ce que tu dois faire :

* Lire le fichier de données (ex : `data.csv`)
* Extraire les colonnes `mileage` et `price`
* Stocker ces deux colonnes dans deux listes ou tableaux (X et Y)

### ✅ À vérifier :

* Format correct du fichier
* Pas de valeurs manquantes
* Bonne conversion en float

---

## 🟦 2. Initialisation

### 🎯 Tu dois définir :

* `theta0 = 0.0`
* `theta1 = 0.0`
* Un `learning_rate` (ex: 0.01 ou 0.001)
* Un `nombre_d_iterations` (ex: 1000 ou 5000)

---

## 🟦 3. Fonction d’estimation

### 🎯 Définir une fonction `estimate_price(mileage, theta0, theta1)`

Elle retournera `theta0 + theta1 * mileage`

👉 Cette fonction sera utilisée :

* Dans le calcul d’erreur
* Dans les formules de mise à jour

---

## 🟦 4. Boucle d'entraînement (gradient descent)

### 🎯 Répéter pendant `n` itérations :

1. Calculer l’erreur entre la prédiction et la vraie valeur pour chaque point
2. Calculer :

   * `tmp_theta0` avec la moyenne des erreurs
   * `tmp_theta1` avec la moyenne des erreurs pondérées par `mileage`
3. Mettre à jour `theta0` et `theta1` **en même temps**

### ✅ À vérifier :

* Que les formules sont appliquées proprement
* Que les erreurs diminuent (tu peux imprimer une métrique régulièrement)

---

## 🟦 5. (Optionnel) Suivi visuel ou log

* Afficher `theta0`, `theta1` tous les X tours
* Ou afficher l’erreur moyenne
* Cela permet de savoir si ton modèle apprend bien

---

## 🟦 6. Sauvegarde des paramètres

### 🎯 Sauvegarder `theta0` et `theta1` dans un fichier (`thetas.json` par exemple)

Format recommandé :

```json
{
  "theta0": 1234.56,
  "theta1": -0.045
}
```

Tu pourras le recharger dans `estimate_price.py`.

---

## 🟦 7. (Optionnel) Évaluation finale

🎁 Bonus utile : calculer une **métrique d’erreur finale** (ex : MSE – moyenne des erreurs au carré) pour évaluer la performance de ton modèle.

---

## 🟦 8. Tests

* Tester avec un jeu de données simple (tu peux créer ton propre `data.csv`)
* Vérifier que les paramètres changent
* Tester avec peu d’itérations, puis beaucoup
* Vérifier que `estimate_price.py` lit bien les bons paramètres ensuite

---

## 🗂️ Structure finale du projet :

```
.
├── data.csv               ← données : mileage, price
├── linear_regression.py   ← ce que tu codes ici
├── estimate_price.py      ← ton programme de prédiction (déjà fait)
├── thetas.json            ← fichier de sortie du modèle entraîné
```

---

## Pseudo code du gradient descent : 
```
1. Charger les données d'entraînement :
   - Liste des kilométrages (X)
   - Liste des prix (Y)

2. Initialiser les paramètres :
   - theta0 ← 0
   - theta1 ← 0
   - learning_rate ← petit nombre (ex: 0.01)
   - nombre_iterations ← nombre de répétitions (ex: 1000)

3. Pour chaque itération (de 1 à nombre_iterations) :
   a. Initialiser deux sommes d'erreurs à 0 :
      - somme_erreur_theta0 ← 0
      - somme_erreur_theta1 ← 0

   b. Pour chaque point dans les données :
      - Prédire le prix avec la formule :
        estimation ← theta0 + theta1 × kilométrage
      - Calculer l’erreur :
        erreur ← estimation - prix réel
      - Ajouter à la somme des erreurs :
        somme_erreur_theta0 ← somme_erreur_theta0 + erreur
        somme_erreur_theta1 ← somme_erreur_theta1 + erreur × kilométrage

   c. Calculer la moyenne des corrections :
      correction_theta0 ← (learning_rate × somme_erreur_theta0) ÷ nombre_total_de_données
      correction_theta1 ← (learning_rate × somme_erreur_theta1) ÷ nombre_total_de_données

   d. Mettre à jour les paramètres simultanément :
      theta0 ← theta0 - correction_theta0
      theta1 ← theta1 - correction_theta1

4. Sauvegarder theta0 et theta1 dans un fichier
```
