MyCarDetails = {
    "Model":1970,
    "Name":"Mercedez",
    "Color":"Black"
}

print(MyCarDetails)
print(MyCarDetails["Model"])
MyCarDetails["Class"]= "E-Class"
for i in MyCarDetails:
    print(i,MyCarDetails[i])