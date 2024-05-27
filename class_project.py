class Countries:
    country = 0
    def __init__(self,name,location,capital):
        self.name = name
        self.location = location
        self.capital = capital
        Countries.country += 1
        self.countries = []
    
    def get_info(self):
        return self.countries
    
    # def __str__(self):
    #     return '%s,%s,%s' % (self.name,self.location,self.capital)
    
    def __repr__(self):
        return f"{self.name.title()} is situated in the {self.location}. Capital city of {self.name.capitalize()} is {self.capital.title()}"
    
    def __eq__(self,other):
        return self.name == other
    def __neq__(self,other):
        return self.name != other
  
    def __add__(self,value):
        if isinstance(value,Countries):
            new_country =  Countries(f"{self.name} {value.name}")
            new_country.countries = self.countries + value.countries
            return new_country
        
    def __sub__(self, nation):
        if nation in self.countries:
            self.countries.pop(nation)
    
    def __mul__(self):
        pass
    def __truediv__(self):
        pass
    def __del__(self):
        pass
    def __cmp__(self):
        pass

    def __le__(self,other):
        return self.name <= other
    def __lt__(self,other):
        return self.name < other
    def __gt__(self,other):
        return self.name > other
    def __ge__(self,other):
        return self.name >= other
    
    def add_country(self,*nation):
        self.nation = nation
        if self.nation  not in self.countries:
            self.countries.append(nation)
            for index,country in enumerate(self.countries):
                print(index+1, country)

    def __getitem__(self,index):
        return self.countries[index]
    
    def __len__(self):
        return len(self.countries)
    
    def __setitem__(self,index,value):
        if isinstance(value,Countries):
            self.countries[index]=value

    def __call__(self):
        return [country for country in self.countries]
    

n = Countries('mongolia','east asia','Ulan-baatar.')
n2 = Countries('kyrgystan','central asia','bishkek')
n3 = Countries('uzbekistan','central asia','tashkent')
n4 = Countries('myanmar','south asia','NayPyiTaw')
n5 = Countries('somali','east africa','mogadishu')
n6 = Countries('indonesia','south asia','jakarta')
print(n)
print(n2)
print(n3)
print(n4)
print(n5)
print(Countries.country)
isinstance(n,Countries)

# nation = Countries('usa','north america','washington')
# nation.add_country('france')
# nation.add_country('sinegal')
# nation.add_country('kenya')
# nation.add_country('germany')
# print(nation.get_info())
# #print(nation.__call__())
# print(len(nation))