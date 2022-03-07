"""
Created by : Ramprasad Ingle
Program:- Reveresed a given interger number with forloop, stack, recursion etc
Usage: reversed a given number
"""
def reverse_num(num):
    rev = 0

    while(num>0):
        digit = num %10
        rev = rev*10 + digit

        num = num//10
    return rev    

def main():
    print("Entrer the number : ")
    num = int(input())
    rev = reverse_num(num)
    print("Number after reversed : ", rev)

if __name__=="__main__":
    main()