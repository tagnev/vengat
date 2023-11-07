import streamlit as st

# Set page config
st.set_page_config(page_title="Vengateswaran Arunachalam's Resume", layout="wide")

# Custom styles for the resume
st.markdown("""
<style>
body {
    font-family: 'Helvetica', sans-serif;
}
h1, h2, h3, h4, h5, h6, .sidebar-header {
    font-family: 'Helvetica';
    font-weight: 700;
    letter-spacing: 0.1em;
}
div.block-container {
    padding-top: 2rem;
}
.section-header {
    background-color: #0e1117;
    color: #ffffff;
    padding: 1em 2em;
    border-radius: 0.5em;
    margin-bottom: 1em;
}
.contact-form {
    background-color: #fafafa;
    padding: 2em;
    border-radius: 0.5em;
    margin-top: 1em;
}
.contact-form input, .contact-form textarea {
    margin-bottom: 1em;
}
</style>
""", unsafe_allow_html=True)

# Main title with image
col1, col2 = st.columns([1, 4])
with col1:
    st.image('https://media.licdn.com/dms/image/D5603AQGzch8kk3Cs1A/profile-displayphoto-shrink_200_200/0/1696458140217?e=1704931200&v=beta&t=IC1H7RGnR3fJFLhMeWRZq95-_VWJH7yh2HxGGUNh0dg', width=120)
with col2:
    st.title('Vengateswaran Arunachalam')
    st.write('Santa Clara, CA 95051  |  tagnev.vengat@gmail.com')
st.markdown('---')

# Sidebar with contact info
st.sidebar.header('Contact Information')
st.sidebar.write("""
Santa Clara, CA 95051  
[tagnev.vengat@gmail.com](mailto:tagnev.vengat@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/vengateswaran-arunachalam/)  
[GitHub](https://github.com/tagnev)  
[Medium](https://medium.com/@tagnev.vengat)
""")
st.sidebar.markdown('---')

# Contact form in the main page
st.markdown('<p class="section-header">Contact Me</p>', unsafe_allow_html=True)
with st.form(key='contact_form'):
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')
    submit_button = st.form_submit_button('Send')

    if submit_button:
        # Process the form data (e.g., send an email)
        st.write('Thank you for your message!')

# Professional Summary
st.subheader('Professional Summary')
st.write("""
Accomplished Full Stack Data Engineer & Data Architect with 14+ years of expertise in BI solutions. 
Proficient in Spark, Hadoop, Python, ReactJS, and the complete SDLC. Solid experience in cloud services 
with AWS & GCP, database solutions both in the cloud and on-premise, and mastery of BI tools including 
Tableau and MicroStrategy. Demonstrable skills in customer-focused open-source projects, content creation, 
and community engagement. Excel at advanced database solutions, ETL processes, and enhancing data 
infrastructure. Well-versed in partnering with diverse teams to foster data-driven strategies.
""")

# Skills
st.subheader('Skills')
st.write("""
- Docker, DBT, Kubernetes, Git
- AWS & GCP architecture
- Python (Django, Flask, FastAPI)
- Shell scripting
- MySQL/Relational DB, Snowflake, Postgresql
- Hadoop, Tableau, MicroStrategy, Looker
- Cassandra, NoSQL, Pyspark, Airflow, Streamlit, openAI, Incorta
""")

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
