contacts = {
    'number': 4,
    'students':
        [
            {'name':'Sarah Holderness','email':'sarah@gmail.com'},
            {'name':'Piyush Jain','email':'piyush@gmail.com'},
            {'name':'Harry Potter','email':'harry@yahho.com'},
            {'name':'Bruce Wayne','email':'bruce@batman.com'}
        ]
}

print("Student emails:")
for student in contacts['students']:
    
    print(student['email'])