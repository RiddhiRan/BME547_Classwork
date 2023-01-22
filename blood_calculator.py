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