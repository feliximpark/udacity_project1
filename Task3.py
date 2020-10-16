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

def identify_prefixes(number):
    # collect all prefixes with parentheses
    if number[:2] == "(0":
        # identify the Bangalore area code
        if number[:5] == "(080)":
            return "(080)"
        # identify every other area code
        else:
            split_string = number.split(")")
            prefix = split_string[0] + ")"
            return prefix
    # check for mobile numbers (all with space in the middle)
    elif " " in number: 
        split_string = number.split(" ")
        return split_string[0][:4]
    elif number[:3]=="140":
        return number[:3]
    else: 
        return "no prefix found"

# sort values with built-in method sorted()
def sort_values(list_to_sort):
    sorted_list = sorted(list_to_sort)
    return sorted_list

# collect all numbers called from Bangalore, give back sorted list
def find_numbers_called_from_Bangalore(data): 
    list_prefixes = [] # list for collecting prefixes and area codes
    for i in range(len(data)):
        row = data[i]
        if identify_prefixes(row[0])=="(080)":
            list_prefixes.append(identify_prefixes(row[1]))
    list_prefixes_ordered = sort_values(list_prefixes)
    return list_prefixes_ordered

# print out results part A
def print_all_areacodes(list_prefixes):
    set_prefixes = set(list_prefixes)
    ordered_prefixes = sort_values(set_prefixes)
    print("The numbers called by people in Bangalore have codes:")
    for elem in ordered_prefixes:
        print(elem)

# part B
# count bangalor-numbers called from Bangalore
def count_bangalore_prefix(list_numbers): 
    counter = 0
    for elem in list_numbers: 
        if elem == "(080)": 
            counter +=1
    return counter

# calculate percentag share
def percentage_inner_bangalore_calls(list_numbers):
    int_b_to_b_calls = count_bangalore_prefix(list_numbers) 
    int_all_b_calls = len(list_numbers)
    return (int_b_to_b_calls / int_all_b_calls) * 100

# prepare print-Statement
def print_percentage_innercalls(percent):
    return f"{round(percent,2)} percent of calls from fixed lines in "\
        "Bangalore are calls to other fixed lines in Bangalore."

# final function calling helper-functions
def examine_bangalore_calls(data): 
    list_numbers = find_numbers_called_from_Bangalore(data)
    print_all_areacodes(list_numbers)
    percentage_innercalls = percentage_inner_bangalore_calls(list_numbers)
    print(print_percentage_innercalls(percentage_innercalls))

examine_bangalore_calls(calls)








# def test(): 
#     assert identify_prefixes("(080)345 6667") == "(080)"
#     assert identify_prefixes("12344456") == "no prefix found"
#     assert identify_prefixes("1234 5567") == "1234"
#     assert identify_prefixes("140667890") == "140"
#     assert sort_values(["03", "05", "01", "04"]) == ["01", "03", "04", "05"]
#     assert sort_values(['01', '04', '03', '(080)', '(070)', '(07030)']) == \
#         ['(070)', '(07030)', '(080)', '01', '03', '04']
#     assert find_numbers_called_from_Bangalore(\
#         [["(080) 234", "140556"], ["140", "567"], \
#             ["(080)666777", "8969 456"], ["(080)447", "(080)4456"]]) == \
#             ["(080)","140", "8969"]
#     assert count_bangalore_prefix(["(080)", "080", "(070)", "140", "(080)"])==\
#         2
#     print("all tests finished")
# test()
