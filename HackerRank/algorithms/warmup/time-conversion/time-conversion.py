input_time = raw_input()

hour = int(input_time[:2])
if "PM" in input_time:
    if hour < 12:
        print str(12 + hour) + input_time[2:-2]
    else:
        print input_time[:-2]
else:
    if hour < 12:
        print input_time[:-2]
    else:
        print "00" + input_time[2:-2]