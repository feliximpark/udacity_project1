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

def check_all_numbers(call, text):
    telemarketers = set()
    text_sender = set([txt[0] for txt in text])
    text_receiver = set([txt[1] for txt in text])
    caller = set([cll[0] for cll in call])
    call_receiver = set([cll[1] for cll in call])
    for call_nr in caller: 
        if call_nr not in text_sender and call_nr not in text_receiver and \
            call_nr not in call_receiver: 
            telemarketers.add(call_nr)
    return sorted(telemarketers) 
    
def print_marketing_nums(calls, texts):
    set_telemarketers = check_all_numbers(calls, texts)
    print("These numbers could be telemarketers: ")
    for num in set_telemarketers: 
        print(num)

print_marketing_nums(calls, texts)