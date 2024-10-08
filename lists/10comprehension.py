#A new way to build a list by applying an expression for each item in a sequence
numbers = [item for item in range(1, 6)] 
squares = [x*x for x in range(0,10)]
numbers2 = [item+10 for item in numbers]
#List comprehension looks like a backward for  loop
#Comprehension with an if and nested loop
evens = [x for x in range(1,100) if x %2 == 0]
cards = [face+' of '+suite for face in 'JKQA' for suite in ['hearts', 'clubs', 'diamonds', 'spades']]
deckOfCards2 = [f'{number} of {suite}' for suite in ['clubs', 'diamonds', 'hearts', 'spades']
                for number in [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace']]
print(deckOfCards2)

