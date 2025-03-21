import streamlit as st
import pickle
import pandas as pd

# Load the trained model
file_path = r"D:\pyu\lung_disease_model.pkl"
with open(file_path, 'rb') as file:
    classifier = pickle.load(file)

st.title("Lung Cancer Prediction App")

# Create input fields for each feature
gender = st.selectbox("Gender", ["M", "F"])
age = st.number_input("Age", min_value=0, max_value=120, value=30)
smoking = st.selectbox("Smoking", ["YES", "NO"])
yellow_fingers = st.selectbox("Yellow Fingers", ["YES", "NO"])
anxiety = st.selectbox("Anxiety", ["YES", "NO"])
peer_pressure = st.selectbox("Peer Pressure", ["YES", "NO"])
chronic_disease = st.selectbox("Chronic Disease", ["YES", "NO"])
fatigue = st.selectbox("Fatigue", ["YES", "NO"])
allergy = st.selectbox("Allergy", ["YES", "NO"])
wheezing = st.selectbox("Wheezing", ["YES", "NO"])
alcohol_consuming = st.selectbox("Alcohol Consuming", ["YES", "NO"])
coughing = st.selectbox("Coughing", ["YES", "NO"])
shortness_of_breath = st.selectbox("Shortness of Breath", ["YES", "NO"])
swallowing_difficulty = st.selectbox("Swallowing Difficulty", ["YES", "NO"])
chest_pain = st.selectbox("Chest Pain", ["YES", "NO"])

# Convert categorical inputs to numerical (as the model expects)

gender_m = 1 if gender == "M" else 0
smoking_num = 1 if smoking == "YES" else 0
yellow_fingers_num = 1 if yellow_fingers == "YES" else 0
anxiety_num = 1 if anxiety == "YES" else 0
peer_pressure_num = 1 if peer_pressure == "YES" else 0
chronic_disease_num = 1 if chronic_disease == "YES" else 0
fatigue_num = 1 if fatigue == "YES" else 0
allergy_num = 1 if allergy == "YES" else 0
wheezing_num = 1 if wheezing == "YES" else 0
alcohol_consuming_num = 1 if alcohol_consuming == "YES" else 0
coughing_num = 1 if coughing == "YES" else 0
shortness_of_breath_num = 1 if shortness_of_breath == "YES" else 0
swallowing_difficulty_num = 1 if swallowing_difficulty == "YES" else 0
chest_pain_num = 1 if chest_pain == "YES" else 0

# Create a DataFrame from the user input
user_input = pd.DataFrame([[gender_m, age, smoking_num, yellow_fingers_num, anxiety_num,
                            peer_pressure_num, chronic_disease_num, fatigue_num, allergy_num,
                            wheezing_num, alcohol_consuming_num, coughing_num,
                            shortness_of_breath_num, swallowing_difficulty_num, chest_pain_num]],
                           columns=['GENDER_M', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
                                    'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ',
                                    'WHEEZING', 'ALCOHOL CONSUMING', 'COUGHING',
                                    'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN'])

if st.button("Predict"):
    prediction = classifier.predict(user_input)
    if prediction[0] == 1:
        st.write("Prediction: Lung Cancer (YES)")
    else:
        st.write("Prediction: No Lung Cancer (NO)")