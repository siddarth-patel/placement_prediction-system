

import streamlit as st
import pickle

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎯",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}

/* Main heading */
.hero-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.hero-subtitle {
    text-align: center;
    font-size: 17px;
    color: #6b7280;
    margin-bottom: 35px;
}

/* Input card */
.input-card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    margin-bottom: 25px;
}

/* Result card */
.result-card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    margin-top: 25px;
}

.result-title {
    font-size: 24px;
    font-weight: 600;
}

.result-status {
    font-size: 30px;
    font-weight: 700;
    margin-top: 10px;
}

.footer {
    text-align: center;
    color: #777;
    font-size: 13px;
    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# ---------- LOAD MODEL ----------
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)


# ---------- HEADER ----------
st.markdown(
    '<div class="hero-title">🎓 Placement Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Check your placement possibility using academic and skill-related information.'
    '</div>',
    unsafe_allow_html=True
)


# ---------- INPUT SECTION ----------
st.markdown('<div class="input-card">', unsafe_allow_html=True)

st.subheader("📝 Student Information")

col1, col2 = st.columns(2)

with col1:
    cgpa = st.slider(
        "CGPA",
        min_value=1.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )

    apt = st.slider(
        "Aptitude Score",
        min_value=1,
        max_value=100,
        value=60
    )

    cs = st.slider(
        "Communication Skills",
        min_value=1,
        max_value=100,
        value=50
    )

with col2:
    ins = st.selectbox(
        "Internship Experience",
        ["Yes", "No"]
    )

    project = st.number_input(
        "Number of Projects",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )

st.markdown("</div>", unsafe_allow_html=True)


# ---------- PREDICT BUTTON ----------
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    predict = st.button(
        "🎯 Predict Placement",
        type="primary",
        use_container_width=True
    )


# ---------- PREDICTION ----------
if predict:

    internship = 1 if ins == "Yes" else 0

    result = model.predict([
        [cgpa, apt, cs, internship, project]
    ])

    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="result-title">📊 Prediction Result</div>',
        unsafe_allow_html=True
    )

    if result[0] == 1:

        st.markdown(
            '<div class="result-status">🎉 Likely to be Placed</div>',
            unsafe_allow_html=True
        )

        st.success(
            "Based on the information provided, the model predicts "
            "that the student can be placed."
        )

    else:

        st.markdown(
            '<div class="result-status">⚠️ Placement Needs Improvement</div>',
            unsafe_allow_html=True
        )

        st.warning(
            "Based on the information provided, the model predicts "
            "that the student may not be placed."
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------- FOOTER ----------
st.markdown(
    '<div class="footer">'
    'Placement Prediction System • Machine Learning Based Prediction'
    '</div>',
    unsafe_allow_html=True
)
