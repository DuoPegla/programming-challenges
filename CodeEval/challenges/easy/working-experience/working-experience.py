import sys

MONTHS = {"Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3,
          "May": 4, "Jun": 5, "Jul": 6, "Aug": 7,
          "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11}


def update_calendar(calendar_to_update, from_month, from_year, to_month, to_year):

    current_month = from_month
    current_year = from_year

    while True:
        calendar_to_update[current_year][current_month] = True
        current_month += 1

        if current_month >= 12:
            current_month = 0
            current_year += 1

        if current_year == to_year and current_month == to_month:
            calendar_to_update[current_year][current_month] = True
            break

    return calendar_to_update


def calculate_working_experience(calendar):
    months_of_experience = 0
    for year in range(1990, 2021):
        for month in range(0, 12):
            if calendar[year][month]:
                months_of_experience += 1

    return months_of_experience/12


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    calendar = {x: [False for y in range(0, 12)] for x in range(1990, 2021)}

    for date_range in test.split("; "):
        from_date, to_date = date_range.split('-')
        calendar = update_calendar(calendar, MONTHS[from_date.split(' ')[0]], int(from_date.split(' ')[1]),
                                           MONTHS[to_date.split(' ')[0]], int(to_date.split(' ')[1]))

    print(calculate_working_experience(calendar))

test_cases.close()
