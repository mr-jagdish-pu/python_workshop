#WAP to store the data name,age,address of five students, ask name to retrieve the persons data. also ask if he wants to see all data, if y response then show else not

students = {}
list_of_students = {
    #dummy 5 DICTIONARIES
 "stu1" : {'name':'John','age':20,'address':'New York'},
  "stu2" :  {'name':'Doe','age':21,'address':'California'},
  "stu3" :  {'name':'Jane','age':22,'address':'Texas'},
   "stu4" : {'name':'Tom','age':23,'address':'Florida'},
 "stu5" :   {'name':'Jerry','age':24,'address':'Arizona'}
}



def show_data():
    stu_name = input("Enter the name of the student: ")
    for student in list_of_students:
       if list_of_students[student]['name'] == stu_name:
            print("Name: ",list_of_students[student]['name'])
            print("Age: ",list_of_students[student]['age'])
            print("Address: ",list_of_students[student]['address'])
            break
        
    show = input("Do you want to see all data? (y/n): ")
    if show == 'y':
        for student in list_of_students:
            print("Name: ",list_of_students[student]['name'])
            print("Age: ",list_of_students[student]['age'])
            print("Address: ",list_of_students[student]['address'])
    else:
        print("Thank you")
show_data()