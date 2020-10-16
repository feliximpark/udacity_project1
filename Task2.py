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
# change list to type set to delete duplicates
def return_unique_listvalues(list_to_count):
    set_from_list = set(list_to_count)
    return list(set_from_list)

# collect numbers from dataset
def collect_telnumbers_from_list(number_list):
    collection_list = []
    for i in range(len(number_list)):
        data_row = number_list[i]
        collection_list.extend([data_row[0], data_row[1]])
    return collection_list

# iterate over dataset to collect all numbers with speaking-time
def check_every_row(data, numbers_list):
    # dictionary to collect all numbers and seconds per number
    numbers_dict = {}
    #iterating every unique number
    for num in numbers_list: 
        #creating key for number
        numbers_dict[num] = 0
        # iterating every row of calls-dataset
        for i in range(len(data)): 
            actual_row = data[i]
            number_one = actual_row[0]
            number_two = actual_row[1]
            if (num == number_one) | (num == number_two): 
                    seconds = actual_row[3]
                    numbers_dict[num] = numbers_dict[num] + int(seconds)
    return numbers_dict

#find highest value and corresponding key
def find_highest_dictvalue(dict):
    highest_key = max(dict, key=dict.get)
    highest_value = dict[highest_key]
    return highest_key, highest_value

# final function where helper-function are called
def find_longest_telephonetime(data): 
    list_numbers = collect_telnumbers_from_list(data)
    list_unique_numbers = return_unique_listvalues(list_numbers)
    
    create_dict_all_numbers = check_every_row(data, list_unique_numbers)
    print(create_dict_all_numbers)
    highest_values = find_highest_dictvalue(create_dict_all_numbers)
    return f"{highest_values[0]} spent the longest time, {highest_values[1]}"\
        " seconds, on the phone during during September 2016."

print(find_longest_telephonetime(calls))


# def test():
#     assert return_unique_listvalues([1,2,2,3]) == [1,2,3]
#     assert return_unique_listvalues([1,1,1,1,1,2]) == [1,2]
#     assert return_unique_listvalues([1,2,3,4,5,2,1]) == [1,2,3,4,5]
#     assert collect_telnumbers_from_list([[123, 456, 789, 000]])==[123,456]
#     assert collect_telnumbers_from_list([[987, 654, 321], [111, 222, 333, 444],
#         [123, 4565, 788], [987, 222]]) == \
#             [987, 654, 111, 222, 123, 4565, 987, 222]
#     assert check_every_row([[123, 234, 10, 10], [567, 123, 20, 5]], \
#         [123,234,567]) == {123:15, 234:10, 567:5}
#     assert find_highest_dictvalue({23: 45, 67: 120, 25: 34}) == (67, 120)

#     print("run all tests")
# test()