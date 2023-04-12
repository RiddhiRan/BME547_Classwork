from tkinter import filedialog
import requests
import base64
from flask import Flask, request, jsonify
app = Flask(__name__)


server = "http://vcm-21170.vm.duke.edu"


# Select image to upload
def select_image():
    filename = filedialog.askopenfilename(initialdir="Images")
    return filename


# Convert image to base 64 string
def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


# upload base64 string to server
def post_base64_string_to_server(b64_string, net_id, id_on):
    b64_dict = {"image": b64_string, "net_id": net_id, "id_no": id_on}
    r = requests.post(server + "/add_image", json=b64_dict)
    print(r.status_code)
    print(r.text)


# download watermarked image
def get_image(net_id, id_no):
    b64_string = requests.get(server + "/get_image/" +
                              net_id + "/" + str(id_no))
    b64_bytes = base64.b64decode(b64_string.text)
    with open("retrieved_file.jpg", "wb") as out_file:
        out_file.write(b64_bytes)


def main():
    filename = select_image()
    if filename == "":
        return
    b64_string = convert_image_file_to_base64_string(filename)
    print(b64_string)
    post_base64_string_to_server(b64_string, "rr238", 64)
    get_image("rr238", 64)


if __name__ == "__main__":
    main()
