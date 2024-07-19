import random

def display_intro():
    print("Welcome to the Footballer Guessing Game!")
    print("Try to guess the footballer's name based on the hint provided.")
    print("You can type 'quit' anytime to exit the game.")
    print()

def get_hint_and_name(footballers):
    if not footballers:
        return None, None
    footballer, hint = random.choice(list(footballers.items()))
    del footballers[footballer]
    return hint, footballer

def main():
    footballers = {
        "Lionel Messi": "Argentinian player who won the Ballon d'Or seven times.",
        "Cristiano Ronaldo": "Portuguese player known for his time at Manchester United and Real Madrid.",
        "Neymar": "Brazilian player who played for Barcelona and PSG.",
        "Kylian Mbappe": "French player who won the World Cup in 2018.",
        "Luka Modric": "Croatian player who won the Ballon d'Or in 2018.",
        "Kevin De Bruyne": "Belgian player known for his time at Manchester City.",
        "Mohamed Salah": "Egyptian player known for his time at Liverpool.",
        "Virgil van Dijk": "Dutch defender known for his time at Liverpool.",
        "Harry Kane": "English striker known for his time at Tottenham Hotspur.",
        "Robert Lewandowski": "Polish striker known for his time at Bayern Munich and Barcelona.",
        "Sunil Chhetri": "Indian player who is the all-time top scorer for the Indian national team.",
        "Rodrygo": "Brazilian winger known for his time at Real Madrid.",
        "Vinicius Junior": "Brazilian winger known for his time at Real Madrid.",
        "Erling Haaland": "Norwegian striker known for his goal-scoring prowess at Borussia Dortmund and Manchester City."
    }

    display_intro()

    while footballers:
        hint, correct_name = get_hint_and_name(footballers)
        if hint is None:
            print("No more footballers to guess! Thanks for playing!")
            break
        
        print("Hint:", hint)
        
        guess = input("Your guess: ").strip()
        
        if guess.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        elif guess.lower() == correct_name.lower():
            print("Correct! Well done!\n")
        else:
            print(f"Wrong! The correct answer was {correct_name}.\n")

if __name__ == "__main__":
    main()
