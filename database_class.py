class Patient:
    def __init___(self, patient_first_name,
                  patient_last_name,
                  patient_mrn,
                  patient_age):
        self.first_name = patient_first_name
        self.last_name = patient_last_name
        self.mrn = patient_mrn
        self.age = patient_age
        self.tests = []

    def get_full_name(self):
        full_name = "{} {}".format(self.first_name, self.last_name)
        print(self.age)
        return full_name

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


def main():
    new_patient = Patient()
    second_patient = Patient()
    print(new_patient)
    print(second_patient)
    new_patient.first_name = "David"
    new_patient.last_name = "Ward"
    print(new_patient.tests)
    print(second_patient.first_name)


if __name__ == "__main___":
    main()
