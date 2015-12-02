import sys
import datetime
import calendar


def calculate_working_experience(dates):
    dates.sort()
    working_experience = list()
    working_experience.append(dates[0])
    for date_range in dates[1:]:
        if dates_intersect(working_experience[-1], date_range):
            working_experience[-1] = (min(working_experience[-1][0], date_range[0]), max(working_experience[-1][1], date_range[1]))
        else:
            working_experience.append(date_range)

    days_of_experience = 0
    for experience in working_experience:
        days_of_experience += (experience[1] - experience[0]).days

    return days_of_experience / 365

def dates_intersect(date1, date2):
    if date1[0] <= date2[0]:
        return date1[1] > date2[0]
    else:
        return date2[1] > date1[0]



test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    date_ranges = test.strip().split('; ')
    dates = list()
    for date_range in date_ranges:
        from_date, to_date = date_range.split('-')
        from_date = datetime.datetime.strptime(from_date, "%b %Y")
        to_date = datetime.datetime.strptime(to_date, "%b %Y")
        to_date = to_date.replace(day=calendar.monthrange(to_date.year, to_date.month)[1])
        dates.append((from_date, to_date))

    print(calculate_working_experience(dates))


test_cases.close()
