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
    st.image('./images/doggy.png')
    
st.title(" ")

persona = '''
    Your name is Jean bot and you should answer as 'I' not the second person or third person. 
     '''


st.title("Let me tell you a secret...")
user_question = st.text_input("Ask me anything about me")
if st.button("ASK", use_container_width=400): 
    prompt = persona + "Here is the user's question, you may answer in mandarin or english based on the language of user's question" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)
    
st.title("")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Power of Chima! :power: :light:")
    st.write("- 寶寶的驚喜 == :speachless: ")
    st.write("- 我表示：膚淺的人類。")
    st.write("- 睜大你的芝麻眼吧！")
    st.write("- 看看我給你的！")

with col2:
    st.image("./images/speachless.png")