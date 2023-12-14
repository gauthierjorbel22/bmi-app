import streamlit as st 

def bmi_categories():
    st.title('BMI Categories')
    st.write("""
    - **Underweight**: BMI less than 18.5
    - **Healthy**: BMI between 18.5 and 24.9
    - **Overweight**: BMI between 25 and 29.9
    - **Obese**: BMI of 30 or greater
     """)