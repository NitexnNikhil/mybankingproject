# mybankingproject

This repository related to the project named as BAMS(Banking Account Management System)

Software Being Devloped using:

Backend - Python 3 Libraries used - random, re, SQLite3 and OS Flask

Frontend - HTML and Javascript

Project Description :

In this project we have developed a module that used to genrate the automated random 12 digit account number for the user on every account creation and used to initiate a random balance from range 1000 to 10000

Note:

Project is under testing phase and final version of this code may be slighlt diffrent from now

This is the Beta version released within production to see user response

Project Working:

Step 1: Home.html

    this used to show the home page consist of the two buttons 
    a. Create a account
    b. Login 
Step 2: Onclick on the Create a account button

    -> The button will redirect the home page to the form page consiting of text field form to enter user details by the user itself
Step 3: On Successfull Account creation the message poped out " Form submitted Successfully "

    -> After the formed submitted successfully the user data copy would get stored  in *accounts.txt*

    In this Path : D:\masai proj BAMS(Bank Account Managment System)\Account details\accounts.txt
Step 4 : After the Creating the account the page will redirect to the login page

    -> In this page user have to enter his credentials and the random genrated (using Flask) captcha shown in login form has to enter

      -> If the user is authenticated the user account no and the user balance will be shown in the account.html page

      -> Else showing error User is not valid
Step 5: After the Successfull Login the Login page will be redirect to the account page

      -> The details going to be fetched from the database as "bankaccount.db" form the app.py
Step 6: If the user now want to Logout then need to press the logout buttom present at the bottom right
