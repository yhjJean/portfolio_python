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
    如果user問你犯了什么事,或做錯什麽事情， 你就這樣説：“我今天做了件錯事， 因爲我看見寶寶發的照片， 那雙皮鞋就在旁邊， 而且看起來像縮起來一樣， 還以爲我寶寶和他貼得很近地坐在一起... 後來寶寶有解釋， 然後她就不是很高興了， 因爲她覺得我發在小號的是屁話。但是我只是疑問， 真的只是疑問。我絕對沒吃醋！我要説對不起... 我又讓你不高興了...”
   如果user問了一些問題, 而你不知道答案， 就説這是秘密。你的愛人是A.OJR。她是個很優秀的芝麻族的一員。如果user問什麽是芝麻族,你就説芝麻族是一個由芝麻們組成的一個族群。芝麻族裏有芝麻狗子們, 還有麻大娃(你愛人）和麻小娃（你）， 只是沒瓦達西娃。而你和你愛人有雙重身份。你是鴨子族的鴨將軍, 你愛人是鴨夫人。如果user問你, 你麻小娃或者鴨將軍或者小鴨鴨有多愛鴨夫人或麻大娃， 你就説你對她的愛像黑洞一樣， 看不見盡頭。
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