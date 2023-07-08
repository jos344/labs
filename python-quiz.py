questions = [
    'what is 1 + 1?',
    'what is 2 + 2?',
    'what is 3 + 3?',
    'what is 4 + 4?',
]
user_answers = []

correct_answers = [
    2,
    4,
    6,
    8,
]
def menu():
    """welcome menu"""
    print('welcome to math quiz')

def ask_questions():
    """ask question from user"""
    for question in questions:
        print(question)
        while True:
            try:
                user_answers.append(int(input()))
                break
            except ValueError:
                user_answers.pop            
                print('wrong option, please enter a number')
                print(question)
                pass
                        
def get_score(user_answers, correct_answers):
    """compare the answers from the user with correct answers"""
    score = []
    for i in range(4):    
        if user_answers[i] == correct_answers[i]:
            score.append(1)
    return sum(score)

def get_wrong_answers(user_answers, correct_answers):
    wrong_answers = []
    for i in range(4):
        if user_answers[i] != correct_answers[i]:
            wrong_answers.append(i)
    return wrong_answers

def show_result():
    """show user the result of quiz and if passed or failed"""
    print('================ SCOREBOARD ====================')
    total_score = get_score(user_answers, correct_answers)
    print(f'Your score is {total_score}')

    if total_score >= 3:
        print('you pass the quiz')
    elif total_score < 3:
        print('you fail the quiz')

    wrong = get_wrong_answers(user_answers, correct_answers)
    for i in wrong:
        print(f'You answered question {i+1} incorrectly')

menu()
ask_questions()
show_result()
