class account:

    def __init__(self):
        pass

    def getDetail(self):
        self.__acNumber=int(input("enter account number="))
        self.__name=input("enter account holder name=")

    def showDetail(self):
        print("ACCOUNT NUMBER IS=",self.__acNumber)
        print("ACCOUNT HOLDER NAME IS=",self.__name)

    

    