list1 = [3,4,5,1,4,6,1,7,7]
list2 = [5,8,2,9,9,4,6,3]

print("List 1:", list1)
print("List 2:", list2)

print("\nIntersection of list 1 and 2:")
print(list(set(list1) & set(list2))) # converts the list to a set, which removes duplicates. '&' is the intersection operator for sets. The intersection is then converted back to a list
