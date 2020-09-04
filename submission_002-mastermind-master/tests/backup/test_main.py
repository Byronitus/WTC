import unittest
from test_base import captured_io
from io import StringIO
import mastermind


class MyTestCase(unittest.TestCase):
    def test_correct(self):
        mastermind.random.randint = lambda a, b: 0

        with captured_io(StringIO('0000\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! Your are a codebreaker!
The code was: [0, 0, 0, 0]""", output)

    def test_too_long(self):
        mastermind.random.randint = lambda a, b: 0

        with captured_io(StringIO('12345\n0000\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! Your are a codebreaker!
The code was: [0, 0, 0, 0]""", output)

    def test_too_short(self):
        mastermind.random.randint = lambda a, b: 0

        with captured_io(StringIO('123\n0000\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! Your are a codebreaker!
The code was: [0, 0, 0, 0]""", output)

    def test_2_turns(self):
        mastermind.random.randint = lambda a, b: 0

        with captured_io(StringIO('1111\n0000\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Number of correct digits in correct place:     0
Number of correct digits not in correct place: 0
Turns left: 11
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! Your are a codebreaker!
The code was: [0, 0, 0, 0]""", output)


if __name__ == '__main__':
    unittest.main()
