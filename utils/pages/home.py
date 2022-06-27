from datetime import date
import streamlit as st

def app():
        
    st.markdown("### Applied Regression Models using R")
    st.markdown(
        """
        Welcome to the instructors' portal for ***Applied Regression Models using R***.
        This is a one-stop portal for instructors to monitor learners' progress and teaching feedback :books:
        """
        )
    st.markdown("#### Module Co-Ordinators")
    st.markdown("##### Batch 2")
    st.markdown("- Qian Jiang (Senior Lecturer)\n- Lam Fu Yuan, Kevin (Instructor)")
    st.markdown("##### Batch 1")
    st.markdown("- Nirmala Ramakrishnan (Instructor)\n- Lam Fu Yuan, Kevin (Instructor)")
    st.markdown(f"Last Updated on {date.today().strftime('%d %b %Y')}.")