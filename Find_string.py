"""
Created by : Ramprasad Ingle
Program:- Find a string in sentance
Usage: Find a string in given words
"""


# function created for counting substring
def count_substring(string, sub_string):
    index = 0
    count = 0
    while index < len(string):
        index = string.find(sub_string, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count

# main function starts from here
def main():
    print("Enter the string to reversed :")
    string = str(input())
    print("Enter the sub-string to find in words :")
    sub_string = str(input())
    count = count_substring(string, sub_string)
    print(f"Count of sub-string {sub_string} is :", count)
# Starter code starts from here
if __name__ =="__main__":
    main()