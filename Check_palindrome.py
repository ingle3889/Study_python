"""
Created by : Ramprasad Ingle
Program:- Chek palindrome

"""
def palindrome(String):
    rev = ''
    for STR in String:
        rev = STR + rev
    
    if String == rev:
        return True
    else :
        return False        

def main():
    print("Enter the words")
    String= str(input())

    rev_str = String[::-1]
    
    rev = palindrome(String)
    print("String is Palindrome :", rev)

    print("Simple way to reverse the string :",rev_str)

if __name__=="__main__":
    main()



