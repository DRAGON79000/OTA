# OTA
This are the files that I made for an OTA system.

# Note:
- Change all the `ip_address` to the ip address of the system that is going to run the OTA server.
- Change all the `port_number` to the port number that you are going to use for the OTA server. This can be any integer.
- Change the `ssid` and `password` to your respective network's ssid and password.
- Change the `token_of_user` to the your github token.
- Change the `repo_name` to the repo at which the main code exists.

# Installation:
- Setting up the OTA server
  1. Download the files present in the `service_code` folder to your machine.
  2. Change the `token_of_user` and `repo_name` to the respective values in the `.env` file.
  3. Change the `ip_address` to the system's ip address.
  4. Change the `port_number` to any integer of your choice.
  5. Install all the requirements using the command `python3 -m pip install -r requirements.txt`
