"""
Created by : Ramprasad Ingle
Program:- Reveresed a given string with forloop, stack, recursion etc
Usage: check whether given string is anagram or not
"""



# reversed a string  
def revesed_string(String):
    rev = ""
    for STR in String:
        rev = STR + rev
    return rev    

# reversed a string using stack    
def revesed_stack(String):
    # Creating an empty stack (list to use as stack)
    stack = []
    # Push all characters of string to stack

    for char in String:
        stack.append(char)
    # Pop all characters of string and add it to the rev
    rev= ""
    while len(stack) > 0:
        last = stack.pop()
        rev = rev + last
        # print(rev and last)
    return rev    
#use .pop() method to get the last element of the list

# Revesed a string using recursion
def reversed_recur(String):

    if len(String) == 0:
        return String
    else :
        return reversed_recur(String[1:]) + String[0]    


# main function starts from here
def main():
    print("Enter the string to reversed :")
    Input_string = str(input())

    OBS = revesed_string(Input_string)
    Stack = revesed_stack(Input_string)
    Str_rec = reversed_recur(Input_string)

    print("Output using for loop: ",OBS)
    print("Output using for Stack: ", Stack)
    print("Output using for Recursion: ", Str_rec)
    print("Fastest way to reversed a string :", Input_string[::-1])

# Starter code starts from here
if __name__ =="__main__":
    main()