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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def delete_duplicates(list_with_duplicates):
    list_to_set = set(list_with_duplicates)
    set_to_list = list(list_to_set)
    return set_to_list

def find_all_numbers(data):
    list_all_callers = []
    list_all_called = []
    for i in range(len(data)): 
        row = data[i] 
        list_all_callers.append(row[0])
        list_all_called.append(row[1])
        list_all_callers_clean = delete_duplicates(list_all_callers)
        list_all_called_clean = delete_duplicates(list_all_called)
    
    return list_all_callers_clean, list_all_called_clean

def compare_lists(list1, list2): 
    # give back only values of list1, that are NOT in list2
    list_cleaned = [el for el in list1 if el not in list2]
    return list_cleaned

def clean_caller_list(calls, texts):
    caller_list, called_list = find_all_numbers(calls)
    textsender_list, textrecipient_list = find_all_numbers(texts)
    lists_to_compare = [called_list, textsender_list, textrecipient_list]
    print(len(called_list))
    print(len(textsender_list))
    print(len(textrecipient_list))
    for li in lists_to_compare: 
        caller_list = compare_lists(caller_list, li)
    return caller_list

def print_marketing_nums(calls, texts):
    nums_list = clean_caller_list(calls, texts)
    # sort list
    nums_list = sorted(nums_list)
    print("These numbers could be telemarketers: ")
    for num in nums_list: 
        print(num)

print(print_marketing_nums(calls, texts))


# def test(): 
#     assert delete_duplicates(["(080)344", "140756", "080344", "(080)344"]) ==\
#         ["(080)344", "080344", "140756"]
#     assert compare_lists([1,2,3,4,5], [3,4,5,6,7,8]) == [1,2]
#     assert compare_lists(["123", "456", "7", "6"], ["123", "6", "4567"]) == \
#         ["456", "7"]
#     assert find_all_numbers([["123", "456", "789"], ["321", "654"], \
#         ["123", "987", "111", "222" ]]) == \
#             (["321", "123"], ["456", "654", "987"])
#     print("all tests finished")

# test()
