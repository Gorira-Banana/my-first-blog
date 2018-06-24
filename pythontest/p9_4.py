import matplotlib.pyplot as plt

steps=[6543,7000,8900,10789,3467,11045,5095]
labels=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
labels1=[2000,4000,6000,8000,10000]
num_bars=len(steps)
position=range(1,num_bars+1)
position1=range(1,len(labels1)+1)
plt.bar(position,steps)

plt.yticks(position1,labels1)
plt.xlabel('Steps')
plt.ylabel('Day')
plt.title('Number of steps walked')

plt.grid()
plt.show()