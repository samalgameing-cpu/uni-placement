
import streamlit as st
from pathlib import Path

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="UniPlace | ADYPU Placement Portal",
    page_icon="🎓",
    layout="wide"
)

# ---------------- COLORS & CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: #f7f9fc;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.brand {
    color: #102b50;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -1px;
}

.brand span {
    color: #d62839;
}

.university {
    color: #52647b;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1.2px;
}

.topline {
    background: #102b50;
    color: white;
    padding: 9px 20px;
    border-radius: 5px;
    text-align: center;
    font-size: 12px;
}

.hero {
    background: linear-gradient(90deg, rgba(8,31,59,.94), rgba(8,31,59,.45)),
    url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600');
    background-size: cover;
    background-position: center;
    padding: 75px 55px;
    border-radius: 12px;
    color: white;
    margin-top: 20px;
    min-height: 350px;
}

.hero h1 {
    font-size: 43px;
    line-height: 1.25;
    font-weight: 800;
    color: white;
}

.hero p {
    font-size: 16px;
    color: #edf3fa;
    max-width: 600px;
}

.section-title {
    color: #102b50;
    font-size: 27px;
    font-weight: 800;
    margin-top: 35px;
}

.section-sub {
    color: #68778a;
    font-size: 14px;
}

.stat-card {
    background: white;
    padding: 22px 12px;
    border-radius: 10px;
    text-align: center;
    border-bottom: 4px solid #d62839;
    box-shadow: 0 3px 15px rgba(0,0,0,.05);
}

.stat-number {
    color: #102b50;
    font-size: 30px;
    font-weight: 800;
}

.stat-label {
    color: #68778a;
    font-size: 12px;
}

.feature-card {
    background: white;
    padding: 24px;
    border-radius: 10px;
    min-height: 175px;
    border: 1px solid #e7ebf1;
    box-shadow: 0 3px 12px rgba(0,0,0,.04);
}

.feature-card h3 {
    color: #102b50;
    font-size: 18px;
}

.feature-card p {
    color: #68778a;
    font-size: 13px;
}

.company {
    background: white;
    border: 1px solid #e7ebf1;
    padding: 20px 8px;
    border-radius: 8px;
    text-align: center;
    color: #102b50;
    font-size: 15px;
    font-weight: 800;
}

.about-box {
    background: #102b50;
    color: white;
    padding: 30px;
    border-radius: 12px;
}

.about-box h2 {
    color: white;
}

.about-box p {
    color: #e0e8f2;
    font-size: 14px;
}

.footer {
    background: #0b203b;
    color: white;
    padding: 30px;
    border-radius: 10px;
    margin-top: 40px;
    text-align: center;
}

.footer p {
    color: #c5d0df;
    font-size: 12px;
}

div.stButton > button {
    background: #d62839;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 22px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #a91d2c;
    color: white;
    border: none;
}

[data-testid="stRadio"] > div {
    gap: 12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
logo_path = Path("assets/adypu_logo.png")

left, middle, right = st.columns([1, 3, 2])

with left:
    if logo_path.exists():
        st.image(str(logo_path), width=85)
    else:
        st.markdown("## ADYPU")

with middle:
    st.markdown("""
    <div class="brand">Uni<span>Place</span></div>
    <div class="university">PLACEMENT & CAREER PORTAL</div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div style="text-align:right;color:#102b50;font-size:12px;
    font-weight:600;padding-top:15px;">
    AJEENKYA D Y PATIL UNIVERSITY<br>
    <span style="color:#d62839;">THE INNOVATION UNIVERSITY</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- NAVIGATION ----------------
selected = st.radio(
    "Navigation",
    ["Home", "Jobs", "Companies", "About Us", "Contact", "Student Login"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("""
<div class="topline">
    Welcome to UniPlace — Connecting Talent with Opportunity
</div>
""", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------
if selected == "Home":

    st.markdown("""
    <div class="hero">
        <h1>BUILD YOUR FUTURE.<br>
        FIND YOUR OPPORTUNITY.</h1>
        <p>
        Explore career opportunities, connect with leading employers
        and take the next step towards your professional journey.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="section-title">Placement Highlights</div>
    <div class="section-sub">ADYPU Placement Excellence 2025 — figures published on the university website.</div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    stats = [
        ("1100+", "Total Job Offers"),
        ("500+", "Internships"),
        ("55 LPA", "Highest Package"),
        ("13–14 LPA", "Average Package of Top Offers")
    ]

    for col, (number, label) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">Our Recruiter Network</div>
    <div class="section-sub">
    Organisations listed on ADYPU's official placements page.
    </div>
    """, unsafe_allow_html=True)

    companies = [
        "Tech Mahindra", "Deloitte", "HSBC", "Tata Technologies",
        "Cohesity", "Entrata", "TVS Lucas", "Syneos Health"
    ]

    cols = st.columns(4)
    for i, company in enumerate(companies):
        with cols[i % 4]:
            st.markdown(
                f'<div class="company">{company}</div>',
                unsafe_allow_html=True
            )
            st.write("")

    st.markdown("""
    <div class="section-title">Explore UniPlace</div>
    <div class="section-sub">
    Everything you need to prepare for your career journey.
    </div>
    """, unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)

    features = [
        ("💼", "Career Opportunities",
         "Discover job openings, internships and career opportunities."),
        ("🎯", "Skill Development",
         "Prepare for interviews and improve your professional skills."),
        ("🤝", "Industry Connect",
         "Explore organisations and connect with the world of work.")
    ]

    for col, (emoji, heading, description) in zip([f1, f2, f3], features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div style="font-size:32px">{emoji}</div>
                <h3>{heading}</h3>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div class="about-box">
        <h2>About Placements at ADYPU</h2>
        <p>
        The Student Progression & Corporate Relations Office supports
        students through career guidance, industry interaction,
        employability training and placement opportunities.
        </p>
        <p>
        UniPlace brings career-related information together in one
        convenient portal.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        <h2>UniPlace</h2>
        <p>Ajeenkya D Y Patil University | Pune, Maharashtra</p>
        <p>Placement & Career Portal</p>
        <p>© 2026 UniPlace. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- JOBS PAGE ----------------
elif selected == "Jobs":
    st.title("Career Opportunities")
    st.write("Explore job and internship opportunities.")
    st.info("Job listings will be added in the next development step.")

# ---------------- COMPANIES PAGE ----------------
elif selected == "Companies":
    st.title("Recruiter Network")
    st.write("Explore organisations featured on the university placement page.")
    for company in companies:
        st.write("•", company)

# ---------------- ABOUT PAGE ----------------
elif selected == "About Us":
    st.title("About UniPlace")
    st.write("""
    UniPlace is a placement and career portal concept for bringing
    students and career opportunities together.

    It is designed around the placement journey, career preparation
    and industry connections at ADYPU.
    """)
    st.markdown("[Visit ADYPU Official Website](https://adypu.edu.in/)")

# ---------------- CONTACT PAGE ----------------
elif selected == "Contact":
    st.title("Contact Us")
    st.write("Ajeenkya D Y Patil University")
    st.write("D Y Patil Knowledge City, Charholi Bk., Pune – 411081")
    st.markdown("[University Website](https://adypu.edu.in/)")

# ---------------- STUDENT LOGIN PAGE ----------------
elif selected == "Student Login":
    st.title("Student Login")
    st.write("Access your placement portal.")

    email = st.text_input("Student Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.warning("Student authentication will be connected in the next step.")

