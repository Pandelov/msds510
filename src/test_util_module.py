from msds510.utils import utils

records = [
    dict(year='1988', intro='Jun-88'),
    dict(year='1989', intro='May-89'),
    dict(year='2005', intro='5-May'),
    dict(year='2013', intro='13-Nov'),
    dict(year='2014', intro='14-Jan'),
]

for record in records:
    print("Input Record - ", record)
    print("Date Joined - ",
          utils.get_date_joined(record["year"], record["intro"]))

    print("Days since joined - ",
          utils.days_since_joined(record["year"], record["intro"]))

    print()
