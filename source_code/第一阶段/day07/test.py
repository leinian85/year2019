dict02 = {}
dict01 = {"a":10,"b":8,"c":5}
for k,v in dict01.items():
    dict02[k] = v**2

dict02 = {k:v**2 for k,v in dict01.items()}
print(dict02)

lista = ["a","b","c"]
listb = ["d","e"]
listc = []
for itema in lista:
    for itemb in listb:
        listc.append(itema+itemb)

listc = [itema+itemb for itema in lista for itemb in listb]
print(listc)

set01 = {"a", }
set02 = set()
set02 = set(listc)
print(set02)

frozenset01 = frozenset(["a", "b", "a"])
print(frozenset01) # frozenset(['a', 'b'])
frozenset01 = frozenset("ababa")
print(frozenset01) # frozenset({'a', 'b'})
frozenset01 = frozenset({"a": 10, "b": 8})
print(frozenset01) # frozenset({'a', 'b'})