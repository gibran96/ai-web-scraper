import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scraper")

url = st.text_input("Enter a website URL: ")

if st.button("Scrape"):
    st.write("Scraping...")
    result = scrape_website(url)
    st.write("Done!")
    body_content = extract_body_content(result)
    clean_body_content = clean_body_content(body_content)
    
    st.session_state.dom_content = clean_body_content
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", clean_body_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("What information do you need?")
    if st.button("Parse"):
        if parse_description:
            st.write("Parsing the content")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)