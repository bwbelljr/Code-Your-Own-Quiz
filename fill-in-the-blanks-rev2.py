# IPND Stage 2 Final Project
# Bob Bell
# 13 January 2018 (Revision 2)

def prompt_for_difficulty():
    """
    Function that prompts the user for difficulty level
    Input(s):
                none
    Behavior:
                Asks user for difficulty level
                Takes input, converts to lowercase characters, and returns
    Output(s):
                user_string: level entered by user in lowercase letters
    """
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    user_string = raw_input() # prompt for user input
    user_string = user_string.lower() # converts input to lowercase
    return user_string

def valid_difficulty_level(difficulty, difficulty_levels):
    """
    Function checks that string for difficulty level is valid and repeatedly
    prompts for valid string otherwise
    Input(s):
                difficulty: user-generated difficulty level
                difficulty_levels: list of valid difficulty levels
    Behavior:
                tests that user-generated difficulty level is valid
                if valid, return user-generated difficulty level
                if not valid, call prompt_for_difficulty() for valid level
    Output(s):
                difficulty: valid user-generated difficulty level
    """
    while difficulty not in difficulty_levels:
        print "That's not an option!"
        difficulty = prompt_for_difficulty()
    return difficulty

def display_sample(sample):
    """
    Function that prints sample text for quiz
    Input(s):
                sample: sample text for quiz
    Behavior:
                prints sample text preceded by message "The current paragraph.."
    Output(s):
                none
    """
    # printing the sample text
    print "The current paragraph reads as such:"
    print sample # print sample text for user

def convert_to_quiz_string(index):
    """
    Function creates string from an index
    For example, if the index=5, this function creates the string "__5__"
    This is useful for parsing thw quiz string
    Input(s):
                index: number that we want to convert to a string
    Behavior:
                Uses index to create a string "__[index]__"
    Output(s):
                quiz_string: this string "__[index]__" is returned
    """
    quiz_string = "_"*2 + str(index) + "_"*2
    return quiz_string

def test_for_answer(index, answers):
    """
    Function tests if the user input matches the answer string
    Input(s):
                index: represents the index of the word we are testing
                answers: list representing the answers to all words in quiz
    Behavior:
                Convert current index to quiz_string (index=0 is __1__)
                Prompt user for string to be substituted for quiz_string
                Take user input, convert to lowercase, store in answer_string
                Check that answer_string equals actual answer
    Output(s):
                True/False: returns True if user's answer is actual answer
    """
    quiz_string = convert_to_quiz_string(index+1)

    # Prompt the user for the string that should be substituted for quiz_string
    print
    print
    print "What should be substituted in for", quiz_string + "?",
    answer_string = raw_input()
    answer_string = answer_string.lower() # converts input to lowercase

    # if answer_string==answers[index]:
    if answer_string==answers[index].lower(): # ensures the same case
        return True
    else:
        return False

def correct_message():
    """
    Function prints "Correct!" with additional lines for readability
    Input(s):
                none
    Behavior:
                print new line, "Correct!" message, and another new line
    Output(s):
                none
    """
    # print Correct! message
    print
    print "Correct!"
    print

def you_won_message():
    """
    Function prints "You won!" with additional lines for readability
    Input(s):
                none
    Behavior:
                print new line, "You won!" message, and another new line
    Output(s):
                none
    """
    # print You Won! message
    print
    print "You won!"
    print

def answer_correct(index, sample_answers, sample, num_answer):
    """
    Function prints appropriate message(s) if user-generated answers are correct
    and replaces all instances of the quiz string (e.g., __1__) with the
    actual answer
    Input(s):
                index: index for the quiz word we are currently evaluating
                sample_answers: list of actual answers to the quiz
                sample: current quiz text
                num_answer: total number of answers to fill in for the quiz
    Behavior:
                prints correct message, replaces quiz string (e.g., __1__) with
                actual answer, prints sample text, and prints "You Won!"
                message if the current index represents the last question in
                our quiz
    Output(s):
                sample: updated quiz text
    """
    # Inform the user her/his answer is correct
    # and return updated sample and remaining_attempts
    correct_message()

    # Convert index into quiz_string
    quiz_string = convert_to_quiz_string(index+1)

    # Based on Madlibs code, replace quiz_string with actual answer
    sample = sample.replace(quiz_string, sample_answers[index])

    print sample # print updated sample for user to see
    if index == num_answer-1: # print "Won" statement if all answers correct
        you_won_message()
    return sample

