import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("You chai is being brewed")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala added to chai")
    

tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Honey", "Sugar"])
st.write(f"Selected {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
st.write(f"Selected Flavour: {flavour}")

sugar = st.slider("Sugar level", 0, 5, 2)


st.number_input("How many cups", min_value=1, max_value=10, step=1)

name = st.text_input("Enter you name ")
if name:
    st.write(f"Welcome {name} ! Your chai is on the way.")

dob = st.date_input("Select your date of birth")
if dob:
    st.write("Your age is ", 2025 - dob.year)

