import streamlit as st
import random
import pandas as pd

def app():
        
    st.markdown("### Game")
    st.markdown(
        """
        Game
        """
        )
    
    # initializing with a random number
    if "score" not in st.session_state:
        st.session_state["score"] = 0
        
    if "tries" not in st.session_state:
        st.session_state["tries"] = 10
        
    def click1():
        st.session_state["score"] = st.session_state["score"]+1
        st.session_state["tries"] = st.session_state["tries"]-1
        return
    
    def click2():
        st.session_state["score"] = st.session_state["score"]+10
        st.session_state["tries"] = st.session_state["tries"]-1
        return
    
#    # callback function to change the random number stored in state
#    def change_number():
#        st.session_state["rn"] = random.randint(1,100)
#        return
    
    st.write(st.session_state.score)
    st.write(st.session_state.tries)
    
    ## button to generate a new random number
    st.button("Click1", on_click=click1)
    st.button("Click2", on_click=click2)

#    with st.form('Form', clear_on_submit=True):
#        inputted_idx = st.text_input('Input the number written above')
#        submit = st.form_submit_button('Submit')
    
#    if submit:
#        data = pd.DataFrame({'inputted_idx':[inputted_idx], 'idx':[st.session_state.rn]})
#        st.dataframe(data)