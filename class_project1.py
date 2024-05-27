class Perfect:
    totalNumberOfUsingThisCode = 0
    def __init__(self,last,first):
        self.last = last
        self.first = first
        self.talabalar = []
        self.talabalar_soni = 0
        Perfect.totalNumberOfUsingThisCode +=1
        
    @classmethod
    def HowManyTimes(cls):
        return cls.totalNumberOfUsingThisCode
    def add_students(self,*names):
        for name in names:
            self.talabalar.append(name)
            self.talabalar_soni += 1
    def remove_students(self,*name):
        if name in self.talabalar:
            self.talabalar.remove(name)
            self.talabalar_soni -= 1
        else:
            print(f'sorry, {name} talaba mavjud emas')
    def get_students(self):
        for i, talaba in enumerate(self.talabalar):
            print(i+1, talaba.capitalize())

from uuid import uuid4
class Stunning(Perfect):
    def __init__(self,last,first,birthdate,nationality):
        super().__init__(last,first)
        self.birthdate = birthdate
        self.nationality = nationality
        self.__id = uuid4()
    def getId(self):
        return self.__id
    def get_nation(self, nationality):
        self.nationality = nationality
    def get_birthday(self,birthtime):
        self.birthtime = birthtime
    def get_students(self):
        info = f"Fullname: {self.first}-{self.last}"
        info += f" who was born in {self.birthdate}."
        info += f" Nationality: {self.nationality}"
        return info
    def __repr__(self):
        return '%s,%s,%d,%s' % (self.last, self.first, self.birthdate, self.nationality)
    #def __str__(self):
        #return '{}{}{}'.format(self.first,self.last,self.nationality)
    #def get_info(self):
     #   return f"{self.first}, {self.last},{self.nationality}"
