from statistics import mean

numbers = []
print("Please enter 5 numbers.")
for number in range(0, 5):
    numbers.append(int(input("Number: ")))

print("The first number is: {}".format(numbers[0]))
print("The last number is: {}".format(numbers[4]))
print("The smallest number is: {}".format(min(numbers)))
print("The largest number is: {}".format(max(numbers)))
print("The average of the numbers is: {}".format((mean(numbers))))
