import streamlit as st

# Sidebar navigation
st.sidebar.title("Test My Mind 🧠")
option = st.sidebar.radio("Choose a tool", ["Home", "Resume Maker", "Interview Bot", "Career Finder", "Top Courses"])

# Navigation Logic
if option == "Home":
    st.title("Welcome to Test My Mind!")
    st.write("Your one-stop solution for career guidance, resume building, mock interviews, and more.")
    st.image("assets/home_banner.png")

elif option == "Resume Maker":
    import resume
    resume.run()

elif option == "Interview Bot":
    import interview
    interview.run()

elif option == "Career Finder":
    import career_finder
    career_finder.run()

elif option == "Top Courses":
    import course_recommendation
    course_recommendation.run()

 



