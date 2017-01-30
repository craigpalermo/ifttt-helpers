import pandas
import re

from datetime import datetime

ARRIVED = 'Arrived at work'
EXITED = 'Left work'


def hours_worked_for_day(group):
    """
    Given a dataframe containing times entered and exited work for a single day,
    calculate the total number of hours spent at work for that day.
    :param group:
    :return:
    """
    seconds_worked = 0
    temp_arr = None

    for idx, row in group.iterrows():
        if row['event'] == ARRIVED:
            temp_arr = row['datetime']
        elif row['event'] == EXITED and temp_arr:
            seconds_worked += (row['datetime'] - temp_arr).total_seconds()
            temp_arr = None

    return seconds_worked / 60 / 60


def parse_date(timestamp):
    m = re.search(r'^(.*) at (.*)$', timestamp)
    if m:
        return datetime.strptime(m.group(1), '%B %d, %Y').strftime('%Y%m%d')


def parse_datetime(timestamp):
    m = re.search(r'^(.*) at (.*)$', timestamp)
    if m:
        return datetime.strptime('{} {}'.format(m.group(1), m.group(2)), '%B %d, %Y %I:%M%p')


def main():
    # create dataframe from CSV file
    df = pandas.read_csv('data.csv', header=None, names=['event', 'timestamp'])

    # parse date from timestamp for each record
    df['date'] = df.apply(lambda row: parse_date(row['timestamp']), axis=1)
    df['datetime'] = df.apply(lambda row: parse_datetime(row['timestamp']), axis=1)

    # group records by day
    grouped_by_date = df.groupby('date')

    # compute average hours worked per day
    hours_by_day = [hours_worked_for_day(group) for date, group in grouped_by_date if hours_worked_for_day(group) > 1]

    # convert to dataframe so we can easily find average
    hours_df = pandas.DataFrame(hours_by_day, columns=['hours'])

    print('Average hours worked per day: {}'.format(hours_df['hours'].mean()))
    print('Days sampled: {} of {}'.format(len(hours_df), len(grouped_by_date)))


if __name__ == '__main__':
    main()
