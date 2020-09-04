import random

def generate_code():
    '''This function generates a 4 digit code without duplicates'''
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

def getting_input():
    '''This function gets input from a user'''
    global answer
    answer = input("Input 4 digit code: ")
    if len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        0/0

def checking_the_result():
    '''This function checks the user's input and compares it to the code generate'''
    global correct_digits_and_position,correct_digits_only
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

def showing_results():
    '''This function prints out the result of the checking'''
    global turns
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    turns += 1 

def check_for_win():
    '''This function checks for the win'''
    global correct
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))  

# TODO: Decompose into functions
def run_game():
    '''This function is the main function where it calls other functions'''
    global turns,answer,correct
    generate_code()
    correct = False
    turns = 0
    while not correct and turns < 12:
        try:
           getting_input() 
        except:
            continue
        checking_the_result()
        showing_results()
        check_for_win()
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()
