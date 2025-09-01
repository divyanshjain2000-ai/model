import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('linear_reg.sav', 'rb'))

st.title('Patient Outcome Prediction App')

# Input features
IMPLANT_USED__Y = st.number_input('IMPLANT_USED__Y', min_value=0.0)
PAST_MEDICAL_HISTORY_CODE_Diabetes2 = st.number_input('PAST_MEDICAL_HISTORY_CODE_Diabetes2', min_value=0.0)
STATE_AT_THE_TIME_OF_ARRIVAL_CONFUSED = st.number_input('STATE_AT_THE_TIME_OF_ARRIVAL_CONFUSED', min_value=0.0)
KEY_COMPLAINTS_CODE_other_tetralogy = st.number_input('KEY_COMPLAINTS_CODE_other-tertalogy', min_value=0.0)
CREATININE = st.number_input('CREATININE', min_value=0.0)
LENGTH_OF_STAY_ICU = st.number_input('LENGTH_OF_STAY_ICU', min_value=0.0)
KEY_COMPLAINTS_CODE_PM_VSD = st.number_input('KEY_COMPLAINTS_CODE_PM-VSD', min_value=0.0)
MARITAL_STATUS_UNMARRIED = st.number_input('MARITAL_STATUS_UNMARRIED', min_value=0.0)
KEY_COMPLAINTS_CODE_CAD_VSD = st.number_input('KEY_COMPLAINTS_CODE_CAD-VSD', min_value=0.0)
KEY_COMPLAINTS_CODE_CAD_DVD = st.number_input('KEY_COMPLAINTS_CODE_CAD-DVD', min_value=0.0)
PAST_MEDICAL_HISTORY_CODE_hypertension1 = st.number_input('PAST_MEDICAL_HISTORY_CODE_hypertension1', min_value=0.0)
TOTAL_LENGTH_OF_STAY = st.number_input('TOTAL_LENGTH_OF_STAY', min_value=0.0)
MODE_OF_ARRIVAL_WALKED_IN = st.number_input('MODE_OF_ARRIVAL_WALKED IN', min_value=0.0)
KEY_COMPLAINTS_CODE_CAD_TVD = st.number_input('KEY_COMPLAINTS_CODE_CAD-TVD', min_value=0.0)
BP_LOW = st.number_input('BP_LOW', min_value=0.0)
BODY_WEIGHT = st.number_input('BODY_WEIGHT', min_value=0.0)
TOTAL_AMOUNT_BILLED_TO_THE_PATIENT = st.number_input('TOTAL_AMOUNT_BILLED_TO_THE_PATIENT', min_value=0.0)
COST_OF_IMPLANT = st.number_input('COST_OF_IMPLANT', min_value=0.0)
KEY_COMPLAINTS_CODE_other_general = st.number_input('KEY_COMPLAINTS_CODE_other-general', min_value=0.0)
CONCESSION = st.number_input('CONCESSION', min_value=0.0)
ACTUAL_RECEIVABLE_AMOUNT = st.number_input('ACTUAL_RECEIVABLE_AMOUNT', min_value=0.0)
HR_PULSE = st.number_input('HR_PULSE', min_value=0.0)
BODY_HEIGHT = st.number_input('BODY_HEIGHT', min_value=0.0)
BMI = st.number_input('BMI', min_value=0.0)
BP_HIGH = st.number_input('BP_HIGH', min_value=0.0)
RR = st.number_input('RR', min_value=0.0)
KEY_COMPLAINTS_CODE_CAD_SVD = st.number_input('KEY_COMPLAINTS_CODE_CAD-SVD', min_value=0.0)
UREA = st.number_input('UREA', min_value=0.0)
KEY_COMPLAINTS_CODE_OS_ASD = st.number_input('KEY_COMPLAINTS_CODE_OS-ASD', min_value=0.0)
KEY_COMPLAINTS_CODE_RHD = st.number_input('KEY_COMPLAINTS_CODE_RHD', min_value=0.0)
LENGTH_OF_STAY_WARD = st.number_input('LENGTH_OF_STAY_WARD', min_value=0.0)
HB = st.number_input('HB', min_value=0.0)
PAST_MEDICAL_HISTORY_CODE_hypertension3 = st.number_input('PAST_MEDICAL_HISTORY_CODE_hypertension3', min_value=0.0)
RECEIVABLE_BILLED_RATIO = st.number_input('RECEIVABLE_BILLED_RATIO', min_value=0.0)
PAST_MEDICAL_HISTORY_CODE_Hypertension1 = st.number_input('PAST_MEDICAL_HISTORY_CODE_Hypertension1', min_value=0.0)
PAST_MEDICAL_HISTORY_CODE_other = st.number_input('PAST_MEDICAL_HISTORY_CODE_other', min_value=0.0)
KEY_COMPLAINTS_CODE_other_respiratory = st.number_input('KEY_COMPLAINTS_CODE_other- respiratory', min_value=0.0)
GENDER_M = st.number_input('GENDER_M', min_value=0.0)
KEY_COMPLAINTS_CODE_other_heart = st.number_input('KEY_COMPLAINTS_CODE_other- heart', min_value=0.0)
MODE_OF_ARRIVAL_TRANSFERRED = st.number_input('MODE_OF_ARRIVAL_TRANSFERRED', min_value=0.0)
PAST_MEDICAL_HISTORY_CODE_hypertension2 = st.number_input('PAST_MEDICAL_HISTORY_CODE_hypertension2', min_value=0.0)
TYPE_OF_ADMSN_EMERGENCY = st.number_input('TYPE_OF_ADMSN_EMERGENCY', min_value=0.0)
KEY_COMPLAINTS_CODE_other_nervous = st.number_input('KEY_COMPLAINTS_CODE_other-nervous', min_value=0.0)

