required=['byr','iyr','eyr','hgt','hcl','ecl','pid']
with open("day4/input.txt") as f:
    passports=[dict([field.split(':') for field in p.split('\n')]) for p in f.read().replace(' ', '\n').split('\n\n')]
count=len(passports)
for p in passports:
    for field in required:
        if field not in p.keys():
            count-=1
            break
print(count)