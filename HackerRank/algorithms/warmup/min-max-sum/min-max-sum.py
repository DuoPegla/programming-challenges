number_list = raw_input()
number_list = number_list.strip().split(' ')
number_list = map(int, number_list)

min_number = number_list[0]
max_number = number_list[0]

min_index = 0
max_index = 0
for i in xrange(1, len(number_list)):
    current_number = number_list[i]
    if current_number < min_number:
        min_number = current_number
        min_index = i
    elif current_number > max_number:
        max_number = current_number
        max_index = i
        
min_list = list(number_list)
del min_list[max_index]

max_list = list(number_list)
del max_list[min_index]

print str(sum(min_list)) + " " + str(sum(max_list))