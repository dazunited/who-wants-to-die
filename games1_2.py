
import sys 
import random
import msvcrt
import time
import os




questions_easy = [
    {
        "question": "In which European city would you find the city of Orly?",
        "options": ["A) Paris B) Barcelona C) Indonesia D) Belfast"],
        "answer": "A"
    },
    {
        "question": "What is the average height in the UK?",
        "options": [" A) 5ft 10in B) 6ft 2in C)7ft 3in D) 8ft 9in"],
        "answer": "A"
    },
    {
        "question": "How many people on Earth?",
        "options": ["A) 7,5 billion  B) 3,4 billion C) 7 million D) 149 million"],
        "answer": "A"
    },
    {
        "question": "What countries make Great Britain?",
        "options": ["A) Germany, Wales, France B) London, Manchester, England C) England, Scotland, wales D) England, Wales, Scotland and northern Ireland"],
        "answer": "C"
    },
    {
        "question": "How many signs are there in the Zodiac?",
        "options": ["A) 15 B) 11 C) 12 D) 14"],
        "answer": "C"
    },
    {
        "question": " What did Adam eat from the forbidden tree?",
        "options": ["A)The tree itself B) A Leaf C) Apple D) Adam Sandler"],
        "answer": "C"
    },
    {
        "question": " What is your body's largest organ?",
        "options": ["A) Skin B) brain C) stomach D) heart"],
        "answer": "A"
    },
    {
        "question": " How many cm in a millimeter?",
        "options": ["A) 10000mm in 1cm B) 200cm in 1mm C) 0.1cm in 1mm D) 0.2cm in 1mm"],
        "answer": "C"
    },
    {
        "question": "What is the name of the bird on the social media platform Twitter",
        "options": ["A) Bob B) Jason Derulo C) Larry D) Jackson"],
        "answer": "A"
    },
    {
        "question": "What can one catch that is not thrown?",
        "options": ["A) A bobsleigh team B) A spear C) Baby giraffe D) A cold"],
        "answer": "D"
    },
    {
        "question": "What Netflix show has the most streaming views in 2021",
        "options": ["A) Squid Game B) Lupin C) Bridgerton  D) Money Heist"],
        "answer": "A"
    },
    {
        "question": "If your mother has 4 kids North, East, South…. What is the name of the last child?",
        "options": ["A) Brad Pitt   B) Your mum  C) You  D) West"],
        "answer": "C"
    },
    {
        "question": "Zurich is the capital of which country",
        "options": ["A) Germany B) United Kingdom C) Africa D) Switzerland"],
        "answer": "D"
    },
    {
        "question": "What do you call a woman who knows where her husband is all the time?",
        "options": ["A) Paranoid B) A widow C) Happy lady D) Superwoman"],
        "answer": "B"
    },
    {
        "question": "How many days are in a leap year?",
        "options": ["A) 365 B) 356 C) 366 D) 369"],
        "answer": "C"
    },
    {
        "question": "What never asks a question but gets answered",
        "options": ["A) The Doorbell   B) A letter   C) A Post card    D) The Phone"],
        "answer": "A"
    }
]

