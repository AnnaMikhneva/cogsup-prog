"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
"""
Computer guesses a number that the human is thinking of between 1 and 100.
The computer uses a binary search algorithm to efficiently guess the number.
"""

def get_human_feedback(guess):

    while True:
        feedback = input(f"Is your number {guess}? (Enter 'correct', 'too high', or 'too low'): ").lower().strip()
        if feedback in ['correct', 'too high', 'too low']:
            return feedback
        else:
            print("Please enter only 'correct', 'too high', or 'too low'.")

def computer_guesses_number():

    print("Think of a number between 1 and 100. I will try to guess it!")
    print("After each guess, tell me if my guess is 'correct', 'too high', or 'too low'.\n")
    

    low = 1
    high = 100
    attempts = 0
    
    while low <= high:

        guess = (low + high) // 2
        attempts += 1
        

        feedback = get_human_feedback(guess)
        
        if feedback == 'correct':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts!")
            return
        
        elif feedback == 'too high':

            high = guess - 1
            print("Okay, I'll guess lower next time.")
        
        elif feedback == 'too low':

            low = guess + 1
            print("Okay, I'll guess higher next time.")
    

    print("Hmm, I couldn't find your number. Did you give me consistent feedback?")


if __name__ == "__main__":
    computer_guesses_number()