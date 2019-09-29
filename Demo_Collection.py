#Step1- Creating a list
#Step2- Displaying Elements
#Step3- Adding elements
#Step4- Displaying elements

Mycars = ["jaguar","Range Rover","MG-Hector"]
print(Mycars)
Mycars.append("Tesla")
for car in Mycars:
    print(car)
Mycars.insert(0,"Tesla")
Mycars[-1]= "BMW"
for car in Mycars:
    print(car)