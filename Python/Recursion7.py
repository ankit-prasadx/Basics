
def Display(No):

    if (No > 0):
        No = No - 1
        Display(No)     # Recursice function call
        print(No)

Display(4)      # Function call