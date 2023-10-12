import streamlit as st
import pandas as pd
import time

# streamlit run test_streamlit.py


# title
st.title('new project')

# header

st.header('header')

# sub header
st.subheader('sub header')

# write : -  to write any word
st.write('this is noraml text')

#markdown
st.markdown("""
# ratan
## ratan kumar jha
- ratan
- kumar
- jha

""")


# code:  we can also  display code

st.code("""
def foo(input):
        return foo**2
x=foo(2)
""")

#dataframe

df=pd.DataFrame({

    'name':['nitish','ankit','anupam'],
    'marks':[50,60,70],
    'package':[10,20,30]
})

st.dataframe(df)


#metrics

st.metric('revenue','rs 3L','3%')
st.metric('revenue','rs 10L','-10%')

#json
st.json({

    'name':['nitish','ankit','anupam'],
    'marks':[50,60,70],
    'package':[10,20,30]
})


#displaying video/image
st.image('Électricité_de_France.svg.png')
#st.video('')


#creating layout

st.sidebar.title('sidebar ka title')

st.sidebar.image('Électricité_de_France.svg.png')


# column:  this help in arrange content side by side

col1,col2 = st.columns(2)

with col1:
    st.image('Électricité_de_France.svg.png')

with col2:
    st.image('Électricité_de_France.svg.png')



# error msg

st.error('login failed')
st.success('success msg')
st.info('information blue')
st.warning('warning')


# progess bar

bar=st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)



# how to take user input

email=st.text_input('enter email')

#number input
number=st.number_input('enter your age')

#date input
st.date_input('enter regis date')


# button

email_id =st.text_input('enter email_id ')

password=st.text_input('enter password')




# dropdown

gender= st.selectbox('select gender',['male','female','other'])



btn = st.button('login')
# this will work with button
if btn:
    if email_id=='imratankj@gmail.com' and password=='1234':
        st.success('login successful')
        st.write(gender)
    else:
        st.error('login failed')



#file uploader

file = st.file_uploader('upload a csv file')

if file is not None:
    df=pd.read_excel(file)
    st.dataframe(df.describe())




