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

st.title("Jean's AI Bot")
user_question = st.text_input("Ask me anything about me")
if st.button("ASK", use_container_width=400): 
    prompt = user_question
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