# Recherche par dichotomie (_binary search_)

### Le problème

On cherche à savoir si un nombre est présent dans une tableau **ordonné** de nombres.

Dans ce cas, on retournera son index, sinon une valeur de type `None` / `null`.

**Remarque :** _cet algorithme est valable pour tout tableau d'objets qu'il est possible de trier._

### Le principe

On va **_réduire la taille de l'intervalle de recherche en le divisant par 2 à chaque étape_**.

On part d'une intervalle de recherche [*a*, *b*] correspondant au tableau dans son entier en prenant pour _a_ la valeur minimale de la liste (donc d'indice 0 si la liste est ordonnée de manière _croissante_) et pour _b_ la valeur maximale.

On s'intéresse alors à la **_valeur m au milieu de l'intervalle_**, c'est-à-dire dont l'indice est la **_somme des indices de a et de b divisé par 2_**.

On compare alors cette valeur médiane _m_ avec la valeur recherchée :

- si _m_ est égale à la valeur recherchée, c'est fini et on retourne l'indice de _m_.

- si _m_ est inférieure à la valeur recherchée, alors celle-ci ne peut-être que dans l'intervalle [*m*, *b*] : on pose alors _a_ = _m_ et on itère.

* si _m_ est supérieur à la valeur recherchée, alors celle-ci ne peut-être que dans l'intervalle [*a*, *m*] : on pose alors _b_ = _m_ et on itère.

La recherche s'achève dès lors que la valeur est trouvée où que l'intervalle [*a*, *b*] est vide (dès que _a_ > _b_).

### Les performances

L'intervalle de recherche étant divisé par 2 à chaque étape, on a un **_algorithme de complexité en O (log n)_** donc très performant.

Une _recherche linéaire_ où on regarderait successivement chaque valeur du tableau a elle une complexité en O (_n_).
