
import streamlit as st

st.set_page_config(
    page_title="UniPlace | Placement Portal",
    page_icon="🎓",
    layout="wide"
)

# Professional styling
st.markdown("""
<style>
.stApp {
    background-color: #F5F7FB;
}

[data-testid="stHeader"] {
    background-color: #102447;
}

.hero {
    background: linear-gradient(120deg, #102447, #263F70);
    padding: 55px 40px;
    border-radius: 18px;
    color: white;
}

.hero h1 {
    color: white;
    font-size: 42px;
}

.hero p {
    color: #E4EAF5;
    font-size: 18px;
}

.stat-card {
    background: white;
    padding: 22px;
    border-radius: 14px;
    text-align: center;
    border: 1px solid #E1E7F0;
}

.stat-card h2 {
    color: #263F70;
    font-size: 32px;
}

.stat-card p {
    color: #64748B;
}

.section-title {
    color: #102447;
    font-size: 26px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h3 style="color:#102447;">
🎓 UniPlace
<span style="font-size:14px;color:#64748B;">
| AJEENKYA D Y PATIL UNIVERSITY
</span>
</h3>
""", unsafe_allow_html=True)

st.divider()

# Hero section
st.markdown("""
<div class="hero">
    <h1>Build Your Future With UniPlace</h1>
    <p>
    Discover career opportunities, connect with leading companies
    and take the next step in your professional journey.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Statistics
st.markdown(
    '<p class="section-title">Placement Overview</p>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

stats = [
    (c1, "500+", "Registered Students"),
    (c2, "35+", "Partner Companies"),
    (c3, "120+", "Job Opportunities"),
    (c4, "85%", "Demo Placement Rate")
]

for col, number, label in stats:
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <h2>{number}</h2>
            <p>{label}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.markdown(
    '<p class="section-title">Explore UniPlace</p>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 💼 Career Opportunities")
    st.write("Explore job openings and internship opportunities.")

with c2:
    st.markdown("### 👨‍🎓 Student Dashboard")
    st.write("Manage your profile and track your applications.")

with c3:
    st.markdown("### 📊 Placement Insights")
    st.write("View placement activities and career statistics.")

st.divider()

st.markdown("""
<div style="text-align:center;color:#64748B;padding:15px;">
    UniPlace | Connecting Students With Career Opportunities
</div>
""", unsafe_allow_html=True)
