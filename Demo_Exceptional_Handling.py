#exceptional handling
i = int(input("Enter a no"))
try:
    print(i/0)

except:
    print("Exception occurs ...Handle it ")
finally:
    print("Thank you for using my application ....")