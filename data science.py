import numpy as np
data_type = [ ('name' , 'S15')  ,  ('class' , int)  ,  ('height' , float) ]
students_details = [ ('NATHEN ', 6 , 38.9)  ,  ('ABHI', 11 , 70.6)  ,  ('AJAY' , 12 , 80.07 )  ,  ('Navatej' , 6 , 49.9)]
students = np.array(students_details , dtype= data_type)
print('Sort By Height')
print(np.sort(students , order = 'height'))