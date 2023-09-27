import streamlit as st
import pickle
model=pickle.load(open("stroke_rfmodel",'rb'))

def main():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.title("BRAIN STROKE PREDICTOR BY MANIKANTA")
    
    gender=st.radio("choose gender",["Male","Female"])
    
    age=st.text_input("Enter Age")
    hypertension=st.radio("Do you have blood pressure",["Yes","No"])
    heartproblem=st.radio("Do you have Heart problem",["Yes","No"])
    married_or_not=st.radio("Are you married",["Yes","No"])
    private_or_self_or_gov_job=st.radio("IN Which sector you are working",["GOVERNMENT","PRIVATE","SELF-EMPLOYED"])
    urban_or_rural=st.radio("which area ypou are living",["Rural","Urban"])
    glucose_levels=st.text_input("glucose_levels")
    BMI=st.text_input("BMI")
    smoker_or_not=st.radio("Are you a smoker",["SMOKING","NOT SMOKING","SMOKED IN PAST NOT NOW"])
    d1={  "Yes":1,
          "No":0,
          "Male":1,
          "Female":0,
          "PRIVATE":2,
          "SELF-EMPLOYED":3,
          "GOVERNMENT":0,
          "Rural":0,
          "Urban":1,
          "SMOKING":3,
          "NOT SMOKING":2,
          "SMOKED IN PAST NOT NOW":1




          }
    if st.button('Predict'):
        makeprediction=model.predict([[d1[gender],age,d1[hypertension],d1[heartproblem],d1[married_or_not],d1[private_or_self_or_gov_job],d1[urban_or_rural],glucose_levels,BMI,d1[smoker_or_not]]])
        if makeprediction[0]==1:
            st.warning("YOU MAY HAVE STROKE IN FUTURE IT IS JUST PREDICTION DON'T WORRY CONFIRM WITH YOUR DOCTOR")
        else:
            st.success("YOU ARE LUCKY NO STROKE IN FUTURE ACCORDING TO GIVEN DATA")
        



if __name__=='__main__':
    main()
