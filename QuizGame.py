#-----------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("____________________")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("enter (A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    
    display_score(correct_guesses,guesses)
#-----------------
def check_answer(answer , guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong :( ")
        return 0 
#-----------------
def display_score(correct_guesses , guesses ):
    print("____________________")
    print("RESULTS")
    print("____________________")
    print("answers : ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses : ",end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(" Your score is : " + str(score)+"%")
#-----------------
def Play_again():
    response = input("do you want to play again? (YES/NO) : ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#-----------------
questions = {
 "who created python? : ":"A",
 "what yaer was python created? :" : "B",
 "python is tributed to which comedy group? :": "C",
 "is the earth round? : ":"A",
 "What is the capital of France? : ":"A"}
#-----------------
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"],
          ["A. Paris", "B. London", "C. Berlin", "D. Madrid"]]
new_game()
print()
while Play_again():
    new_game()
print("byee")