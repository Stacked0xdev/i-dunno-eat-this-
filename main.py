import random
import time


# Simple food suggestions grouped by mood
food_ideas = {
    "Happy": [
        "Pizza Margherita 🍕",
        "Waffle Ice Cream 🍦",
        "Masala Dosa 🌯"
    ],
    "Sad": [
        "Mac and Cheese 🧀",
        "Chicken Soup 🍲",
        "Rasam Rice 🍚"
    ],
    "Lazy": [
        "Instant Ramen 🍜",
        "PB&J Sandwich 🥪",
        "Maggi Noodles 🍝"
    ],
    "Adventurous": [
        "Sushi 🍣",
        "Spicy Biryani 🍛",
        "Durian Ice Cream 🍧"
    ]
}

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    # Display ASCII art food image
    print(r"""
      ,--./,-.
     / #      \
    |          |     ___  ___  ___
     \        /     |   ||   ||   |
      `._,._,'      |___||___||___|
        
   ╔════════════════════════════╗
   ║   I Dunno, Eat This! 🍔🍜   ║
   ╚════════════════════════════╝
   
    [Pizza] [Burger] [Noodles] [Cake]
     [Soup]  [Sushi]  [Salad] [Tacos]
""")
    slow_print("✨ Your mood-matched food suggestion app ✨\n")

def get_food(mood):
    mood = mood.title()
    if mood not in food_ideas:
        print("❌ Mood not recognized. Try: Happy, Sad, Lazy, Adventurous")
        return
    suggestion = random.choice(food_ideas[mood])
    slow_print(f"🍽 Suggested for '{mood}' mood: {suggestion}")

def main():
    intro()
    while True:
        mood = input("How do you feel? (Happy, Sad, Lazy, Adventurous): ").strip()
        get_food(mood)
        again = input("Want another suggestion? (yes/no): ").strip().lower()
        if again != "yes":
            slow_print("\nThanks for using 'I Dunno, Eat This!' 😋")
            break

if __name__ == "__main__":
    main()