class Library:
    year=2024
    def __init__(self):
        self.name=""
        self.id=0
        self.book=""
        
        print("Constructor")
    def set_name(self):
        #global n,i
        self.name=input("ENTER THE NAME :")
        self.id=int(input("ENTER THE ID "))
        self.book="blahblah"
    def get_data(self):
        print("NAME :"+self.name)
        print("ID :"+str(self.id))
        print("BOOK :"+ self.book)
        print("Year :"+str(Library.year))

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1





Library.add_year()
d=Library()
e=Library()
d.set_name()
d.get_data()

e.set_name()
e.get_data()

