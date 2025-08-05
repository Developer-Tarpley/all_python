'''
  Grade Class
'''
class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    if self.score > self.minimum_passing:
      return 'Pass'
    else:
      return 'Did not pass.'

'''
  Student Class
'''
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {
      # date : True/False
    }
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
  
  def get_average(self):
    grades_sum = sum(self.grades)
    average = grades_sum / len(self.grades)
    return average

'''
  instances
'''  
roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)
pieters_grade = Grade(100)
print(pieters_grade.is_passing())
pieter.add_grade(pieters_grade)
