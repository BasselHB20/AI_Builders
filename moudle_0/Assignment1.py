
students = [
    {"name": "Lara",  "age": 23, "track": "AI",   "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",   "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",  "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",   "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]},
]

def Part1(students):
    # 1
    print(f"The first student name is: {students[1]['name']}, and the last student name is: {students[-1]['name']}")
    # 2
    for student in students:
        if student['name']== "Rim":
            print(f"Rim's scores are: {student['scores']}")
            break
    # 3
    for student in students:
        print(f"{student['name']} is {student['age']} years old and studies {student['track']}")    
        
def Part2(students):
    #1
    new_list = []
    for student in students:
        if student['track']=='AI':
            new_list.append(student['name'])
    print(new_list)        
    print(len(new_list))
    #2
    new_list_v2 = [student['name'] for student in students if student['track'] == 'AI']
    print(new_list_v2)
    #3
    new_list_v3 = [student['name'] for student in students if student['hours_studied'] > 30]
    print(new_list_v3)
    #4
    new_list_v4 = [student['name'] for student in students if student['age'] > 24 and student['track'] =='AI']
    print(new_list_v4)
    
                    
def Part3(students):
    #1
    sum_Age = 0
    for student in students:
        sum_Age += student['age']
    print(sum_Age/len(students))   
    #2
    total_hours = 0
    for student in students:
            total_hours += student['hours_studied']
    print(total_hours)
    #3
    max_student = max(students, key=lambda s: s['hours_studied'])
    print(f"Student who studied the most hours is: {max_student['name']}, studied for {max_student['hours_studied']}")
    #4
    for student in students:
        print(f"name is: {student['name']}, average score is: {round(sum(student['scores'])/len(student['scores']),1)}")
            

def Part4(students):
    #1
    new_list = [{'name': student['name'], 'scores': student['scores']} for student in students]   
    print(new_list)  
    #2
    dict_track = {}
    for student in students:
        track = student["track"] 
        if track in dict_track:
            dict_track[track] += 1
        else:
            dict_track[track] = 1
    print(dict_track)  
    #3
    set_track = set()
    for student in students:
        set_track.add(student['track'])
    print(set_track)          
    """
    we use sets insted of lists becuase sets don't duplicate values
    """

# Part5
def filter_by_track(students, track):
    return [student for student in students if student['track']==track]

print(filter_by_track(students, 'AI'))
print(filter_by_track(students, 'Data'))

def average_score(student):
    return round(sum(student['scores']) / len(student['scores']), 2)
    
    
def top_student(students):
    max_average = 0
    max_student = ""
    for student in students:
        average = average_score(student)
        print(f"{student['name']} has average score is: {round(average,2)}")
        if average > max_average:
            max_average = average
            max_student = student['name']
    
    print(f"{max_student} has the highest average score {round(max_average,2)}")

def summary(students):
    new_dict = dict()
    new_dict["total_students"] = len(students)
    new_dict["average_age"] = round(sum([student['age'] for student in students]) / len(students),2)
    new_dict["track"] = set(student['track']  for student in students)
    return new_dict

print(summary(students))


# Bonus — Mini Data Pipeline
def report(students, min_hours):
    stud = [student for student in students if student['hours_studied']>= min_hours]
    new_list = []
    for i in stud:
        new_list.append({'name': i['name'], 'average_score' : average_score(i)})
    return new_list    

print(report(students, 48))
       
                
            
    
