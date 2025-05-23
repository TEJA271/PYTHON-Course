#8. Create code-breaking game using python

import random
c = ''.join(random.choices('0123456789', k=4))
for i in range(10):
    g = input("Guess: ")
    if g == c:
        print("Win!"); break
    print(sum(a==b for a,b in zip(c,g)), "correct")
else:
    print("Code:", c)
