from functools import reduce
with open('day21/input.txt') as f:
    data=[l.split(' (contains ') for l in f.read().replace(')', '').splitlines()]
allergen_ingredient=dict()
for d in data:
    for allergen in d[1].split(', '):
        if allergen in allergen_ingredient.keys():
            allergen_ingredient[allergen]=allergen_ingredient[allergen].intersection(d[0].split(' '))
        else:
            allergen_ingredient[allergen]=set(d[0].split(' '))
for _ in range(100):
    for k1, v1 in allergen_ingredient.items():
        if len(v1)==1:
            for k2, v2 in allergen_ingredient.items():
                if k1!=k2:
                    allergen_ingredient[k2]=v2-v1
ingredients=reduce(lambda a,b: a+b, [d[0].split(' ') for d in data])
for ing in allergen_ingredient.values():
    ingredients=list(filter((list(ing)[0]).__ne__, ingredients))    #remove ingredients with allergens
print(len(ingredients))