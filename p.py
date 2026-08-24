import streamlit as st

st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Placement Prediction System")

st.subheader("Predict Your Placement Chances")

st.write("""
This system will help students estimate their placement possibility
based on academic performance, aptitude, communication skills,
internship experience and projects.
""")

st.markdown("---")

st.subheader("How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### 📝 1. Enter Details")
    st.write("Provide your academic and skill-related information.")

with col2:
    st.write("### 🤖 2. Get Prediction")
    st.write("The machine learning model will analyze your information.")

with col3:
    st.write("### 📊 3. View Result")
    st.write("Check your predicted placement result.")

st.markdown("---")

st.info("👉 Select **Prediction** from the sidebar to check your placement prediction.")
