# app.py
import streamlit as st
import time

# 初始化狀態
if "day" not in st.session_state:
    st.session_state.day = 1
if "last_choice" not in st.session_state:
    st.session_state.last_choice = None
if "reset_choice" not in st.session_state:
    st.session_state.reset_choice = False
if "zhinan_index" not in st.session_state:
    st.session_state.zhinan_index = 0
if "suile_count" not in st.session_state:
    st.session_state.suile_count = 0

st.set_page_config(page_title="戀愛存亡選擇", page_icon="💬")
st.title("My Happy Day")

# 每次 day 增加時清除 choice
if st.session_state.reset_choice:
    st.session_state.pop("choice", None)
    st.session_state.reset_choice = False

# 顯示狀態
st.markdown(f"### 📆 Day {st.session_state.day}")
st.markdown("女朋友問：**「要不要去找你？」**")
if st.session_state.suile_count > 0:
    for _ in range(st.session_state.suile_count):
        st.markdown("女朋友問：**「所以勒？」**")

# 顯示直男指數
st.progress(st.session_state.zhinan_index / 100)
st.markdown(f"#### 🧠 直男指數：{st.session_state.zhinan_index}%")
if st.session_state.zhinan_index >= 100:
    st.markdown("## 💥 你個臭直男！！")

# 選項按鈕
choice = st.radio("你要怎麼回應？", [
    "好，來找我",
    "看你啊，會累或太麻煩也不用勉強沒關係",
    "看你啊"
], key="choice")

if st.button("送出回覆"):
    st.session_state.last_choice = choice
    if choice == "好，來找我":
        st.markdown("""
        她來了。  
        她說：「你都沒有好好對待我，我常常都很累或不順路但我還是會去找你。」  
        😡 **Bad End：女友生氣**
        """)
        st.session_state.day += 1
        st.session_state.zhinan_index = min(100, st.session_state.zhinan_index + 25)
        st.session_state.reset_choice = True
        time.sleep(3)
        st.rerun()

    elif choice == "看你啊，會累或太麻煩也不用勉強沒關係":
        st.markdown("""
        她說：「那好，不要就算了。」  
        她說：「我們不好了。」  
        💔 **Bad End：女友生氣**
        """)
        st.session_state.day += 1
        st.session_state.zhinan_index = min(100, st.session_state.zhinan_index + 25)
        st.session_state.reset_choice = True
        time.sleep(3)
        st.rerun()

    elif choice == "看你啊":
        st.session_state.suile_count += 1
        st.markdown("""
        她說：「看你。」  
        🌀 你們看著彼此
        """)
        countdown = st.empty()
        for i in range(5, 0, -1):
            countdown.markdown(f"**{i}...**")
            time.sleep(1)
        st.rerun()