import streamlit as st 
from utils.helper_functions import bmi_calculator
from pages.bmi_categories.bmi_categories_page import bmi_categories
from pages.about.about_page import about
from utils.helper_functions import bmi_calculator

st.set_page_config(page_title='BMI Application', page_icon=':heart:')

st.markdown(
    """
    <style>
    %s
    </style>
    """ % open("static/styles.css").read(), unsafe_allow_html=True
)

def main():
    page = st.sidebar.selectbox('Select a page', ['BMI Calculator', 'About', 'BMI Categories'])
    
    if page ==  'BMI Calculator':
        st.title('BMI Calculator')
        height = st.number_input('Enter your height in meters', min_value=0.1, max_value=2.5, step=0.1)
        weight = st.number_input('Enter your weight in Kilograms', min_value=1.0, max_value=300.0, step=0.1)
        
        if st.button('Calculate BMI'):
            bmi = bmi_calculator(height, weight)
            st.write(f'Your BMI is: {bmi: .2f}')
            if bmi < 18.5:
                st.warning('You are Underweight')
            elif bmi >= 18.5 and bmi < 25:
                st.success('You are Healthy')
            elif bmi >= 25 and bmi < 30:
                st.warning('You are Overweight')
            elif bmi >=30:
                st.error('You are Obese')
            else:
                st.error('Please enter valid details')
    elif page == 'About':
            about()
    elif page == 'BMI Categories':
            bmi_categories()
   
    
    # if st.button('Calculate BMI'):
    #     bmi = bmi_calculator(height, weight)
    #     st.write(f"Your BMI is: {bmi: .2f}")
        
    if st.button('Reset'):
        height = 0.0
        weight = 0.0
if __name__ == '__main__':
    main()
    
