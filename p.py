import streamlit as st
import json
import os
import hashlib


USERS_FILE = "users.json"


# ---------------- PASSWORD HASH ----------------

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ---------------- LOAD USERS ----------------

def load_users():

    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r") as file:
        return json.load(file)


# ---------------- SAVE USERS ----------------

def save_users(users):

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


# ---------------- SIGN UP ----------------

def signup():

    st.subheader("Create Account")

    username = st.text_input(
        "👤 Username",
        key="signup_username"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        key="signup_password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password",
        key="confirm_password"
    )

    if st.button(
        "Create Account",
        use_container_width=True
    ):

        if not username or not password:

            st.error("Please fill all fields.")
            return

        if password != confirm_password:

            st.error("Passwords do not match.")
            return

        users = load_users()

        if username in users:

            st.error("Username already exists.")
            return

        users[username] = {
            "password": hash_password(password)
        }

        save_users(users)

        st.success("Account created successfully!")
        st.info("Now you can login.")


# ---------------- LOGIN ----------------

def login():

    st.subheader("Welcome Back 👋")

    username = st.text_input(
        "👤 Username",
        key="login_username"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        key="login_password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        users = load_users()

        if username not in users:

            st.error("Username does not exist.")
            return

        hashed_password = hash_password(password)

        if users[username]["password"] == hashed_password:

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login successful!")

            st.rerun()

        else:

            st.error("Incorrect password.")


# ---------------- AUTH PAGE ----------------

def auth_page():

    st.markdown(
        "<h1 style='text-align:center;'>🎓 Placement Prediction System</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:gray;'>"
        "Your journey towards placement starts here"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")

    login_tab, signup_tab = st.tabs(
        ["🔐 Login", "📝 Sign Up"]
    )

    with login_tab:

        login()

    with signup_tab:

        signup()
