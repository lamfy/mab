# Import Packages

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Style

style = """<style>body {text-align: justify;}</style>"""
st.markdown(style, unsafe_allow_html=True)

# Title and Instructions

st.markdown("### National University of Singapore")
st.markdown("""
            <b>Instructions:</b> You have five dice which might or might not be fair.
            During each turn, you must roll one of the five dice and observe the result ("result").
            Your goal is to maximise the total result ("total") across 25 turns. Good luck 🍀
            """,
            unsafe_allow_html=True)
st.markdown("""---""")

# Initialise Variables

if "result" not in st.session_state: st.session_state["result"] = 0         
if "total" not in st.session_state: st.session_state["total"] = 0
if "tries" not in st.session_state: st.session_state["tries"] = 25
if "outcome1" not in st.session_state: st.session_state["outcome1"] = np.array([0,0,0,0,0,0])
if "outcome2" not in st.session_state: st.session_state["outcome2"] = np.array([0,0,0,0,0,0])
if "outcome3" not in st.session_state: st.session_state["outcome3"] = np.array([0,0,0,0,0,0])
if "outcome4" not in st.session_state: st.session_state["outcome4"] = np.array([0,0,0,0,0,0])
if "outcome5" not in st.session_state: st.session_state["outcome5"] = np.array([0,0,0,0,0,0])

# Define Functions

def roll(pvals):
    outcome = np.random.multinomial(n=1, pvals=pvals)
    outcome = np.where(outcome==1)[0]+1
    return outcome

def button1():
    if st.session_state["tries"]>0:
        outcome = roll(pvals=[1/6]*6)[0]
        st.session_state["result"] = outcome
        st.session_state["total"] = st.session_state["total"]+outcome
        st.session_state["tries"] = st.session_state["tries"]-1
        st.session_state["outcome1"][outcome-1] = st.session_state["outcome1"][outcome-1]+1
    return

def button2():
    if st.session_state["tries"]>0:
        outcome = roll(pvals=[0]*2+[2/6]*3+[0])[0]
        st.session_state["result"] = outcome
        st.session_state["total"] = st.session_state["total"]+outcome
        st.session_state["tries"] = st.session_state["tries"]-1
        st.session_state["outcome2"][outcome-1] = st.session_state["outcome2"][outcome-1]+1
    return

def button3():
    if st.session_state["tries"]>0:
        outcome = roll(pvals=[3/6]+[0]*4+[3/6])[0]
        st.session_state["result"] = outcome
        st.session_state["total"] = st.session_state["total"]+outcome
        st.session_state["tries"] = st.session_state["tries"]-1
        st.session_state["outcome3"][outcome-1] = st.session_state["outcome3"][outcome-1]+1
    return

def button4():
    if st.session_state["tries"]>0:
        outcome = roll(pvals=[0]*3+[3/6]*2+[0])[0]
        st.session_state["result"] = outcome
        st.session_state["total"] = st.session_state["total"]+outcome
        st.session_state["tries"] = st.session_state["tries"]-1
        st.session_state["outcome4"][outcome-1] = st.session_state["outcome4"][outcome-1]+1
    return

def button5():
    if st.session_state["tries"]>0:
        outcome = roll(pvals=[1/6]*3+[2/6]+[1/6]+[0])[0]
        st.session_state["result"] = outcome
        st.session_state["total"] = st.session_state["total"]+outcome
        st.session_state["tries"] = st.session_state["tries"]-1
        st.session_state["outcome5"][outcome-1] = st.session_state["outcome5"][outcome-1]+1
    return

# Buttons

col1a, col2a, col3a, col4a, col5a, col6a, col7a, col8a, col9a, col10a, col11a = st.columns(11)

with col1a: pass
with col3a: pass
with col5a: pass
with col7a: pass
with col9a: pass
with col11a: pass

col2a.markdown("<center>1️⃣</center>", unsafe_allow_html=True)
col2a.button(label="🎲", key="click1", on_click=button1)

col4a.markdown("<center>2️⃣</center>", unsafe_allow_html=True)
col4a.button(label="🎲", key="click2", on_click=button2)

col6a.markdown("<center>3️⃣</center>", unsafe_allow_html=True)
col6a.button(label="🎲", key="click3", on_click=button3)

