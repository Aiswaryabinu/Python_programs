class parent:
    def add_names(self,name):
        self.name=name
    def __add__(self,other):
        name=self.name+other.name
        return name
u=parent()
v=parent()
u.add_names("Afnash")
v.add_names("Aiswarya")
fname=u+v
print(fname)
