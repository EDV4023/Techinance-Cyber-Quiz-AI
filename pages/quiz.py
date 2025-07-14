from google import genai
from google.genai.types import Content, Part
import streamlit as st


if "user" not in st.session_state:
    st.session_state['user'] = "default_user"
if "exp" not in st.session_state:
    st.session_state["exp"] = ""

if "user" in st.session_state:
    user = st.session_state['user']

client = genai.Client(api_key="api-key")

chat = client.chats.create(model="gemini-2.0-flash", history = [
    Content(role = "user", parts = [Part(text="You are a Cybersecurity question generating bot and the user will choose a difficulty between Easy, Intermediate, Hard, and Extreme.")]),
    Content(role="model", parts = [Part(text="Understood!")])
])

level_select = st.selectbox(label = "**Difficulty**", options = ["Easy", "Intermediate", "Hard", "Extreme"])
quest_bool = st.button("Question")

def point_change():
    try:
        with open("user_db.txt","r") as user_db:
            lines = user_db.readlines()
    except FileNotFoundError:
        lines = []
    
    
    line_index = None
    for index, line in enumerate(lines):
        if line.strip() and line.split(" ")[0] == user:
            line_index = index
            break
    
    if level_select=="Easy":
        points = 1
    elif level_select=="Intermediate":
        points = 5
    elif level_select=="Hard":
        points = 10
    elif level_select=="Extreme":
        points = 20
    
    if line_index is not None:
        
        new_score = int(lines[line_index].split(" ")[1]) + points
        lines[line_index] = user + " " + str(new_score) + "\n"
    else:
        
        lines.append(user + " " + str(points) + "\n")
    
    with open("user_db.txt", "w") as user_db:
        user_db.writelines(lines)
    
    st.success("Correct! You earned " + str(points) + " points!")

if quest_bool:
    response = chat.send_message(f"Generate a multiple choice cybersecurity question of {level_select} difficulty, without additional text such as Okay and Here is your question, in the form, separated by commas, of: Question: Insert Cyber Security Question?, Choices:A:Choice_A|B:Choice_B|C:Choice_C|D:Choice_D, Answer: Correct_Answer_Letter")
    print(response.text)
    question = response.text.split(",")[0]
    choices = response.text.split(",")[1]
    choices = choices.replace("Choices:","")
    choice_list = []
    for choice in choices.split("|"):
        choice_list.append(choice.split(":")[1])

    answer = response.text.split(",")[2]
    answer = answer.replace(" Answer:","").strip()
    print(answer)
    
    
    st.session_state["current_question"] = question
    st.session_state["current_choices"] = choice_list
    st.session_state["current_answer"] = answer


if "current_question" in st.session_state:
    st.markdown("**"+st.session_state["current_question"]+"**")
    for choice in st.session_state["current_choices"]:
        st.write(choice)
    
    col_1, col_2, col_3, col_4 = st.columns([1,1,1,1])

    with col_1:
        if st.button("A"):
            if st.session_state["current_answer"] == "A":
                point_change()
                print("Correct A selected")
            else:
                st.error("Incorrect!")
    with col_2:
        if st.button("B"):
            if st.session_state["current_answer"] == "B":
                point_change()
                print("Correct B selected")
            else:
                st.error("Incorrect!")

    with col_3:
        if st.button("C"):
            if st.session_state["current_answer"] == "C":
                point_change()
                print("Correct C selected")
            else:
                st.error("Incorrect!")

    with col_4:
        if st.button("D"):
            if st.session_state["current_answer"] == "D":
                point_change()
                print("Correct D selected")
            else:
                st.error("Incorrect!")