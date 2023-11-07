import streamlit as st

# Set page config
st.set_page_config(page_title="Vengateswaran Arunachalam's Resume", layout="wide")

# Custom styles
st.markdown("""
<style>
body {
    font-family: 'Helvetica', sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

h1, h2, h3, h4, h5, h6, .sidebar-header, .section-header, .contact-header {
    font-family: 'Helvetica';
    font-weight: 700;
    letter-spacing: 0.1em;
    color: #0e1117;
}

.section-header {
    font-size: 26px;
    background-color: #ff4b4b;
    color: white;
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 25px;
    text-align: center;
}

.detail-text {
    padding: 0.25rem 1rem;
    margin: 0.25rem 0;
    border-left: 5px solid #ff4b4b;
    background-color: #f2f2f2;
    border-radius: 5px;
}

.sidebar .sidebar-content {
    background-color: #f0f8ff;
    padding: 2rem;
    border-radius: 10px;
}

.contact-form {
    background-color: #f0f8ff;
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 25px;
}

.contact-form input, .contact-form textarea {
    margin-bottom: 1rem;
}

.icon {
    font-size: 1.5rem;
    margin-right: 5px;
    color: #ff4b4b;
}
</style>
""", unsafe_allow_html=True)

# Load FontAwesome for icons
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-1PCqXZRn1zEe5m+gkxvf8VN4Q2xvgzw0KfXZ0Uf3lCzXCFvVXqrrUizwQfJjyApt8B/5lTh5QBE6P6VnqQZNug==" crossorigin="anonymous" />
""", unsafe_allow_html=True)

# Main title with image
col1, col2 = st.columns([1, 4])
with col1:
    st.image('https://media.licdn.com/dms/image/D5603AQGzch8kk3Cs1A/profile-displayphoto-shrink_200_200/0/1696458140217?e=1704931200&v=beta&t=IC1H7RGnR3fJFLhMeWRZq95-_VWJH7yh2HxGGUNh0dg', width=120)
with col2:
    st.title('Vengateswaran Arunachalam')
    st.write('Santa Clara, CA 95051  |  tagnev.vengat@gmail.com')

# Contact Information
st.sidebar.markdown('<p class="contact-header"><i class="fas fa-envelope icon"></i>Contact Information</p>', unsafe_allow_html=True)
st.sidebar.markdown("""
Santa Clara, CA 95051  
[tagnev.vengat@gmail.com](mailto:tagnev.vengat@gmail.com)  
[<i class="fab fa-linkedin icon"></i>LinkedIn](https://www.linkedin.com/in/vengateswaran-arunachalam/)  
[<i class="fab fa-github icon"></i>GitHub](https://github.com/tagnev)  
[<i class="fab fa-medium icon"></i>Medium](https://medium.com/@tagnev.vengat)
""", unsafe_allow_html=True)

# Professional Summary
st.markdown('<p class="section-header"><i class="fas fa-user-tie icon"></i>Professional Summary</p>', unsafe_allow_html=True)
st.markdown("""
<p class="detail-text">Accomplished Full Stack Data Engineer & Data Architect with 14+ years of expertise in BI solutions. 
Proficient in Spark, Hadoop, Python, ReactJS, and the complete SDLC. Solid experience in cloud services 
with AWS & GCP, database solutions both in the cloud and on-premise, and mastery of BI tools including 
Tableau and MicroStrategy. Demonstrable skills in customer-focused open-source projects, content creation, 
and community engagement. Excel at advanced database solutions, ETL processes, and enhancing data 
infrastructure. Well-versed in partnering with diverse teams to foster data-driven strategies.</p>
""", unsafe_allow_html=True)

# Skills
st.markdown('<p class="section-header"><i class="fas fa-lightbulb icon"></i>Skills</p>', unsafe_allow_html=True)
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
st.subheader('Work History')

st.markdown('**Data Architect/Senior Data Engineer**')
st.write('Keysight Technologies – Santa Clara, CA (10/2021 - Current)')
st.markdown("""
- Managed the data migration process during a merger, which included transitioning data from legacy 
systems of both companies into a single data warehouse.
- Developed and executed migration scripts and ETL processes to ensure data integrity and consistency.
- Collaborated with business stakeholders to prioritize data migration efforts, identifying critical data 
elements and dependencies.
- Orchestrated the decommissioning of legacy systems post-migration, reducing operational costs and 
streamlining data management.
""")

st.markdown('**Full Stack Data Engineer/Startup Founder**')
st.write('Teckiy – Santa Clara, CA (01/2020 - 12/2022)')
st.markdown("""
- Collaborated with a cross-functional team to design, develop, and deploy a comprehensive end-to-end 
data product leveraging Django as the backend framework and Google Cloud Platform (GCP) for cloud 
infrastructure.
- Designed and implemented a robust data pipeline on GCP, incorporating services like Google Cloud 
Storage, BigQuery, and Cloud Dataflow for data ingestion, storage, transformation, and analysis.
""")

st.markdown('**Data Engineer Lead**')
st.write('Keysight Technologies – Santa Clara, CA (04/2018 - 10/2021)')
st.markdown("""
- Designed and implemented a data lake architecture on AWS S3, providing a scalable and cost-effective 
solution for storing and processing massive volumes of structured and unstructured data.
- Optimized data ingestion pipelines using AWS Glue to automate data cataloging, ETL, and 
transformation processes, resulting in a 30% reduction in data processing time.
""")

st.markdown('**Senior BI Developer**')
st.write('Cognizant (Client: Keysight Technologies) – Santa Clara, CA (06/2014 - 04/2018)')
st.markdown("""
- Involved in Data Warehousing and worked extensively on RDBMS (Oracle, MS SQL) and ETL tools such 
as Informatica, Shell Scripting, and Python.
- Facilitated knowledge transfer sessions for new resources.
""")

# Education
st.subheader('Education')
st.write('Bachelor of Science: Information Technology, 05/2009')
st.write('Mount Zion College of Engineering & Technology - Tamilnadu, India')
st.write('Aggregate: 80%')

# Open Source Projects
st.subheader('Open Source Projects')
st.write('[Teckiy, Developer support platform](https://www.teckiy.com)')
st.write("[HelpU, India's first customer experience sharing portal](https://www.helpu.in)")

# Run this with `streamlit run resume_app.py` in your command line
