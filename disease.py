import pickle
import streamlit as st 


model=pickle.load(open("diabetes_model.pkl","rb"))


st.header("Predict Diabetes using ML algorithm")
col1,col2,col3=st.columns(3)
with col1:
    pregnancies=st.number_input("no of pregnancies",min_value=0,max_value=17)
with col2:
    glucose=st.number_input("Glucose level",min_value=0,max_value=200)
with col3:
    bloodpresure=st.number_input("Blood Presure value",min_value=0,max_value=120)
    
with col1:
    skinthickness=st.number_input("Skin Thickness value",min_value=0,max_value=100)
with col2:
    insulin=st.number_input("Insulin level",min_value=0,max_value=850)
with col3:
    bmi=st.number_input("BMI value",min_value=0.0,max_value=70.0)

with col1:
    diabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function value",min_value=0.0,max_value=3.0)
with col2:
    age=st.number_input("Age of the person",min_value=20,max_value=80)
   
if st.button("Make prediction"):
    df=[[pregnancies,glucose,bloodpresure,skinthickness,insulin,bmi,diabetesPedigreeFunction,age]]
    prediction=model.predict(df)[0]
    if prediction==1:
        st.subheader("The Person Having a Diabetes")
    else:
        st.subheader("The Person Not Having a Diabetes")


