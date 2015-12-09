import sys


def distribute_age(age):
    if 0 <= age <= 2:
        return "Still in Mama's arms"
    if 3 <= age <= 4:
        return "Preschool Maniac"
    if 5 <= age <= 12:
        return "Elementary school"
    if 12 <= age <= 14:
        return "Middle school"
    if 15 <= age <= 18:
        return "High school"
    if 19 <= age <= 22:
        return "College"
    if 23 <= age <= 65:
        return "Working for the man"
    if 66 <= age <= 100:
        return "The Golden Years"
    if age < 0 or age > 100:
        return "This program is for humans"


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    test = test.strip()
    print distribute_age(int(test))


test_cases.close()