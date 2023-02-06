#Dictionary. (UNORDERED)
di = {} #Empty dictionary
print("di : ", di)
di[0] = "ZERO" #Inserting or adding element to the dictionary
print("di :", di)
di = {2:"II", 1:"I", 4:"IV", 3:"III"} #Initialization
print("di :", di)
print("di[2] : ",di[2])
print("KEYS:")
for k in di: #Iterating Keys
print(k)
print("VALUES")
for v in di.values(): #Iterating Values
print(v)
print("ITEMS")
for k,v in di.items(): #Iterating Items (Keys and Values)
print(k,v)
del di[2] #Delete an item
print("di : ",di)
