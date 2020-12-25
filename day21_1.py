class Day21_1:
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
        for a in all_allergens:
            for ingr in all_allergens[a]:
                ingredients_with_allergens.add(ingr)

        ingredients_without_allergens = all_ingredients - ingredients_with_allergens
        occurrences = 0

        for ingr in ingredients_without_allergens:
            sum = ingredient_occurrences.count(ingr)
            occurrences += sum

        print(occurrences)


Day21_1()
