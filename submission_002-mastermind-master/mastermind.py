import random
from random import randint


def run_game():
    """
    TODO: implement Mastermind code here
    """
    wrong = False
    list_of_nums = ['0','0','0','0']
    count = 0
    num_of_guesses = 12
    while count < 4 :
        list_of_nums[count] = random.randint(1,8)
        count2 = count -1
        while count2 >= 0:
            if list_of_nums[count] == list_of_nums[count2]:
                count = count - 1
            count2 = count2 - 1
        count = count + 1
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    while num_of_guesses > 0:
        check = False
        while check == False:
            count = 0
            check2 = True
            user_input = input('Input 4 digit code: ')
            while count < 4:
                if len(user_input) == 4:
                    temp = user_input[count]
                    if temp not in ['1','2','3','4','5','6','7','8']:
                        check2 = False
                count = count + 1
            if len(user_input) == 4 and check2 == True:
                check = True
            elif len(user_input) != 4:
                print('Please enter exactly 4 digits.')
        user_input = list(map(int, user_input))
        count = 0
        num_in_correct_place = 0
        temp_list = list_of_nums.copy()
        while count < 4:
            if user_input[count] == temp_list[count]:
                num_in_correct_place = num_in_correct_place + 1
                temp_list[count] = ' '
            count = count + 1
        num_in_incorrect_place = 0
        count = 0
        while count < 4:
            count2 = 0
            while count2 < 4:
                if user_input[count] == temp_list[count2]:
                    num_in_incorrect_place = num_in_incorrect_place + 1
                    temp_list[count2] = ' '
                count2 = count2 + 1
            count = count + 1
        print('Number of correct digits in correct place:     ' + str(num_in_correct_place))
        print('Number of correct digits not in correct place: ' + str(num_in_incorrect_place))
        if user_input == list_of_nums:
            print('Congratulations! You are a codebreaker!')
            print('The code was: ' + ''.join(map(str, list_of_nums)))
            break
        else:
            wrong = True
        if wrong == True:
            num_of_guesses = num_of_guesses - 1
            print('Turns left: ' + str(num_of_guesses))
    

    pass


if __name__ == "__main__":
    run_game()
