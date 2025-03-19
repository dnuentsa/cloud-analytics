import streamlit as st

# Set page config
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="👋",
)

# Main app
def main():
    st.title("Welcome to My Streamlit App! 👋")
    st.write("This is a starter template for your Streamlit application.")

    st.sidebar.header("Sidebar")
    st.sidebar.write("You can add controls here")

    # Example widgets
    if st.button("Click me!"):
        st.balloons()

    st.write("## Getting Started")
    st.write("1. Edit `streamlit_app.py` to customize this app")
    st.write("2. Add widgets using `st.` commands")
    st.write("3. Run the app using the Run button")

if __name__ == "__main__":
    main()