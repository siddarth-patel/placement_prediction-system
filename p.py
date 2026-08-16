import streamlit as st
import pickle
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)
st.title("Placement-Prediction App")
cgpa=st.slider("CGPA",1.0,10.0,7.0)
apt=st.slider("Aptitude Score",1,100,60)
cs=st.slider("communication Skills",1,100,50)
ins=st.selectbox("Internship",["Yes","No"])
# otr=st.slider("Other Skills",1,100,50)
project=st.number_input("Projects",0)
submit=st.button("Predict Placement",type="primary")

if submit:
    if ins=="Yes":
       ins=1
    else:
        ins=0
    result=model.predict([[cgpa,apt,cs,ins,project]])
    if result[0]==1:
        st.success("student can be placed.")
    else:
        st.error("student can not be placed.")