def answer_incorrect(remaining_attempts, index, num_answer):
    """
    Function handles case when the user's answer is incorrect
    Input(s):
                remaining_attempts: number of remaining attempts for question
                index: index for the quiz word we are currently evaluating
                num_answer: total number of answers to fill in for the quiz
    Behavior:
                if remaining_attempts is 1, print special message
                if remaining_attempts is 0, print special message and set
                    index=num_answer to exit while loop (where index < num_answer)
                if remaining attempts is any other number, print standard
                    message
    Output(s):
                i: return index for while loop (which depends on value of i)
    """
    if remaining_attempts == 1: # special message for 1 attempt left
        print "That isn't the correct answer! You only have", remaining_attempts, "try left! Make it count!"
        print
        display_sample(sample)
    elif remaining_attempts == 0: # special message for no more attempts
        print "You've failed too many straight guesses!  Game over!"
        index = num_answer
    else: # standard message
        print "That isn't the correct answer! Let's try again; you have", remaining_attempts, "trys left!"
        print
        display_sample(sample)
    return index

def run_quiz(num_answer, sample_answers, sample):
    """
    Function runs the main quiz code
    Input(s):
                num_answer: total number of answers to fill in for the quiz
                sample_answers: list of actual answers to the quiz
                sample: current quiz text
    Behavior:
                instantiates index to count through all quiz questions
                for each quiz question, gives 5 remaining_attempts
                tests whether user answers are valid. if so, moves on to next
                    question. if not, provides attempts until they run out
    Output(s):
                none
    """
    # initialize index variable to loop through the strings for the quiz
    index = 0
    while index < num_answer: # while we have not completed all quiz answers
        remaining_attempts = 5 # initialize number of attempts per question
        while remaining_attempts > 0:
            if test_for_answer(index, sample_answers): # test that user gives right answer
                sample = answer_correct(index, sample_answers, sample, num_answer)
                remaining_attempts=0 # we get out of loop if answer is correct
            else: # here, the user did not enter the right anwer
                #### CREATE FUNCTION FOR THIS SECTION OF CODE ####
                remaining_attempts = remaining_attempts-1 #decrement
                index = answer_incorrect(remaining_attempts, index, num_answer)
        index = index + 1 # increment index

# Procedural code starts here

difficulty = prompt_for_difficulty() # assigns formatted string to difficulty
difficulty_levels = ["easy", "medium", "hard"]

difficulty = valid_difficulty_level(difficulty, difficulty_levels)

# Once user has chosen valid difficulty level, print statement
print "You've chosen " + difficulty + "!", "\n"
print "You will get 5 guesses per problem", "\n"

# Depending on difficulty level, assign appropriate sample and answers
# Using dictionary data structure to add another layer of abstraction

game_data = {
    'easy':{
        'sample':'''A common first thing to do in a language is display 'Hello __1__!'
In __2__ this is particularly easy; all you have to do
is type in: __3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.
It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.''',
        'sample_answers': ["world", "Python", "print", "HTML"]
    },
    'medium':{
        'sample': '''A __1__ is created with the def keyword. You specify the inputs a __1__ takes by
adding __2__ separated by commas between the parentheses. __1__s by default return __3__ if you
don't specify the value to return. __2__ can be standard data types such as string, number, dictionary,
tuple, and __4__ or can be more complicated such as objects and lambda functions.''',
        'sample_answers': ["function", "arguments", "none", "list"]
    },
    'hard':{
        'sample': '''__1__ is a computer programming language that is __2__ instead
__3__. You benefit with __4__ __5__s and improved productivity.  However,
some people prefer __3__ languages because they run much faster and are
typically better for production systems. However, let's not worry about this
for now, but simply enjoy learning to code in __1__ on __6__.''',
        'sample_answers': ["Python", "interpreted", "compiled", "dynamic", "type", "Udacity"]
    }
}

sample = game_data[difficulty]['sample']
sample_answers = game_data[difficulty]['sample_answers']

display_sample(sample)

num_answer = len(sample_answers) # number of strings to guess for the sample

run_quiz(num_answer, sample_answers, sample)
