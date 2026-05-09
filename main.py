set1={1,2,3,4,5,9}
set2={1,3,5,6,7,8}

print(f"set1: {set1}")
print(f"set1: {set2}")

set1.add(10)

print(f"new set1: {set1}")
set3=set1.union(set2)
print(f"Union:{set3}")
set4=set1.intersection(set2)
print(f"Intersection: {set4}")

set5=set1.difference(set2)
print(f"difference: {set5}")