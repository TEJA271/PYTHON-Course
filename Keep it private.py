class myclass:

    __privatevar = 27;

    def __privmeth (self):
        print("I Am Inside MyClass")

    def hello(self):
        print("Private Variable Value :",myclass.__privatevar)

foo = myclass()
foo.hello()
foo.__privmeth