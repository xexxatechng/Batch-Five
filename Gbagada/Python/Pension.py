#Print out the purpose of the program
print("This is a program to calculate pension year either by age or year in service")




import datetime

#asking the user to input their birthdate
birthDate = input("Enter your birth date (dd/mm/yyyy)\n>>> ")


#asking the user to input their fist day of employment
employmentDate = input("Enter your employment date (dd/mm/yyyy)\n>>> ")

birthDate = datetime.datetime.strptime(birthDate, "%d/%m/%Y").date()
print("Your birthday is on "+ birthDate.strftime("%d") + " of " + birthDate.strftime("%B, %Y"))

currentDate = datetime.datetime.today().date()

employmentDate = datetime.datetime.strptime(employmentDate, "%d/%m/%Y").date()
print("Your employmentday is on "+ employmentDate.strftime("%d") + " of " + employmentDate.strftime("%B, %Y"))

currentDate = datetime.datetime.today().date()

#some calculations here 
age = currentDate.year - birthDate.year
monthVeri = currentDate.month - birthDate.month
dateVeri = currentDate.day - birthDate.day

#Type conversion here
age = int(age)
monthVeri = int(monthVeri)
dateVeri = int(dateVeri)

# some decisions
if monthVeri < 0 :
    age = age-1
elif dateVeri < 0 and monthVeri == 0:
    age = age-1

#lets print the age now
print("Your age is {0:d}".format(age))

#some calculations here
age = currentDate.year - employmentDate.year
monthVeri = currentDate.month - birthDate.month
dateVeri = currentDate.day - employmentDate.day

#Type conversion here
age = int(age)
monthVeri = int(monthVeri)
dateVeri = int(dateVeri)

# some decisions
if monthVeri < 0 :
    age = age-1
elif dateVeri < 0 and monthVeri == 0:
    age = age-1

#lets print the year now
print("Your serviceyear is {0:d}".format(age))

#If the age is equal or greater than 60, display: "Stop salary"
if age>=60:
   print("stop salary")
   
#Else display: "Pay salary"
else:
    print("Pay salary")

#If the serviceyear is greater than 35, display: "Stop salary"
if serviceyear>=35:
   print("stop salary")

#Else display: "Pay salary"
else:
    print("Pay salary")


