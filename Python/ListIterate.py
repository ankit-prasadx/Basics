# Data : Heterogenous
# Ordered : Yes  -----> | Both are Dependant   |
# Indexed : Yes  -----> |   on one another     |
# Mutable : Yes
# Duplicates : Yes

Data = [11,21,51,101]

print("Output using for")
for no in Data:
    print(no, end = " ")
print("\n______________________________")

print("Output using for with index")
for i in range (0,len(Data),1):
    print(Data[i], end = " ")
print("\n______________________________")

i = 0

print("Output using while with index")

while ( i < len(Data)):
    print (Data[i], end = " ")
    i+=1    # i = i + 1
print("\n______________________________")