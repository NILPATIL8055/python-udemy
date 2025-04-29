#type error because length fuction not work with integers.
len(123456)

# to find the datatype of the words.
print(type("Hello")) #string
print(type(123.325)) #float
# print(type(123_45)) #int
# print(type(True)) #boolean


# #type conversion 
print(int("123") + int ("456")) # it work as int datatype we convert string into int

int()
float()
str()
bool()


#run this line it give type error
print("Number of letters in your name :" + len(input("Enter your name")))
#solve this problem
name_of_the_user =input("Enter your Name "  )
length_of_name =len(name_of_the_user )
print(type("Number of letter in your name:"))
print(type(length_of_name))

print("Number of letter in your name:" + str(length_of_name))
