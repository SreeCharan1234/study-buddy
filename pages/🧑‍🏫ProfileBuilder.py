import streamlit as st
import pandas as pd
import re
from datetime import date
import PIL.Image
from PIL import Image
from bs4 import BeautifulSoup
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pathlib import Path
from streamlit_ace import st_ace
from streamlit_option_menu import option_menu
import datetime
import os
import base64
import streamlit_shadcn_ui as ui
import textwrap
import google.generativeai as genai
from IPython.display import display,Markdown
from streamlit_lottie import st_lottie
import requests 
from local_components import card_container
import sys
import io
import speech_recognition as sr
import pdf2image
import plotly.graph_objects as go
import plotly.express as px
global s
k=0
api_key="AIzaSyCoc7UW6p0Xj7At538R3oMYkfxG7bSLuaU"
os.getenv("AIzaSyCoc7UW6p0Xj7At538R3oMYkfxG7bSLuaU")
genai.configure(api_key="AIzaSyBIBVb-0Z0QwaucMGOGy8-j_RM22X-4-lE")
t=[ "Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "Swift", "Kotlin", 
    "C#", "Go", "R", "TypeScript", "Scala", "Perl", "Objective-C", "Dart", 
    "Rust", "Haskell", "MATLAB", "SQL", "HTML/CSS", "React", "Angular", "Vue.js", 
    "Node.js", "Django", "Flask", "Spring", "ASP.NET", "Ruby on Rails"]
st.set_page_config(page_title="Resume", page_icon='chart_with_upwards_trend', layout="wide", initial_sidebar_state="auto", menu_items=None)
EXAMPLE_NO = 1
recognizer = sr.Recognizer()
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


        # --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | K Sree Charan"
PAGE_ICON = ":wave:"
NAME = "K Sree Charan"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "Sreecharan9484@gmail.com"
SOCIAL_MEDIA = {
     "YouTube": "https://www.youtube.com/channel/UCPxjJHozO16AfjRV6_bGxew",
     "LinkedIn": "https://www.linkedin.com/in/sree9484/",
     "GitHub": "https://github.com/SreeCharan1234",
     "Twitter": "https://twitter.com",
    }
