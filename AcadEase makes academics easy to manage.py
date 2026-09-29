intro="STUDENT MANAGEMENT SYSTEM"
print(intro)
print("1. Show all students\n2. Add student\n3.Search student\n4. Show highest scorer\n5. Exit")
students=[{'Name':'Gagnesh','Registration number': '26BAI19976','Branch':'AI-ML',"Physics":50,"Chemistry":50},{'Name':'Punit','Registration number':"26BAI10920","Branch":'Computer science ai and ml','Physics':78,'Chemistry':68}]
students.append({"Name":"Krit","Registration number":'26BMR10003',"Branch":"Robotics and AI","Physics":98,"Chemistry":87})
students[1]['Branch']='Computer Science'
while True:
 choice=int(input("Enter your choice:"))
 if choice==1:
    print("***List of Students***")
    for i in students:
        print(i['Name'])
 elif choice==2:
    add=input("Enter the name of student you want to add:")
    add2=input("Enter the registration number:")
    branch=input("Enter the branch:")
    physics=int(input("Enter the physics marks: "))
    chemistry=int(input("Enter the chemistry marks: "))
    info_students.append({'Name':add,'Registration number':add2,'Branch':branch,"Physics":physics,"Chemistry":chemistry})
    print("you are added successfully")
 elif choice==3:
     search=input("Enter the registration number:")
     if search == students[0]["Registration number"]:
         print("Name:",students[0]['Name'])
         print("Branch:",students[0]['Branch'])
         print("Physics:",students[0]['Physics'])
         print("Chemistry:",students[0]['Chemistry'])
     elif search == students[1]["Registration number"]:
         print("Name:",students[1]['Name'])
         print("Branch:",students[1]['Branch'])
         print("Physics:",students[1]['Physics'])
         print("Chemistry:",students[1]['Chemistry'])
     elif search == students[2]["Registration number"]:
         print("Name:",students[2]['Name'])
         print("Branch:",students[2]['Branch'])
         print("Physics:",students[2]['Physics'])
         print("Chemistry:",students[2]['Chemistry'])
     else:
         print("Name:",students[3]['Name'])
         print("Branch:",students[3]['Branch'])
         print("Physics:",students[3]['Physics'])
         print("Chemistry:",students[3]['Chemistry'])
 elif choice==4:
     highest_marks=0
     for x in students:
         total_marks=x['Physics']+x['Chemistry']
         if total_marks > highest_marks:
          highest_marks=total_marks
     print(x['Name'],"scored the highest marks.\nMarks=",highest_marks)
else:
     print("Thank You")
