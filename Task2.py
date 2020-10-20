"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# iterate over dataset to collect all numbers with speaking-time
def create_dict(data):
    # dictionary to collect all numbers and seconds per number
    numbers_dict = dict()
    #iterating every unique number
    for i in range(len(data)):
        # check every number, if allready existing in dict, sum up 
        # actual seconds of the number with seconds in actual row
        numbers_dict[data[i][0]] = numbers_dict.get(data[i][0], 0) \
            + int(data[i][3])
        numbers_dict[data[i][1]] = numbers_dict.get(data[i][1], 0) \
            + int(data[i][3])
    return numbers_dict

#find highest value and corresponding key
def find_highest_dictvalue(dic):
    print(len(dic))
    highest_key = max(dic, key=dic.get)
    highest_value = dic[highest_key]
    return highest_key, highest_value

# final function where helper-function are called
def find_longest_telephonetime(data):
    create_dict_all_numbers = create_dict(data)
    highest_values = find_highest_dictvalue(create_dict_all_numbers)
    return f"{highest_values[0]} spent the longest time, {highest_values[1]}"\
        " seconds, on the phone during during September 2016."

print(find_longest_telephonetime(calls))

