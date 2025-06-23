import streamlit as st
import random

st.markdown("<h1 style='text-align: center; margin-bottom: 30px'>Love Calci</h1>", unsafe_allow_html=True)
st.image("love.svg")

st.subheader("Our fun, light-hearted love algorithm calculates your connection and gives you a percentage score, plus a personalized message to spice up your results. Ready to see if it's a match made in heaven or just a fleeting crush?")

st.subheader("Find out now! 💌📜")

user_name = st.text_input("Enter your name:", placeholder="e.g., Alex")
beloved_name = st.text_input("Enter your crush's name:", placeholder="e.g., Taylor")

if user_name or beloved_name:
    if st.button("Submit"): 
        generate_random_num = random.randint(1, 100)

        if generate_random_num <= 100 and generate_random_num >= 80:
            st.subheader(f"Your Love Percenatge is {generate_random_num}%")
            st.success("You both are made for each other 🤗")
        elif generate_random_num<=80 and generate_random_num >= 50:
            st.subheader(f"Your Love Percenatge is {generate_random_num}%")
            st.warning("You both moves like Oil and Water moves together 😖")
        elif generate_random_num <= 50 and generate_random_num >= 1:
            st.subheader(f"Your Love Percenatge is {generate_random_num}%")
            st.error("Someone has to perform some extra effort to make things work  💔")


