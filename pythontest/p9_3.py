import matplotlib.pyplot as plt

steps=[6543,7000,8900,10789,3467,11045,5095]
labels=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
num_bars=len(steps)
position=range(1,num_bars+1)
plt.barh(position,steps,align='center')

plt.yticks(position,labels)
plt.xlabel('Steps')
plt.ylabel('Day')
plt.title('Number of steps walked')

plt.grid()
plt.show()