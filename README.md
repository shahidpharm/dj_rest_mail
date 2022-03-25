# dj_rest_mail
Django user authentication and mail

This application is based on django rest framework. For user authentication djoser (https://djoser.readthedocs.io/en/latest/) package has been used here.


Use postman to check the below api endpoint are working or not.......

For Login:
http://{domainname}/auth/token/login
Method: post

headers: {

"Accept": "application/json",
"Content-Type": "application/json"

}


body: {
"email": "admin@rupga.net",
"password": "admin123"
}


response: 
{
    "auth_token": "authtoken will be displayed here"
}


For New user registration:

http://{domain name}/auth/users/
Method: post
headers: {

"Accept": "application/json",
"Content-Type": "application/json"

}

body:
{   "email":"avalidmail@gmail.com",
    "first_name": "X",
    "last_name": "Y",
    "password": "qwerty123",
    "re_password": "qwerty123",
}

After user creation below response will be shown and user will receive email with a link for activation. But I am not receiving--

{  
"id": 2,
"email":"avalidmail@gmail.com",
    "first_name": "X",
    "last_name": "Y",
    
}


For password reset:
http://{domain name}/auth//users/reset_password/

Method: post
headers: {

"Accept": "application/json",
"Content-Type": "application/json"

}

body:
{   "email":"avalidmail@gmail.com",
    
}
User will receive a link in email. But I am not receiving---
