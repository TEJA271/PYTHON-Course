#1. Mad Libs Game A fun word game where you can create a silly story by filling in blanks with random words. In Python, you can ask the user for different words (like a noun, verb, or adjective), and then use those words to complete a funny story.


name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
food = input("Enter a type of food: ")

print(f"""One day, {name} went to {place} to see a {adjective} {animal}.
Suddenly, the {animal} started to {verb} around the place!
Everyone laughed and took pictures.
After all the fun, {name} ate some delicious {food} and went home happy.""")
