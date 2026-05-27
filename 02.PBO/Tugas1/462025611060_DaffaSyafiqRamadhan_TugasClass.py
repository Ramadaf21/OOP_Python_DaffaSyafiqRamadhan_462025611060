class Campus:
    name = '';
    district = '';
 
class Student:
    name = '';
    nim = '';
    study_program = '';

Student1 = Student()
Student1.name = 'Daffa Syafiq Ramadhan'
Student1.nim = 'Teknik informatika'
Student1.study_program = '462025611060'
Campus1 = Campus()
Campus1.name = 'Universitas Darussalam'
Campus1.district = 'Siman, Ponorogo, Jawa Timur, Indonesia'
print(Student1.name)
print(Student1.nim)
print(Student1.study_program)
print(Campus1.name)
print(Campus1.district)


Student2 = Student()
Student2.name = 'Muhammad Zaky Ramadhan'
Student2.nim = 'Bahasa Inggris'
Student2.study_program = '123456789'
Campus2 = Campus()
Campus2.name = 'Universitas Airlangga'
Campus2.district = 'Surabaya, Jawa Timur, Indonesia'
print(Student2.name)
print(Student2.nim)
print(Student2.study_program)
print(Campus2.name)
print(Campus2.district)