import streamlit as st

st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="🎓",
    layout="wide"
)

# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# ---------------- LOGIN PAGE ----------------

def login_page():

    st.markdown("""
        <style>
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            margin-top: 80px;
        }

        .subtitle {
            text-align: center;
            color: #777;
            font-size: 18px;
            margin-bottom: 35px;
        }

        .login-box {
            padding: 25px;
            border-radius: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="main-title">🎓 Placement Prediction System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Login to continue</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown('<div class="login-box">', unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password"
        )

        login = st.button(
            "Login",
            use_container_width=True
        )

        if login:

            # Temporary login
            if username == "admin" and password == "1234":

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Login successful!")
                st.rerun()

            else:
                st.error("Invalid username or password")

        st.markdown(
            """
            <p style="text-align:center; color:gray;">
            Demo: admin / 1234
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)


# ---------------- HOME PAGE ----------------

def home_page():

    st.title("🏠 Welcome to Placement Prediction System")

    st.write(
        f"Hello, **{st.session_state.username}** 👋"
    )

    st.markdown("---")

    st.subheader("🎯 Predict Your Placement Chances")

    st.write(
        "Use our placement prediction system to analyze "
        "your profile and estimate your placement chances."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🔮 **Prediction**\n\nPredict your placement chances.")

    with col2:
        st.success("📜 **History**\n\nView your previous predictions.")

    with col3:
        st.warning("ℹ️ **About**\n\nLearn about the system.")

    st.markdown("---")

    if st.button("Logout", type="secondary"):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.rerun()


# ---------------- MAIN ----------------

if not st.session_state.logged_in:

    login_page()

else:

    home_page()
