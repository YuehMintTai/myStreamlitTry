import streamlit as st 
from faker import Faker
fake=Faker('zh-TW')
st.title(fake.sentence(20))
st.header(fake.sentence(5))
st.text(fake.sentence(50))
st.write(fake.sentences(10))
st.divider()
st.text(fake.name())