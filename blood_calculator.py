def interface():
    print("Blood calculator")
    keep_running =True
    while keep_running:
        print("Options")
        print("1 - Cholestrol")
        print("9 - Quit")
        choice = input("Select an option")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            cholestrol_driver()
    print("Program ending") 

def cholestrol_driver():
    cholestrol_in = cholestrol_input()
    cholestrol_analy = cholestrol_analysis(cholestrol_in)
    cholestrol_output(cholestrol_in, cholestrol_analy)

def cholestrol_input():
    cholestrol_value = input("Enter the Cholestrol results")
    cholestrol_value = int(cholestrol_value)
    return cholestrol_value

def cholestrol_analysis(cholestrol_int):
    if cholestrol_int < 200:
        answer = "Normal"
    elif 200 <= cholestrol_int <= 239:
        answer = "Borderline High"
    elif 240 <= cholestrol_int:
        answer = "High"
    return answer

def cholestrol_output(cholestrol_value, cholestrol_analy):
    print("The Cholestrol result of {} is considered {}".format(cholestrol_value, cholestrol_analy))

interface()

def interface():
    print("Blood calculator")
    keep_running =True
    while keep_running:
        print("Options")
        print("1 - LDL")
        print("9 - Quit")
        choice = input("Select an option")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            LDL_driver()
    print("Program ending") 

def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)

def LDL_input():
    LDL_value = input("Enter the LDL results")
    LDL_value = int(LDL_value)
    return LDL_value

def LDL_analysis(LDL_int):
    if LDL_int < 130:
        answer = "Normal"
    elif 130 <= LDL_int < 159:
        answer = "Borderline High"
    elif 160 <= LDL_int < 189:
        answer = "High"
    elif 190 <= LDL_int:
        answer = "Very High"
    return answer

def LDL_output(LDL_value, LDL_analy):
    print("The LDL result of {} is considered {}".format(LDL_value, LDL_analy))

interface()
