# app.py
import streamlit as st
import time

# 初始化 Day 狀態
if "day" not in st.session_state:
    st.session_state.day = 1
if "last_choice" not in st.session_state:
    st.session_state.last_choice = None

st.set_page_config(page_title="戀愛存亡選擇", page_icon="💬")
st.title("My Happy Day")

# 回到選項畫面
st.markdown(f"### 📆 Day {st.session_state.day}")
st.markdown("女朋友問：**「要不要來找我？」**")

# 選項按鈕
choice = st.radio("你要怎麼回應？", [
    "你來找我",
    "看你啊，會累或太麻煩也不用勉強沒關係",
    "看你啊"
])

if st.button("送出回覆"):
    st.session_state.last_choice = choice
    if choice == "好，來找我":
        st.markdown("""
        她來了。  
        她說：「你都沒有好好對待我，我常常都很累或不順路但我還是會去找你。」  
        😡 **Bad End：女友生氣**
        """)
        st.session_state.day += 1

    elif choice == "看你啊，會累或太麻煩也不用勉強沒關係":
        st.markdown("""
        她說：「那好，不要就算了。」  
        她說：「我們不好了。」  
        💔 **Bad End：女友生氣**
        """)
        st.session_state.day += 1

    elif choice == "看你啊":
        st.markdown("""
        她說：「看你。」  
        🌀 你們看著彼此
        """)
        countdown = st.empty()
        for i in range(5, 0, -1):
            countdown.markdown(f"**{i}...**")
            time.sleep(1)
        st.rerun()
