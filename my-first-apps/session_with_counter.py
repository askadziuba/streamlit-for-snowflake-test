import streamlit as st

# Initialize a counter in session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Button to increment the counter
if st.button('Increment'):
    st.session_state.counter += 1

# Display the counter
st.write(f'Counter: {st.session_state.counter}')
