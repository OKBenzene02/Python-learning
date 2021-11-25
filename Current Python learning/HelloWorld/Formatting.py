# for i in range(1,14):
#     print("Number {0:>3} is squared is {1:>3} and cubed is {2:>3}.".format(i, i**2, i**3))

# print("pi is {:<12f}".format(22/7))
# print("pi is {:<12.56f}".format(22/7))
# print("pi is {:<75.50f}".format(22/7))
# print("pi is {:.2f}".format(22/7))

""" FCFS With Arrival time"""

n = int(input("Enter number of processes: "))
l = []
ct = [0] * n
tat = [0] * n
total_tat = 0
avg_tat = 0
wt = [0] * n
total_wt = 0
avg_wt = 0

for i in range(n):
    process = f"P{i + 1}"
    a = int(input(f"Enter arrival time P{i+1}: "))
    b = int(input(f"Enter burst time P{i+1}: "))
    l.append([process, [a, b]])

l = sorted(l, key=lambda item: item[1][0])
# print(l)

# For Completion time and Turn around time
for i in range(1, n):
    ct[0] = l[0][1][1]
    if l[i][1][0] - l[i - 1][1][0] > 1:
        if l[i][1][0] - l[i - 1][1][0] > 2 and l[i][1][0] < ct[i - 1]:
            ct[i] = l[i][1][1] + l[i][1][0]
        else:
            ct[i] = l[i][1][1] + ct[i - 1]
    else:
        ct[i] = ct[i - 1] + l[i][1][1]

for i in range(n):
    tat[i] = ct[i] - l[i][1][0]
    total_tat += tat[i]

avg_tat = total_tat / n

# For waiting time
for i in range(n):
    wt[i] = tat[i] - l[i][1][1]
    total_wt += wt[i]

avg_wt = total_wt / n


print("Processes\tArrival time\tBurst time\tCompletion time\tTurn around time\tWaiting time")
for i in range(n):
    print("{0:>4} {1:>12} {2:>14} {3:>15} {4:>16} {5:>17}".format(l[i][0], l[i][1][0], l[i][1][1], ct[i], tat[i], wt[i]))

print()
print("Average Turn around time: {:.2f}".format(avg_tat))
print("Average Waiting time: {:.2f}".format(avg_wt))
