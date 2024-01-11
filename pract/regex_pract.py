# Practice using Python regular expressions based on
# the W3Schools page explaining them
# https://www.w3schools.com/python/python_regex.asp

import re

def vowel_check(op, ts):
    if op == "1":  # count
        res = len(re.findall("[a-zA-z]*[aeiou][a-zA-z]*", ts))
        return "Number of words with vowels in test string: " + str(res)
    if op == "2":  # list words
        res = re.findall("[a-zA-z]*[aeiou][a-zA-z]*", ts)
        return "List of words with vowels in test string: " + str(res)
    if op == "3":  # list vowels
        res = re.findall("[aeiou]", ts)
        return "List of vowels in test string: " + str(res)
    
def main():
    print("================")
    print("Regex practice:")
    test_str = "Could one of our resident fire lords give me a quick advice in the fire channel"
    ts_print_flag = True
    while True:
        if ts_print_flag:
            print("Current test string:", test_str, "\n")
            ts_print_flag = False
        print("Operations list:\n================")
        print("1: count vowels\n2: list words with vowels\n3: list all vowels used\n4: input new test string\n0: quit")
        print("================")
        print("Input an operation number: ", end="")
        u_input = input()
        print()
        if re.findall("[0-4]", u_input):
            if u_input == "0":
                print("program closing...")
                break
            elif u_input == "4":
                test_str = input("Enter new test string:")
            else:
                print("Running operation", u_input + "...")
                print(str(vowel_check(u_input, test_str)) + "\n")
        else:
            print("ERR - unrecognized operation number, try again or use 0 to exit\n")

if __name__ == "__main__":
    main()