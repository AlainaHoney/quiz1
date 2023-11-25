import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Function to generate n-grams from a text
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

# Streamlit web interface
def main():
    st.title("N-gram Generator")

    # User input for text passage
    text = st.text_area("Enter your text passage:")

    # User input for n-gram order
    n_value = st.slider("Select the order of n-gram:", 2, 5, 2)

    # Submit button
    if st.button("Submit"):
        if text:
            st.subheader(f"{n_value}-grams:")
            n_grams = generate_ngrams(text, n_value)
            st.write(n_grams)
        else:
            st.warning("Please enter a text passage.")

if __name__ == "__main__":
    main()