# Make prediction
if st.button('Predict Outcome'):
    input_data = np.array([[
        IMPLANT_USED__Y,
        PAST_MEDICAL_HISTORY_CODE_Diabetes2,
        STATE_AT_THE_TIME_OF_ARRIVAL_CONFUSED,
        KEY_COMPLAINTS_CODE_other_tetralogy,
        CREATININE,
        LENGTH_OF_STAY_ICU,
        KEY_COMPLAINTS_CODE_PM_VSD,
        MARITAL_STATUS_UNMARRIED,
        KEY_COMPLAINTS_CODE_CAD_VSD,
        KEY_COMPLAINTS_CODE_CAD_DVD,
        PAST_MEDICAL_HISTORY_CODE_hypertension1,
        TOTAL_LENGTH_OF_STAY,
        MODE_OF_ARRIVAL_WALKED_IN,
        KEY_COMPLAINTS_CODE_CAD_TVD,
        BP_LOW,
        BODY_WEIGHT,
        TOTAL_AMOUNT_BILLED_TO_THE_PATIENT,
        COST_OF_IMPLANT,
        KEY_COMPLAINTS_CODE_other_general,
        CONCESSION,
        ACTUAL_RECEIVABLE_AMOUNT,
        HR_PULSE,
        BODY_HEIGHT,
        BMI,
        BP_HIGH,
        RR,
        KEY_COMPLAINTS_CODE_CAD_SVD,
        UREA,
        KEY_COMPLAINTS_CODE_OS_ASD,
        KEY_COMPLAINTS_CODE_RHD,
        LENGTH_OF_STAY_WARD,
        HB,
        PAST_MEDICAL_HISTORY_CODE_hypertension3,
        RECEIVABLE_BILLED_RATIO,
        PAST_MEDICAL_HISTORY_CODE_Hypertension1,
        PAST_MEDICAL_HISTORY_CODE_other,
        KEY_COMPLAINTS_CODE_other_respiratory,
        GENDER_M,
        KEY_COMPLAINTS_CODE_other_heart,
        MODE_OF_ARRIVAL_TRANSFERRED,
        PAST_MEDICAL_HISTORY_CODE_hypertension2,
        TYPE_OF_ADMSN_EMERGENCY,
        KEY_COMPLAINTS_CODE_other_nervous
    ]])
    prediction = model.predict(input_data)
    st.success(f'Predicted Outcome: {prediction:.2f}')