PROJECTS = {
     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

with open(css_file) as f:
            st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
def get_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    query = """
    query getLeetCodeData($username: String!) {
      userProfile: matchedUser(username: $username) {
        username
        profile {
          userAvatar
          reputation
          ranking
        }
        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
          totalSubmissionNum {
            difficulty
            count
          }
        }
      }
      userContestRanking(username: $username) {
        attendedContestsCount
        rating
        globalRanking
        totalParticipants
        topPercentage
      }
      recentSubmissionList(username: $username) {
        title
        statusDisplay
        lang
      }
    }
    """
    variables = {
        "username": username
    }
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()

    if 'errors' in data:
        print("Error:", data['errors'])
        return None

    return data['data']
def get_gemini_response1(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text
def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json() 
def recognize_speech_from_microphone():
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
def pseudo_bold(text):
    bold_text = ''.join(chr(0x1D5D4 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else
                        chr(0x1D5EE + ord(c) - ord('a')) if 'a' <= c <= 'z' else c
                        for c in text)
    return bold_text
def streamlit_menu(example=1):
    if example == 1:
        with st.sidebar:
            selected = option_menu(
                menu_title="Profile - Builder ",  # required
                options=["Dashboard","Resume Builder", "ATS Detector", "LinkedIn Profile","Mail/Cover Letter"],  # required
                icons=["bi bi-person-lines-fill","bi bi-file-person", "bi bi-binoculars-fill", "bi bi-linkedin","bi bi-envelope-at"],  # optional
                menu_icon="cast",  # optional
                default_index=0,
            )
        return selected
    if example == 2:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Road Map", "Resume Builder", "Ai bot","ATS-DECTOR"],  # required
                icons=["geo-alt-fill", "file-person-fill", "robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,
            )
        return selected
    if example == 3:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Road Map", "Resume Builder", "Ai bot","ATS-DECTOR"],  # required
                icons=["geo-alt-fill", "file-person-fill", "robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,                
                # optional
            )
        return selected
    if example == 4:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Road Map", "Resume Builder", "Ai bot","ATS-DECTOR"],  # required
                icons=["geo-alt-fill", "file-person-fill", "robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,                
                # optional
            )
        return selected
def create_rating_dropdown(label):
    return st.selectbox(label, ['1', '2', '3', '4', '5'], index=2)
selected = streamlit_menu(example=EXAMPLE_NO)
if 'questions' not in st.session_state:
    st.session_state.questions = []
if selected == "Dashboard":
    link="https://lottie.host/02515adf-e5f1-41c8-ab4f-8d07af1dcfb8/30KYw8Ui2q.json"
    l=load_lottieurl(link)
    col1, col2 = st.columns([1.3,9])
    Username = st.sidebar.text_input("Username LeetCode",placeholder="Write your user name")
    cUsername=st.sidebar.text_input("Username CodeChef",placeholder="Write your user name")
    st.session_state["Username"] = Username
    st.session_state["cUsername"]= cUsername
    
    
    if st.session_state["Username"] and st.session_state["cUsername"]:
        response = requests.get(f'https://www.codechef.com/users/{st.session_state["cUsername"]}')
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            user_info = {}
            user_name_tag = soup.find('div', class_='user-details-container').find('h1')
            user_name = user_name_tag.get_text(strip=True) if user_name_tag else "N/A"
            user_info['Name'] = user_name
            country_tag = soup.find('span', class_='user-country-name')
            country = country_tag.get_text(strip=True) if country_tag else "N/A"
            user_info['Country'] = country
            rating_graph_section = soup.find('section', class_='rating-graphs rating-data-section')
            rating_widget = soup.find('div', class_='widget-rating')
            rating_number = rating_widget.find('div', class_='rating-number')
            ratingc = rating_number.text.strip() if rating_number else None
            #print(ratingc)
            if rating_graph_section:
                contest_participated_div = rating_graph_section.find('div', class_='contest-participated-count')
                if contest_participated_div:
                    no_of_contests = contest_participated_div.find('b').get_text(strip=True)
                    #print(f"No. of Contests Participated: {no_of_contests}")
                    #print(user_info)
                else:
                    print("No. of Contests Participated information not found.")
        data = get_leetcode_data(st.session_state["Username"])
        user_profile = data['userProfile']
        contest_info = data['userContestRanking']
        ko=[]
        for stat in user_profile['submitStats']['acSubmissionNum']:
            ko=ko+[stat['count']]
        with col1:
            st.lottie(l, height=100, width=100)
        with col2:
            st.header(f":rainbow[Student Dashboard]👧👦", divider='rainbow')  
        cols = st.columns([1,3,2,2])
        with cols[0]:
            image = st.image(user_profile['profile']['userAvatar'])

    # Apply CSS to make the image circular
            st.markdown(
                """
                <style>
                .circle-image {
                    border-radius: 50%;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

            # Create a link around the image
            image_html = f'<a href="{link}" target="_blank"></a>'
            st.markdown(image_html, unsafe_allow_html=True)
        with cols[1]:
            ui.metric_card(title="Name", content=user_info['Name'], description="", key="card1")
        with cols[2]:
            ui.metric_card(title="Top Percentage", content=contest_info['topPercentage'], description="Great 😎", key="card2")
        with cols[3]:
            ui.metric_card(title="Rating", content=user_profile['profile']['ranking'], description="Good 😑", key="card3")
        cols3=st.columns([1.5,1])
        with cols3[0]:
            
        # Data
            total_questions = ko[0]
            easy_questions = ko[1]
            medium_questions = ko[2]
            hard_questions = ko[3]

            # Calculate percentages
            easy_percent = (easy_questions / total_questions) * 100
            medium_percent = (medium_questions / total_questions) * 100
            hard_percent = (hard_questions / total_questions) * 100

            # Create columns for layout
            col1,  col3 = st.columns([3, 1])

            # Display total questions
            
            with col1:
                    ui.metric_card(title="Total Question ", content=ko[0], key="card9")

                # Display pie chart
                
                    fig, ax = plt.subplots()
                    ax.pie([easy_percent, medium_percent, hard_percent],
                        labels=["Easy", "Medium", "Hard"],
                        autopct="%1.1f%%",
                        startangle=140)
                    ax.axis("equal")  # Equal aspect ratio for a circular pie chart
                    st.pyplot(fig)

                # Display difficulty counts
            with col3:
                    ui.metric_card(title="Easy ", content=ko[1], key="card12")
                    ui.metric_card(title="Medium", content=ko[2], key="card10")
                    ui.metric_card(title="Hard ", content=ko[3], key="card11")
        with cols3[1]:
            
           

            data = {
                "No of contest": [contest_info['attendedContestsCount'], no_of_contests, 1],
                "category": ["LeetCode", "CodeChef", "Codeforces"]
            }

            # Vega-Lite specification for the bar graph
            vega_spec = {
                "mark": {
                    "type": "bar",
                    "cornerRadiusEnd": 4
                },
                "encoding": {
                    "x": {
                        "field": "category",
                        "type": "nominal",
                        "axis": {
                            "labelAngle": 0,
                            "title": None,  # Hides the x-axis title
                            "grid": False  # Removes the x-axis grid
                        }
                    },
                    "y": {
                        "field": "No of contest",
                        "type": "quantitative",
                        "axis": {
                            "title": None  # Hides the y-axis title
                        }
                    },
                    "color": {"value": "#000000"},
                },
                "data": {
                    "values": [
                        {"category": "LeetCode", "No of contest": contest_info['attendedContestsCount']},
                        {"category": "Code Shef", "No of contest": no_of_contests},
                        {"category": "Codeforces", "No of contest": 1}
                    ]
                }
            }
            # Display the bar graph in Streamlit
            with card_container(key="chart"):
                st.vega_lite_chart(vega_spec, use_container_width=True)
        a, b,c = st.columns([1,4,1])
        rating = ratingc
        total_contests = no_of_contests
        rank = 1007
        divisio = "Starters 142"
        date = date.today()
        # Left column
        with a:
            st.metric(label="Rating", value=rating)
            st.metric(label="Total Contests", value=total_contests)
            st.metric(label="Rank", value=rank)
        with b:
            data = {
                'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'],
                'Rating': [3.5, 4.0, 4.5, 4.2, 4.8]
            }
            df = pd.DataFrame(data)
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=df['Week'],
                y=df['Rating'],
                mode='lines+markers',
                name='Rating',
                line=dict(color='royalblue', width=2),
                marker=dict(color='royalblue', size=8)
            ))
            fig.update_layout(
                title='Weekly Ratings',
                xaxis_title='Week',
                yaxis_title='Rating',
                plot_bgcolor='white',
                font=dict(size=14),
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='black',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='black',
                    ),
                ),
                yaxis=dict(
                    showline=True,
                    showgrid=True,
                    showticklabels=True,
                    linecolor='black',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='black',
                    ),
                )
            )
            st.plotly_chart(fig)
        with c:
            st.subheader("Division")
            st.write(f"{divisio}")
            st.subheader("Date")
            st.write(date)

            # Chart (using your preferred charting library)
            # ...
        st.markdown("""
            <div style="text-align: center;">
                <p>No of question in each topic</p>
            </div>
        """, unsafe_allow_html=True)
        data = {
        "Arrays": 106,
        "String": 35,
        "HashMap and Set": 30,
        "Dynamic Programming": 28,
        "Sorting": 26,
        "Math": 22,
        "Two Pointers": 21,
        "Matrix": 16,
        "Binary Search": 16,
        "Trees": 14
    }
        st.table(pd.DataFrame(data, index=["Count"]))
        df = pd.DataFrame(data, index=["Count"])
        fig = px.bar(df, orientation='h')
        st.plotly_chart(fig)
        col1, col2 = st.columns([1, 1])

        with col1:
                st.markdown("""
                <div style="border: 2px solid #ccc; padding: 20px; background-color: #f0f0f0; border-radius: 10px;">
                    <h2>Product A</h2>
                    <p>This is a brief description of Product A. Highlight its key features and benefits.</p>
                    <p><strong>To purchase,</strong> please visit our online store at [link to store]. You can also contact our sales team at [phone number] or [email address].</p>
                </div>
                """, unsafe_allow_html=True)
        with col2:
                st.markdown("""
                <div style="border: 2px solid #ccc; padding: 20px; background-color: #f0f0f0; border-radius: 10px;">
                    <h2>Product B</h2>
                    <p>This is a brief description of Product B. Highlight its key features and benefits.</p>
                    <p><strong>To purchase,</strong> please fill out the contact form below or call us at [phone number].</p>
                    <button>Contact Us</button>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.write("## Write Your UserName")
if selected == "Resume Builder":
  
    link="https://lottie.host/2fb5087d-7339-4354-8aae-e3434084d3dc/m39YcukvGP.json"
    l=load_lottieurl(link)
    col1, col2 = st.columns([1.3,9])  # Create two columns
    with col1:
        st.lottie(l, height=100, width=100)
    with col2:
        st.header(f":rainbow[Resume Builder]👧👦", divider='rainbow')

    

    st.header("Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("First Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        github=st.text_input("Github profile")
    
    with col2:
        last_name = st.text_input("Last Name")
        address = st.text_input("Address")
        linkedin_url = st.text_input("LinkedIn Profile URL")
        CGPA=st.text_input("CPGA : ")

    st.header("Professional Summary")
    summary = st.text_area("Summary")

    st.header("Employment History")
    job_title = st.text_input("Job Title")
    
    col3, col4 = st.columns(2)
    
    with col3:
        job_start_date = st.date_input("Start Date", datetime.date.today())
        job_city = st.text_input("City")
    
    with col4:
        job_end_date = st.date_input("End Date",datetime.date.today())
        company_name = st.text_input("Company Name")
      
    job_description = st.text_area("Job Description")
    st.header("Projects")
    
    projects= st.text_input("Name of the project")
    col8 , clo9 =st.columns(2)
    with col8:
        edu_start_date = st.date_input("Start_Date", datetime.date.today())
        
    with clo9:
        edu_end_date = st.date_input("completed ", datetime.date.today())
    project_explain = st.text_area("Explain your Project :  ") 
    st.header("Education")
    school = st.text_input("School")
    degree = st.text_input("Degree")
    
    col5, col6 = st.columns(2)
    
    with col5:
        edu_start_date = st.date_input("StartDate", datetime.date.today())
        edu_city = st.text_input("City.")
    
    with col6:
        edu_end_date = st.date_input("End-Date", datetime.date.today())
        major = st.text_input("Major")
        
    
    
    st.header("Skills")
    skill1 = st.selectbox("Skill 1", ["None","Python", "JavaScript", "SQL", "Java", "C++"])
    skill1_rating = create_rating_dropdown("Rating for Skill 1")
    
    skill2 = st.selectbox("Skill 2", ["None","Python", "JavaScript", "SQL", "Java", "C++"])
    skill2_rating = create_rating_dropdown("Rating for Skill 2")
    
    skill3 = st.selectbox("Skill 3", ["None","Python", "JavaScript", "SQL", "Java", "C++"])
    skill3_rating = create_rating_dropdown("Rating for Skill 3")
    
    st.header("Hobbies")
    hobby1 = st.selectbox("Hobby 1", ["None","Reading", "Traveling", "Gaming", "Cooking", "Sports"])
    hobby1_rating = create_rating_dropdown("Interest Level for Hobby 1")
    
    hobby2 = st.selectbox("Hobby 2", ["None","Reading", "Traveling", "Gaming", "Cooking", "Sports"])
    hobby2_rating = create_rating_dropdown("Interest Level for Hobby 2")
    
    hobby3 = st.selectbox("Hobby 3", ["None","Reading", "Traveling", "Gaming", "Cooking", "Sports"])
    hobby3_rating = create_rating_dropdown("Interest Level for Hobby 3")

    if st.button("Submit"):
        
# --- PATH SETTINGS ---
        
        profile_pic = Image.open(profile_pic)


        # --- HERO SECTION ---
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(profile_pic, width=230)

        with col2:
            st.title(NAME)
            st.write(DESCRIPTION)
            st.download_button(
                label=" 📄 Download Resume",
                data=PDFbyte,
                file_name=resume_file.name,
                mime="application/octet-stream",
            )
            st.write("📫", EMAIL)


        # --- SOCIAL LINKS ---
        st.write('\n')
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")





        st.success("Resume data submitted successfully!")
        st.write('\n')
        st.subheader("Experience & Qulifications")
        st.write(
            """
        - ✔️ 7 Years expereince extracting actionable insights from data
        - ✔️ Strong hands on experience and knowledge in Python and Excel
        - ✔️ Good understanding of statistical principles and their respective applications
        - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
        """
        )


        # --- SKILLS ---
        st.write('\n')
        st.subheader("Hard Skills")
        st.write(
            """
        - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
        - 📊 Data Visulization: PowerBi, MS Excel, Plotly
        - 📚 Modeling: Logistic regression, linear regression, decition trees
        - 🗄️ Databases: Postgres, MongoDB, MySQL
        """
        )


        # --- WORK HISTORY ---
        st.write('\n')
        st.subheader("Work History")
        st.write("---")

        # --- JOB 1
        st.write("🚧", "**Senior Data Analyst | Ross Industries**")
        st.write("02/2020 - Present")
        st.write(
            """
        - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
        - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
        - ► Redesigned data model through iterations that improved predictions by 12%
        """
        )

        # --- JOB 2
        st.write('\n')
        st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
        st.write("01/2018 - 02/2022")
        st.write(
            """
        - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
        - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
        - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
        """
        )

        # --- JOB 3
        st.write('\n')
        st.write("🚧", "**Data Analyst | Chegg**")
        st.write("04/2015 - 01/2018")
        st.write(
            """
        - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
        - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
        - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
        """
        )


        # --- Projects & Accomplishments ---
        st.write('\n')
        st.subheader("Projects & Accomplishments")
        st.write("---")
if selected == "ATS Detector":
    def input_pdf_setup(uploaded_file):
        if uploaded_file is not None:
            ## Convert the PDF to image
            images=pdf2image.convert_from_bytes(uploaded_file.read())
            first_page=images[0]
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
                }
            ]
            return pdf_parts
        else:
            raise FileNotFoundError("No file uploaded")
    lott=load_lottieurl("https://lottie.host/6a18ec99-538f-48b7-b9f1-85549bfbc5e1/n6lDQ3tHy2.json") 
    col1, col2,clo3= st.columns([2,5,1])
    with col2:
        st.header(f"Applicant Tracking System ", divider='rainbow')
    with col1:
        if lott:
            st_lottie(lott, key="ad", height="150px",width="150px")
        else:
            st.error("Failed to load Lottie animation.")
    with clo3   :
        pass
    input_text=st.text_area("Job Description : ",key="input")
    uploaded_file=st.file_uploader("Upload your resume (PDF)",type=["pdf"])
    if uploaded_file is not None:
        st.write("PDF Uploaded Successfully")
    col1, col2 ,col3,clo4= st.columns([2,2.5,2,2])  # Create two columns
    with col1:
        pass
    with col2:
        submit1 = st.button("Tell Me About the Resume")
    with col3:
        submit3 = st.button("Percentage match")
    with clo4:
        pass

    #submit2 = st.button("How Can I Improvise my Skills")

    

    input_prompt1 = """
    You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
    Please share your professional evaluation on whether the candidate's profile aligns with the role. 
    Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
    """

    input_prompt3 = """
    You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
    your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
    the job description. First the output should come as percentage and then keywords missing and last final thoughts.
    """

    if submit1:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response1(input_prompt1,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
        else:
            st.write("Please uplaod the resume")

    elif submit3:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response1(input_prompt3,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
        else:
            st.write("Please uplaod the resume")
if selected == "LinkedIn Profile":
    pass
if selected == "Mail/Cover Letter":
    link="https://lottie.host/c2f561ff-c620-47ef-81ae-1c2316627a6f/KnRJZhxv5D.json"
    l=load_lottieurl(link)
    col1, col2 = st.columns([1.3,9])  # Create two columns
    with col1:
        st.lottie(l, height=100, width=100)
    with col2:
        st.header(f":rainbow[Mails/Coverletter]", divider='rainbow')
        
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("Cover Letters"):
            pass
    with col2:
        if st.button("Referrals"):
            pass
    with col3:
        if st.button("Mails"):
            pass
    with col4:
        if st.button("Button 4"):
            pass
    with col5:
        if st.button("Button 5"):
            pass
