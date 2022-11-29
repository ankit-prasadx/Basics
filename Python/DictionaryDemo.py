print("Demonstration of Dictionary")

# Data : Heterogenous
# Ordered : Yes
# Indexed : No
# Mutable : Yes
# Duplicates : No

programming = {"C" : "Ritchie", "C++" : "Stroustrup", "Java" : "Gosling", "Python" : "Rossum","C" : "Thompson"}

Batches = {"PPA" : 18000, "LB" : 16700, "Python" : 16500, "Angular" : 15000}

print("Data of Dictionary : ",Batches)
print("Data type is : ",type(Batches))
print("Length of dictionary : ",len(Batches))
print("Value of PPA  is : ",Batches["PPA"])

print("Data of Dictionary : ",programming)
print("Data type is : ",type(programming))
print("Length of dictionary : ",len(programming))
print("Value of C  is : ",programming["C"])