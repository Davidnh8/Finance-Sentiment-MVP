import streamlit as st
import os

# ------------- PAGE CONFIG & BASIC STYLING -------------
st.set_page_config(page_title="AI War Room - Finance Sentiment", layout="wide")

# Optional: Hide the Streamlit menu & footer for a cleaner look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    </style>
""", unsafe_allow_html=True)

# ------------- TITLE & INTRO SECTION -------------
st.title("AI War Room: Finance Sentiment Analysis")

st.markdown("""
Welcome to the **AI War Room** — where four advisor agents 
(**Optimist**, **Pessimist**, **Neutral**, and **Degen**) analyze
social media sentiment on a selected stock. 

**Select a ticker below**, click **Analyze**, then **chat** with each 
agent for their perspective, and finally, see the **consensus**.
""")

# ------------- TICKER SELECTION & ANALYSIS -------------
tickers = ["Tesla", "Nvidia"]
selected_ticker = st.selectbox("Choose Ticker:", options=tickers, index=0)
analyze_button = st.button("Analyze Sentiment")

# Mock data for social sentiment based on selected ticker
mock_data_map = {
    "Tesla": "TSLA is on fire! Everyone says it's going to the moon.",
    "Nvidia": "NVDA just reported record earnings, but some say it's overpriced."
}
mock_social_text = mock_data_map[selected_ticker]

# ------------- MOCK SENTIMENT ANALYSIS LOGIC -------------
def mock_sentiment_analysis(text):
    text_lower = text.lower()
    if "moon" in text_lower or "fire" in text_lower or "record" in text_lower:
        return {"sentiment": "Positive", "score": 0.8}
    elif "overpriced" in text_lower or "bad" in text_lower or "drops" in text_lower:
        return {"sentiment": "Negative", "score": -0.6}
    else:
        return {"sentiment": "Neutral", "score": 0.0}

if "analysis_result" not in st.session_state:
    st.session_state["analysis_result"] = None

if analyze_button:
    st.session_state["analysis_result"] = mock_sentiment_analysis(mock_social_text)

# ------------- AGENT LOGIC -------------
def get_agent_response(agent, user_message, sentiment_result):
    responses = {
        "Optimist": f"Optimist sees {sentiment_result['sentiment']} sentiment. Cheer up! This could be a rocket ride!",
        "Pessimist": f"Pessimist sees {sentiment_result['sentiment']} sentiment. Careful... storm clouds could be on the horizon.",
        "Neutral": f"Neutral sees a balanced view. With sentiment {sentiment_result['sentiment']}, we should weigh both sides carefully.",
        "Degen": f"Degen says YOLO! Who cares about {sentiment_result['sentiment']}? We're going ALL IN regardless!"
    }
    return responses.get(agent, "I have no comment.")

# ------------- AGENT IMAGES SETUP -------------
agent_names = ["Optimist", "Pessimist", "Neutral", "Degen"]
image_directory = "images/"  # Make sure the images are in this directory

agent_images = {agent: os.path.join(image_directory, f"{agent.lower()}.jpg") for agent in agent_names}

# ------------- TOP AGENTS DISPLAY -------------
st.markdown("---")
st.subheader("Agents")

if "active_agent" not in st.session_state:
    st.session_state.active_agent = None

for agent in agent_names:
    if f"{agent}_chat" not in st.session_state:
        st.session_state[f"{agent}_chat"] = []

cols = st.columns(4)
for i, agent in enumerate(agent_names):
    with cols[i]:
        if os.path.exists(agent_images[agent]):
            st.image(agent_images[agent], width=100)
        else:
            st.write(f"⚠️ Missing {agent} image")
        
        if st.button(agent, key=f"select_{agent}"):
            st.session_state.active_agent = agent

# ------------- CHAT WITH ACTIVE AGENT -------------
if st.session_state.active_agent:
    st.markdown(f"### Chat with {st.session_state.active_agent}")

    for msg in st.session_state[f"{st.session_state.active_agent}_chat"]:
        st.write(msg)

    user_input = st.text_input(f"Your question or comment to {st.session_state.active_agent}:")

    if st.button("Send", key="send_message"):
        if user_input.strip():
            st.session_state[f"{st.session_state.active_agent}_chat"].append(f"**You**: {user_input}")

            if st.session_state["analysis_result"]:
                agent_sentiment = st.session_state["analysis_result"]
            else:
                agent_sentiment = {"sentiment": "Unknown", "score": 0}

            bot_reply = get_agent_response(st.session_state.active_agent, user_input, agent_sentiment)
            st.session_state[f"{st.session_state.active_agent}_chat"].append(f"**{st.session_state.active_agent}**: {bot_reply}")

# ------------- CONSENSUS SECTION -------------
st.markdown("---")
st.subheader("Final Consensus")

if st.session_state.get("analysis_result"):
    sentiment_label = st.session_state["analysis_result"]["sentiment"]
    sentiment_score = st.session_state["analysis_result"]["score"]

    if sentiment_score > 0.3:
        consensus = "Bullish"
    elif sentiment_score < -0.3:
        consensus = "Bearish"
    else:
        consensus = "Neutral"

    st.markdown(
        f"The War Room's combined view on {selected_ticker} is: **{consensus}** "
        f"(underlying social sentiment detected as {sentiment_label})."
    )
else:
    st.info("Run the **Analyze** step above to get a sentiment reading and see a final consensus.")
