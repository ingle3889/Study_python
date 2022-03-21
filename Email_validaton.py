import re

def email_validation(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def main():
    print("Enter valid email id :")
    email_id = str(input())

    val = email_validation(email_id)
    if val == True:
        print("Valid email id")
    else:
        print("Invalid email id")
        
if __name__ =="__main__":
    main()