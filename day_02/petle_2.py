dictionary = {"imie": "Patryk", "Nazwisko": "Kowalski"}
for i in dictionary:
    print(i)

for i in dictionary.keys():
    print(i)

for i in dictionary.values():
    print(i)

for i in dictionary.items():
    print(i)

for k, v in dictionary.items():
    print(k, "=>", v)

for k, v in dictionary.items():
    print(k, v, sep="=>")

for k, v in dictionary.items():
    print(k, v, sep="=>", end=" : ")

slow_pol_ang = {'czesc': 'hi', 'kot': 'cat'}
slow_ang_pol = {}

for k, v in slow_pol_ang.items():
    slow_ang_pol[v] = k

print(slow_ang_pol)

print({value: key for key, value in slow_pol_ang.items()})
