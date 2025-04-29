print("hello world!")


# write a multiople line in simple print ("...") by using \n.

print("hellow world \nhello world") 

#concatinate two string  by using (+).

print("Nilesh" + " patil") # if we want more space between two strings we can add empty string between "".

# if we take extra space then it give indentationError 



# input() fuction use for collect input from the user and use it in code
input ("my name is nilesh")

# take user input and print it in the code(we concatinate the input)
print("hii " + input("what is your name")) # whatever na me you entre in the terminal as input it show = hii name


#variable is use to store value in container which we use later
name = input(" what is the name ") # input value is assign to the name
print(name)


#variable reslease the first value if we add another value assign to it
name = "jack"
print(name) # if we run this code it print name jack

name("robin")
print(name) # here it relese the value name jack and provide output as robin 

# to get length of string we use len() function
print(len(input("my name is")))

#OR 
userame = input("what is my name")
length = len(userame)
print(length)#it provid the length of string which we provide in input



# #if want to give space between word use (_) if we give direct space then it show syntax error.
# user_name = "nilesh"

#project (Band name generator)

print("welcome to band name generator")
pet = input("enter the name of your pet \n")
city = input("enter the name of your city \n ")
print("your band name should be " + pet +" "+ city)