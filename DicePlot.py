#6,9,2,7,2,4,9,4,10,10,3
#We will be looking at a pattern which hold universally true for almost all kind of data

#Roll two dice again and again
#Record the sums we get on a file
#Example:4+4=8,4+3=7...etc.
#Now lets plot the sums

import plotly.figure_factory as ff
import random

#dice_result=[6,9,2,7,2,4,9,4,10,10,3]
#fig=ff.create_distplot([dice_result],["Result"])
#fig.show()

#We want to roll both the dice 100 times and note down this sum
dice_result=[]
count=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

fig=ff.create_distplot([dice_result],["Result"])
fig.show()
 
#If we join all the left edges of the bar graph we see a bell shaped curve
#Bell shaped distribution is called the normal distribution because most of the data in the universe follow this pattern
#Y axis- shows the frequency of the sum of the numbers