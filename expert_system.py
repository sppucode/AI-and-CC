symptoms = {
    'fever':False,
    'cough':False,
    'headache':False,
    'rash':False
}


def ask_symptoms(symptoms):
    print("please answer in yes or no ")
    for i in symptoms:
        response = input(f'Do you have {i}?')
        if response == 'yes':
            symptoms[i]= True

def diagnose(symptoms):

    if symptoms["fever"] and symptoms["cough"] and symptoms["headache"] and symptoms["rash"]:
        print("You may have a serious viral infection (like Measles or Dengue). Immediate medical attention is recommended.")
    elif symptoms['fever'] and symptoms['cough'] and symptoms['headache']:
        print('You may have severe flu or viral infection')
    elif symptoms['fever'] and symptoms['cough'] and symptoms['rash']:
        print('You may have Measles')
    elif symptoms['fever'] and ['headache'] and symptoms['rash']:
        print('You may have Dengue or viral skin disease.')
    elif symptoms['fever'] and symptoms['cough']:
        print("you may have flu")
    elif symptoms["fever"] and symptoms["headache"]:
        print("You may have Meningitis.")
    elif symptoms["fever"] and symptoms["rash"]:
        print("You may have Measles.")
    elif symptoms["headache"] and not symptoms["fever"]:
        print("You may have a tension headache.")
    elif symptoms["fever"] and not (symptoms["cough"] or symptoms["headache"] or symptoms["rash"]):
        print("You may have a mild fever or initial infection.")
    elif symptoms["cough"] and not (symptoms["fever"] or symptoms["headache"] or symptoms["rash"]):
        print("You may have a respiratory infection or common cold.")
    elif symptoms["rash"] and not (symptoms["fever"] or symptoms["cough"] or symptoms["headache"]):
        print("You may have an allergic reaction or skin infection.")
    else:
        print("It's difficult to diagnose with the given symptoms. Please consult a doctor.")
    
    
ask_symptoms(symptoms)
diagnose(symptoms)






