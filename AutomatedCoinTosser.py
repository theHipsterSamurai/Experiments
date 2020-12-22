import random

#declaration of count
Hcount = 0
Tcount = 0

#poorly writtten introduction
print("Welcome person to Rishi's automated coin flipper which provides reasonable output")
print()
a = int(input("Input the number of times you want the flip the coin: "))

#loop which does stuff
for i in range(1, a+1):
    n = random.randint(0,1)
    if n == 0:
        Hcount = Hcount + 1
    else:
        Tcount = Tcount + 1

#number of outcomes
print("Number of times heads appeared: ", Hcount)
print("Number of times tails appeared: ", Tcount)


#probability of outcomes
probH = Hcount/a
probT = Tcount/a

print("The probabilty of getting a heads is: ", probH)
print("The probablity of getting a tails is: ", probT)


#percentage of outcomes
percentH = probH * 100
percentT = probT * 100

print("The percent of heads appearing is", percentH,'%')
print("The percent of tails appearing is", percentT, '%')

print()
print("As you can see... The probablity is almost never 50/50")
print("Thank you for runnning this program and taking part in this mathematical experiment, now shoo....")

