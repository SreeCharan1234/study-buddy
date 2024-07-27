from pathlib import Path
from googletrans import Translator
import speech_recognition as sr
import pdf2image
import gtts
import playsound
from streamlit_ace import st_ace
from PIL import Image
import base64
import streamlit as st
from streamlit_extras.let_it_rain import rain
from tempfile import NamedTemporaryFile
from streamlit_option_menu import option_menu
from streamlit_extras.mandatory_date_range import date_range_picker
import datetime
import os
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from streamlit_lottie import st_lottie
import requests 
import sys
import io
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import speech_recognition as sr
from youtube_transcript_api import YouTubeTranscriptApi
import time
global s
k=0
os.getenv("AIzaSyBIBVb-0Z0QwaucMGOGy8-j_RM22X-4-lE")
genai.configure(api_key="AIzaSyBIBVb-0Z0QwaucMGOGy8-j_RM22X-4-lE")
t=[ "Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "Swift", "Kotlin", 
    "C#", "Go", "R", "TypeScript", "Scala", "Perl", "Objective-C", "Dart", 
    "Rust", "Haskell", "MATLAB", "SQL", "HTML/CSS", "React", "Angular", "Vue.js", 
    "Node.js", "Django", "Flask", "Spring", "ASP.NET", "Ruby on Rails"]
