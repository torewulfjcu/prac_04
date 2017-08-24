import random

number_of_quick_picks = int(input("How many quick picks? "))
LENGTH_OF_LINE = 6
lottery_ticket = []

for line in range(0, number_of_quick_picks):
    lottery_ticket.append([])
    for number in range(LENGTH_OF_LINE):
        lottery_ticket[line].append(random.randint(1, 45))

for line in range(0, number_of_quick_picks):
    lottery_ticket[line] = set(lottery_ticket[line])
    lottery_ticket[line] = list(lottery_ticket[line])
    while len(lottery_ticket[line]) is not LENGTH_OF_LINE:
        lottery_ticket[line].append(random.randint(1, 45))
        lottery_ticket[line] = set(lottery_ticket[line])
        lottery_ticket[line] = list(lottery_ticket[line])
    print((sorted(lottery_ticket[line])))

