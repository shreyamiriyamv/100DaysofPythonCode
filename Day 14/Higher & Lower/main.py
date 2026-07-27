import random
import art
from game_data import data

def game():
    is_playing = True
    score = 0
    option1 = random.randint(0, len(data) - 1)
    print(art.logo)
    while is_playing:
        option2 = random.randint(1, len(data) - 1)
        while option2 == option1:
            option2 = random.randint(1,len(data) - 1)
        print(f"Compare A: {data[option1]["name"]}, {data[option1]['description']}, from {data[option1]['country']}")
        print(art.vs)
        print(f"Against B: {data[option2]["name"]}, {data[option2]['description']}, from {data[option2]['country']}")
        choice = input("Who has more followers? Type 'A' or 'B' : ").upper()
        if choice == 'A' and data[option1]['follower_count'] > data[option2]['follower_count']:
            score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
            option1 = option2
        elif choice == 'B' and data[option1]['follower_count'] < data[option2]['follower_count']:
            score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
            option1 = option2
        else:
            print("\n" * 20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            is_playing = False

game()