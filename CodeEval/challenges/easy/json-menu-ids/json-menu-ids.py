import sys
import json


def menu_sum(menu_string):
    json_menu = json.loads(menu_string)

    id_sum = 0
    for item in json_menu['menu']['items']:
        if item and 'label' in item.keys():
            id_sum += item['id']

    return id_sum

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    print(menu_sum(test.strip()))

test_cases.close()
