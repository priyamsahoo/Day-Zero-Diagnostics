import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data_ritwik_8_Oct_2018.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append((int(str(row[0]).replace(":", ""))))
        x.append(int(str(row[1]).replace(":", "")))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('Time')
plt.ylabel('Heartbeat (in BPM)')
plt.gca().set_xticks([])
plt.title('Fitbit Analysis')
plt.legend()
plt.show()
