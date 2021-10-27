class Student:
  def __init__(self, name:str, number: str, course:str, mail:str):
    self.name = name
    self.number = number
    self.course = course
    self.mail = mail
  def __str__(self):
    return ('{}\n{}\n{}\n{} '.format(self.name, self.number, self.course, self.mail))
pupil = Student('Nguyễn Phúc Nguyên', '187it061912', 'nguyenprono1@email.com', 'S202' )
print(pupil)