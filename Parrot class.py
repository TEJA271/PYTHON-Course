class parrot:
    species = 'bird'
    def __init__(self , name , age ):
        self.name = name 
        self.age = age

hi = parrot ( 'hi' , 10)
suji = parrot ( 'suji' , 12)

print(" hi is a {}".format(hi.species))
print(" suji is a {}".format(suji.species))
print("{} is {} years old ".format(suji.name , suji.age))
