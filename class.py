planet_list =[{
    'Name':'Mercury',
    'Atmospheric gases':[],
    'Moons':0,
    'Rings':'No'
}, {
    'Name':'Venus',
    'Atmospheric gases':['Carbon dioxide', 'Nitrogen'],
    'Moons':0,
    'Rings':'No'
},
{
    'Name':'Earth',
    'Atmospheric gases':['Nitrogen', 'Oxygen'],
    'Moons':1,
    'Rings':'No'
}, {
    'Name':'jupitor',
    'Atmospheric gases':['Hydrogen', 'Helium'],
    'Moons':79,
    'Rings':'Yes'
},
{
    'Name':'Saturn',
    'Atmospheric gases':['Hydrogen', 'Helium'],
    'Moons':83,
    'Rings':'Yes'
},{
    'Name':'Uranus',
    'Atmospheric gases':['Hydrogen', 'Helium', 'Methane'],
    'Moons':27,
    'Rings':'Yes'
}
]

class Planets:
  def __init__(self, Planet_list):
       self.Planet_list=Planet_list
  def count_of_moons(self):
       count=0
       for item in self.Planet_list:
           if item['Rings'] == 'Yes':
               count+=item['Moons']
       print(count)
  def gas_in_more_planets(self):
       array=[]
       for item in self.Planet_list:  
            array= [*array, *item['Atmospheric gases']]
       count_of_item=[]
       for item in array:
           count_of_item.append(array.count(item))
       highest_count = max(count_of_item)
       list_a=[]
       for item in array:
           if array.count(item)==highest_count:
               list_a.append(item)
       print(*set(list_a))
      
planet = Planets(planet_list)
planet.count_of_moons()
planet.gas_in_more_planets()
       