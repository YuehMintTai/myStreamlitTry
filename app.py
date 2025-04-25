from faker import Faker
import streamlit as st
fake=Faker('zh-TW')
st.title(fake.sentence(20))
for i in fake.sentences(10):
    st.write(i)