col8a.markdown("<center>4️⃣</center>", unsafe_allow_html=True)
col8a.button(label="🎲", key="click4", on_click=button4)

col10a.markdown("<center>5️⃣</center>", unsafe_allow_html=True)
col10a.button(label="🎲", key="click5", on_click=button5)

st.markdown("""<br>""", unsafe_allow_html=True)

# Results

col1b, col2b, col3b, col4b, col5b, col6b, col7b = st.columns(7)

with col1b: pass
with col3b: pass
with col5b: pass
with col7b: pass

with col2b:
    st.write("Total: ", st.session_state.total)
    
with col4b:
    st.write("Result: ", st.session_state.result)

with col6b:
    st.write("Left: ", st.session_state.tries)

st.markdown("""---""")

# Visualisation

with st.expander("Visualise the Results!"):
    
    plot1, plot2 = st.columns(2)
    plot3, plot4 = st.columns(2)
    plot5, plot6 = st.columns(2)

    values = np.array(["1", "2", "3", "4", "5", "6"])

    df1 = pd.DataFrame({"Outcome": values, "Proportion": st.session_state["outcome1"]/(st.session_state["outcome1"].sum())})
    df2 = pd.DataFrame({"Outcome": values, "Proportion": st.session_state["outcome2"]/(st.session_state["outcome2"].sum())})
    df3 = pd.DataFrame({"Outcome": values, "Proportion": st.session_state["outcome3"]/(st.session_state["outcome3"].sum())})
    df4 = pd.DataFrame({"Outcome": values, "Proportion": st.session_state["outcome4"]/(st.session_state["outcome4"].sum())})
    df5 = pd.DataFrame({"Outcome": values, "Proportion": st.session_state["outcome5"]/(st.session_state["outcome5"].sum())})

    p1 = (alt.Chart(df1, title="1️⃣").
          mark_bar().
          encode(x=alt.X("Outcome", scale=alt.Scale(domain=values)),
                 y=alt.Y("Proportion", scale=alt.Scale(domain=[0,1])),
                 color=alt.Color("Outcome", scale=alt.Scale(scheme="tableau10"), legend=None),
                 tooltip=["Outcome", "Proportion"]).
          interactive())

    p2 = (alt.Chart(df2, title="2️⃣").
          mark_bar().
          encode(x=alt.X("Outcome", scale=alt.Scale(domain=values)),
                 y=alt.Y("Proportion", scale=alt.Scale(domain=[0,1])),
                 color=alt.Color("Outcome", scale=alt.Scale(scheme="tableau10"), legend=None),
                 tooltip=["Outcome", "Proportion"]).
          interactive())

    p3 = (alt.Chart(df3, title="3️⃣").
          mark_bar().
          encode(x=alt.X("Outcome", scale=alt.Scale(domain=values)),
                 y=alt.Y("Proportion", scale=alt.Scale(domain=[0,1])),
                 color=alt.Color("Outcome", scale=alt.Scale(scheme="tableau10"), legend=None),
                 tooltip=["Outcome", "Proportion"]).
          interactive())

    p4 = (alt.Chart(df4, title="4️⃣").
          mark_bar().
          encode(x=alt.X("Outcome", scale=alt.Scale(domain=values)),
                 y=alt.Y("Proportion", scale=alt.Scale(domain=[0,1])),
                 color=alt.Color("Outcome", scale=alt.Scale(scheme="tableau10"), legend=None),
                 tooltip=["Outcome", "Proportion"]).
          interactive())

    p5 = (alt.Chart(df5, title="5️⃣").
          mark_bar().
          encode(x=alt.X("Outcome", scale=alt.Scale(domain=values)),
                 y=alt.Y("Proportion", scale=alt.Scale(domain=[0,1])),
                 color=alt.Color("Outcome", scale=alt.Scale(scheme="tableau10"), legend=None),
                 tooltip=["Outcome", "Proportion"]).
          interactive())

    plot1.altair_chart(p1, use_container_width=True)
    plot2.altair_chart(p2, use_container_width=True)
    plot3.altair_chart(p3, use_container_width=True)
    plot4.altair_chart(p4, use_container_width=True)
    plot5.altair_chart(p5, use_container_width=True)