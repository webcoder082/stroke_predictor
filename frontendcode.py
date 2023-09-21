import streamlit as st

def main():
    st.title("Stroke Prediction a product by Intro-Me")
    gender=st.text_input("Gender")
    
    age=st.text_input("Enter Age")
    hypertension=st.radio("Do you have blood pressure",["Yes","No"])
    heartproblem=st.radio("Do you have Heart problem",["Yes","No"])
    married_or_not=st.radio("Are you married",["Yes","No"])
    private_or_self_or_gov_job=st.radio("IN Which sector you are working",["GOVERNMENT","PRIVATE","SELF-EMPLOYEE"])
    urban_or_rural=st.radio("which area ypou are living",["Rural","Urban"])
    glucose_levels=st.text_input("glucose_levels")
    BMI=st.text_input("BMI")
    smoker_or_not=st.radio("Are you a smoker",["Yes","No"])
    if st.button('Predict'):
        st.success("youclicked ",{hypertension})



if __name__=='__main__':
    main()
