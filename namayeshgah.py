import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("Crime_Data_from_2020_to_Present.csv") 
time=list(data['TIME OCC'])
integer_time=list(map(int,time))
plot_data=[]
for i in integer_time:
    i+=10000
    plot_data.append(i)
list1=[]
list2=[]
list3=[]
list4=[]
for i in plot_data:
    if 10000<i<10600:
        list1.append(i)
    if 10600<i<11200:
        list2.append(i)
    if 11200<i<11800:
        list3.append(i)
    if 11800<i<12400:
        list4.append(i)
four_digit_numbers = [str(number)[1:] for number in plot_data] 
y=np.array([len(list1),len(list2),len(list3),len(list4)])
plt.plot(four_digit_numbers,y,"o",ls="-",color="red")
plt.xlabel("Time Occ")
plt.ylabel("Number Of Crime")
plt.grid()
plt.show()




