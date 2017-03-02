import sys


def analyze_country_data(data):
    result = dict()

    for i in range(0, len(data)):
        teams_in_country = data[i]
        for team in teams_in_country:
            team = int(team)
            if team in result:
                result[team].append(str(i+1))
            else:
                result[team] = [str(i+1)]

    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if len(test) == 0:
        continue

    country_data = test.strip().split(' | ')
    input_data = list()
    for data in country_data:
        data = data.split(' ')
        input_data.append(data)

    #print (input_data)
    analyzed_data = analyze_country_data(input_data)

    sorted_keys = analyzed_data.keys()
    sorted_keys.sort()

    formatted_result = str()
    for key in sorted_keys:
        formatted_result += str(key) + ':' + ','.join(analyzed_data[key]) + '; '

    print (formatted_result.strip())

test_cases.close()

# import sys
# import collections
#
# def main():
#     test_cases = open(sys.argv[1], 'r')
#     for test in test_cases:
#         test = test.strip()
#         if len(test) == 0: continue
#         test = [[int(team) for team in country.strip().split(' ')] for country in test.split('|')]
#         team_to_fan_countries = collections.defaultdict(list)
#         for country in range(len(test)):
#             liked_teams = test[country]
#             for team in liked_teams:
#                 team_to_fan_countries[team].append(country+1)
#         result = []
#         for team in sorted(team_to_fan_countries.keys()):
#             result.append(str(team) + ':' + ','.join([str(c) for c in team_to_fan_countries[team]]))
#         print('; '.join(result) + ';')
#     test_cases.close()
#
# if __name__ == '__main__':
#     main()