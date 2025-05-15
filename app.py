# from flask import Flask,redirect,url_for,render_template, request, jsonify
# import pickle
# import sklearn
# import pandas as pd
# import numpy as np
# import joblib

# app = Flask(__name__)

# @app.route('/')
# def home():
#     # Render the HTML file
#     return render_template('home.html')

# @app.route('/submit-data', methods=['POST'])
# def submit_data():
#     # Retrieve data from the form
#     gender = request.form.get('gender')
#     age = request.form.get('age')
#     occupation = request.form.get('occupation')
#     sleep_duration = request.form.get('sleep_duration')
#     sleep_quality = request.form.get('sleep_quality')
#     physical_activity = request.form.get('physical_activity')
#     stress_level = request.form.get('stress_level')
#     bmi_category = request.form.get('bmi_category')
#     blood_pressure = request.form.get('blood_pressure')
#     heart_rate = request.form.get('heart_rate')
#     daily_steps = request.form.get('daily_steps')

#     # Process the data
#     data = {
#         "gender": gender,
#         "age": age,
#         "occupation": occupation,
#         "sleep_duration": sleep_duration,
#         "sleep_quality": sleep_quality,
#         "physical_activity": physical_activity,
#         "stress_level": stress_level,
#         "bmi_category": bmi_category,
#         "blood_pressure": blood_pressure,
#         "heart_rate": heart_rate,
#         "daily_steps": daily_steps,
#     }
#     print(data)
#     processed_data = preprocess_data(data)
#     data = pd.DataFrame(processed_data)
#     predict = makeprediction(data)
#     final_class = {0:'Healthy', 1:'Insomnia', 2:'Sleep Apnea'}
#     print(final_class[predict[0]])
#     return render_template("home.html",message=final_class[predict[0]])

# def preprocess_data(data):
#     categorical_map = c_map = {'gender':{'Female': 0, 'Male': 1},
#                                'occupation':{'Accountant': 0,'Doctor': 1,'Engineer': 2, 'Lawyer': 3, 'Manager': 4,'Nurse': 5,'Sales Representative': 6,'Salesperson': 7,'Scientist': 8,'Software Engineer': 9,'Teacher': 10},
#                                'bmi_category':{'Normal': 0, 'Normal Weight': 1, 'Obese': 2, 'Overweight': 3}
#                                }
#     temp_data = data
#     for key in categorical_map.keys():
#         temp_data[key] = categorical_map[key][data[key]]
#     temp_data['Systolic'],temp_data['Diastolic']= map(int,temp_data['blood_pressure'].split('/'))
#     print(temp_data)
#     del temp_data['blood_pressure']
#     final_data ={ x: [temp_data[x]] for x in temp_data.keys()}
#     final_data = process_name(final_data)
#     return final_data

# def process_name(data):
#     model_cols = {'gender':'Gender', 'age':'Age', 'occupation':'Occupation', "sleep_duration":'Sleep Duration',"sleep_quality": 'Quality of Sleep',
#        "physical_activity":'Physical Activity Level',"stress_level": 'Stress Level', "bmi_category":'BMI Category',"heart_rate": 'Heart Rate',
#        "daily_steps":'Daily Steps', 'Systolic':'Systolic', 'Diastolic':'Diastolic'}
#     result = {}
#     for key in data.keys():
#         result[model_cols[key]]=data[key]
#     return result

# def makeprediction(data):
#     model = joblib.load('templates/models/gb_model_2jb.joblib')
#     result = model.predict(data)
#     return result 
    

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    # Render the HTML file
    return render_template('home.html')

@app.route('/submit-data', methods=['POST'])
def submit_data():
    # Retrieve data from the form
    gender = request.form.get('gender')
    age = request.form.get('age')
    occupation = request.form.get('occupation')
    sleep_duration = request.form.get('sleep_duration')
    sleep_quality = request.form.get('sleep_quality')
    physical_activity = request.form.get('physical_activity')
    stress_level = request.form.get('stress_level')
    bmi_category = request.form.get('bmi_category')
    blood_pressure = request.form.get('blood_pressure')
    heart_rate = request.form.get('heart_rate')
    daily_steps = request.form.get('daily_steps')

    # Process the data
    data = {
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,
        "Sleep Duration": sleep_duration,
        "Quality of Sleep": sleep_quality,
        "Physical Activity Level": physical_activity,
        "Stress Level": stress_level,
        "BMI Category": bmi_category,
        "Blood Pressure": blood_pressure,
        "Heart Rate": heart_rate,
        "Daily Steps": daily_steps,
    }
    print(data)
    processed_data = preprocess_data(data)
    data_df = pd.DataFrame(processed_data)
    predict = makeprediction(data_df)
    final_class = {0: 'Healthy', 1: 'Insomnia', 2: 'Sleep Apnea'}
    prediction_result = final_class[predict[0]]

    # Render the results on the home page
    return render_template("home.html", message=prediction_result, input_data=data)

def preprocess_data(data):
    categorical_map = {
        'Gender': {'Female': 0, 'Male': 1},
        'Occupation': {
            'Accountant': 0, 'Doctor': 1, 'Engineer': 2, 'Lawyer': 3, 'Manager': 4,
            'Nurse': 5, 'Sales Representative': 6, 'Salesperson': 7, 'Scientist': 8,
            'Software Engineer': 9, 'Teacher': 10
        },
        'BMI Category': {'Normal': 0, 'Normal Weight': 1, 'Obese': 2, 'Overweight': 3}
    }
    temp_data = data.copy()
    for key in categorical_map.keys():
        temp_data[key] = categorical_map[key][data[key]]
    temp_data['Systolic'], temp_data['Diastolic'] = map(int, temp_data['Blood Pressure'].split('/'))
    del temp_data['Blood Pressure']
    return {x: [temp_data[x]] for x in temp_data.keys()}

def makeprediction(data):
    model = joblib.load('templates/models/gb_model_2jb.joblib')
    result = model.predict(data)
    return result

if __name__ == '__main__':
    app.run(debug=True)

