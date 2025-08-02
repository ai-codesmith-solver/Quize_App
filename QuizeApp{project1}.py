import random
import time 
import pyfiglet

RESET = "\033[0m"
YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"

def quize():

    # Displaying a welcome message using pyfiglet
    banner=pyfiglet.figlet_format("Welcome to Code Quiz Master!")
    print(YELLOW + banner + RESET)

    n=input("What's your name? >> ")
    print(f"\nHi {n}! Let's start the quiz. \n")
    print("You will be asked 10 questions \n")
    print("You will get 1 point for each correct answer \n")

    ques=[{"question": "What is the output of: print('Hello' + 'World')?",
            "options": ['a) HelloWorld', 'b) Hello World', 'c) Hello+World', 'd) Error'],
            "answer": "a"},

        {"question": "Which function is used to take input from user in Python?",
            "options": ['a) scanf()', 'b) input()', 'c) get()', 'd) read()'],
            "answer": "b"},

            {"question": "Which symbol is used to make a comment in Python?",
            "options": ['a) //', 'b) <!-- -->', 'c) #', 'd) /* */'],
            "answer": "c"},
            {
            "question": "What is the result of: type('5')?",
            "options": ['a) int', 'b) str', 'c) float', 'd) bool'],
            "answer": "b"},
        {
            "question": "Which escape character is used for a new line?",
            "options": ['a) \\t', 'b) \\a', 'c) \\n', 'd) \\b'],
            "answer": "c"},

            {"question":" All keywords in Python are in _________",
            "options": ['a) Capitalized','b) lower case','c) UPPER CASE','d) None of the mentioned'],
            "answer":"d"},

            {"question":"Which of the following is used to define a block of code in Python language?",
            "options":['a) Indentation','b) Key','c) Brackets','d) All of the mentioned'],
            "answer":"a"},

            {"question":"Which keyword is used for function in Python language?",
            "options":['a) Function','b) def','c) Fun','d) Define'],
            "answer":"b"},

            {"question":"Which of the following is not a core data type in Python programming?",
                "options":['a) Tuples','b) Lists','c) Dictionary','d) Class'],
                "answer":"d"},

                {"question":"What is the output of the following code? print(type([]) is list)",
                "options":['a) True','b) False','c) Error','d) None'],
                "answer":"a"}
    ]

    random.shuffle(ques) #shuffles the questions

    score=0
    #Quiz loop
    val=input(f"Are you ready {n} :").lower()
    if val=="yes":
        for i,q in enumerate(ques):
            print(f"{i+1}. {q['question']}")
            for opt in q['options']:
                print(opt)

            #time 

            print(RED+"⏱️ You have 10 seconds to answer..."+RESET)
            start=time.time()
            
            ans=input("Your answer: ").strip().lower()
            t=time.time()-start

            if t>=10:
                print(RED+"⌛ Time's up!"+RESET)
                print(BLUE+"This will not be count\n"+RESET)
                continue    

            elif ans==q['answer']:
                print(GREEN+"\nCorrect!"+RESET)
                score+=1
                print("\n")
            else:
                print(RED+f"Wrong! \nThe correct answer is: {q['answer']}"+RESET)
                print("\n")
            

    print(YELLOW+f"Your score is: {score}/{len(ques)}"+RESET)
    print("\n")
    per=(score/len(ques))*100
    print(CYAN+f"Your percentage is: {per}%"+RESET)

    #position check
    if score==len(ques):
        print(GREEN+"🎉 Excellent! You're a Python pro!"+RESET)
    elif score>=5:
        print(YELLOW+"👍 Good job! Keep practicing."+RESET)
    else:
        print(BLUE+"💡 Keep learning. You're getting there!"+RESET)

    # To retry
    print("\n")
    retry=input("\nDo you want to try again? (yes/no): ").strip().lower()

    if retry=="yes":
        quize()
    else:
        print("Thnaks for playing! 👋")

quize() #start the quiz

