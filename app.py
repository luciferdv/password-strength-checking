import streamlit as st
import pickle 

st.title('password strength checking')
model=pickle.load(open('model.pkl','rb'))

col=st.columns
password=col.number_input('Enter password')

if st.button('predict'):
    data=[[password]]
    result=model.predict(data)[0]
    st.success(result)