#3.Create a list Add 'kiwi' to the list and remove 'banana'.


fruits = ['apple', 'banana', 'orange', 'STRAWBERRY'  ,  'PEACH']
fruits = [fruit for fruit in fruits if fruit != 'banana']
fruits += ['kiwi']
print(fruits)
