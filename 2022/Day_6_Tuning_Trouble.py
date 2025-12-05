# directly getting the input test from the test problem
from get_input import fetch_input

# Logic for when we want to test cases
testing_case = False

if testing_case:
    input_text = input("Please paste the text set you want to test on!:\n")
else:
    input_text = fetch_input(2022,6)


# The actual problem solving logic

# Part-1
for i in range(len(input_text)-3):
    current_chunk=input_text[i:i+4]
    if len(set(current_chunk)) == 4:
        print(current_chunk)
        print(f"Found the correct position at {i+4}")
        break

# Part-2
# Since we take the buffer of 14 characters now, we can simply do a increment of 10 everywhere we were using a 4 character window!
for i in range(len(input_text)-3-10):
    current_chunk=input_text[i:i+4+10]
    if len(set(current_chunk)) == 4+10:
        print(f"Found the correct position at {i+4+10}")
        break



