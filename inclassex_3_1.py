import requests

r = requests.get("http://vcm-7631.vm.\
                  duke.edu:5002/get_patients/rr238")
print(r.text)
blood_type_donor = requests.get("http://vcm-7631.vm.\
                                 duke.edu:5002/get_blood_type/M1")
# print(blood_type_donor.text)
blood_type_receiver = requests.get("http://vcm-7631.vm.\
                                    duke.edu:5002/get_blood_type/M3")
# print(blood_type_receiver.text)
if blood_type_donor.text == blood_type_receiver.text:
    match = "Yes"
else:
    match = "No"
blood_dict = {"Name": "rr238", "Match":  match}
p = requests.post("http://vcm-7631.vm.\
                   duke.edu:5002/match_check", json=blood_dict)
print(p.text)
