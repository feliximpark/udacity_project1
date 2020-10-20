"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:

    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Part A

# collect all numbers called from Bangalore, give back sorted list
def find_numbers_called_from_Bangalore(data):
    called_numbers = [] # set for collecting prefixes and area codes
    for i in range(len(data)):
        if data[i][0][:5] == "(080)":
            if data[i][1][0] == "(":
                index_nr = data[i][1].find(")")
                #saving area-code without brackets
                called_numbers.append(data[i][1][1:index_nr])
            elif data[i][1][:3] == "140":
                called_numbers.append("140")
            else:
                called_numbers.append(data[i][1][:4])
    return called_numbers

# print out results part A
def print_all_areacodes(set_prefixes):
    print("The numbers called by people in Bangalore have codes:")
    for elem in set_prefixes:
        print(elem)

def examine_bangalore_calls(data):
    list_all_called = find_numbers_called_from_Bangalore(data)
    set_unique_called = sorted(set(list_all_called))
    print_all_areacodes(set_unique_called)
    # Part B
    number_innercalls = list_all_called.count("080")
    percentage_innercalls = number_innercalls / len(list_all_called) * 100
    print(f"{round(percentage_innercalls,2)} percent of calls from fixed " \
        "lines in Bangalore are calls to other fixed lines in Bangalore.")

examine_bangalore_calls(calls)