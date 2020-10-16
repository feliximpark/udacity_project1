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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# convert list to set to delete duplicates and count unique values
def count_unique_listvalues(list_to_count): 
    set_from_list = set(list_to_count)
    unique_values = len(set_from_list)
    return unique_values

# collect all numbers (caller/sender and called/recipient) 
# in one list
def collect_telnumbers_from_list(number_list):
    collection_list = []
    for i in range(len(number_list)): 
        data_row = number_list[i]
        collection_list.extend([data_row[0], data_row[1]])
    return collection_list

# pass two datasets for identify all telephonnumbers
# count unique values and give back string-statement
def count_telnumbers_in_lists(*args):
    # list for collecting numbers from different datasets
    all_numbers = []
    for i in range(len(args)):
        actual_list = args[i]
        tel_numbers = collect_telnumbers_from_list(actual_list)
        all_numbers.extend(tel_numbers)
    # count unique values
    result = count_unique_listvalues(all_numbers)     
    return f"There are {result} different telephone numbers in the records."

print(count_telnumbers_in_lists(calls, texts))

# def test():
#     assert count_unique_listvalues([1,2,2,3]) == 3
#     assert count_unique_listvalues([1,1,1,1,1,2]) == 2
#     assert count_unique_listvalues([1,2,3,4,5,2,1]) == 5
#     assert collect_telnumbers_from_list([[123, 456, 789, 000]])==[123,456]
#     assert collect_telnumbers_from_list([[987, 654, 321], [111, 222, 333, 444],
#         [123, 4565, 788], [987, 222]]) == \
#             [987, 654, 111, 222, 123, 4565, 987, 222]

#     print("run all tests")
# test()