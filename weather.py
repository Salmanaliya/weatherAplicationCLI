import json, sys, requests
def call_weather(city: object) -> object:

    location = city

    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=11c6327f07a2a03a9353b0fd4c3ebe56" % location
    response = requests.get(url)
    response.raise_for_status()

    weatherdata = json.loads(response.text)
    print(weatherdata)

    temp = weatherdata['main']
    print('Average temperature is : ', temp['temp'] - 273.15, "(\u00B0C)")
    print('pressure is : ', temp['pressure'])

    humidity = weatherdata['main']
    print('humidity is : ', humidity['humidity'])

    pressure = weatherdata['wind']
    print('wind speed is : ', pressure['speed'], "\nwind degree is : ", pressure['deg'])

    print()

granted = False

def callAnotherCity():
    city = input("Enter country/city: ")
    call_weather(city)
    #callAnotherCity()




def grant():
    global granted
    granted = True

def login(name, password):
    success = False
    file = open("user_detail.txt", "r")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == name and b == password):
            success = True
            break
    file.close()
    if (success):
        print("Login Successful")
        grant()
        if (granted):
            print("Welcome to Weather Monitor")
            print("### USER DETAILS ###")
            print("Username: ", name)
        print("granted sucessfull")
        callAnotherCity()
    else:
        print("wrong user name or password")


def register(name, password):
    file = open("user_detail.txt", "a")
    file.write("\n" + name + "," + password)
    grant()


def access(option):
    global name
    if (option == "login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        #city = input("Enter your country/city ")
        login(name, password)


    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        print("Account Registered successfully")
        register(name, password)


def begin():
    global option
    print("welcome to weather condition")
    option = input("Login or Register (Login,Reg): ")
    if (option != "login" and option != "reg"):
        begin()

begin()
access(option)
print ("access weather update")









