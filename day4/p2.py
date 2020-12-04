import re
required={
    'byr' : re.compile(r"^19[2-9][0-9]|200[0-2]$") ,
	'iyr' : re.compile(r"^201[0-9]|2020$") ,
	'eyr' : re.compile(r"^202[0-9]|2030$") ,
	'hgt' : re.compile(r"^((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6]))in$") ,
	'hcl' : re.compile(r"^#(\d|[a-f]){6}$") ,
	'ecl' : re.compile(r"^amb|blu|brn|gry|grn|hzl|oth$") ,
	'pid' : re.compile(r"^\d{9}$") ,
}

with open("day4/input.txt") as f:
    passports=[dict([field.split(':') for field in p.split('\n')]) for p in f.read().replace(' ', '\n').split('\n\n')]
count=len(passports)
for p in passports:
    for field in required.keys():
        if field not in p.keys() or not required[field].match(p[field]):
            count-=1
            break
print(count)