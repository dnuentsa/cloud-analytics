
# Streamlit Tutorial App

A simple Streamlit app that demonstrates basic concepts and widgets.

## App Structure Explanation

Let's go through the code line by line:

```python
import streamlit as st
```
First, we import the Streamlit library which provides all the UI components and app functionality.

```python
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="👋",
)
```
This configures the browser tab title and icon. The page_icon can be an emoji or an image URL.

```python
def main():
    st.title("Welcome to My Streamlit App! 👋")
    st.write("This is a starter template for your Streamlit application.")
```
- The `main()` function is our app's entry point
- `st.title()` displays the main heading
- `st.write()` is a versatile function to display text, data, or other content

```python
    st.sidebar.header("Sidebar")
    st.sidebar.write("You can add controls here")
```
These lines demonstrate the sidebar functionality:
- `st.sidebar` creates a collapsible sidebar
- You can add any Streamlit components to the sidebar

```python
    if st.button("Click me!"):
        st.balloons()
```
This shows interactive widgets:
- `st.button()` creates a clickable button
- When clicked, it triggers the balloon animation

```python
    st.write("## Getting Started")
    st.write("1. Edit `streamlit_app.py` to customize this app")
    st.write("2. Add widgets using `st.` commands")
    st.write("3. Run the app using the Run button")
```
These lines show how to create a simple getting started guide using markdown formatting.



