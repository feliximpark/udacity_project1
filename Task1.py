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
# pass two datasets for identify all telephonnumbers
# count unique values and give back string-statement
def count_telnumbers_in_lists(calls, texts):
    # list for collecting numbers from different datasets
    all_numbers = set()
    for i in range(len(texts)):
        all_numbers.add(texts[i][0])
        all_numbers.add(texts[i][1])
    for i in range(len(calls)):
        all_numbers.add(calls[i][0])
        all_numbers.add(calls[i][1])
    # count unique values
        
    return f"There are {len(all_numbers)} different telephone numbers in the records."

print(count_telnumbers_in_lists(calls, texts))
