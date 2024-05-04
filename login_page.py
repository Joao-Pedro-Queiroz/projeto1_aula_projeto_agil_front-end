import streamlit as st

def main():
    menu = ["Home", "Login", "Cadastro"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            st.sidebar.success("Logged In as {}".format(username))
    elif choice == "Cadastro":
        st.subheader("Create New Account")
        new_username = st.text_input("User Name")
        new_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if new_password == confirm_password:
            st.success("Password Confirmed")
        else:
            st.warning("Passwords not the same")
        if st.button("Create Account"):
            st.success("Account Created")

if __name__ == "__main__":
    main()