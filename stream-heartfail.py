import pickle
import streamlit as st

heart_model = pickle.load(open('heartfail-model3.sav', 'rb'))

st.title('Prediksi Gagal Jantung Dengan Support Vector Machine')

age = st.text_input('Masukan Umur')
anaemia = st.text_input('Apakah anda memiliki Anemia ? (0=tidak,1=ya)')
creatinine_phosphokinase = st.text_input('Masukan level CPK darah')
diabetes = st.text_input('Apakah anda memiliki Diabetes ? (0=tidak, 1=ya)')
ejection_fraction = st.text_input('Masukan presentasi ejaction fraction')
high_blood_pressure = st.text_input(
    'Apakah anda memiliki tekanan darah tinggi ? (0=tidak, 1=ya)')
platelets = st.text_input('Masukan jumlah Platelets')
serum_creatinine = st.text_input('Masukan level serum creatinine')
serum_sodium = st.text_input('Masukan level serum sodium')
sex = st.text_input('Masukan jenis kelamin (0=wanita, 1=pria)')
smoking = st.text_input('Apakah anda perokok ? (0=tidak, 1=ya)')
time = st.text_input('Follow-up period')

heartfail_diag = ' '

if st.button('Prediksi SEKARANG'):
    heartfail_pred = heart_model.predict([[age, anaemia, creatinine_phosphokinase, diabetes,
                                         ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])
    if(heartfail_pred == 0):
        heartfail_diag = 'Pasien Tidak Beresiko Gagal Jantung'
        st.success(heartfail_diag)
    else:
        heartfail_diag = 'Pasien Beresiko Gagal Jantung'
        st.warning(heartfail_diag)
