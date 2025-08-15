

class School:
    def __init__(self, name, level, number_of_students):
        self._name = name
        self._level = level
        self._number_of_students = number_of_students
    def __repr__(self):
        return f'{self.get_name()}\nStudents: {self.get_number_of_students()}\nEducation level: {self.get_level()}'
    

    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def get_number_of_students(self):
        return self._number_of_students

    def set_name(self, name):
        self._name = name
    def set_level(self, level):
        self._level = level
    def set_number_of_students(self, number_of_students):
        self.number_of_students = number_of_students

class Primary(School):
    def __init__(self, name, number_of_students, pickup_policy):
        super().__init__(name, 'primary', number_of_students)
        self.pickup_policy = pickup_policy
    def __repr__(self):
        school_repr = super().__repr__()
        return school_repr + '\n' + self.pickup_policy    
    
class Middle(School):
    def __init__(self, name, number_of_students):
        super().__init__(name, 'middle', number_of_students)
        

class High(School):
    def __init__(self, name, number_of_students, sports_teams):
        super().__init__(name, 'high', number_of_students)
        self.sports_teams = sports_teams
    def __repr__(self):
        school_repr = super().__repr__()
        return school_repr + '\n' + 'Sports available: ' + str(self.sports_teams)  

# school = School('here')
# print(school)

primary_school = Primary('PS_101', 116, 'The pickup policy is 3pm')
print(primary_school)

print('*******************\n\n')

middle_school = Middle('MS_201', 300)
print(middle_school)


print('*******************\n\n')

high_school = High('HS_301', 220, ['basketball', 'tennis', 'volleyball'])
print(high_school)