import streamlit as st

# Title of the Resume
st.title('Vengateswaran Arunachalam')

# Contact Information
st.sidebar.header('Contact Information')
st.sidebar.image('https://media.licdn.com/dms/image/D5603AQGzch8kk3Cs1A/profile-displayphoto-shrink_200_200/0/1696458140217?e=1704931200&v=beta&t=IC1H7RGnR3fJFLhMeWRZq95-_VWJH7yh2HxGGUNh0dg', width=150)  
st.sidebar.write("""
Santa Clara, CA 95051  
tagnev.vengat@gmail.com  
""")
st.sidebar.write('[LinkedIn Profile](https://www.linkedin.com/in/vengateswaran-arunachalam/)')
st.sidebar.write('[GitHub](https://github.com/tagnev)')
st.sidebar.write('[Medium](https://medium.com/@tagnev.vengat)')

# Professional Summary
st.header('Professional Summary')
st.write("""
Accomplished Full Stack Data Engineer & Data Architect with 14+ years of expertise in BI solutions. Proficient in Spark, Hadoop, Python, ReactJS, and the complete SDLC. Solid experience in cloud services with AWS & GCP, database solutions both in the cloud and on-premise, and mastery of BI tools including Tableau and MicroStrategy. Demonstrable skills in customer-focused open-source projects, content creation, and community engagement. Excel at advanced database solutions, ETL processes, and enhancing data infrastructure. Well-versed in partnering with diverse teams to foster data-driven strategies.
""")

# Skills
st.header('Skills')
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
st.header('Work History')

st.subheader('Data Architect/Senior Data Engineer')
st.write('10/2021 - Current, Keysight Technologies – Santa Clara, CA')
st.write('''
- Managed data migration and system decommissioning during a merger.
- Architected serverless data pipelines on AWS.
- Designed real-time stream processing with Apache Kafka and Spark.
''')

st.subheader('Full Stack Data Engineer/Startup Founder')
st.write('01/2020 - 12/2022, Teckiy – Santa Clara, CA')
st.write('''
- Designed and developed end-to-end data product on GCP.
- Implemented data security and access control within Django application.
- Managed cloud infrastructure and optimized resource usage.
''')

st.subheader('Data Engineer Lead')
st.write('04/2018 - 10/2021, Keysight Technologies – Santa Clara, CA')
st.write('''
- Designed data lake architecture on AWS S3.
- Led multi-source data integration and consolidation.
''')

st.subheader('Senior BI Developer')
st.write('06/2014 - 04/2018, Cognizant (Client: Keysight Technologies) – Santa Clara, CA')
st.write('''
- Data Warehousing with RDBMS (Oracle, MS SQL) and ETL tools.
- Managed data projects and facilitated knowledge transfer.
''')

# Education
st.header('Education')
st.write('Bachelor of Science: Information Technology, 05/2009')
st.write('Mount Zion College of Engineering & Technology - Tamilnadu, India')
st.write('Aggregate: 80%')

# Open Source Projects
st.header('Open Source Projects')
st.write('[Teckiy, Developer support platform](https://www.teckiy.com)')
st.write('[HelpU, India\'s first customer experience sharing portal](https://www.helpu.in)')

# Run this with `streamlit run resume_app.py` in your command line
