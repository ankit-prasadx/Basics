
def Display(No):

    if (No > 0):
        print(No)
        No = No - 1
        # Display(No - 1)
        Display(No)     # Recursice function call

Display(4)      # Function call