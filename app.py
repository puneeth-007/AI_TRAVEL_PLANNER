import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


st.markdown('<h1 style="text-align: center;">✈️AI TRAVEL PLANNER🚄</h1>', unsafe_allow_html=True)

with open(r'C:\Users\punee\OneDrive\Desktop\python\Internship\key.txt.txt') as f:
    api=f.read()

#genai.configure(api_key=os.environ["api_token"])

llm= ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp",api_key=api)
prompt_template=ChatPromptTemplate.from_messages([('system','''
You are an AI travel planner that takes source and destination and provides the detailed travel plan'''),('human','{prompt}')])

chain=prompt_template | llm

source=st.text_input('Enter the source location',key='source')

destination=st.text_input('Enter the destination location',key='destination')

st.write(source)
st.write(destination)

user='I am travelling from '+source+ 'to '+destination+' provide me travel plan with cost, time and if possible different modes of travel available with detailed table as well'

if st.button('Submit'):
    input={'prompt':prompt}
    st.write(source)
    st.write(destination)
    #response=chain.invoke(input)

    #content=response.content

    #st.markdown(content)


