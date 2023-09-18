import streamlit as st

def main():
    st.title('SESSION')
    for key in st.session_state:
        st.write(f"{key}----{st.session_state[key]}")

if __name__ == "__main__":
    main()