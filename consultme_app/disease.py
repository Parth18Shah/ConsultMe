# import pickle
import joblib as jb
import pandas as pd

def get_diseaselist():
    diseaselist=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction','Peptic ulcer diseae','AIDS','Diabetes ',
  'Gastroenteritis','Bronchial Asthma','Hypertension ','Migraine','Cervical spondylosis','Paralysis (brain hemorrhage)',
  'Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D',
  'Hepatitis E', 'Alcoholic hepatitis','Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
  'Heart attack', 'Varicose veins','Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
  'Arthritis', '(vertigo) Paroymsal  Positional Vertigo','Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']
    return diseaselist

def get_symptomslist():
    symptomslist=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
  'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination',
  'fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy',
  'patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating',
  'dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
  'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
  'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
  'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
  'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
  'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
  'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
  'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
  'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
  'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
  'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
  'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
  'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
  'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
  'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
  'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
  'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
  'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
  'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
  'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
  'yellow_crust_ooze']
    alphabaticsymptomslist = sorted(symptomslist)
    return alphabaticsymptomslist

def predict_disease(inputed_symptoms):
    # with open('consultme_app/diseasepredictor/model_predict','rb') as f:
    #     mp = pickle.load(f)
    print("hello")
    with open('consultme_app/diseasepredictor/trained_model','rb') as mp:
        model = jb.load(mp)

    actual_ip = []
    symptomslist =  symptomslist=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination',
    'fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy',
    'patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating',
    'dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
    'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']
    for i in range(0,len(symptomslist)):
        actual_ip.append(0)       
    
    for i in range(0, len(symptomslist)):
        for z in inputed_symptoms:
            if z == 0:
                continue
            elif z == symptomslist[i]:
                actual_ip[i] = 1

    # predict = clf.predict([actual_ip])
        
        # return(predict)
    print(actual_ip)
    print("len",len(actual_ip))
    diseasename = model.predict([actual_ip])
    print(diseasename,len(diseasename))
    return diseasename

def get_description(diseasename):
    try:
        description = pd.read_csv('consultme_app/diseasepredictor/dataset/symptom_Description.csv')
        desp = list(description[description['Disease'] == diseasename[0]]['Description'])[0]
        return(desp)
    except Exception as ex:
        print(ex)
        return 0


def get_cure(diseasename):
    try:
        df = pd.read_csv('consultme_app/diseasepredictor/dataset/symptom_precaution.csv')
        # idx = df[df['Disease'] == diseasename[0]].index[0]
        # precautions = list(df.iloc[idx])[1:]    
        idx = df[df['Disease'] == diseasename[0]].values[0]
        print(idx)
        return idx
    except Exception as ex:
        print(ex)
        return 0

# my_model = pickle.load(open('model_predict','rb'))
# print(my_model.predict(X_test))
def get_specialization(predicted_disease):
    Rheumatologist = [  'Osteoarthristis','Arthritis']

    Cardiologist = [ 'Heart attack','Bronchial Asthma','Hypertension ']

    ENT_specialist = ['(vertigo) Paroymsal  Positional Vertigo','Hypothyroidism' ]

    Orthopedist = []

    Neurologist = ['Varicose veins','Paralysis (brain hemorrhage)','Migraine','Cervical spondylosis']

    Allergist_Immunologist = ['Allergy','Pneumonia',
    'AIDS','Common Cold','Tuberculosis','Malaria','Dengue','Typhoid']

    Urologist = [ 'Urinary tract infection',
        'Dimorphic hemmorhoids(piles)']

    Dermatologist = [  'Acne','Chicken pox','Fungal infection','Psoriasis','Impetigo']

    Gastroenterologist = ['Peptic ulcer diseae', 'GERD','Chronic cholestasis','Drug Reaction','Gastroenteritis','Hepatitis E',
    'Alcoholic hepatitis','Jaundice','hepatitis A',
        'Hepatitis B', 'Hepatitis C', 'Hepatitis D','Diabetes ','Hypoglycemia']

    if predicted_disease in Rheumatologist :
           consultdoctor = "Rheumatologist"
           
    if predicted_disease in Cardiologist :
        consultdoctor = "Cardiologist"
        
    elif predicted_disease in ENT_specialist :
        consultdoctor = "ENT specialist"
    
    elif predicted_disease in Orthopedist :
        consultdoctor = "Orthopedist"
    
    elif predicted_disease in Neurologist :
        consultdoctor = "Neurologist"
    
    elif predicted_disease in Allergist_Immunologist :
        consultdoctor = "Allergist/Immunologist"
    
    elif predicted_disease in Urologist :
        consultdoctor = "Urologist"
    
    elif predicted_disease in Dermatologist :
        consultdoctor = "Dermatologist"
    
    elif predicted_disease in Gastroenterologist :
        consultdoctor = "Gastroenterologist"
    
    else :
        consultdoctor = "Other"
    print(consultdoctor,predicted_disease)
    return consultdoctor