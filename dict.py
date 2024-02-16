acronyms = {'LOL':'Laugh Out Load', 'GTG':'Got To Go', 'IDK': "I Don't Know", 'TBH':'To Be Honest'}

print(acronyms['IDK'])

# Get Method -> Wont crush your program
definition = acronyms.get('BTW')
#print(definition) #None
#None - means absence of value and values to False in a conditional

if definition:
    print(definition) #will execute if there is value other than None
else:
    print("Key doesnt exist")   #Execute for None

sentence = 'IDK'+" what happened "+'TBH'
translation = acronyms.get('IDK')+' what happended '+ acronyms.get('TBH')

print('sentence: ', sentence)
print('translation:', translation)