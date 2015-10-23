def array_sum(numbers):
    sum = 0
    for number in numbers:
        sum += int(number)
    return sum

count = input()
number_list = raw_input()
number_list = number_list.strip().split(' ')

print(array_sum(number_list))