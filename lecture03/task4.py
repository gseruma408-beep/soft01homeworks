year = int(input("Enter year: "))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"(yesr) is a leaf, ")
else:
    print(f"(yesr) is not a leaf year. ")

