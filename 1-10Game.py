answer = 5
def check(x):
   if x == answer:
       print ("You got it!")
   elif x != answer:
       print ("Wrong")
print ("I am thinking of a number between 1 and 10.")
check(int(input("Any guesses: ")))