class Day21_2:
    input = """"""

    def __init__(self):
        lines = self.input.split('\n')
        all_allergens = {}
        all_ingredients = set()
        ingredient_occurrences = []

        for l in lines:
            ingredients, allergens = l.split(' (contains ')
            ingredients = set(ingredients.split())
            ingredient_occurrences += list(ingredients)
            for i in ingredients:
                all_ingredients.add(i)

            allergens = allergens[:-1].split(', ')
            for a in allergens:
                if a not in all_allergens:
                    all_allergens[a] = ingredients.copy()
                else:
                    all_allergens[a] &= ingredients.copy()

        ingredients_with_allergens = set()
        while any([len(all_allergens[a]) != 1 for a in all_allergens]):
            for a in all_allergens.copy():
                if len(all_allergens[a]) == 1:
                    ingredients_with_allergens.add(next(iter(all_allergens[a])))
                else:
                    for ingr in all_allergens[a].copy():
                        if ingr in ingredients_with_allergens:
                            all_allergens[a].remove(ingr)
                    if len(all_allergens[a]) == 1:
                        ingredients_with_allergens.add(next(iter(all_allergens[a])))

        cdil = ""
        for a in sorted(all_allergens.keys()):
            cdil = cdil + next(iter(all_allergens[a])) + ','
        print(cdil[:-1])


Day21_2()
