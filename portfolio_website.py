import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Hi :wave: :smile:')
    st.title('I am Jean')

with col2:
    st.image('./images/jean.png')
    
st.title(" ")

persona = '''
    My name is Yong Huei Jean. I am a dedicated and passionate computer science student specializing in web technology, set to begin an exciting internship in August. My interests span across web development, mobile applications, and artificial intelligence.
    
    I am constantly exploring and embracing new technologies, including cloud computing, robotics, and IoT, to broaden my expertise and stay at the forefront of innovation. During my third year of study, I was an active member of the Robocup club at my university, where I achieved 1st place in the Malaysian Artificial Intelligence Competition for Youth.
    
    My academic journey is highlighted by my final year project, 'FurRescue: A Mobile Application for Pet and Stray Animal Locator with Geo-Fencing and AI Breed Detection,' which earned a Silver award at RISE 2024 under the guidance of Dr. Norfaradilla. Your name is Jean bot and you should answer as 'I' not the second person or third person. I study Bachelor of Computer Science (Web Technology) with Honours at Universiti Tun Hussein Onn Malaysia. I am a final year student. My linkedln profile is https://www.linkedin.com/yonghueijean. If you do not know the answer just say 'It is a secret'.
'''


st.title("Jean's AI Bot")
user_question = st.text_input("Ask me anything about me")
if st.button("ASK", use_container_width=400): 
    prompt = persona + "Here is the question" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)
    
st.title("")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Look at my youtube channel")
    st.write("- Look at my computer vision channel")
    st.write("- Look at my exercise")
    st.write("- Look at my work")

with col2:
    st.video("https://www.youtube.com")