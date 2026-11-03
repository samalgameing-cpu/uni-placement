
import streamlit as st

st.set_page_config(
    page_title="UniPlace | ADYPU",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #ffffff;
    color: #252033;
}

[data-testid="stHeader"] {
    background: white;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1rem;
    max-width: 1400px;
}

.brand {
    color: #a50021;
    font-size: 25px;
    font-weight: 800;
    line-height: 1.2;
}

.brand small {
    color: #444;
    font-size: 11px;
    letter-spacing: 2px;
}

.hero {
    background: linear-gradient(110deg, #97001e, #c9002b);
    border-radius: 14px;
    padding: 55px 35px;
    color: white;
    min-height: 300px;
}

.hero h1 {
    color: white;
    font-size: 43px;
    line-height: 1.15;
}

.hero p {
    color: #fff0f2;
    font-size: 17px;
}

.hero-button {
    display: inline-block;
    background: white;
    color: #a50021 !important;
    padding: 12px 22px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
}

.section-title {
    color: #8f001e;
    font-size: 27px;
    font-weight: 750;
}

.stat-card {
    background: #fff7f8;
    border: 1px solid #f1d9df;
    border-radius: 12px;
    padding: 20px 8px;
    text-align: center;
}

.stat-number {
    color: #a50021;
    font-size: 30px;
    font-weight: bold;
}

.stat-label {
    color: #4b4550;
    font-size: 14px;
}

.feature-card {
    background: #fffafa;
    border: 1px solid #f0dce1;
    border-radius: 13px;
    padding: 22px;
    min-height: 150px;
}

.feature-card h3 {
    color: #97001e;
}

.recruiter {
    background: white;
    border: 1px solid #eadde0;
    border-radius: 10px;
    padding: 16px 8px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #333;
}

.footer {
    background: #90001d;
    color: white;
    text-align: center;
    padding: 22px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# UNIVERSITY HEADER
left, right = st.columns([1.5, 2])

with left:
    st.markdown("""
    <div class="brand">
        🎓 AJEENKYA<br>
        D Y PATIL UNIVERSITY
        <small><br>THE INNOVATION UNIVERSITY</small>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <h3 style="color:#a50021; text-align:right;
    padding-top:15px;">
    PLACEMENT PORTAL
    </h3>
    """, unsafe_allow_html=True)

st.divider()

# NAVIGATION
n1, n2, n3, n4, n5, n6 = st.columns(6)

with n1:
    st.button("🏠 Home", use_container_width=True)

with n2:
    st.button("💼 Jobs", use_container_width=True)

with n3:
    st.button("🏢 Companies", use_container_width=True)

with n4:
    st.button("ℹ️ About Us", use_container_width=True)

with n5:
    st.button("✉️ Contact", use_container_width=True)

with n6:
    st.button("🔐 Student Login", use_container_width=True)

st.write("")

# HERO SECTION
hero_left, hero_right = st.columns([1.15, 1])

with hero_left:
    st.markdown("""
    <div class="hero">
        <h1>Building Careers,<br>Shaping Futures</h1>
        <p>Your Placement Journey Begins Here at
        <b>Ajeenkya D Y Patil University</b></p>
        <a class="hero-button" href="#opportunities">
        Explore Opportunities →</a>
    </div>
    """, unsafe_allow_html=True)

with hero_right:
    st.image(
        "https://images.unsplash.com/photo-1523050854058-8df90110c9f1",
        use_container_width=True
    )

st.write("")

# PLACEMENT STATISTICS
st.markdown(
    '<p class="section-title">Placement Overview</p>',
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)

stats = [
    (s1, "500+", "Students Placed"),
    (s2, "350+", "Recruiting Companies"),
    (s3, "1200+", "Job Opportunities"),
    (s4, "95%", "Placement Success")
]

for col, number, label in stats:
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{number}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# TOP RECRUITERS
st.markdown(
    '<p class="section-title">Our Top Recruiters</p>',
    unsafe_allow_html=True
)

recruiters = st.columns(7)

companies = [
    "TCS", "Infosys", "Accenture", "Wipro",
    "Deloitte", "Capgemini", "Amazon"
]

for col, company in zip(recruiters, companies):
    with col:
        st.markdown(
            f'<div class="recruiter">{company}</div>',
            unsafe_allow_html=True
        )

st.write("")

# FEATURES AND ABOUT SECTION
st.markdown(
    '<p class="section-title">Explore UniPlace</p>',
    unsafe_allow_html=True
)

f1, f2, f3 = st.columns(3)

features = [
    (f1, "💼 Career Opportunities",
     "Explore job and internship opportunities."),
    (f2, "📈 Skill Development",
     "Improve your skills with industry-ready training."),
    (f3, "🤝 Industry Connect",
     "Build connections with leading recruiters.")
]

for col, title, description in features:
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")

about_left, about_right = st.columns([1.3, 1])

with about_left:
    st.markdown(
        '<p class="section-title">About Placements</p>',
        unsafe_allow_html=True
    )
    st.write("""
    At UniPlace, we aim to connect students with
    career opportunities and industry professionals.

    Our placement portal helps students explore jobs,
    prepare for interviews and manage applications
    throughout their career journey.
    """)

with about_right:
    st.image(
        "https://images.unsplash.com/photo-1523580494863-6f3031224c94",
        use_container_width=True
    )

st.write("")

# FOOTER
st.markdown("""
<div class="footer">
    <h3>🎓 UniPlace</h3>
    Connecting Students With Career Opportunities
    <br><br>
    © 2026 UniPlace | Placement Portal
</div>
""", unsafe_allow_html=True)
