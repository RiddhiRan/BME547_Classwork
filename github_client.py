import requests


r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/rr238")
# print(type(r))
# print(r.status_code)
print(r.text)
# branches = r.json()

# message = {"user": "yl625", "message": "Today is a good day"}
# p = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
# json = message)
# print(p.text)
