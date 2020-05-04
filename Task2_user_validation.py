import random
import string

#function that enables one choose its own password
def choosing_password():
    choosen_pass = input("Kindly choose your preferred password(it must not be less than 7 characters): ")
    while len(choosen_pass) <= 7:
        choosen_pass = input("Please enter a new password with more than 7 characters: ")
    password = choosen_pass
    return password
 
# user enters his/her details and system generates password
def new_user():
    
    first_name = input("Enter your First name: ")
    last_name = input("Enter your Last name: ")
    email = input("Enter your email: ")

    user = [first_name, last_name, email]

    rand_str = ""
    for keys in range(5):
        gen = random.choice(letters)
        rand_str += gen

    password = first_name[0:2]+ last_name[-2:] + rand_str

    # prints out system generated password for the user
    print("Your password is: " + password)

    pass_confirm = input("Are you satisfied with your password? YES/NO: ").upper()
    choice_psw = True
    # loop that prints out customers details if h/she is satisfied with password.
    while choice_psw:
        if pass_confirm == "NO":
            password = choosing_password()
            user.append(password)
         
            choice_psw = False
            contact_details = (f"FIRST NAME: {first_name}\n LAST NAME: {last_name}\n EMAIL: {email}\n PASSWORD: {password}")
            print(contact_details)

        elif pass_confirm == "YES":
            user.append(password)
        
            choice_psw = False
            contact_details = (f"FIRST NAME: {first_name}\n LAST NAME: {last_name}\n EMAIL: {email}\n PASSWORD: {password}")
            print(contact_details)

        else:
            pass_confirm = input("Invalid Answer, please enter YES/NO: ").upper()
        
    return user


# main program

letters = string.ascii_lowercase
user_counter = 1
database = {}

while True:

    user = new_user()
    database[user_counter] = user
    
    new_user_request = input("Do you want to enter a new user details: YES/NO:").upper()

    # loop that continues to run until a user enter yes or no to validate their request.
    while new_user_request != "YES" and new_user_request != "NO":
        print("Invalid answer please enter YES/NO")
        new_user_request = input("Do you want to enter a new user details: YES/NO:").upper()

    if new_user_request == "YES":
        user_counter += 1
        continue
    else:
        
        for all in database:
            print(database.get(all))
    break
            

