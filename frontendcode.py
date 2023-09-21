import streamlit as st

def main():
    st.title("Stroke Prediction a product by Intro-Me")
    gender=st.text_input("Gender")
    
    age=st.text_input("age")
    hypertension=st.text_input("Hypertension")
    heartproblem=st.text_input("heartproblem")
    married_or_not=st.text_input("married_or_not")
    private_or_self_or_gov_job=st.text_input("private_or_self_or_gov _job")
    urban_or_rural=st.text_input("urban_or_rural")
    glucose_levels=st.text_input("glucose_levels")
    BMI=st.text_input("BMI")
    smoker_or_not=st.text_input("smoker_or_not")
    if st.button('Predict'):
        st.success("youclicked ")



if __name__=='__main__':
    main()
