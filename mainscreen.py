import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")
st.title("Cyber-Quiz AI")
user = st.text_input("**Input a username for the leaderboard:**")
if user not in st.session_state:
    st.session_state['user'] = user
if user:
    st.page_link("pages/quiz.py", label = "***Play***", icon = ":material/videogame_asset:")

with open(r"Techinance\user_db.txt", "a") as user_db:
    user_db.write(user + " " + "0\n")





#leaderboard for top ten



#username system for leadeboard



# Point system - 1 pt. = Easy, 5 pt. = Intermediate, 10 pt. = Hard, 20 pt. = Extreme 




# Streak System - +1 for all, 10 streak = +1 Bonus Point, 20 streak = +2 Bonus Point, etc