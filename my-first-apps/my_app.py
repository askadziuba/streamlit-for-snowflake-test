import streamlit as st
import time
st.title("My first app")

st.text("This is some text ( st.text).")
st.code("print('Hello, world!')")
st.markdown("This is a markdown text.")
st.latex(r"\LaTeX AbCdeeeeX")
st.write("This is a write text.")


# Sample JSON data
data = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}

# Display the JSON data
st.json(data)


#Create an empty placeholder
# placeholder = st.empty()

# Update the placeholder with different content
# for i in range(10):
#     placeholder.text(f"Iteration {i}")
#     time.sleep(1)

# Clear the placeholder
# placeholder.empty()


# Create a container
with st.container():
    st.write("This is inside the container")
    st.line_chart([1, 2, 3, 4])
    st.button("Click me")

# Elements outside the container
st.write("This is outside the container")

# Create an expander
with st.expander("See more details"):
    st.write("Here are some detailed information.")
    st.line_chart([1, 2, 3, 4])
    st.button("Expander Click me")

# Elements outside the expander
st.write("This is outside the expander")

tabs = st.tabs(["form", "session_with_counter"])
with tabs[0]:
    st.write("Content inside the first tab")
    # Create a form
    with st.form("my_form"):
        st.write("Inside the form")

        # Add input widgets
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=100)

        # Add a submit button
        submitted = st.form_submit_button("Submit")

    # Process the form submission
    if submitted:
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
with tabs[1]:
    st.write("Content inside the second tab")
    # Initialize a counter in session state
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    # Button to increment the counter
    if st.button('Increment'):
        st.session_state.counter += 1

    # Display the counter
    st.write(f'Counter: {st.session_state.counter}')