interview_topics = [
    # Core Python
    "Python fundamentals (syntax, data types, control flow)",
    "Object-oriented programming (OOP) concepts",
    "Data structures (lists, tuples, dictionaries, sets)",
    "Functions and modules",
    "Exception handling",

    # Advanced Python
    "Functional programming paradigms",
    "Decorators and generators",
    "Metaclasses",
    "Concurrency and parallelism",
    "Asynchronous programming",

    # Data Science and Machine Learning
    "NumPy and Pandas",
    "Data cleaning and preprocessing",
    "Exploratory data analysis (EDA)",
    "Machine learning algorithms and models",
    "Model evaluation and deployment",

    # Web Development
    "Django or Flask frameworks",
    "RESTful APIs",
    "Databases (SQL, NoSQL)",
    "Front-end technologies (HTML, CSS, JavaScript)",

    # Software Engineering
    "Design patterns",
    "Algorithms and data structures",
    "Software testing and debugging",
    "Version control (Git)",
    "Code optimization and refactoring",

    # Other
    "Problem-solving and logical reasoning",
    "System design",
    "Project management",
    "Open-source contributions",
    "Soft skills (communication, teamwork, leadership)"
]
st.set_page_config(page_title="Resume", page_icon='chart_with_upwards_trend', layout="wide", initial_sidebar_state="auto", menu_items=None)
EXAMPLE_NO = 1
is_listening = False
recognizer = sr.Recognizer()
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
def get_gemini_response1(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text
def example():
    rain(
        emoji="*",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
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
        while is_listening:
            st.write("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                
                return text
            except sr.UnknownValueError:
                st.error("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
def get_transcript(video_url):

  # Extract the video ID from the URL
  video_id = video_url.split("=")[1]

  # Create an instance of YouTubeTranscriptApi
  transcript_api = YouTubeTranscriptApi()

  # Get the transcript data
  transcript = transcript_api.get_transcript(video_id)

  return transcript
def pseudo_bold(text):
    bold_text = ''.join(chr(0x1D5D4 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else
                        chr(0x1D5EE + ord(c) - ord('a')) if 'a' <= c <= 'z' else c
                        for c in text)
    return bold_text
def streamlit_menu(example=1):
    if example == 1:
        with st.sidebar:
            selected = option_menu(
                
                menu_title="Knowledge Builder🧠",  # required
                options=["Road Map","Code Editor","Mock Interview","AI Bot"],  # required
                icons=["geo-alt-fill","bi bi-code-slash","bi bi-camera-video-fill","robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,
            )
        return selected
    if example == 2:
        selected = option_menu(
                menu_title="Knowledge Builder",  # required
                options=["Road Map","Code Editor","Mock Interview","AI Bot"],  # required
                icons=["geo-alt-fill","bi bi-code-slash","bi bi-camera-video-fill","robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,
            )
        return selected
    if example == 3:
        selected = option_menu(
                menu_title="Knowledge Builder",  # required
                options=["Road Map","Ai bot","Code-editior","Question"],  # required
                icons=["geo-alt-fill","robot","bi bi-code-slash","bi bi-question-diamond-fill"],  # optional
                menu_icon="cast",  # optional
                default_index=0,
            )
        return selected
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
selected = streamlit_menu(example=EXAMPLE_NO)
if 'questions' not in st.session_state:
    st.session_state.questions = []
if selected == "Road Map":
    link="https://lottie.host/76509b4e-81b1-4877-9974-1fa506b294b1/ja7bfvhaEb.json"
    l=load_lottieurl(link)
    col1, col2 = st.columns([1,9])  # Create two columns
    with col1:
        st.lottie(l, height=100, width=100)
    with col2:
        st.header(f":rainbow[Get Your Personalised Roadmap]😎🧑‍🏫", divider='rainbow')
        
    
    

    with st.form(key='survey_form'):
        col1, col2 = st.columns(2)  # Create two columns

        with col1:
            text_stack_placeholder = pseudo_bold("Known Tech Stacks")
            text_know = st.multiselect("Tech Stacks You Already Know", t, [], placeholder="choose tech stacks")
            year = st.radio("Which year you are in", ("1st year 🥳", "2nd year 😃", "3rd year 😊","4th year  🎓"))
        
        with col2:
            End_Gole = st.multiselect("What is your End Goal ?", t, [], placeholder="choose end goal")
            difficulty = st.radio("At what level do you want to learn?", ("Beginner😃🟢", "Intermediate🙂🟡", "Advanced😎🔴"))
        result = date_range_picker("Select a date range")
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        with st.spinner("Analyzing..."):
            s="So now take a role of expert road map desiesner for engiernieg students and now my  end gole is to learn " + str(End_Gole)+"i want to complete this my end gole in "+ str(result)+"i only want to lean till the "+str(difficulty)+"am i am now in "+str(year)+"from these imformation give me proper road map which include the resouce(youtube channels) the time line to each topic in deatle and also tell how much time should i give to each day to  complete that task  and sove leatcode questions which are importatnt add imogies and make your reslut in organised manner  and if possible also make a table to represent all the data  "
            s=get_gemini_response(s)
            st.write(s)
if selected == "AI Bot":
    link="https://lottie.host/364beff7-b5bc-459e-ac28-d26cfa0dfece/FLsJPwNGdK.json"
    l=load_lottieurl(link)
    example()
    col1, col2 = st.columns([2,9])  # Create two columns
    with col1:
        st.lottie(l, height=150, width=150)
    with col2:
        st.header(f"AIBot", divider='rainbow')
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        msg=get_gemini_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)        
if selected=="Code Editor": 
    link="https://lottie.host/d6e55231-a53c-4d19-a142-d71320fcd9a7/hbFKIhu1KA.json"
    l=load_lottieurl(link)
    col1, col2 = st.columns([1,9])  # Create two columns
    with col1:
        st.lottie(l, height=100, width=100)
    with col2:
        st.header(f":rainbow[Code Editor]👨‍💻", divider='rainbow')
    if k==0:
        
        st.markdown("""
        <style>
        .stButton>button, .stTextInput>div>div>input {
            margin: 0 10px 0 0;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: #007BFF;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .button-container {
            display: flex;
            justify-content: flex-start;
            align-items: center;
        }
        .stTextInput>div>div>input {
            margin-right: 10px;
            background-color: white;
            color: black;
            border: 1px solid #ccc;
        }
        </style>
        """, unsafe_allow_html=True)
    python_code = """def sum_of_list(l):
            
    print(sum(l))
sum_of_list([5, 3,4,4])      
    """

    javascript_code = """
    function myFunction(x, y) {
    // Print the sum of x and y
    console.log(x + y);
    }

    myFunction(5, 3);
    """

    # Select language
    selected_lang = st.sidebar.selectbox("Language", ["Python", "JavaScript"])

    # Set session state
    st.session_state["selected_lang"] = selected_lang

    # Conditionally display code editor
    if selected_lang == "Python":
        editor_content = st_ace(value=python_code, language='python', theme='monokai', keybinding='vscode', font_size=14)
    elif selected_lang == "JavaScript":
        editor_content = st_ace(value=javascript_code, language='javascript', theme='monokai', keybinding='vscode', font_size=14)
    else:
        st.write("Unsupported language selected.")

    col1, col2,col3 = st.columns([6,1, 1])
    # JavaScript to simulate button click on Ctrl + Enter
    st.markdown("""
    <script>
    document.addEventListener('keydown', function(event) {
        if (event.ctrlKey && event.key === 'Enter') {
            document.getElementById('run-code').click();
        }
    });
    </script>
    """, unsafe_allow_html=True)
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    with col1:
       text_input = st.text_input("Enter text here:")
    
    with col2:
        if st.button("🎤 Mic"):
            is_listening = True
            voice_input = recognize_speech_from_microphone()

            if voice_input:
                text_input = voice_input  # Update text input with recognized speech
            is_listening = False
        # Hidden run button
       
    with col3:

    # Run Code button
        run_button = st.button("Run Code", key='run-code')

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<button id="run-code" style="display: none;">Hidden Run Button</button>', unsafe_allow_html=True)
    
    # Capture and display the output when the button is clicked
    if run_button:
        # Redirect stdout to capture print statements
        output = io.StringIO()
        sys.stdout = output

        try:
            # Execute the code from the editor
            exec(editor_content)
        except Exception as e:
            # Capture any exceptions
            st.error(f"Error: {e}")
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__

        # Display the captured output
        st.write("### Code Output")
        st.text("The Output of the above code is : "+output.getvalue())

    # Display the captured input
    if text_input:
        st.success(f"You said: {text_input}")
        s="here is python code "+str(editor_content)+"so please do the change like this "+text_input+"and give me the wole answer in python only dont give me it in any english owrd explin it all in comments only "

        s=get_gemini_response(s)
        s=s[9:-3]
        
        editor_content = st_ace(value=str(s), language='python', theme='monokai', keybinding='vscode', font_size=14)
if selected == "Mock Interview":
    link="https://lottie.host/299688b5-e6b2-48ad-b2e9-2fa14b1fb117/TXqg2APXpL.json"
    l=load_lottieurl(link)
    col1, col2 = st.columns([1,9])  # Create two columns
    with col1:
        st.lottie(l, height=100, width=100)
    with col2:
        st.header(f":rainbow[Mock Interview]💻💻", divider='rainbow')
    col1, col2 = st.columns([1,1])   
    with col1:
        text = st.multiselect("Which topic you want to practice ",interview_topics,[],placeholder="Choose the topic")
        video_link = st.text_input(" Enter the video link",placeholder="Enter the url")    
        uploaded_file=st.file_uploader("Upload your study Material (PDF)",type=["pdf"])
    with col2:
        # Camera setup
        webrtc_streamer(key="sample") 
    s=""
    text_input=""
    if st.button("Generate question"):
            if video_link :    
                transcript = get_transcript(video_link)
                s=""
                for segment in transcript:
                    try:
                        s=s+f"{segment['text']}"
                        #print(f"{segment['text']}")
                    except KeyError:
                        print(f"Segment with missing end time: Text: {segment['text']}")
                s=s+str(text)
                s=s+"this is tracprit of yout which i have studing now form this ask me 1 question based on the interview  it should now be mcq and it can be answer by only mic and  dont give answer i have to proctive fro my self "
                s=get_gemini_response(s)
            if text:
                s=str(text)+"from  this is of topic yout which i have studing now form this ask me 1 question based on the interview " 
                s=get_gemini_response(s)
            if uploaded_file:
                if uploaded_file is not None:
                    st.write("PDF Uploaded Successfully")
                    pdf_content=input_pdf_setup(uploaded_file) 
                    s=get_gemini_response1("from the content make a question",pdf_content,"it should not be mcq type question")
            st.session_state["q"]= s
    
    if st.button("🎤Speak now"):
            is_listening = True
            voice_input = recognize_speech_from_microphone()
            st.write(st.session_state["q"])
            if voice_input:
                is_listening = False
                text_input = voice_input
                  
        
            
    if s:
        st.write(s)
        k=s
    if text_input:
        st.success(f"You said: {text_input}") 
        s="the given question is"+str(st.session_state["q"] )+"And the answer is given is "+ text_input +" this is my question and my answer now you give me the coorect answer and also write give me the score for my anwer  out of 10 give me the number  it is a interview also tell how can i improve and be littlebe strict"
        
        s=get_gemini_response(s)
        st.write(s)
    
        

    
    