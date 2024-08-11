import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Replace 'file.pkl' with the path to your pickle file
with open('/home/ubuntu/Diabetics_prediction/diabetes.pkl', 'rb') as file:
    data = pickle.load(file)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

page_icon = r"C:\Users\shank\Desktop\Diabetics\diabe.png"
    
st.set_page_config(
    page_title="DIABETES PREDICTION",
   page_icon= get_base64_of_bin_file(page_icon)
)

st.markdown("""
<style>
h1 {
    color: red; /* Change to your desired color */
}
""", unsafe_allow_html=True)



def main():
    option = st.sidebar.radio("Options",["Home","App Page"])
    if option == "Home":
        st.title("About Diabetics")
    
        st.write("""
        Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. 
        Glucose is your body’s main source of energy. Your body can make glucose, but glucose also comes from the food you eat.
        Insulin is a hormone made by the pancreas that helps glucose get into your cells to be used for energy. 
        If you have diabetes, your body doesn’t make enough—or any—insulin, or doesn’t use insulin properly. 
        Glucose then stays in your blood and doesn’t reach your cells.
        Diabetes raises the risk for damage to the eyes, kidneys, nerves, and heart. 
        Diabetes is also linked to some types of cancer. Taking steps to prevent or manage diabetes may lower your risk of developing diabetes health problems.
""")
        st.image(r"C:\Users\shank\Desktop\istockphoto-913172026-612x612.jpg")
        st.header("Signs-and-Symptoms")
        st.image(r"C:\Users\shank\Desktop\Signs-and-Symptoms-of-Diabetes.jpg")
        st.header("Treatments")
        st.write("Diabetes treatments can include lifestyle changes, medications, and other options:")
        st.write(""" 
        Lifestyle changes
                 
        These can include:
                 
        Healthy eating: Eat more fruits and vegetables, and reduce sugar, salt, white grains, and processed foods. Choose water over sugary drinks.
        Exercise: Exercise can help you lose weight and lower your blood sugar.
        Sleep: Get enough sleep.
        Stress management: Manage stress.
        
        Medications
                 
        These can include:
                 
        Insulin: People with type 1 diabetes need insulin injections to survive. People with type 2 diabetes may need insulin if lifestyle changes and other treatments don't control their blood sugar well enough. Insulin can also be used for a short time, such as when you're pregnant or ill, or to bring your blood sugar down when you're first diagnosed.
        Other medications: These can include metformin, sulfonylureas, sodium-glucose co-transporters type 2 (SGLT-2) inhibitors, and dipeptidyl peptidase-4 inhibitors. Your doctor or diabetes specialist can recommend the best type of insulin treatment or other medications for you.

        Other options
                 
        These can include:
                 
        Blood sugar monitoring: Depending on your treatment plan, you may need to check and record your blood sugar as many as four times a day or more often if you're taking insulin.
        Transplantation
        Bariatric surgery
""")

    else:
        st.title("Diabetics Prediction")

        gender = st.selectbox("Gender",["Select Gender"]+["Male","Female","Other"])
        age = st.text_input("Age")
        hyp_ten =st.selectbox("Hyper Tension",["Choose Option"]+["Yes","No"])
        heart_dis = st.selectbox("Heart Disease",["Choose Option"] +["Yes","No"])
        smok_hist = st.selectbox("Smoking History",["Choose Option"] +["Never","No Info","Current","Former","Ever","Not current"])
        bmi = st.text_input("BMI")
        hba1c = st.text_input("HbA1C Level")
        glu_level = st.text_input("Blood Glucose Level")

        details = []
        details1 = []

        if gender != "Select Gender":

            if gender == "Female":
                gender = 0
            elif gender == "Male":
                gender = 1
            elif gender == "Other":
                gender = 2
        else:
            st.warning("Please choose your gender")

        if hyp_ten != "Choose Option":

            if hyp_ten  == "Yes":
                hyp_ten =1
            if hyp_ten  == "No":
                hyp_ten =0
        else:
            st.warning("Please choose yes if have hyper tension else no")

        if heart_dis != "Choose Option":    
            if heart_dis  == "Yes":
                heart_dis =1
            if heart_dis  == "No":
                heart_dis =0
        else:
            st.warning("Please choose yes if have heart disease else no")

        if smok_hist != "Choose Option":
            if smok_hist == "Never":
                smok_hist = 4
            if smok_hist == "No Info":
                smok_hist = 0
            if smok_hist == "Current":
                smok_hist = 1
            if smok_hist == "Former":
                smok_hist = 3
            if smok_hist == "Ever":
                smok_hist = 2
            if smok_hist == "Not current":
                smok_hist = 5
        else:
            st.warning("Please choose smoking history")

        details1.append(gender)
        if age:
            details1.append(int(age))
        else:
            pass

        details1.append(hyp_ten)
        details1.append(heart_dis)
        details1.append(smok_hist)
        if bmi:
            details1.append(float(bmi))
        else:
            pass

        if hba1c:
            details1.append(float(hba1c))
        else:
            pass

        if glu_level:
            details1.append(float(glu_level))
        else:
            pass       
        
        details.append(details1)

        if st.button("Submit"):
            prediction = data.predict(details)
            prediction =int(prediction)
            if prediction == 0:
                st.success("Hurray! You dont have diabetics :)")
                st.balloons()
            else:
                st.success("Oops! You have diabetics :(")
                st.success("Take Care of your health")


        



        

if __name__ == "__main__":
    main()
