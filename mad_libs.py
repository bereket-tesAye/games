# Mad Libs Generator with Conditional Story Variation

# Prompt the user for words
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter one more adjective: ")
adj4 = input("Enter a final adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb ending with -ing: ")

# Conditional twist: story changes if the animal is "lion"
if animal.lower() == "lion":
    story = f"""
    On a beautiful {adj1} day, I went to the zoo. 
    I saw a funny {adj2} monkey {verb} from the trees. 
    Then, I spotted a majestic {adj3} {animal} roaring loudly. 
    What a wild and {adj4} experience!
    """
else:
    story = f"""
    On a beautiful {adj1} day, I went to the zoo. 
    I saw a funny {adj2} monkey {verb} from the trees. 
    Then, I spotted a majestic {adj3} {animal} lounging in the sun. 
    What a wild and {adj4} experience!
    """

# Print the final story
print(story)
