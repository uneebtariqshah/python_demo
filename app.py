import streamlit as st

# Chatbot logic
def get_response(user_input):
    user_input = user_input.lower()

    if "course" in user_input:
        return "We offer BCA, BBA, B.Tech, MBA."
    elif "admission" in user_input:
        return "Admission is based on merit."
    elif "fee" in user_input:
        return "Fees range from 50k to 1.5 lakh."
    elif "location" in user_input:
        return "We are located in Srinagar."
    elif "contact" in user_input:
        return "Call us at 9876543210."
    else:
        return "Sorry, I didn't understand."

# Streamlit UI
st.set_page_config(page_title="College Chatbot")

st.title("🎓 College Chatbot")
st.write("Ask me about courses, fees, admission, etc.")

# Session state to store chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        response = get_response(user_input)

        # Save chat
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display chat
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")