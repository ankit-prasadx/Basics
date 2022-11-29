print("Demonstration of List")

# Data : Heterogenous
# Ordered : Yes  -----> | Both are Dependant   |
# Indexed : Yes  -----> |   on one another     |
# Mutable : Yes
# Duplicates : Yes

data = [11,21,51,101,21,11]     # Duplicates

data1 = [11, 90.80, True, "Hello"] # Heterogenous

print("Data is Heterogenous : ",data1)
print("Data is Ordered : ",data1)
print("Data at index 2 : ",data1[2])
print("Data with duplicate elements : ",data)

print("List is Mutable")
data.append(201)
print("Data after append : ",data)
data.pop()
print("Data after pop : ",data)
