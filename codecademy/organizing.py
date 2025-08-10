'''
    restaurant menu and franchise application
'''
# Business Class
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return f'Welcome to {self.name}'

# Franchise class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    '''
    def available_menus(self, time):
    available = []
    time_int = int(''.join(filter(str.isdigit, time)))
    for menu in self.menus:
        start = int(''.join(filter(str.isdigit, menu.start_time)))
        end = int(''.join(filter(str.isdigit, menu.end_time)))
        if start <= time_int <= end:
            available.append(menu)
    return available
    '''
    if time.endswith('pm'):
      time = ''.join(filter(str.isdigit, time))
      for menu in self.menus:
        end = ''.join(filter(str.isdigit, menu.end_time))
        if menu.end_time.endswith('pm') and int(time) <= int(end):
          print(menu)
    else:
      time = ''.join(filter(str.isdigit, time))
      for menu in self.menus:
        start = ''.join(filter(str.isdigit, menu.start_time))
        if menu.start_time.endswith('am') and int(time) >= int(start):
          print(menu)
      

# Menu class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return f'{self.name} menu available from {self.start_time} to {self.end_time}'
  def calculate_bill(self, purchased_items):
    '''
    for item in purchased_items:
    if item in self.items:
        bill_total += self.items[item]
    else:
        print(f"Warning: {item} not found in menu.")
    '''
    bill_total = 0
    for item in purchased_items:
      bill_total = bill_total + self.items[item] 
    # print(f'Your bill total is: ${bill_total}')
    return f'Your bill total is: ${bill_total}'

# brunch
brunch = Menu(
  'Brunch',
  {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  },
  '11am',
  '4pm' 
)
# print(brunch)
# print(brunch.items)
# brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])

# early-bird dinners
early_bird = Menu(
  'Early-bird',
  {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
  },
  '3pm',
  '6pm'
)
# print(early_bird)
# print(early_bird.items)
# early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

# dinner
dinner = Menu(
  'Dinner',
  {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
  },
  '5pm',
  '11pm'
)
# print(dinner)

# kids menu
kids = Menu(
  'Kids',
  {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  },
  '11am',
  '9pm'
)
# print(kids)

arepas_menu = Menu('Take a\' Arepa', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
    },
    '10am',
    '8pm'
)
# print(arepas_menu)


'''
    Franchises
'''
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
# print(flagship_store)
# print(flagship_store.available_menus('12 noon'))
# print(flagship_store.available_menus('11am'))
# print(flagship_store.available_menus('8am'))
# print('')
# print(flagship_store.available_menus('5pm'))
# print(flagship_store.available_menus('8pm'))

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])
# print(new_installment)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])
# print(arepas_place)

'''
    Businesses
'''
business_1 = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])
# business_2 = Business('Basta Fazoolin\' with my Heart')
business_2 =Business('Take a\' Arepa!', [arepas_place])

line_01 =  '           ***************************'
line_02 = f'           *{business_2}*'
line_03 = f'           *  {arepas_place}  *'
line_04 = f'           *                         *'
line_05 = f'  *{arepas_menu}*'

print(line_01)
print(line_02)
print(line_03)
print(line_01)
print(line_04)
print(line_05)
print(line_04)
print(line_01)