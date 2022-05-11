# OTA
This are the files that I created when developing an OTA system for an ESP32.

# Note:
- Change all the `ip_address` to the ip address of the system that is going to run the OTA server.
- You should have a system that is free to be used as an server.
- You should have the ESP32 setup with the `.bin` file in the link https://micropython.org/download/esp32/
- To setup the ESP32, check out https://docs.micropython.org/en/latest/esp32/tutorial/intro.html

# Working Principle:
<img src="https://drive.google.com/file/d/1lD_eUbedrPQLy86DDMEz-1sq6UXjKoFm/preview" width="640" height="480">

# Installation:
- Setting up the OTA server:
  1. Download the files present in the `service_code` folder to your machine.
  2. Change the `token_of_user` and `repo_name` to the respective values in the `.env` file.
  3. Change the `ip_address` to the system's ip address in the `server.py`.
  4. Change the `port_number` to any integer of your choice in the `server.py`.
  5. Install all the requirements using the command `python3 -m pip install -r requirements.txt`
  6. Then run the `server.py` file to start the server.
- Setting up the ESP32:
  1. Download the files present in the `microcontroller_code` folder to your machine.
  2. Change the `ip_address` to the server's ip address in the `config.env`.
  3. Change the `port_number` to the server's port number in the `config.env`.
  4. Change the `ssid` and `password` in the `networks.json` file to the ssid and password of the network to which the server is connected to.
  5. Install all the requirements using the command `python3 -m pip install -r requirements.txt`
  6. Run the following commands:
    - `ampy -p {PORT} put config.env` where PORT is the COM port at which your ESP32 board is connected to.
    - `ampy -p {PORT} put networks.json` where PORT is the COM port at which your ESP32 board is connected to.
    - `ampy -p {PORT} put boot.py` where PORT is the COM port at which your ESP32 board is connected to.
# Resources:
- https://docs.micropython.org/en/latest/esp32/tutorial/ - for developing the code for microcontroller
- https://fastapi.tiangolo.com/ - for developing the server
- https://docs.python.org/3/library/hashlib.html - for checking for updates
- https://docs.python.org/3/library/base64.html - for encrypting and decrypting data sent by server to microcontroller
