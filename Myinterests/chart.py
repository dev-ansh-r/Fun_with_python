import matplotlib.pyplot as plt
partition= 'Learning','Research','Music','Books','Movies','Travel','Others'
sizes=[200,150,150,100,30,100,10]
colors=['gold','yellowgreen','lightcoral','lightskyblue','red','green','blue']
figl,ax1=plt.subplots()
ax1.pie(sizes,labels=partition,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()

#Thanks for reading this snippet. If you have any questions, please feel free to ask.
#Code snippet written by: Devansh Shukla
