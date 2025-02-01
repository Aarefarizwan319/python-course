my_set={1,2,4,6,8,8,10,}
print("Set :",my_set)
my_set.add(12)
print("Updated Set :",my_set)
set1=my_set
set2={1,3,5,9}
print("\nSet 1",set1)
print("\nSet 2",set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric differnce")
print(set1.symmetric_difference(set2))