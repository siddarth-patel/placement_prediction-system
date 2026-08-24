import streamlit as st
import json
import os
import hashlib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# =========================================================
# USER FILE
# =========================================================

USERS_FILE = "users.json"


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def load_users():

    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r") as file:
        return json.load(file)


def save_users(users):

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


# =========================================================
# LOGIN PAGE
# =========================================================

def login_page():

    st.markdown(
        """
        <style>

        .title {
            text-align: center;
            font-size: 42px;
            font-weight: 700;
            margin-top: 70px;
        }

        .subtitle {
            text-align: center;
            color: #777;
            font-size: 18px;
            margin-bottom: 35px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">🎓 Placement Prediction System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Login or create an account to continue</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        login_tab, signup_tab = st.tabs(
            ["🔐 Login", "📝 Sign Up"]
        )

        # =================================================
        # LOGIN
        # =================================================

        with login_tab:

            username = st.text_input(
                "👤 Username",
                placeholder="Enter your username",
                key="login_username"
            )

            password = st.text_input(
                "🔒 Password",
                type="password",
                placeholder="Enter your password",
                key="login_password"
            )

            if st.button(
                "Login",
                use_container_width=True
            ):

                users = load_users()

                if username not in users:

                    st.error("Username does not exist.")

                elif users[username]["password"] != hash_password(password):

                    st.error("Incorrect password.")

                else:

                    st.session_state.logged_in = True
                    st.session_state.username = username

                    st.success("Login successful!")

                    st.rerun()


        # =================================================
        # SIGN UP
        # =================================================

        with signup_tab:

            new_username = st.text_input(
                "👤 Create Username",
                placeholder="Choose a username",
                key="signup_username"
            )

            new_password = st.text_input(
                "🔒 Create Password",
                type="password",
                placeholder="Create a password",
                key="signup_password"
            )

            confirm_password = st.text_input(
                "🔒 Confirm Password",
                type="password",
                placeholder="Re-enter password",
                key="confirm_password"
            )

            if st.button(
                "Create Account",
                use_container_width=True
            ):

                if not new_username or not new_password:

                    st.error("Please fill all fields.")

                elif new_password != confirm_password:

                    st.error("Passwords do not match.")

                else:

                    users = load_users()

                    if new_username in users:

                        st.error("Username already exists.")

                    else:

                        users[new_username] = {
                            "password": hash_password(new_password)
                        }

                        save_users(users)

                        st.success(
                            "Account created successfully! "
                            "Now login using your credentials."
                        )


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    st.title("🏠 Welcome to Placement Prediction System")

    st.write(
        f"Hello, **{st.session_state.username}** 👋"
    )

    st.markdown("---")

    st.subheader("🎯 Predict Your Placement Chances")

    st.write(
        "Analyze your academic and skill profile "
        "to estimate your placement chances."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
            🔮 **Prediction**

            Predict your placement chances.
            """
        )

    with col2:

        st.success(
            """
            📜 **History**

            View your previous predictions.
            """
        )

    with col3:

        st.warning(
            """
            ℹ️ **About**

            Learn about the system.
            """
        )

    st.markdown("---")

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.rerun()


# =========================================================
# MAIN
# =========================================================

if not st.session_state.logged_in:

    login_page()

else:

    home_page()
