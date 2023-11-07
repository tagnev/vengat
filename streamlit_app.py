import streamlit as st

# Configuring the page
st.set_page_config(page_title="Vengateswaran Arunachalam's Resume", page_icon=":briefcase:", layout="wide")

# Defining custom styles for the resume
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Assuming you have a styles.css file in the same directory with your desired CSS
# local_css("styles.css")

# Using raw HTML for custom styling, if you don't have a styles.css file
st.markdown("""
<style>
body {
    font-family: 'Helvetica', sans-serif;
}
.header {
    font-weight: bold;
    font-size: 36px;
    line-height: 1.6;
}
.subheader {
    font-weight: 500;
    font-size: 24px;
    line-height: 1.4;
}
.section {
    margin-bottom: 20px;
}
.detail-text {
    font-size: 16px;
    line-height: 1.6;
}
.sidebar-text {
    font-size: 14px;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

# Resume Header
st.image('https://media.licdn.com/dms/image/D5603AQGzch8kk3Cs1A/profile-displayphoto-shrink_200_200/0/1696458140217?e=1704931200&v=beta&t=IC1H7RGnR3fJFLhMeWRZq95-_VWJH7yh2HxGGUNh0dg', width=150)
st.markdown('<p class="header">Vengateswaran Arunachalam</p>', unsafe_allow_html=True)

# Contact Information in Sidebar
st.sidebar.markdown('<p class="sidebar-text">Santa Clara, CA 95051<br>(408)784-9915<br>tagnev.vengat@gmail.com</p>', unsafe_allow_html=True)
st.sidebar.markdown('[LinkedIn Profile](https://www.linkedin.com/in/vengateswaran-arunachalam/)', unsafe_allow_html=True)
st.sidebar.markdown('[GitHub](https://github.com/tagnev)', unsafe_allow_html=True)
st.sidebar.markdown('[Medium](https://medium.com/@tagnev.vengat)', unsafe_allow_html=True)

# Professional Summary
st.markdown('<p class="subheader">Professional Summary</p>', unsafe_allow_html=True)
st.markdown("""
<p class="detail-text">Accomplished Full Stack Data Engineer & Data Architect with 14+ years of expertise in BI solutions. Proficient in Spark, Hadoop, Python, ReactJS, and the complete SDLC. Solid experience in cloud services with AWS & GCP, database solutions both in the cloud and on-premise, and mastery of BI tools including Tableau and MicroStrategy. Demonstrable skills in customer-focused open-source projects, content creation, and community engagement. Excel at advanced database solutions, ETL processes, and enhancing data infrastructure. Well-versed in partnering with diverse teams to foster data-driven strategies.</p>
""", unsafe_allow_html=True)

# Skills
st.markdown('<p class="subheader">Skills</p>', unsafe_allow_html=True)
st.markdown("""
<p class="detail-text">
- Docker, DBT, Kubernetes, Git<br>
- AWS & GCP architecture<br>
- Python (Django, Flask, FastAPI)<br>
- Shell scripting<br>
- MySQL/Relational DB, Snowflake, Postgresql<br>
- Hadoop, Tableau, MicroStrategy, Looker<br>
- Cassandra, NoSQL, Pyspark, Airflow, Streamlit, openAI, Incorta
</p>
""", unsafe_allow_html=True)

# Work History
st.markdown('<p class="subheader">Work History</p>', unsafe_allow_html=True)
# ... include your work history here, using detail-text class for paragraphs ...

# Education
st.markdown('<p class="subheader">Education</p>', unsafe_allow_html=True)
# ... include your education here ...

# Open Source Projects
st.markdown('<p class="subheader">Open Source Projects</p>', unsafe_allow_html=True)
# ... include your projects here ...

# You can continue adding more sections using the same pattern.

# Run this with `streamlit run styled_resume_app.py` in your command line
