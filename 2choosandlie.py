import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1

    def __str__(self):
        return self.name

def game(player):
    answer = []
    index = 0
    print(f"Welcome {player.name} to two choos and a lie !")
    print("Enter two fun facts about you? \n ")

    while len(answer) < 2:
        fact = input(f"Fact {index + 1} :")
        answer.append(fact)
        index += 1
    print(answer)

    lie = ai_generate_lie()
    answer.append(lie)
    
    print("\nHere are the statements:")
    for i, statement in enumerate(answer):
        print(f"{i + 1}. {statement}")

    guess = int(input("Which statement is a lie? "))

    if answer[guess - 1] == lie:
        print("You are correct!")
        player.add_score()

#the facts could be prompts of pictures representing the truths and a lie
#choose the lie and the player gets a point
#create a train on js, going up and down,
#stickman represent people
#create a mobile view
#play with ai feature, ai generates two truths and a lie you try to guess the lie

def ai_generate_lie():
    lie = "I have a pet dragon"
    return lie

def test_player():
    player = Player("Alice")
    player.add_score()
    game(player)

test_player()