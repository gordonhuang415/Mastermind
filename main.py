import requests
import sys
import json
from config import api_key
import constants


def select_difficulty():
    """
    The select_difficulty function allows the user to choose a
    difficulty that will determine the number of digits the user
    needs to guess with easy being 3 digits, normal being 4, and
    hard being 5.

    Returns:
        integer: This number will represent the number of digits the
        user needs to guess
    """
    digits = 0
    while digits == 0:
        diff = input(
            "Please enter the desired difficulty level (easy, normal, hard): "
            )
        if diff.lower() == "easy":
            digits = constants.EASY_DIGIT_NUM
        elif diff.lower() == "normal":
            digits = constants.NORMAL_DIGIT_NUM
        elif diff.lower() == "hard":
            digits = constants.HARD_DIGIT_NUM
        else:
            print("Please type either 'easy', 'normal', or 'hard'.")
    return digits


def validate_input(s):
    """
    valid_input(s) is used to validate the input for each guess. The try
    and except block is used to verify if the input is an integer with the
    if statements verifying that the integer is between 0 and 7 and a single
    digit. Any value error will return false.

    Args:
        s (integer): This represents the input from the user.

    Returns:
        boolean: This will return True if the input satisfies all requirements.
    """
    try:
        int(s)
        if len(str(s)) == 1:
            if int(s) <= constants.MAX_NUM_SELECT:
                if int(s) >= constants.MIN_NUM_SELECT:
                    return True
                else:
                    print("Please enter a number between 0 and 7.")
            else:
                print("Please enter a number between 0 and 7.")
        else:
            print(
                "Please enter only one digit between 0 and 7 as your guess."
            )
    except ValueError:
        print("Please enter a number between 0 and 7.")
        return False


def random_generator():
    """
    random_generator returns the list of randomly generated numbers
    using the random.org API. The select_difficulty() function is used
    to determine the input for the n parameter.

    Returns:
        list: A list of randomly generated numbers from the API
        integer: The number of digits the user needs to guess
    """
    numbers = select_difficulty()
    print("Type 'quit' at anytime to exit the game.")
    url = 'https://api.random.org/json-rpc/1/invoke'
    data = {
        'jsonrpc': '2.0',
        'method': 'generateIntegers',
        'params': {
         'apiKey': api_key,
         'n': numbers,
         'min': 0,
         'max': 7,
         'replacement': 'true',
         'base': 10
         },
        'id': 1
        }
    params = json.dumps(data)
    response = requests.post(url, params)
    rand_nums_dict = json.loads(response.content)
    rand_nums_list = rand_nums_dict['result']['random']['data']
    return rand_nums_list, numbers


def ask_hint(lst):
    """
    ask_hint will prompt the user to enter y or n to recieve a hint. This
    will run when the tries counter == 9, asking if the user would like a hint.
    Any input other than y or n will rerun the ask_hint() function.
    Args:
        lst (list): A list of the randomly generated numbers

    Returns:
        boolean: Returns True if the user enters y for a hint. Returns
        False if the user enters n for a hint. Any other input will rerun
        the function.
    """
    hint = ""
    while hint.lower != "y" or hint.lower != "n":
        hint = input("Would you like a hint? (y/n): ")
        if hint.lower() == "y":
            print("The sum of all the correct numbers is: " +
                  str(sum(lst)))
            break
        elif hint.lower() == "n":
            print("You got this!")
            break
        else:
            print("Please type 'y' or 'n'")
            ask_hint(lst)
    return True


def retry_game():
    """
    retry_game prompts the user to enter y or n if they
    want to play mastermind again. If y is selected, master_mind()
    is run on the next line.
    Returns:
        boolean: Returns True if y is entered to play the game again.
        Any other input returns false.
    """
    retry = input("Do you want to play again? Please enter y or n: ")
    if retry.lower() == "y":
        return True
    else:
        False


def check_guesses(numbers, order_hash):
    """
    This function validates the guesses made by the user
    using the validate_input() function and creates
    a list with those inputs.
    
    Args:
        numbers (int): The numbers variable from the
        select_difficulty() function
        order_hash (dictionary): A dictionary used to
        assign each guess with a corresponding ordinal
        placement

    Returns:
        list: A list of guesses the user made this attempt
    """
    guess_list = [None] * numbers
    n = 0
    while n < numbers:
        while True:
            guess_list[n] = (input("\nEnter " + order_hash[n] + " digit: "))
            if guess_list[n] == "quit":
                sys.exit("Goodbye, thanks for playing!")
            if validate_input(guess_list[n]):
                guess_list[n] = int(guess_list[n])
                break
        n += 1
    return guess_list


def check_victory(current_guess_list, rand_nums_list):
    """
    This function checks if the list of current guesses is equal to the
    list of randomly generated numbers.
    Args:
        current_guess_list (list): A list of the current guesses
        rand_nums_list (list): A list of the randomly generated numbers
    """
    if current_guess_list == rand_nums_list:
        print("You won!")
        if retry_game():
            master_mind()
        else:
            sys.exit("Thank you for playing!")


def master_mind():
    """
    master_mind is the main function where a majority of the code
    for the game is. The function is run in the mastermind.py file in the
    terminal.
    """
    print("Welcome to the Mastermind game!")
    rand_nums_list, numbers = random_generator()
    correct = 0
    location = 0
    tries = 0
    guess_lists_dict = {}
    order_hash = {
        0: "First",
        1: "Second",
        2: "Third",
        3: "Fourth",
        4: "Fifth"
        }
    while location < numbers:
        print("Please guess numbers between 0 and 7.\n")
        guess_list = check_guesses(numbers, order_hash)

        tries += 1

        tries_hash = {
            1: "First",
            2: "Second",
            3: "Third",
            4: "Fourth",
            5: "Fifth",
            6: "Sixth",
            7: "Seventh",
            8: "Eigth",
            9: "Ninth",
            10: "Tenth"
            }

        guess_lists_dict[tries_hash[tries]] = guess_list

        check_victory(guess_list, rand_nums_list)

        copy_randnums_list = rand_nums_list.copy()

        n = 0
        while n < numbers:
            if guess_list[n] in copy_randnums_list:
                correct += 1
                correct_digit_index = copy_randnums_list.index(
                    guess_list[n]
                    )
                copy_randnums_list.pop(correct_digit_index)
            if guess_list[n] == rand_nums_list[n]:
                location += 1
            n += 1

        print("\nYou guessed " + str(correct) + " number(s) correctly and " +
              str(location) + " location(s) correctly.")
        print("You have " + str(10 - tries) + " tries left!")
        print("Your previous guesses: " + str(guess_lists_dict) + "\n")
        correct = 0
        location = 0
        if tries == 9:
            ask_hint(rand_nums_list)
        if tries == 10:
            print("Game over! Here is the correct answer: " +
                  str(rand_nums_list))
            if retry_game():
                master_mind()
            else:
                sys.exit("Thank you for playing!")
