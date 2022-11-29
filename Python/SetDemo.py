print("Demonstration of Set")

# Data : Heterogenous
# Ordered : No
# Indexed : No
# Mutable : Yes     (Frozen Set is Immutable)
# Duplicates : No

data = {11,21,51,101,21,11}

data1 = {11, 90.809, True, "Hello"} # Heterogenous

print("First set data : ", data)
print("Lenght of data :", len(data))
print("Data is Heterogenous : ",data1)
print("Data is Not ordered : ",data1)
# print("Data at index 2 : ",data1[2])
print("Data with Unique elements : ",data)

print("Set is Mutable")

# Insert element in set
data.add(211)
print("Data after insertion",data)

# Remove element
data.remove(211)
print("Data after removal : ",data)

data.discard(201)
print("Data after discard : ",data)

