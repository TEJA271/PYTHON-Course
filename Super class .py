class bird:

    def __init__(self):
        print("Bird Is Ready")

    def whoisthis(self):
        print("bird")

    def swim(self):
        print(" swim faster")

class penguin(bird):

    def __init__(self):
        super().__init__()
        print("penguin is ready")

    def whoisthis(self):
        print("penguin")

    def run(self):
        print(" run faster")

peggy = penguin()
peggy.whoisthis()
peggy.run()
peggy.swim()