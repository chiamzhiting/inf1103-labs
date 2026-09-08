#Activity 1
#Q1 #done
#Q2
print("===========================")
print("Welcome here")
print("My first post!")
print("===========================")

#Q2
##a. yes 
##b. top to bottom
##c. output appear in terminal 

#Q4 #git add hello.py

#Q5
#Q6
#Q7

#Activity 2
#Q1

username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

#Q2
##a. variables are used to store profile information about the profile
##b. if the values changes, the printed output will also change to show the new information.
##c. output appear in the terminal 

#Q3 #done
#Q4 #done

#Activity 3
followers = 100

followers += 50
print("Day 1:", followers)

followers += 20
print("Day 2:", followers)

followers += 10
print("Day 3:", followers)

#2
##a. no
##b. the current value
##c. they add or subtract from the variable and save the result back into it 

#3

#Activity 4
#1
username = input("Enter Username: ")
age = input("Enter Age: ")
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("===========================")
print("Username: ", username)
print("Age: ", age)
print("Category: ", category)

#2
##a. it shows the prompt text, waits for you to type and stores what you typed im the variable
##b. dynamic, the output depends on what the user types, not a fixed value in the code
##c.  run it a few times with different values - it prints back whatever you typed, since input() always treats it as text 

#3

#Activity 5
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("===========================")
print("Username: ", username)
print("Age: ", age)
print("Category: ", category)

if age>40 and category == "fun":
    print("You are old what is fun for you??")

#3.
##a. always a string even for numbers thats why age uses int() to convert it
##b. with if, using and/== to test multiple things at once - here, age>40 and category is "fun". Both must be true for the code inside to run
