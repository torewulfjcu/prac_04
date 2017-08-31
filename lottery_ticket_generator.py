import random

number_of_quick_picks = int(input("How many quick picks? "))
LENGTH_OF_LINE = 6
lottery_ticket = []

for line in range(0, number_of_quick_picks):
    lottery_ticket.append([])
    for number in range(LENGTH_OF_LINE):
        lottery_ticket[line].append(random.randint(1, 45))

for line in range(0, number_of_quick_picks):
    lottery_ticket[line] = list(set(lottery_ticket[line]))
    while len(lottery_ticket[line]) is not LENGTH_OF_LINE:
        lottery_ticket[line].append(random.randint(1, 45))
        lottery_ticket[line] = list(set(lottery_ticket[line]))


#for line in range(0, number_of_quick_picks):
#    print(''.join(str(sorted(lottery_ticket[line]))))

for line in range (0, number_of_quick_picks):
    lottery_ticket.sort()
    print(" ".join("{:2}".format(number) for line in lottery_ticket for number in line))


# s = ' '.join([str(number) for line in lottery_ticket for number in line])
# print(s)