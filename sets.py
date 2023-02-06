 #SETS. (UNORDERED)
se = set() #Empty Set
se.add(2) # Add element to the set. (one at a time)
print("se : ",se)
se.add((3,4)) # Add a tuple in the set
print("se : ",se)
se.update([5,3,6]) # Add elements to the set (Input should be iterable)
print("se : ",se)
se2 = {4, 5, 6, 7} # Initializing a set. {} - symbol used for the set.(Don't␣
,→use it for creating empty set)
print("se2 : ",se2)
print(se.intersection(se2)) #Common elements
print(se.union(se2)) #all elements from se and se2 without duplicates
