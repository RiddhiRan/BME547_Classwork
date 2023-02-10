def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
    # new_patient = [patient_name, patient_mrn, patient_age, []]
    new_patient = {"First Name": first_name, "Last Name": last_name, 
                   "MRN": patient_mrn, "Age": patient_age, "Tests":[]}
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Ann","Ables", 1, 34))
    db.append(create_patient_entry("Bob", "Boyles", 2, 45))
    db.append(create_patient_entry("Chris", "Chou", 3, 52))
    print(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 100)
    room_numbers = ["103", "232", "333"]
    print(db)
    print_directory(db, room_numbers)

def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient["First Name"], room_numbers[i]))
    for patient, rn in zip(db, room_numbers):
        print("Patient {} is in room {}".format(patient["First Name"], rn))
        
def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient["MRN"] == mrn_to_find:
            return patient
    return False

def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient == False:
        print("Bad entry")
    else:
        patient["Tests"].append([test_name, test_value])
    return None

def get_test_value_from_test_list(test_list, test_name):
    for test in test_list:
        if test[0] == test_name:
            return test["Tests"]
    return False

def get_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_value = get_test_value_from_test_list(patient["Tests"], test_name)
    return test_value

def get_full_name(patient):
    """ full_name = ""
    full_name.append(patient_name.get("First Name"))
    full_name.append(" ")
    full_name.append(patient_name.get("Last Name"))
    print(full_name) """
    return "{} {}".format(patient["First Name"], patient["Last Name"])

def print_database(db):
    for patient in db:
        print("MRN: {}, Full Name: {}, Age: {}".format(patient["MRN"],
                                                       get_full_name(patient), 
                                                       patient["Age"]))
        
    
if __name__ == "__main__":
    main_driver()