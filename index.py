import streamlit as st

style = """
<style>
body {text-align: justify;}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

st.markdown("### National University of Singapore")
st.markdown(
    """
    <b>Instructions:</b> You have 100 tries. 
    """,
    unsafe_allow_html=True)

st.markdown("""---""")

if "score" not in st.session_state:
    st.session_state["score"] = 0
    
if "tries" not in st.session_state:
    st.session_state["tries"] = 10
    
if "last" not in st.session_state:
    st.session_state["last"] = 0

def click1():
    st.session_state["score"] = st.session_state["score"]+1
    st.session_state["last"] = 1
    st.session_state["tries"] = st.session_state["tries"]-1
    return

def click2():
    st.session_state["score"] = st.session_state["score"]+10
    st.session_state["tries"] = st.session_state["tries"]-1
    return

def click3():
    st.session_state["score"] = st.session_state["score"]+10
    st.session_state["tries"] = st.session_state["tries"]-1
    return


def click4():
    st.session_state["score"] = st.session_state["score"]+10
    st.session_state["tries"] = st.session_state["tries"]-1
    return


def click5():
    st.session_state["score"] = st.session_state["score"]+10
    st.session_state["tries"] = st.session_state["tries"]-1
    return

col1a, col2a, col3a, col4a, col5a, col6a, col7a, col8a, col9a, col10a, col11a = st.columns(11)

with col1a: pass
with col3a: pass
with col5a: pass
with col7a: pass
with col9a: pass
with col11a: pass

col2a.markdown("<center>1️⃣</center>", unsafe_allow_html=True)
col2a.button(label="🎲", key="click1", on_click=click1)

col4a.markdown("<center>2️⃣</center>", unsafe_allow_html=True)
col4a.button(label="🎲", key="click2", on_click=click2)

col6a.markdown("<center>3️⃣</center>", unsafe_allow_html=True)
col6a.button(label="🎲", key="click3", on_click=click3)

col8a.markdown("<center>4️⃣</center>", unsafe_allow_html=True)
col8a.button(label="🎲", key="click4", on_click=click4)

col10a.markdown("<center>5️⃣</center>", unsafe_allow_html=True)
col10a.button(label="🎲", key="click5", on_click=click5)

st.markdown("""---""")

col1b, col2b, col3b, col4b, col5b, col6b, col7b = st.columns(7)

with col1b: pass
with col3b: pass
with col5b: pass
with col6b: pass

with col2b:
    st.write("Total: ", st.session_state.score)
    
with col4b:
    st.write("Previous: ", st.session_state.last)

with col6b:
    st.write("Left: ", st.session_state.tries)
