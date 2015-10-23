def number_stats(numbers):
    positive_numbers = 0
    negative_numbers = 0
    zeros = 0
    for number in numbers:
        if int(number) > 0:
            positive_numbers += 1
        elif int(number) < 0:
            negative_numbers += 1
        else:
            zeros += 1

    return float(positive_numbers)/len(numbers), float(negative_numbers)/len(numbers), float(zeros)/len(numbers)

n = input()
numbers = raw_input()
numbers = numbers.split(' ')
results = number_stats(numbers)
print("{0:.3f}".format(results[0]))
print("{0:.3f}".format(results[1]))
print("{0:.3f}".format(results[2]))
