import pandas as pd
import random

# use API?

df = pd.read_csv("RickAndMortyScripts.csv")


characters = ["Beth", "Morty", "Rick", "Jerry", "Summer"]

df = df[(df['name'] == "Beth") | (df['name'] == "Rick") | (df['name'] == "Morty") | (df['name'] == "Jerry") | (df['name'] == "Summer")]
LENGTH = df.shape[0]


def game_selection():
    print("\nGame A: Who said it?\nGame B: Fill in the sentence!\nX: exit")
    inp = input("Which game would you like to play (enter letter)?\n")

    return inp

def generate_q_gameA(df):
    line_number = random.randint(0,LENGTH)
    line = df.iloc[line_number]
    question = '"' + line["line"] + '"\n'
    answer = line["name"]
    return (question, answer)

def generate_q_gameB(df):
    line_number = random.randint(0,LENGTH)
    line = df.iloc[line_number]
    
    line= line["line"].split()
    line_length = len(line)
    
    random_index = random.randint(0, line_length)
    
    
    question = ""
    for index in range(line_length):
        
        if index != random_index:
            question += line[index]
        else:
            question += "______"
        question += " "
    answer = line.pop(random_index)

    return (question, answer)
    
def check_answer(inp, correct):
    correctAnswer = inp.lower() == correct.lower()

    if correctAnswer:
        print("Good job!")

    else:
        print("Nice try! It was", answer)

playing = True

while playing: 
    game = game_selection()
    
    if game == "A":
        (question, answer) = generate_q_gameA(df)
        
        print(question)

        for index in range(len(characters)):
            print(index + 1, ":", characters[index])

        inp = input("Who said it?\n")
        
        check_answer(inp, answer)
    elif game == "B":
        (question, answer) = generate_q_gameB(df)

        print(question)

        inp = input("Finish the sentence:\n")
        check_answer(inp, answer)
    elif game == "X":
        playing = False
        
        
    

