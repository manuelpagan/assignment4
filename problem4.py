# Manny Pagan
# Sept 24th Python Course
# Assignment 5
# Due: Oct 10th

user_input = input("What calculation would you like to do? (add, sub, mult, div)")
prompt_one = int(input("What is number 1?"))
prompt_two = int(input("What is number 2?"))

def problem_4_calculator():
    if "add" in user_input:
        print(prompt_one + prompt_two)
    elif "sub" in user_input:
        print(prompt_one - prompt_two)
    elif "mult" in user_input:
        print(prompt_one * prompt_two)
    elif "div" in user_input:
        print(prompt_one / prompt_two)
    else:
        print("Try typing add, sub, mult or div in the first prompt. Spelling Matters.")

problem_4_calculator()