questions_medium = [
    {
        "question": "What type of energy does an unlit match have?",
        "options": ["A) Kinetic Energy B) Potential Energy C) Electrical Energy D) Thermal Energ"],
        "answer": "B"
    },
    {
        "question": "How many Bronte sisters were there?",
        "options": ["A)3 B)7 C) 141 D) 16"],
        "answer": "A"
    },
    {
        "question": "What year did World War II end?",
        "options": ["A)1945 B)1845 C)1941 D)1967"],
        "answer": "A"
    },
    {
        "question": "Which country has the largest population in the world?",
        "options": ["A) India    B)  Russia    C) USA   D) China"],
        "answer": "D"
    },
    {
        "question": " Muhammed Ali is best known in which sport?",
        "options": ["A) Boxing B) Football C) NASCAR D) Wrestling"],
        "answer": "A"
    },
    {
        "question": "Pure gold is how many carats?",
        "options": ["A) 24 carats B) 21 C) Mike wozaowski D) 44"],
        "answer": "A"
    },
    {
        "question": " What is your body's largest organ?",
        "options": ["A) Skin B) brain C) stomach D) heart"],
        "answer": "A"
    },
    {
        "question": "What is the name of the biggest technology company in South Korea?",
        "options": ["A) Samsung B) Xiaomi C) Vivo D) Huawei"
],
        "answer": "A"
    },
    {
        "question": "How many bones are in the human body?",
        "options": ["A) 252 B) 97 C) 206 D) 310"],
        "answer": "C"
    },
    {
        "question": "Which store chain sells the most sandwiches per year?",
        "options": ["A) Tesco B) Sainsburys C) Subway D) Aunt Maggies Swag Sandwiches"],
        "answer": "C"
    },
    {
        "question": "How long can a person live without water?",
        "options": ["A) About 3 day B) About 1 day C) About 1 week D) About 2 weeks"],
        "answer": "A"
    },
    {
        "question": "What is the name of the largest country in the world?",
        "options": ["A) China B) India C) Russia D) Africa"],
        "answer": "C"
    },
    {
        "question": "What was the first Disney princess?",
        "options": ["A) Elsa B) Snow White C) Peach D) Diana"],
        "answer": "B"
    },
    {
        "question": "What does 9+10 equal?",
        "options": ["A) 17 B) 28 C) 21 D) 19"],
        "answer": "D"
    },
    {
        "question": "How many days does it take for the Earth to orbit the Sun?",
        "options": ["A) 365 b) 678 c) 411 d)730"],
        "answer": "A"
    },

]

questions_hard = [
    {
        "question": "What colour are the sunsets on Mars?",
        "options": ["A) Yellow B) Orange C) Blue D) Purple"],
        "answer": "C"
    },
    {
        "question": "What year was saxophone invented?",
        "options": [" A) 1846 B) 1947 C) 1283 D) 2003"],
        "answer": "A"
    },
    {
        "question": "What's the smallest country in the world?",
        "options": [" A) The Vatican B) The Monako C) The Palau D) Tonga"],
        "answer": "A"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["A) Neil Degracy B) Isaac Newton C) Nicolaus Copernicus D) Alexander Fleming"],
        "answer": "D"
    },
    {
        "question": "What is Maralyn Monroe's Natural hair colour",
        "options": ["A) Blonde B) Red C) Black D) Brown"],
        "answer": "B"
    },
    {
        "question": " What day do lions eat?",
        "options": ["A) Friday B) Wednesday C) On the break D) Chewsday"],
        "answer": "D"
    },
    {
        "question": " When did they open the London underground?",
        "options": [" A) 1863 B) 1954 C) 1877 D) 1930"],
        "answer": "A"
    },
    {
        "question": " Which cartoon character lives in a pineapple under the sea?",
        "options": ["A) Nemo B) Milo  C) Spongebob Squarepants  D)Johnny Test"],
        "answer": "C"
    },
    {
        "question": "What country is wider than the moon?",
        "options": ["A) United States B) Mexico C) Russia D) Australia"],
        "answer": "D"
    },
    {
        "question": "How many home alone movies were created?",
        "options": ["A) 2 B) 3 C) 7 D) 6"],
        "answer": "D"
    },
    {
        "question": "What software company is headquartered in Redmond, Washington?",
        "options": ["A) Microsoft B) Apple C) Samsung D) Google"],
        "answer": "A"
    },
    {
        "question": "which celebrity says hasta la vista baby?",
        "options": ["A) Arnold Schwarzenegger   B) Sylvester Stallone   C) Al Pacino  D) Steven Bauer"],
        "answer": "A"
    },
    {
        "question": "Cheetahs can reach what speed in as little as three seconds?",
        "options": ["A) 70mph B) 64 mph C) 20mph D) 80mph"],
        "answer": "B"
    },
    {
        "question": "How many states are in America?",
        "options": ["A) 22 B) 34 C) 50 D) 89 "],
        "answer": "C"
    },
    {
        "question": "How many countries on the planet",
        "options": ["A) 195 B) 217 C) 1011 D) 307"],
        "answer": "C"
    },
    {
        "question": "What year did steve jobs pass away?",
        "options": ["A) 2015  B) 2012  C) 2011  D)1999"],
        "answer": "C"
    },
]

