# area of circle

class Circle:
  pi = 3.14
  
  def area(self, radius):
    area = self.pi * (radius ** 2)
    return area

circle = Circle()

pizza_area = circle.area( (12 * 0.5) )  # inches
teaching_table_area = circle.area( (36 * 0.5) )  # inches
round_room_area = circle.area( (11_460 * 0.5) )  # inches
# radius is half the diameter

print(pizza_area)
print(teaching_table_area)
print(round_room_area)