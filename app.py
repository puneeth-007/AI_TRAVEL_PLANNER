import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


st.markdown('<h1 style="text-align: center;">✈️🚗AI TRAVEL PLANNER🚄🚌</h1>', unsafe_allow_html=True)

with open(r'C:\Users\punee\OneDrive\Desktop\python\Internship\key.txt.txt') as f:
    api=f.read()

#genai.configure(api_key=os.environ["api_token"])

llm= ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp",api_key=api)
prompt_template=ChatPromptTemplate.from_messages([('system','''
You are an AI travel planner that takes source and destination and provides the detailed travel plan, when starting the message start as Travel plan from source to destination provided by user'''),('human','{prompt}')])

chain=prompt_template | llm

source=st.text_input('Enter the source location',key='source')

destination=st.text_input('Enter the destination location',key='destination')

user='I am travelling from '+source+ 'to '+destination+' provide me travel plan with cost, time and if possible different modes of travel available with detailed table as well'

if st.button('Submit'):
    input={'prompt':user}
    response=chain.invoke(input)

    content=response.content
    st.header('Travel Plan',divider='rainbow')
    st.markdown(content)


