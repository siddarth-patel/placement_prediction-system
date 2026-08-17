import streamlit as st
import pickle

with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎯 Placement Prediction")

cgpa = st.slider("CGPA", 1.0, 10.0, 7.0)
apt = st.slider("Aptitude Score", 1, 100, 60)
cs = st.slider("Communication Skills", 1, 100, 50)
ins = st.selectbox("Internship", ["Yes", "No"])
project = st.number_input("Projects", min_value=0, max_value=20, value=2)

submit = st.button("Predict Placement", type="primary")

if submit:

    internship = 1 if ins == "Yes" else 0

    result = model.predict([[cgpa, apt, cs, internship, project]])

    if result[0] == 1:
        st.success("🎉 Student can be placed.")
    else:
        st.error("Student may not be placed.")
