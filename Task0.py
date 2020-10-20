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
# find data of the first text in texts-dataset
def find_first_text(texts):
    return f"First record of texts, {texts[0][0]} texts "\
         f"{texts[0][1]} at time {texts[0][2]}"

# find data of the last call in calls-dataset
def find_last_call(calls): 
    return f"Last record of calls, {calls[-1][0]} calls "\
        f"{calls[-1][1]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds"

#final function calling helper-functions
def text_output(texts, calls):
    print(find_first_text(texts))
    print(find_last_call(calls))

text_output(texts,calls)


