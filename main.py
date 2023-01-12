import requests
import sys
import json
from config import api_key

def select_difficulty():
    diff = input("Please enter the desired difficulty level (easy, normal, hard): ")
    if diff == "easy":
        digits = 3
    elif diff == "normal":
        digits = 4
    elif diff == "hard":
        digits = 5
    else:
        print("Please choose either easy, normal, or hard.")
        select_difficulty()
    return digits

def integer_check(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def master_mind():
    print("Welcome to the Mastermind game!")
    numbers = select_difficulty()
    print("Type quit at anytime to exit the game.")
    url = 'https://api.random.org/json-rpc/1/invoke'
    # url = 'https://www.random.org/clients/http/api/'
    if numbers == 3:
    # data = {'jsonrpc':'2.0','method':'GET','params': {'apiKey':api_key,'n':4,'min':0,'max':7,'col':1,'base':10,'format':'plain','rnd':'new'},'id':1}
        data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey':api_key,'n':3,'min':0,'max':7,'replacement':'true','base':10},'id':1}

        params = json.dumps(data)

        response = requests.post(url,params)

        # print(response.text)
        # print(type(response.content))
        # print(type(response.content))

        rand_nums_dict = json.loads(response.content)
        # print((rand_nums_dict['result']['random']['data']))
        rand_nums_list = rand_nums_dict['result']['random']['data']

        print(rand_nums_list)

        correct = 0
        location = 0
        tries = 0
        guess_lists_dict = {}
        while location < 3:
            print("Please guess numbers between 0 and 7.")
            while True:
                guess1 = (input("Enter first digit: "))
                if guess1 == "quit":
                    sys.exit("Goodbye, thanks for playing!")
                if integer_check(guess1):
                    guess1 = int(guess1)
                    if len(str(guess1)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7.")
            
            while True:
                guess2 = (input("Enter second digit: "))
                if guess2 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess2):
                    guess2 = int(guess2)
                    if len(str(guess2)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")
                
            while True:
                guess3 = (input("Enter third digit: "))
                if guess3 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess3):
                    guess3 = int(guess3)
                    if len(str(guess3)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")
            
            tries += 1
            tries_hash = {1:"First", 2:"Second", 3:"Third", 4:"Fourth", 5:"Fifth", 6:"Sixth", 7:"Seventh", 8:"Eigth", 9:"Ninth", 10:"Tenth"}

            guess_lists_dict[tries_hash[tries]] = [guess1, guess2, guess3]

            current_guess = guess_lists_dict[tries_hash[tries]]

            print("Current guess: ", current_guess)
            print("Guess List: ", guess_lists_dict[tries_hash[tries]])


            if current_guess == rand_nums_list:
                print("You won!")
                retry = input("Do you want to play again? Please enter y or n: ")
                if retry == "y":
                    master_mind()
                else:
                    sys.exit("Thank you for playing!")
                                
            
            decr_randnums_list = rand_nums_list.copy()
            decr_randnums_hash = {k: v for k, v in enumerate(decr_randnums_list)}

            print("Decrementing hash",decr_randnums_hash)
            
            print(current_guess)
            print(decr_randnums_list)

            n = 0
            while n < 3:
                print("decrementing list",decr_randnums_list)
                print("Decrementing hash",decr_randnums_hash)

                if current_guess[n] in decr_randnums_list:
                    decr_randnums_hash = {k: v for k, v in enumerate(decr_randnums_list)}
                    correct += 1
                    correct_digit_index = list(decr_randnums_hash.keys())[list(decr_randnums_hash.values()).index(current_guess[n])]
                    decr_randnums_list.pop(correct_digit_index)
                if current_guess[n] == rand_nums_list[n]:
                    location += 1
                n += 1
            print("You guessed " + str(correct) + " number(s) correctly and " + str(location) +" location(s) correctly.")
            print("You have " + str(10 - tries) + " tries left!")
            print("Your previous guesses: " + str(guess_lists_dict))
            correct = 0
            location = 0
            if tries == 9:
                hint = input("Would you like a hint? (y/n): ")
                if hint == "y": 
                    print("The sum of all the correct numbers is: " + str(sum(rand_nums_list)))
                else:
                    print("You got this!")

            if tries == 10:
                print("Game over! Here is the correct answer: " + str(rand_nums_list))
                retry = input("Do you want to play again? Please enter y or n: ")
                if retry == "y":
                    master_mind()
                else:
                    sys.exit("Thank you for playing!")                

    if numbers == 4:
    # data = {'jsonrpc':'2.0','method':'GET','params': {'apiKey':api_key,'n':4,'min':0,'max':7,'col':1,'base':10,'format':'plain','rnd':'new'},'id':1}
        data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey':api_key,'n':4,'min':0,'max':7,'replacement':'true','base':10},'id':1}

        params = json.dumps(data)

        response = requests.post(url,params)

        # print(response.text)
        # print(type(response.content))
        # print(type(response.content))

        rand_nums_dict = json.loads(response.content)
        # print((rand_nums_dict['result']['random']['data']))
        rand_nums_list = rand_nums_dict['result']['random']['data']

        print(rand_nums_list)

        correct = 0
        location = 0
        tries = 0
        guess_lists_dict = {}
        while location < 4:
            print("Please guess numbers between 0 and 7.")
            while True:
                guess1 = (input("Enter first digit: "))
                if guess1 == "quit":
                    sys.exit("Goodbye, thanks for playing!")
                if integer_check(guess1):
                    guess1 = int(guess1)
                    if len(str(guess1)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7.")
            
            while True:
                guess2 = (input("Enter second digit: "))
                if guess2 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess2):
                    guess2 = int(guess2)
                    if len(str(guess2)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")
                
            while True:
                guess3 = (input("Enter third digit: "))
                if guess3 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess3):
                    guess3 = int(guess3)
                    if len(str(guess3)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")
            
            while True:   
                guess4 = (input("Enter fourth digit: "))
                if guess4 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess4):
                    guess4 = int(guess4)
                    if len(str(guess4)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")

            
            tries += 1
            tries_hash = {1:"First", 2:"Second", 3:"Third", 4:"Fourth", 5:"Fifth", 6:"Sixth", 7:"Seventh", 8:"Eigth", 9:"Ninth", 10:"Tenth"}

            guess_lists_dict[tries_hash[tries]] = [guess1, guess2, guess3, guess4]

            current_guess = guess_lists_dict[tries_hash[tries]]

            print("Current guess: ", current_guess)
            print("Guess List: ", guess_lists_dict[tries_hash[tries]])


            if current_guess == rand_nums_list:
                print("You won!")
                retry = input("Do you want to play again? Please enter y or n: ")
                if retry == "y":
                    master_mind()
                else:
                    sys.exit("Thank you for playing!")
                                
            
            decr_randnums_list = rand_nums_list.copy()
            decr_randnums_hash = {k: v for k, v in enumerate(decr_randnums_list)}

            print("Decrementing hash",decr_randnums_hash)
            
            print(current_guess)
            print(decr_randnums_list)

            n = 0
            while n < 4:
                print("decrementing list",decr_randnums_list)
                print("Decrementing hash",decr_randnums_hash)

                if current_guess[n] in decr_randnums_list:
                    decr_randnums_hash = {k: v for k, v in enumerate(decr_randnums_list)}
                    correct += 1
                    correct_digit_index = list(decr_randnums_hash.keys())[list(decr_randnums_hash.values()).index(current_guess[n])]
                    decr_randnums_list.pop(correct_digit_index)
                if current_guess[n] == rand_nums_list[n]:
                    location += 1
                n += 1
            print("You guessed " + str(correct) + " number(s) correctly and " + str(location) +" location(s) correctly.")
            print("You have " + str(10 - tries) + " tries left!")
            print("Your previous guesses: " + str(guess_lists_dict))
            correct = 0
            location = 0
            if tries == 9:
                hint = input("Would you like a hint? (y/n): ")
                if hint == "y": 
                    print("The sum of all the correct numbers is: " + str(sum(rand_nums_list)))
                else:
                    print("You got this!")            

            if tries == 10:
                print("Game over! Here is the correct answer: " + str(rand_nums_list))
                retry = input("Do you want to play again? Please enter y or n: ")
                if retry == "y":
                    master_mind()
                else:
                    sys.exit("Thank you for playing!")                
                
    if numbers == 5:
    # data = {'jsonrpc':'2.0','method':'GET','params': {'apiKey':api_key,'n':4,'min':0,'max':7,'col':1,'base':10,'format':'plain','rnd':'new'},'id':1}
        data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey':api_key,'n':5,'min':0,'max':7,'replacement':'true','base':10},'id':1}

        params = json.dumps(data)

        response = requests.post(url,params)

        # print(response.text)
        # print(type(response.content))
        # print(type(response.content))

        rand_nums_dict = json.loads(response.content)
        # print((rand_nums_dict['result']['random']['data']))
        rand_nums_list = rand_nums_dict['result']['random']['data']

        print(rand_nums_list)

        correct = 0
        location = 0
        tries = 0
        guess_lists_dict = {}
        while location < 5:
            print("Please guess numbers between 0 and 7.")
            while True:
                guess1 = (input("Enter first digit: "))
                if guess1 == "quit":
                    sys.exit("Goodbye, thanks for playing!")
                if integer_check(guess1):
                    guess1 = int(guess1)
                    if len(str(guess1)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7.")
            
            while True:
                guess2 = (input("Enter second digit: "))
                if guess2 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess2):
                    guess2 = int(guess2)
                    if len(str(guess2)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")
                
            while True:
                guess3 = (input("Enter third digit: "))
                if guess3 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess3):
                    guess3 = int(guess3)
                    if len(str(guess3)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")
            
            while True:   
                guess4 = (input("Enter fourth digit: "))
                if guess4 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess4):
                    guess4 = int(guess4)
                    if len(str(guess4)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")
            
            while True:   
                guess5 = (input("Enter fifth digit: "))
                if guess5 == "quit":
                    sys.exit("Goodbye, thanks for playing!")                
                if integer_check(guess5):
                    guess5 = int(guess5)
                    if len(str(guess5)) == 1:
                        break
                    else:
                        print("Please enter only one digit as your first guess.")
                else:
                    print("Please enter a number between 0 and 7 an you entered")

            tries += 1
            tries_hash = {1:"First", 2:"Second", 3:"Third", 4:"Fourth", 5:"Fifth", 6:"Sixth", 7:"Seventh", 8:"Eigth", 9:"Ninth", 10:"Tenth"}

            guess_lists_dict[tries_hash[tries]] = [guess1, guess2, guess3, guess4, guess5]

            current_guess = guess_lists_dict[tries_hash[tries]]

            print("Current guess: ", current_guess)
            print("Guess List: ", guess_lists_dict[tries_hash[tries]])

            if current_guess == rand_nums_list:
                print("You won!")
                retry = input("Do you want to play again? Please enter y or n: ")
                if retry == "y":
                    master_mind()
                else:
                    sys.exit("Thank you for playing!")
                                
            
            decr_randnums_list = rand_nums_list.copy()
            decr_randnums_hash = {k: v for k, v in enumerate(decr_randnums_list)}

            print("Decrementing hash",decr_randnums_hash)
            
            print(current_guess)
            print(decr_randnums_list)

            n = 0
            while n < 5:
                print("decrementing list",decr_randnums_list)
                print("Decrementing hash",decr_randnums_hash)

                if current_guess[n] in decr_randnums_list:
                    decr_randnums_hash = {k: v for k, v in enumerate(decr_randnums_list)}
                    correct += 1
                    correct_digit_index = list(decr_randnums_hash.keys())[list(decr_randnums_hash.values()).index(current_guess[n])]
                    decr_randnums_list.pop(correct_digit_index)
                if current_guess[n] == rand_nums_list[n]:
                    location += 1
                n += 1
        
            print("You guessed " + str(correct) + " number(s) correctly and " + str(location) +" location(s) correctly.")
            print("You have " + str(10 - tries) + " tries left!")
            print("Your previous guesses: " + str(guess_lists_dict))
            correct = 0
            location = 0
            if tries == 9:
                hint = input("Would you like a hint? (y/n): ")
                if hint == "y": 
                    print("The sum of all the correct numbers is: " + str(sum(rand_nums_list)))
                else:
                    print("You got this!")            

            if tries == 10:
                print("Game over! Here is the correct answer: " + str(rand_nums_list))
                retry = input("Do you want to play again? Please enter y or n: ")
                if retry == "y":
                    master_mind()
                else:
                    sys.exit("Thank you for playing!")
     
