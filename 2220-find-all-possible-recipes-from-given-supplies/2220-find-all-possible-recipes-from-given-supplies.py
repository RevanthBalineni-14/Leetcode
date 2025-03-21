class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredientsDic = {}
        canMake = defaultdict(lambda: None)
        supplies  = set(supplies)
        for recipe, ingredient in zip(recipes, ingredients):
            ingredientsDic[recipe] = ingredient
            canMake[recipe] = None
        
        def dfs(recipe, canMake, ingredientsDic, supplies, visited):
            if recipe in visited:
                return canMake[recipe]

            if canMake[recipe] or recipe in supplies:
                return True
            if recipe not in ingredientsDic and recipe not in supplies:
                return False

            visited.add(recipe)
            flag = True
            for ingredient in ingredientsDic[recipe]:
                if ingredient in supplies or canMake[ingredient]:
                        continue
                elif ingredient not in supplies and ingredient in ingredientsDic:
                    canMake[ingredient] = dfs(ingredient, canMake, ingredientsDic, supplies, visited)
                    if not canMake[ingredient]:
                        return False
                else: 
                    flag = False

            return flag

        for recipe in recipes:
            visited = set()
            canMake[recipe] = dfs(recipe, canMake, ingredientsDic, supplies, visited)

        res = []
        for recipe in canMake.keys():
            if canMake[recipe] == True:
                res.append(recipe)
        
        return res