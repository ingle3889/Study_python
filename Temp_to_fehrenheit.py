# Program converts tempereteure to hrenheit
# By Ramprasad Ingle
def TempConverter(celcius):
    fahern = 0
    fahern = 9/5*celcius+32
    return fahern

def main():
    print("What is the Celsius tempereture?")
    cel = float(input())
    ret = TempConverter(cel)
    print("The tempera ture is", ret, "degrees fahrenheit .")

if __name__=="__main__":
    main()