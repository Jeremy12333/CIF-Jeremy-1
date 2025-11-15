from random import randint

hp_point = 10
questions_counter = 0

# ----------------------------------------
# CANADA QUESTIONS + ANSWER LISTS
# ----------------------------------------
def question_bank():
    questions= [
    ["What is the capital of Canada?", ["Ottawa", "ottawa"]],
    ["What leaf is on the Canadian flag?", ["Maple", "maple", "Maple Leaf", "maple leaf"]],
    ["What is Canada's national animal?", ["Beaver", "beaver"]],
    ["Which province is the largest by area?", ["Quebec", "quebec"]],
    ["What is the northernmost territory?", ["Nunavut", "nunavut"]],
    ["What is Canada's official summer sport?", ["Lacrosse", "lacrosse"]],
    ["What is Canada's official winter sport?", ["Hockey", "hockey", "Ice Hockey", "ice hockey"]],
    ["Which ocean is to the east of Canada?", ["Atlantic", "atlantic", "Atlantic Ocean", "atlantic ocean"]],
    ] 
    return questions
my_questions= question_bank()
# ----------------------------------------
# ----------------------------------------
while (hp_point > 0) and (hp_point < 18):

    questions_counter += 1

    my_question = my_questions[randint(0, 7)]

    # formats the question
    my_prompt = "Question: " + str(questions_counter) + ". " + my_question[0]

    # ask user
    my_answer = input(my_prompt + "\n> ")
    correct = False

    for answer in my_question[1]:

        if my_answer == answer:
            correct= True
            break 
    if correct == True :
        hp_point += 3
        print("\tCorrect. You earned 3 points. Your HP is", hp_point)
            
    else:
        hp_point -= 3
        print("\tIncorrect. You lost 3 points. Your HP is", hp_point)
        

# ----------------------------------------
# END OF GAME
# ----------------------------------------
if hp_point <= 0:
    print("\nGAME OVER — you ran out of HP!")
else:
    print("\nYOU WIN — you reached 18 HP!")