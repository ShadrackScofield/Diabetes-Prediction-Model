# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:00:56 2022

@author: Scofield
"""
import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('C:/Users/Scofield/diabetes_ai_model.sav', 'rb')) # rb means read binary

# Creating afunction for prediction

def diabetes_prediction(input_data):
    # changing the input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting for one instance
    reshaped_input_data = input_data_as_numpy_array.reshape(1, -1)


    prediction = loaded_model.predict(reshaped_input_data)

    print(prediction)

    if prediction[0]==0:
        return 'This person is healthy'
    else:
        return 'This person is diabetic'
        
        
def main():
    # Give the web app a title
    st.title('Diabetes Predition Web App')
    # Getting the input data from the user
    Pregnancies = st.text_input('Enter Your Number of Pregnancies')
    Glucose = st.text_input('Enter Your Glucose level')
    BloodPressure = st.text_input('Enter Your Blood pressure')
    SkinThickness = st.text_input('Enter Your Skin Thickness')
    Insulin = st.text_input('Enter Your Insulin level')
    BMI = st.text_input('Enter Your BMI')
    DiabetesPedigreeFunction= st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Enter Your Age')
    
         
   # Code for prediction
    diagnosis= ''
   
   # creating a prediction button
   
    if st.button('Diabetes Test Result'):
       diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])

    st.success(diagnosis)
   
   
   
   
   
if __name__=='__main__':
    main()
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   