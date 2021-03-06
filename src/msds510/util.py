from datetime import date, datetime
import re
import csv


def get_month(dateString):
    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]

    for i in range(0, len(months)):
        if months[i] in dateString.lower():
            return i + 1
    return ''


def get_date_joined(yearString, dateString):
    return datetime.date(int(yearString), get_month(dateString), 1)


def days_since_joined(yearString, dateString):
    rval = datetime.date.today() - get_date_joined(yearString, dateString)
    rval = rval.days
    return rval


# function that converts an input value into an integer
def to_int(value):
    try:
        return int(value)
    except:
        return None


# function that takes as args a series of items and a value
# If list or tuple returns integer index, if dict returns the input key
# If no value returns None
def get_value(items, value):
    try:
        return items.index(value)
    except:
        return items[value]
    else:
        return None


# to boolean
def to_bool(value):
    if not value.strip():
        return None
    else:
        return True if value == 'YES' else False


# cleaning up the notes
def clean_notes(value):
    return value.strip()


# making nice names
def make_nice_name(name):
    newString = name.replace(" ", "_")
    newString = newString.replace("/", "_")
    newString = newString.strip("?").strip().lower()
    newString = re.sub(r'[^0-9a-z_\_]', '', newString)
    return newString


# reading the processed csv file
def readProcessedCSVFile(infile):

    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        return list(reader)


# sending the below to markdown
def printMarkdown(records, outfile):
    with open(outfile, 'w') as ofile:
        for idx, rc in enumerate(records):
            ofile.write("# " + str(idx + 1) + ". " + rc["name_alias"] + "\n\n")
            ofile.write("* Number of Appearances: " + rc["appearances"] + "\n")
            ofile.write("* Year Joined: " + rc["year"] + "\n")
            ofile.write("* Years Since Joining: "
                        + rc["years_since_joining"] + "\n")

            ofile.write("* URL: " + rc["url"] + "\n\n")
            ofile.write("## Notes \n\n")
            ofile.write(rc["notes"] + "\n\n")


def readCSVFile(infile):

    with open(infile, 'rU') as csvfile:  # open file
        reader = csv.DictReader(csvfile, delimiter=',')
        return list(reader)


def readFieldNames(infile):

    # open file
    fieldnames = []
    with open(infile, 'rU') as csvfile1:
        fieldreader = csv.reader(csvfile1, delimiter=',')
        fielddata = list(fieldreader)[0]
        fieldnames = [make_nice_name(field) for field in fielddata]
    return fieldnames


def cleanFieldNames(data):
    retdata = []
    for d in data:
        newRow = {}
        for key, val in d.items():
            newRow[make_nice_name(key)] = d[key]
        newRow = transform_record(newRow)
        retdata.append(newRow)
    return retdata


def transform_record(rdict):
    rdict["appearances"] = to_int(rdict["appearances"])
    rdict["current"] = to_bool(rdict["current"])
    rdict["year"] = to_int(rdict["year"])
    rdict['years_since_joining'] = date.today().year - rdict['year']
    rdict["notes"] = clean_notes(rdict["notes"])
    rdict["month_joinded"] = get_month(rdict["full_reserve_avengers_intro"])

    for key, val in rdict.items():
        if (key.startswith('death') or key.startswith('return')):
            rdict[key] = to_bool(rdict[key])
    return rdict


def writeCSVFile(outfile, writedata, fieldnames):
    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=fieldnames,
                                lineterminator='\n')
        writer.writeheader()
        for d in writedata:
            writer.writerow(d)
