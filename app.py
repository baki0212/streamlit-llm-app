from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI  # 追加: ChatOpenAIのインポート

st.title("病気: 心と体の健康相談アプリ")

st.write("##### 相談相手1: 精神科の専門医")
st.write("入力フォームに悩み事を入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 相談相手2: 内科もしくは整形外科の専門医")
st.write("体の健康に関する相談を入力し、「実行」ボタンを押すことでBMI値を計算できます。")

selected_item = st.radio(
    "相談相手を選択してください。",
    ["精神科の専門医", "内科もしくは整形外科の専門医"]
)

st.divider()

if selected_item == "精神科の専門医":
    input_message = st.text_input(label="心の健康に関する悩み事を入力してください。")

else:
    input_message = st.text_input(label="体の健康に関する相談を入力してください。")

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

if st.button("実行"):
    st.divider()

    if selected_item == "精神科の専門医":
        if input_message:
            #精神科専門家であるLLMにからの回答を得る    
            response = llm.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": selected_item + "です。あなたの悩みに優しく親身に相談に乗ります。"},
                    {"role": "user", "content": input_message}
    ]
)
            st.write(response.choices[0].message.content)

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            #内科もしくは整形外科専門家であるLLMにからの回答を得る    
            response = llm.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": selected_item + "です。あなたの悩みに優しく親身に相談に乗ります。"},
                    {"role": "user", "content": input_message}
    ]
)
            st.write(response.choices[0].message.content)
        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")