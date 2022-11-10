# About

This is a description of running the app

# How to use
 - Clone repo Locally


 -  Before proceeding, you should have cloned all service repositories in one folder

   Setup you local env by creating a env and activating it
            i.e `python3 -m venv env` then source env/bin/activate

# Install Requirments

- Run `pip3 install -r requirements.txt`

# Run App

- Create a super user 
            i.e `python3 manage.py createsuperuser`  : provide your ** email and password **
- Server your project 
        i.e ` python3 manage.py runserver`  :- produces you ** url ** to use for apis

- Generate your token for user by  url (from above )/api-token-auth gives

                        `
                        {
                            "token": "865ee573bf8c964ee44221d5118f33ad71a528a9"
                        }
                        `

- Create a Trip with  {url}/api/v1/trips/ provide required fields
        # Header should have a 
        `Authorization : TOKEN <{token}>`

        `
        {
            "driver_id": "1",
            "vehicle_id": "111",
            "customer_id": "jkkghkgkhg",
            "address": "jkkjgkhghkgh",
            "cargo_tonnage": 100.50   
        }
        `