#when we get output in 23.232653 this type of number then we make it roundoff with Round function
bmi = 84 / 1.64 ** 2
print(bmi) #output = 31.231409875074366
print(int(bmi)) # output = 31

print(round(bmi))# output = 31
print(round(bmi, 3)) #output = 31.231 we also get decimal floating point as much we want

 


# below we convert all data types into string by using f in front of string and use { } to put all variable into the string
score = 0
height =1.0
is_winning = True
print(f"Your score is = {score}, your height is = {height}, Your are winng is = {True}")    