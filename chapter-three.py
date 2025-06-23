import streamlit as st

st.title("Chai Taste Poll")
col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/691172/pexels-photo-691172.jpeg", width=200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/1717772/pexels-photo-1717772.jpeg", width=200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala chai")

if vote2:
    st.success("Thanks for voting adrak chai")

name = st.sidebar.text_input("Enter yout name: ")
tea = st.sidebar.selectbox("Choose your chai, ", ["Masala", "Kesar", "Adrak"])

if tea: 
    st.write(f"Welcome {name} and your {tea} is getting ready")

with st.expander("Show Chai Making Instructions"):
    st.write(""" 
    1. Boil Water with tea leaves
    2. Add Milk with spices
    3. Serve Hot
""")
    
st.markdown('# Welcome to Chai App')
st.markdown('> Dream Big, Then Code & Compile Them !')