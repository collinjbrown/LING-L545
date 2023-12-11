import sys
import matplotlib.pyplot as plt
import csv

labels = []
x_strings = []
y_strings = []

with open('outputs.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    cursor = 0
    for row in reader:
        if (cursor == 0):
            labels = row
        elif (cursor == 1):
            x_strings = row
        else:
            y_strings = row
        cursor += 1
    csv_file.close()

x = []
y = []

for i in x_strings:
    x.append(float(i))

for i in y_strings:
    y.append(float(i))

print(labels)
print(x)
print(y)

plt.plot(x, y, 'ro')
plt.title('Relative Word Order of Verb and Object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
cursor = 0
for i in labels:  # Add labels to each of the points
    plt.text(x[cursor]-0.03, y[cursor]-0.03, labels[cursor], fontsize=9)
    cursor += 1
plt.savefig('output_graph.png')