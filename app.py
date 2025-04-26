import streamlit as st 
from faker import Faker
fake=Faker('zh-TW')
st.title(fake.sentence(20))
st.write(fake.sentences(10))
st.divider()
st.text(fake.name())