with open('day21/input.txt') as f:
    data=[l.split(' (contains ') for l in f.read().replace(')', '').splitlines()]
allergen_ingredient=dict()
for d in data:
    for allergen in d[1].split(', '):
        if allergen in allergen_ingredient.keys():
            allergen_ingredient[allergen]=allergen_ingredient[allergen].intersection(d[0].split(' '))
        else:
            allergen_ingredient[allergen]=set(d[0].split(' '))
for _ in range(1000):
    for k1, v1 in allergen_ingredient.items():
        if len(v1)==1:
            for k2, v2 in allergen_ingredient.items():
                if k1!=k2:
                    allergen_ingredient[k2]=v2-v1
for ing in [list(x[1])[0] for x in sorted(allergen_ingredient.items())]:
    print(ing, end=',')