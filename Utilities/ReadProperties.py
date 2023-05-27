import configparser

config = configparser.RawConfigParser()
config.read("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\Configurations\\config.ini")

class Readconfig():

    @staticmethod
    def geturl():
        url = config.get("common info","Url")
        return url


    @staticmethod
    def getusername():
        username = config.get("common info","UserName")
        return username


    @staticmethod
    def getpassword():
        password = config.get("common info","Password")
        return password

