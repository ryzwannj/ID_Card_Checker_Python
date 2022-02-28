from lib2to3.pgen2.token import LESS
from locale import format_string
from urllib.parse import SplitResult

from cv2 import split



class IdCard:
    def __init__(self, firstname: str, 
                       name : str, 
                       birthday : str, 
                       gender : str, 
                       firstAdressDepartment:str,  
                       lineOne:str, 
                       lineTwo:str, 
                       delivery_date:str):
    
        self.firstname = firstname #UPPERCASE
        self.name = name #UPPERCASE
        self.firstAdressDepartment = firstAdressDepartment #Your first adress departement
        self.gender = gender # M : for Male or F : for Female
        self.lineOne = lineOne #FirstLine ID Card eg:  IDFRAPITT<<<<<<<<<<<<<<<<<<<<<923337
        self.lineTwo = lineTwo #SecondLine ID card eg: 1400022013533PATRICK<<<<<<<0305141M1
        self.delivery_date = delivery_date #Delivery card Date : DDMMYY
        self.birthday = birthday #format == DDMMYY

        self.space = 1

        self.splitLineOne = [self.lineOne[i:i + self.space] for i in range(0, len(self.lineOne), self.space)]
        self.splitLineTwo = [self.lineTwo[i:i + self.space] for i in range(0, len(self.lineTwo), self.space)]

        

    def checkIdLineOne(self):

        lenOfSplitLineOne = len(self.splitLineOne)

        print("---------------------------------------------------------")
        print('lenght of the Firstline : ' + str(lenOfSplitLineOne))

        if (lenOfSplitLineOne == 36):
            print(self.splitLineOne)
            print("LENGHT (1) Check : OK")

            id_char = "".join(self.splitLineOne[0:2])

            if (id_char == 'ID'):
                print("ID Check : OK")
            else:
                print("ID Check : ------ERROR------")
                return 

            fra_char = "".join(self.splitLineOne[2 : 5])

            if (fra_char == 'FRA'):
                print("FRA Check : OK")
            else:
                print("FRA Check : ------ERROR------")  
                return 

            LESS_MARK_FIRSTLINE =  25
            markAssigenementFirst = LESS_MARK_FIRSTLINE - len(self.firstname)

            lenOfFirstname = len(self.firstname)
            firstname_char = "".join(self.splitLineOne[5 : 5+lenOfFirstname])
            


            if(firstname_char == self.firstname):
                print("FIRST_NAME Check : OK")
            else: 
                print("FIRST_NAME Check : ------ERROR------")
                return 
            
            lessMark_char = "".join(self.splitLineOne[5+lenOfFirstname : 30])

            if (lessMark_char == markAssigenementFirst*'<'):
                print("LESS_MARK (1) Check : OK")
            else:
                print("LESS_MARK (1) Check : ------ERROR------")
                return 

            self.splitDepartement = [self.firstAdressDepartment[i:i + self.space] for i in range(0, len(self.firstAdressDepartment), self.space)]
            departement_char = "".join(self.splitLineOne[30 : 33])

            self.threeDigitDepartement = "".join(self.splitDepartement[0 : 3])
            print("3 DIGITS : " + self.threeDigitDepartement)
            self.twoDigitDepartement = "".join(self.splitDepartement[0 : 2])
            print("2 DIGITS : " + self.twoDigitDepartement)
            print("CONVERTING TO 3 DIGITS : " + '0' + self.twoDigitDepartement )

            if(departement_char == self.threeDigitDepartement or departement_char == '0' + self.twoDigitDepartement):
                print("DEPARTEMENT Check : OK")
            else: 
                print("DEPARTEMENT Check : ------ERROR------")
                return 

            agentID_char = int("".join(self.splitLineOne[33 : 36]))

            if(agentID_char <= 999 or agentID_char > 000):
                print("AGENT_ID Check : OK")
                print("THE FIRST LINE IS: CORRECT")
            else:
                print("AGENT_ID Check : ------ERROR------")
                return

        else: 
            print("THE ID CARD IS FAKE")
            return 

    def checkIdLineTwo(self):
        self.checkIdLineOne

        from algoControlKey import algo_controlKey

        splitLineTwo = [self.lineTwo[i:i + self.space] for i in range(0, len(self.lineTwo), self.space)]
        print(splitLineTwo)
        lenOfSplitLineTwo = len(splitLineTwo)
        print("---------------------------------------------------------")
        print('lenght of the Secondline : ' + str(lenOfSplitLineTwo))

        if(lenOfSplitLineTwo == 36):
            print(splitLineTwo)
            print("LENGHT (2) Check : OK")
            
            splitDate = [self.delivery_date[i:i + self.space] for i in range(0, len(self.delivery_date), self.space)]

            deliverycardYear_char = "".join(splitLineTwo[0 : 2])

            splitdateYear_char = "".join(self.delivery_date[6 : 8])

            deliverycardMonth_char = "".join(splitLineTwo[2 : 4])

            splitdateMonth_char = "".join(self.delivery_date[2 : 4])

            if(deliverycardMonth_char == splitdateMonth_char and deliverycardYear_char == splitdateYear_char):
                print("DELIVERY CARD Check : OK")
            else:
                print("DELIVERY CARD : ------ERROR------")
                return

            departement_char = "".join(splitLineTwo[4 : 7])

            threeDigitDepartement = "".join(self.firstAdressDepartment[0 : 3])
            print("3 DIGITS : " + threeDigitDepartement)
            twoDigitDepartement = "".join(self.firstAdressDepartment[0 : 2])
            print("2 DIGITS : " + twoDigitDepartement)
            print("CONVERTING TO 3 DIGITS : " + '0' + twoDigitDepartement )

            if(departement_char == threeDigitDepartement or departement_char == '0' + twoDigitDepartement):
                print("DEPARTEMENT Check : OK")
            else: 
                print("DEPARTEMENT Check : ------ERROR------")
                return 

            splitFirstPartLineTwo = "".join(splitLineTwo[0 : 7])
            
            

            partOneLineTwo = int(algo_controlKey(splitFirstPartLineTwo))
            splitSecondPartLineTwo = "".join(splitLineTwo[7 : 12])

            partTwoLineTwo = int(algo_controlKey(splitSecondPartLineTwo))
            getKeyOne = "".join(splitLineTwo[12:13])
            format_string = int(getKeyOne)

            if((partOneLineTwo + partTwoLineTwo) == format_string):
                print("ALGO CONTROL KEY Check : OK")
            else:
                print("ALGO CONTROL KEY Check : ------ERROR------")
                return

            LESS_MARK_SECONDLINE =  14
            markAssigenementSecond = LESS_MARK_SECONDLINE - len(self.name)

            lenOfName = len(self.name)
            name_char = "".join(self.splitLineTwo[13 : 13+lenOfName])


            if(name_char == self.name):
                print("NAME Check : OK")
            else: 
                print("NAME Check : ------ERROR------")
                return

            lessMarkSecond_char = "".join(self.splitLineTwo[13+lenOfName : 27])

            if (lessMarkSecond_char == markAssigenementSecond*'<'):
                print("LESS_MARK (2) Check : OK")
            else:
                print("LESS_MARK (2) Check : ------ERROR------")
                return
            
            split_birthday = splitLineTwo[27 : 33]

            split_birthday_yearLineTwo = "".join(splitLineTwo[27 : 29])
            split_birthday_monthLineTwo = "".join(splitLineTwo[29 : 31])
            split_birthday_dayLineTwo = "".join(splitLineTwo[31 : 33])

            splitBirthday = [self.birthday[i:i + self.space] for i in range(0, len(self.birthday), self.space)]

            birthdayDay = "".join(splitBirthday[0 : 2])
            birthdayMonth = "".join(splitBirthday[2 : 4])
            birthdayYear = "".join(splitBirthday[6 : 8])

            if(split_birthday_yearLineTwo == birthdayYear and split_birthday_monthLineTwo == birthdayMonth and split_birthday_dayLineTwo == birthdayDay):
                print("BIRTHDAY CHECK : OK")
            else:
                print("BIRTHDAY CHECK : ------ERROR------")
                return

            algo_birthday = int(algo_controlKey(split_birthday))

            getKeyTwo = int("".join(splitLineTwo[33 : 34]))


            if(algo_birthday == getKeyTwo):
                print("ALGO BIRTHDAY Check : OK")
            else:
                print("ALGO BIRTHDAY Check : ------ERROR------")
                return

            split_genderIDLine = "".join(splitLineTwo[34 : 35])
            genderKey = "".join(self.gender)
            if(split_genderIDLine == genderKey):
                print("GENDER KEY Check : OK")
            else:
                print("GENDER KEY Check : ------ERROR------")
                return

            lineOne = str("".join(self.splitLineOne[0 : 36]))
            lineTwo = str("".join(self.splitLineTwo[0 : 35]))
            both = lineOne + lineTwo

            algoBothLines = int(algo_controlKey(both))

            if(algoBothLines == int("".join(splitLineTwo[35 : 36]))):
                print("ALGO LAST DIGIT (2) : OK")
                print("THE SECOND LINE IS: CORRECT")
            else:
                print("ALGO LAST DIGIT (2) : ------ERROR------")
                return
        else:
            print("THE CARD IS FAKE")

    def CheckId(self):
        self.checkIdLineOne()
        self.checkIdLineTwo()
