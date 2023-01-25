# onlineFoodDelivery

- Clone the repository
- Create a virtual environment in the main directory of the repository with the following command:

  ``` python -m venv venv ```
- Install all the requirements using the command:

  ``` pip install -r requirements.txt ```
- Sign up into stripe and create your account
- Go to Developers --> API keys and copy your STRIPE SECRET KEY and STRIPE PUBLIC KEY
- Paste the keys in .env file
- Install stripe CLI 
- Login to stripe CLI using command
  
  ``` stripe login --api-key <your_stripe_secret_key> ```
- listen to webhooks on by running the command

  ``` stripe listen --forward-to <your-webhook-url> ```
- Make migrarions to db using the commands:
  
  ```  python manage.py makemigrations ```
  
  ```  python manage.py migrate ```
- Run the server with 
  ``` python manage.py runserver ```
