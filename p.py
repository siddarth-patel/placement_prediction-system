import streamlit as st

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Placement Prediction System")

st.write(
    "Welcome to the Placement Prediction System. "
    "This application will help students check their placement prediction "
    "based on academic and skill-related information."
)

st.subheader("What can you do?")

st.write("🎯 Predict your placement")
st.write("📊 View your prediction results")
st.write("👤 Manage your profile")

st.info("Use the sidebar to navigate through the application.")
