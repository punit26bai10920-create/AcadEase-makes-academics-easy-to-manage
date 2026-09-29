intro="STUDENT MANAGEMENT SYSTEM"
print(intro)
print("1. Show all students\n2. Add student\n3. Search student\n4. Show highest scorer\n5. Exit")
students=[{'Name':'Gagnesh','Registration number': '26BAI19976','Branch':'AI-ML',"Calculus":50,"CSE":50,"EVs":50,"English":50},{'Name':'Punit','Registration number':"26BAI10920","Branch":'Computer science ai and ml',"Calculus":78,"CSE":68,"EVs":70,"English":72}]
students.append({"Name":"Krit","Registration number":'26BMR10003',"Branch":"Robotics and AI","Calculus":98,"CSE":87,"EVs":90,"English":85})
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
    calculus=int(input("Enter the calculus marks: "))
    cse=int(input("Enter the CSE marks: "))
    evs=int(input("Enter the EVs marks: "))
    english=int(input("Enter the English marks: "))
    students.append({'Name':add,'Registration number':add2,'Branch':branch,"Calculus":calculus,"CSE":cse,"EVs":evs,"English":english})
    print("you are added successfully")
 elif choice==3:
     search=input("Enter the registration number:")
     found=False
     for s in students:
         if search == s["Registration number"]:
             print("Name:",s['Name'])
             print("Branch:",s['Branch'])
             print("Calculus:",s['Calculus'])
             print("CSE:",s['CSE'])
             print("EVs:",s['EVs'])
             print("English:",s['English'])
             found=True
             break
     if not found:
         print("Student not found")
 elif choice==4:
     highest_marks=0
     for x in students:
         total_marks=x['Calculus']+x['CSE']+x['EVs']+x['English']
         if total_marks > highest_marks:
          highest_marks=total_marks
          topper=x['Name']
     print(topper,"scored the highest marks.\nMarks=",highest_marks)
 elif choice==5:
     print("Thank You")
     break
 else:
     print("Invalid choice")
