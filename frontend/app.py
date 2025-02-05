import streamlit as st
import requests


API_URL="hugging_face"

st.title("Tweet Sentiment Analysis")

user_input =  st.text_area("Enter a tweet:")

if st.button("Analyze Sentiment"):
    if user_input:
    response = requests.post(API_URL, json={"text":user_input})
    
    if response.status_code == 200:
        result = response.json()
        st.write(f"Sentiment: **{result['sentiment']}**")
        st.write(f"Confidence: **{result['confidence']:.2f}**")

        #visualization
        if result['sentiment'] == "Positive":
            st.success("This tweet has a positive sentiment!")
        else:
            st.error("This tweet has a negative sentiment.")

    else:
        st.error("Error in processing request")
else:
    st.warning("Please enter a tweet to analyze.")

    