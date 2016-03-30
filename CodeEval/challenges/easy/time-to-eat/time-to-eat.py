import sys


def sort_timestamps(timestamps):
    timestamps_in_seconds = list()
    for timestamp in timestamps:
        timestamps_in_seconds.append(timestamp_to_seconds(timestamp))

    timestamps_in_seconds.sort(reverse=True)

    sorted_timestamps = list()
    for timestamp_in_seconds in timestamps_in_seconds:
        sorted_timestamps.append(seconds_to_timestamp(timestamp_in_seconds))
    return ' '.join(sorted_timestamps)


def timestamp_to_seconds(timestamp):
    segments = timestamp.split(':')
    return int(segments[0]) * 3600 + int(segments[1]) * 60 + int(segments[2])


def seconds_to_timestamp(timestamp_in_seconds):
    hours = timestamp_in_seconds / 3600
    minutes = (timestamp_in_seconds - hours * 3600) / 60
    seconds = (timestamp_in_seconds - hours * 3600 - minutes * 60)
    return str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    print sort_timestamps(test.strip().split(' '))


test_cases.close()
