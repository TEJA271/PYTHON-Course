import pandas as pd
import numpy as np

exam_data = { ' name ' :['Anusha' , 'Kesav' , 'Ajay' , 'Abhi' , 'Rohitha' , 'Navatej' , 'Nathen ', 'Chandu' , 'Aditya' , 'Jaibro'] ,
             
            'score': [12.5 , 9 , 16.5 , np.nan , 9 , 20 , 14.5, np.nan , 20  , 19.5],
             'attempts': [ 1 , 3 , 2 , 3 , 3 , 1 , 1 , 2 , 1 , 2] ,
              'qualify' : [ 'yes' , 'no' , 'yes' , 'no' , 'no' , 'yes' , 'yes' , 'no' , 'no' , 'yes' ] }
lables = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' ]
df = pd.DataFrame(exam_data , index = lables)
print(df.info())