# JSON (38-39)

import json

## Creates a key:value pair
person_dict = {'firstName': 'Alfa',
               'lastName': 'Marine'}

person_json = json.dumps(person_dict)
print(person_json)

## Creates a key:list pair
hobbies_dict = ['crochet', 'coloring', 'defending R', 'gardening', 'reading']

hobbies_json = json.dumps(hobbies_dict)
print(hobbies_json)
person_dict['hobbies'] = hobbies_dict

## Creates a key:dict pair
student_dict = {}
student_dict['Belem'] = person_dict

student_json = json.dumps(student_dict)
print(student_json)
