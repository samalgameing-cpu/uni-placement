
import streamlit as st
import sys
from pathlib import Path

# Import database.py from main project folder
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import database

database.create_table()

st.set_page_config(
    page_title="Student Registration | UniPlace",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
}
h1, h2 {
    color: #102b50;
}
div.stButton > button {
    background: #d62839;
    color: white;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Registration")
st.write("Create your UniPlace student account.")
st.divider()

with st.form("student_registration"):

    full_name = st.text_input("Full Name")

    email = st.text_input(
        "University Email ID",
        placeholder="abcd@semedun.in"
    )

    student_id = st.text_input(
        "Student ID",
        placeholder="2000-B-45982554C"
    )

    course = st.selectbox(
        "Course",
        ["Select Course", "BCA", "BBA", "B.Tech", "MBA", "MCA", "Other"]
    )

    semester = st.selectbox(
        "Semester",
        [
            "Select Semester",
            "Semester 1",
            "Semester 2",
            "Semester 3",
            "Semester 4",
            "Semester 5",
            "Semester 6",
            "Semester 7",
            "Semester 8"
        ]
    )

    phone = st.text_input(
        "Mobile Number",
        placeholder="Enter your mobile number"
    )

    password = st.text_input(
        "Create Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    submit = st.form_submit_button("Create Account")

    if submit:

        if not all([
            full_name, email, student_id,
            phone, password, confirm_password
        ]):
            st.error("Please fill in all fields.")

        elif course == "Select Course":
            st.error("Please select your course.")

        elif semester == "Select Semester":
            st.error("Please select your semester.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        elif len(phone) != 10 or not phone.isdigit():
            st.error("Enter a valid 10-digit mobile number.")

        else:
            success, message = database.register_student(
                full_name,
                email,
                student_id,
                course,
                semester,
                phone,
                password
            )

            if success:
                st.success(message)
                st.balloons()
            else:
                st.error(message)

st.divider()

st.caption("UniPlace | Ajeenkya D Y Patil University")
