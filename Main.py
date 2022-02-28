from idCardChecker import *

firstname = '' #UPPERCASE
name = '' #UPPERCASE
birthday = '' #DDMMYY
gender = '' #M : for Male or F : for Female
departement = '' #Your first adress departement with 5 digit
line_one = '' #FirstLine ID Card eg:  IDFRAPITT<<<<<<<<<<<<<<<<<<<<<923337
line_two = '' #SecondLine ID card eg: 1400022013533PATRICK<<<<<<<0305141M1
card_delivery = '' #Delivery card Date : DDMMYY

card1 = IdCard(firstname, name, birthday, gender, departement, line_one, line_two, card_delivery)
card1.CheckId()