elimination_questions = [
    {
        "question": "94 percent of british talk about what topic the most?",
        "options": ["A) The Traffic B) Chavs C) The Weather D) Shopping"],
        "answer": "C"
    },
    {
        "question": "What does the fox say?",
        "options": ["A) Meow B) Woof C) Moo D) Ring-ding-ding-ding-dingeringding"],
        "answer": "D"
    },
    {
        "question": "How many time zones are there in Russia?",
        "options": ["A) 10 b) 11 c)13 d)7"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["a) Atlantic", "b) Indian", "c) Arctic", "d) Pacific"],
        "answer": "D"
    }
]



def get_random_question(current_questions):
    question = random.choice(current_questions)
    current_questions.remove(question)
    return question

def get_random_elimination_question():
    return random.choice(elimination_questions)

def display_options(options):
    for option in options:
        print(option)

def ask_question(question):
    
    display_options(question["options"])
    answer = input("Enter your answer (a, b, c, or d): ").strip().lower()
    return answer == question["answer"].lower()

#slow print function for the typing effect
def print_slow(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice([
          0.09, 0.04, 0.08, 0.07, 0.07,
          0.07, 0.06, 0.06, 0.05, 0.01
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)

#play game function
def play_game(name):
    print_slow(f"Unknown Man - I knew it was something similar.. hmm {name}, I kind of like it.")
    print_slow(f"Unknown Man - Now {name}, you must answer these 15 questions correctly.")
    print_slow("Unknown Man - If you get a question wrong, I get to have my fun with you and try out some new tools.")
    print_slow("Unknown Man - Good luck and I hope you fail.")
    time.sleep(3)

    num_lives = 2
    num_questions_elimination = 2
    num_questions_easy = 5
    num_questions_medium = 5
    num_questions_hard = 5
    current_questions = questions_easy
    num_correct_elimination = 0
    
    while num_lives > 0:
        num_correct_easy = 0
        num_correct_medium = 0
        num_correct_hard = 0
        # Ask 5 questions from questions_easy
        for i in range(num_questions_easy):
            question = get_random_question(current_questions)
            print(f"\nOk {name}, here is your question:\n{question['question']}")
            if ask_question(question):
                print(f"\nCorrect, {name}!")
                num_correct_easy += 1
            else:
                num_lives -= 1
                print(f"\nIncorrect, {name}! You have {num_lives} lives remaining.")
                if num_lives == 1:
                    print_slow("Phone Rings")
                    print_slow("...")
                    print_slow("          ")
                    print_slow("...")
                    print_slow(f"Unknown Man -Hey {name}, I don't want to see you die so soon, I want to have some fun first")
                    print_slow("Unknown Man - So, how about we do this? I'll give you once chance")
                    print_slow("Unknown Man - Lets call this the gulag")
                    print_slow("Unknown Man - If you get this next question wrong, I'll have my fun sooner than I wanted")
                    print_slow("Unknown Man - But if you get this question correct, You'll live for a little longer")
                    print_slow("Phone Line - bzzzzzzzzzzzzzz")
                    print("\033[31m")
                    print("\033[31m")
                    txt = "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀▀ █░█ █░░ ▄▀█ █▀▀\n▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   █▄█ █▄█ █▄▄ █▀█ █▄█"
                    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                        time.sleep(0.006)
                        print(i, end='', flush=True)
                    print("\033[37m")
                    current_questions = elimination_questions
                    # Ask 2 questions from elimination_questions
                    for j in range(num_questions_elimination):
                        question = get_random_question(current_questions)
                        print(f"\nOk {name}, here is your question:\n{question['question']}")
                        if ask_question(question):
                            print(f"\nCorrect, {name}!")
                            num_correct_elimination += 1
                            #return to the easy questions
                            if num_correct_elimination == 2:
                                print(f"\nCongratulations {name}, you have answered two elimination questions correctly!")
                                current_questions = questions_easy
                                break  # break out of the inner loop
                elif num_lives == 0:
                        print(f"\nYou have lost the game, {name}!")
                        play_again = input("Would you like to play again? (y/n) ")
                        if play_again.lower() == 'y':
                            play_game(name)
                        else:
                            print("\nReturning to main menu.")
                            return
                            
                            print(i, end='', flush=True)

        print("\033[31m")
        txt = "█▀▀ ▄▀█ █▀ █▄█   █▀█ █░█ █▀▀ █▀ ▀█▀ █ █▀█ █▄░█ █▀   █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ █▀▀ █▀▄  \n██▄ █▀█ ▄█ ░█░   ▀▀█ █▄█ ██▄ ▄█ ░█░ █ █▄█ █░▀█ ▄█   █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ ██▄ █▄▀  "
        for i in txt: 
            time.sleep(0.006)
            print(i, end='', flush=True)
        print("\033[37m")    
        print(f"\nCongratulations {name}, you have completed the easy questions!")

        # Ask 5 questions from questions_medium
        current_questions = questions_medium
        for i in range(num_questions_medium):
            question = get_random_question(current_questions)
            print(f"\nOk {name}, here is your question:\n{question['question']}")
            if ask_question(question):
                print(f"\nCorrect, {name}!")
                num_correct_medium += 1   
            else:
                num_lives -= 1
                print(f"\nIncorrect, {name}! You have {num_lives} lives remaining.")
                if num_lives == 1:
                    print_slow("Phone Rings")
                    print_slow("...")
                    print_slow("          ")
                    print_slow("...")
                    print_slow(f"Unknown Man -Hey {name}, I don't want to see you die so soon, I want to have some fun first")
                    print_slow("Unknown Man - So, how about we do this? I'll give you once chance")
                    print_slow("Unknown Man - Lets call this the gulag")
                    print_slow("Unknown Man - If you get this next question wrong, I'll have my fun sooner than I wanted")
                    print_slow("Unknown Man - But if you get this question correct, You'll live for a little longer")
                    print_slow("Phone Line - bzzzzzzzzzzzzzz")
                    print("\033[31m")
                    print("\033[31m")
                    txt = "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀▀ █░█ █░░ ▄▀█ █▀▀\n▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   █▄█ █▄█ █▄▄ █▀█ █▄█"
                    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                        time.sleep(0.006)
                        print(i, end='', flush=True)
                    print("\033[37m")
                   
                    current_questions = elimination_questions
                    # Ask 2 questions from elimination_questions
                    for j in range(num_questions_elimination):
                        question = get_random_question(current_questions)
                        print(f"\nOk {name}, here is your question:\n{question['question']}")
                        #return to the easy questions
                        if ask_question(question):
                            print(f"\nCorrect, {name}!")
                            num_correct_elimination += 1
                            if num_correct_elimination == 2:
                                print(f"\nCongratulations {name}, you have answered two elimination questions correctly!")
                                current_questions = questions_medium
                                break  # break out of the inner loop
                elif num_lives == 0:
                    print(f"\nYou have lost the game, {name}!")
                    play_again = input("Would you like to play again? (y/n) ")
                    if play_again.lower() == 'y':
                        play_game(name)
                else:
                    print("\nReturning to main menu.")
                    return
                
                    print(i, end='', flush=True)
        print("\033[32m")
        txt = "█▀▄▀█ █▀▀ █▀▄ █ █░█ █▀▄▀█   █▀█ █░█ █▀▀ █▀ ▀█▀ █ █▀█ █▄░█ █▀   █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ █▀▀ █▀▄\n█░▀░█ ██▄ █▄▀ █ █▄█ █░▀░█   ▀▀█ █▄█ ██▄ ▄█ ░█░ █ █▄█ █░▀█ ▄█   █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ ██▄ █▄▀"
        for i in txt: 
            time.sleep(0.006)
            print(i, end='', flush=True)
        print("\033[37m")
        print(f"\nCongratulations {name}, you have completed the medium questions!")

             # Ask 5 questions from questions_hard   
        current_questions = questions_hard
        for i in range(num_questions_hard):
            question = get_random_question(current_questions)
            print(f"\nOk {name}, here is your question:\n{question['question']}")
            if ask_question(question):
                print(f"\nCorrect, {name}!")
                num_correct_hard += 1
            else:
                num_lives -= 1
                print(f"\nIncorrect, {name}! You have {num_lives} lives remaining.")
                #checking if the player has 1 lives left
                if num_lives == 1:
                    print_slow("Phone Rings")
                    print_slow("...")
                    print_slow("          ")
                    print_slow("...")
                    print_slow(f"Unknown Man -Hey {name}, I don't want to see you die so soon, I want to have some fun first")
                    print_slow("Unknown Man - So, how about we do this? I'll give you once chance")
                    print_slow("Unknown Man - Lets call this the gulag")
                    print_slow("Unknown Man - If you get this next question wrong, I'll have my fun sooner than I wanted")
                    print_slow("Unknown Man - But if you get this question correct, You'll live for a little longer")
                    print_slow("Phone Line - bzzzzzzzzzzzzzz")
                    print("\033[31m")
                    print("\033[31m")
                    txt = "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀▀ █░█ █░░ ▄▀█ █▀▀\n▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   █▄█ █▄█ █▄▄ █▀█ █▄█"
                    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                        time.sleep(0.006)
                        print(i, end='', flush=True)
                    print("\033[37m")
                    print(f"\nYou have one life left, {name}! If you get one more question wrong, you will be sent to the elimination round.")
                    current_questions = elimination_questions
                    # Ask 2 questions from elimination_questions
                    for j in range(num_questions_elimination):
                        question = get_random_question(current_questions)
                        print(f"\nOk {name}, here is your question:\n{question['question']}")
                        if ask_question(question):
                            print(f"\nCorrect, {name}!")
                            num_correct_elimination += 1
                            #return to the easy questions
                            if num_correct_elimination == 2:
                                print(f"\nCongratulations {name}, you have answered two elimination questions correctly!")
                                current_questions = questions_hard
                                break  # break out of the inner loop
                #checking if the player has 0 lives left
                elif num_lives == 0:
                    print(f"\nYou have lost the game, {name}!")
                    play_again = input("Would you like to play again? (y/n) ")
                    if play_again.lower() == 'y':
                        play_game(name)
                else:
                    print("\nReturning to main menu.")
                    return
        #when the player completes all of the rounds they will be congratulated
        print("\033[33m")
        txt = "█▀▀ █▀█ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █░█ █░░ ▄▀█ ▀█▀ █ █▀█ █▄░█ █▀\n█▄▄ █▄█ █░▀█ █▄█ █▀▄ █▀█ ░█░ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄█"
        for i in txt: 
            time.sleep(0.006)
            print(i, end='', flush=True)
        print("\033[37m")
        print(f"\nCongratulations, {name}! You answered {num_correct_hard} out of {num_questions_hard} questions correctly.")
        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() == 'y':
            play_game(name)
        else:
            main_menu()



#The player will be greated with this main menu on launching the game
def main_menu():
    print("Welcome to the Python Quiz Game!")
    while True:
        #big text saying press enter
        print("\033[31m")
        txt = "█▀█ █▀█ █▀▀ █▀ █▀   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █▀█   █▀ ▀█▀ ▄▀█ █▀█ ▀█▀\n█▀▀ █▀▄ ██▄ ▄█ ▄█   ██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▄█   ▄█ ░█░ █▀█ █▀▄ ░█░"
        for i in txt: 
            time.sleep(0.006)
            print(i, end='', flush=True)
        print("\033[37m")
        input("")  # wait for enter to be pressed
        print_slow("The phone rings...")
        print_slow("====================================")
        print_slow("...")
        print_slow("Unknown Man - I hope you are enjoying your time in this dark room tied to a chair!")
        print_slow("Unknown Man - Listen very closely to what I am about to say as I'll only say it once.")
        print_slow("Unknown Man - After that it's time to have some fun.")
        print_slow("...")
        print_slow("Unknown Man - How not to Die is a game based from Who wants to be a millionaire")
        print_slow("Unknown Man - The only difference is your life depends on answering correctly!")
        print_slow("Unknown Man - There is no ask the audience, phone a friend or 50/50.")
        print_slow("Unknown Man - In-fact the only thing 50/50 here is your life.")
        print_slow("Unknown Man - I can't wait to see you fail!")
        print_slow("Unknown Man - Before we start tell me your name.")
        print("Press 'p' to play or 'q' to quit.")
        choice = input("Enter your choice: ").strip().lower()
        if choice == "p":
            print("\033[31m")
            txt = "█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █▄░█ ▄▀█ █▀▄▀█ █▀▀\n██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▄█ █▄█ █▀▄   █░▀█ █▀█ █░▀░█ ██▄"
            for i in txt: 
                time.sleep(0.006)
                print(i, end='', flush=True)
            print("\033[37m")
            name = input("Enter your name: ")
            play_game(name)
           
        elif choice == "q":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main_menu()