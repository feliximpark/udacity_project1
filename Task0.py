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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# find first element
def find_first_record(data):
    first_record = data[0]
    return first_record

#find last element
def find_last_record(data):
    last_record = data[-1]
    return last_record

# find data of the first text in texts-dataset
def find_first_text(texts):
    first_text = find_first_record(texts)
    incoming_number = first_text[0]
    answering_number = first_text[1]
    time = first_text[2]
    return f"First record of texts, {incoming_number} texts "\
         f"{answering_number} at time {time}"

# find data of the last call in calls-dataset
def find_last_call(calls): 
    last_call = find_last_record(calls)
    incoming_number = last_call[0]
    answering_number = last_call[1]
    time = last_call[2]
    seconds = last_call[3]
    return f"Last record of calls, {incoming_number} calls "\
        f"{answering_number} at time {time}, lasting {seconds} seconds"

#final function calling helper-functions
def text_output(texts, calls):
    print(find_first_text(texts))
    print(find_last_call(calls))

text_output(texts,calls)


# def tests():
#     assert find_first_record(texts) == \
#         ['97424 22395', '90365 06212', '01-09-2016 06:03:22']
#     assert find_last_record(calls) == \
#         ['98447 62998', '(080)46304537', '30-09-2016 23:57:15', '2151'] 
    
#     print("run all tests")

#tests()        


