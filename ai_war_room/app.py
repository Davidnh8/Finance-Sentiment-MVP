import streamlit as st
import os

# --------------------- PAGE CONFIG & STYLING ---------------------
st.set_page_config(page_title="AI War Room - Finance Sentiment", layout="wide")

# Hide Streamlit's default menu and footer; add extra bottom padding and spacing styling
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Adjust main container padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;  /* Added bottom padding */
    }

    /* Increase font size for agent headings */
    .agent-heading {
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Extra spacing between sections */
    .section-spacing {
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------- RAW TWITTER DATA ---------------------
raw_twitter_data = """
What's Next? - $NVDA Stock Price Prediction - NVDA Stock Analysis | NVIDIA Stock  
https://youtube.com/watch?v=EWt6B0ONj98  
Chekku  
@ImChekku  
·  
2m  
These are BlackRock's Top 9 largest Stock Investments.  

1. 🇺🇸 Apple: $255B  
2. 🇺🇸 Microsoft: $242B  
3. 🇺🇸 Nvidia: $224B  
4. 🇺🇸 Amazon: $124B  
5. 🇺🇸 Meta Platforms: $93B  
6. 🇺🇸 Alphabet Class A: $71B  
7. 🇺🇸 Broadcom: $61B   
8. 🇺🇸 Alphabet Class C: $60B  
9. 🇺🇸 Eli Lilly: $57B  
Show more  
📊 Stock Master  
@codemaster70  
·  
4m  
The Stock Market Weathered Nvidia’s Plunge. It Couldn’t Withstand Renewed Tariff Threats. - Barron's $NVDA  

#️⃣ #usd #stocks #investing  
From betonmarket.it  

My nvidia stock. 😭😭😭  
pope🌐  
@Pope_Eseka  
·  
7m  
Will $TSLA $GM $F $CVX $XO. $NVIDIA $AAPL $BTC stock go down next week ?  

Canada and Mexico hit back after Trump signs order for punishing tariffs  

Read more on http://vapadefinancial.com  
Jubean 🇸🇬🇺🇸  
@bp_raju  
·  
9m  
Replying to   
@chamath  
And Nvidia stock rose on the back of those sales. So are you saying Nvidia needs to give up that market?  
Just wait for investigation to be over and actually see if any laws were broken. Nvidia already made a public statement that it does not see any illegal activity.  

EMcDonald  
@e2341m_e  
·  
13m  
Nvidia CEO Huang Heads to White House After Wild Week for Chipmaker's Stock  https://investopedia.com/nvidia-ceo-huang-heads-to-white-house-after-wild-week-for-chipmaker-stock-8783857?utm_source=social2&utm_medium=social&utm_campaign=shareurlbuttons via   
@investopedia  
investopedia.com  
Nvidia CEO Huang Heads to White House After Wild Week for Chipmaker's Stock  
Nvidia CEO Jensen Huang is set to meet with President Donald Trump at the White House Friday, after a wild week for the chipmaker's stock.  

tae kim  
@firstadopter  
·  
23m  
My CNBC appearance has already garnered 120,000 views across social media and was featured on Nvidia's Apple News stock page.​​​​​​​​​​​​​​​  

Viewers may appreciate serious, deeply researched, factual insight versus superficial opinions of less substance.​​​​​​​​​​​​​​​ Crazy  

Quote  
tae kim  
@firstadopter  
·  
Jan 31  
Nvidia's future in focus after DeepSeek earthquake. What it all means. Thank you @CNBC @KellyCNBC @dee_bosa for having me on  

What Does Chinese AI Start-Up DeepSeek Mean for Nvidia Stock? https://msn.com/en-us/money/companies/what-does-chinese-ai-start-up-deepseek-mean-for-nvidia-stock/ar-AA1ye4Cg?cvid=931c0c2d5bcc4c56bfc6af27610c4048&ocid=sappioshp  

Emel Alyanak  
@AlyanakEme73701  
·  
41m  
Nvidia stock plunges, Bitcoin dips, and Trump Media surges: Markets news roundup  
blondellonline.com  
Nvidia stock plunges, Bitcoin dips, and Trump Media surges: Markets news roundup - In-Depth...  
Federal Reserve Chair Jerome Powell.Photo: Al Drago/Bloomberg (Getty Images)  

JC  
@Statefan1219  
·  
43m  
Replying to  
@sundarpichai  
@nvidia  
and  
@googlecloud  
This is awesome - great way to tank  
@Nvida  
stock.  
@Banana3Stocks  
@jimcramer  
I think they all went to deepseek and this a lie.  

Sathyarajan B  
@INovaBeing  
·  
1h  
DeepSeek AI just caused shockwaves in the stock market—some companies soared while others crumbled. Who came out on top?  

With Nvidia and Meta caught in the upheaval, AI’s market influence is undeniable. Investors are watching closely—where’s the smart money going next?  

Are you  
Show more  

Harry Grant  
@harryrgrant  
·  
1h  
Why this 50-year old restaurant chain has a stock that's smoking Nvidia's  
From share.gainfully.com  

DewmBoom  
@dewmboom  
·  
1h  
Can Meta’s Massive Manhattan-Sized Data Center Take Nvidia Stock T  
New Record Highs? $NVDA  
From barchart.com  

Trevor McLeod  
@tabmcleod  
·  
1h  
Is this what sparked the selloff of #nvidia stock earlier this week?  
#artificial_intelligence #ai #GPU  
#stocks  
From marketwatch.com  

Drmikemyers  
@drmikemyers  
·  
1h  
Can Meta's Massive Manhattan-Sized Data Center Take Nvidia Stock to New Record Highs?  
theglobeandmail.com  
Can Meta’s Massive Manhattan-Sized Data Center Take Nvidia Stock to New Record Highs?  
Detailed price information for Amazon.com Inc (AMZN-Q) from The Globe and Mail including charting and trades.  

Pure Tech News 🚀📱 🖥️ 🎮  
@Pur3Tech  
·  
1h  
One Blogger Helped Spark NVIDIA's $600B Stock Collapse #Technology  
From puretech.news  

FIRED Up Wealth  
@FIREDUpWealth  
·  
1h  
Replying to  
@GermanDaphne  
and  
@StockMKTNewz  
This breaks it down  
Did DeepSeek AI Just Dethrone Nvidia $NVDA Stock?  
They're developing their own GPUs as China nears parity with Nvidia.  
That might have an effect like oh maybe collapsing a stock.  
Smh  

Chris O.  
@crowd_of_one  
·  
2h  
Replying to  
@crowd_of_one  
@bnk2nde  
and  
@Abiodun0x  
Found an article that explains the DeepSeek innovation with better clarity.  
Towards the end is this explainer on the Nvidia stock price falls.  
https://youtubetranscriptoptimizer.com/blog/05_the_short_case_for_nvda  

Markets Today  
@marketsday  
·  
2h  
Biggest Companies by Market Cap (2024) 🚀  
These stock market giants are leading the way with trillion-dollar valuations! 💰  
💡Top 5 Companies:  
🍏 Apple ( $AAPL ) – $3.59T+  
🖥  Microsoft ( $MSFT ) – $3.11T+  
🎮 Nvidia ( $NVDA ) – $3.05T+  
📦 Amazon ( $AMZN ) – $2.52T+  
🔍 Alphabet  
Show more  

Loretta Renz  
@LorettaRen76196  
·  
2h  
Replying to  
@VivekNewsX  
Yes, her husband just did it again with Nvidia stock and made a boatload. When will this be put to an end? If the average person did this we would be put in jail immediately.  

flow_float  
@FLOwing_124  
·  
2h  
DeepSeek AI-powered chatbot app has quickly overtook OpenAI's ChatGPT as the most-downloaded free iOS app in the US, and caused chip-making company Nvidia to lose almost $600bn (£483bn) of its market value in one day – a new US stock market record.  
From bbc.com  

Sigma77 ⛳  
@SigmaAquarius  
·  
2h  
Replying to  
@TrendSpider  
$NVDA stock's like a plot twist in a movie - you think it's down for the count, then BAM! It's back with a vengeance, proving once again that in the AI world, Nvidia's the hero we didn't know we needed. Here's to betting on AI's favorite chip champ! $DELL  
. Yep, was pretty happy to find mine at MRSP D1 back then.  
But here clearly no stock, kind of a mess from Nvidia. Like 250 for every distributor in the US for the 5090, etc.  
It's all the influencers that got the cards 😂  

G. Ichtertz  
@g_ichtertz  
·  
2h  
The Stock Market Weathered Nvidia’s Plunge. It Couldn’t Withstand Renewed Tariff Threats.  
From barrons.com  

Jason Birch  
@JasonBirch0916  
·  
2h  
Nvidia Stock May Fall As DeepSeek’s ‘Amazing’ AI Model Disrupts OpenAI - Forbes  
From apple.news  

Proxenos  
@Proxenos_zh  
·  
2h  
Replying to  
@malleshwarm1  
and  
@KyleTrainEmoji  
America does cook the data: its economic performance is largely fluff. A trillion was just shaved off the stock exchange earlier this week is a perfect example: NVIDIA and other tech valuations are bullshit.  

Furqi  
@Mr____Dreamer  
·  
2h  
Nvidia stock is ruining my portfolio. Gone down 19% since I bought it. You never know what and when a crash happens.  

ToolMan  
@jonathantoole91  
·  
2h  
Replying to  
@NVIDIAGeForce  
#GeForceRTX50  
I really don't even care about winning a 5090, I just want to be able to buy the damn thing.  
@nvidia  
Why tf would you only release 300 5090 founders edition GPUs the whole world is trying to buy. Go look at your stock, ya'll need to rethink some things...  

FryAI  
@TheFryAI  
·  
2h  
➡️ A single blogger has played a significant role in triggering NVIDIA's $600 billion stock decline, leading to panic in Silicon Valley.  
One Blogger Helped Spark NVIDIA's $600B Stock Collapse  
hardware.slashdot.org  
One Blogger Helped Spark NVIDIA's $600B Stock Collapse - Slashdot  
On January 24th Brooklyn blogger Jeffrey Emanuel made the case for shorting NVIDIA, remembers MarketWatch, "due to a number of shifting tides in the AI world, including the emergence of a China-based...  

Slashdot  
@slashdot  
·  
2h  
One Blogger Helped Spark NVIDIA's $600B Stock Collapse  
hardware.slashdot.org  
One Blogger Helped Spark NVIDIA's $600B Stock Collapse - Slashdot  
On January 24th Brooklyn blogger Jeffrey Emanuel made the case for shorting NVIDIA, remembers MarketWatch, "due to a number of shifting tides in the AI world, including the emergence of a China-based...  

sera 🚬🐈🏳️‍⚧️  
@WRTHLESSANIMAL  
·  
2h  
Replying to  
@_TheGreatAce_  
nah there’s not a lot of hardware allocated to this region, Nvidia simply doesn't gaf about this place. I'm talking strictly 5080s though I've no idea how stock for 5090 was  

Slashdot Media  
@SlashdotMedia  
·  
2h  
One Blogger Helped Spark NVIDIA's $600B Stock Collapse  
hardware.slashdot.org  
One Blogger Helped Spark NVIDIA's $600B Stock Collapse - Slashdot  
On January 24th Brooklyn blogger Jeffrey Emanuel made the case for shorting NVIDIA, remembers MarketWatch, "due to a number of shifting tides in the AI world, including the emergence of a China-based...  

柳青  
@liuqing178  
·  
2h  
The Short Case for Nvidia Stock
"""

# --------------------- TITLE & INTRO SECTION ---------------------
st.title("AI War Room: Finance Sentiment Analysis")

st.markdown("""
Welcome to the **AI War Room** — where four advisor agents 
(**Optimist**, **Pessimist**, **Neutral**, and **Degen**) 
analyze social media sentiment on a selected stock.
""")

# --------------------- TICKER SELECTION (SINGLE) ---------------------
tickers = ["Nvidia"]
selected_ticker = st.selectbox("Choose Ticker:", options=tickers, index=0)

# --------------------- TWITTER DATA DISPLAY (SCROLLABLE BOX) ---------------------
st.subheader("TWITTER (Last 2 hours)")
st.markdown(
    f"""
    <div style="border:1px solid #ccc; background-color:#000000; padding:1rem; max-height:400px; overflow-y:auto; color:#ffffff;">
      {raw_twitter_data.replace('\n', '<br>')}
    </div>
    """,
    unsafe_allow_html=True
)

# Add extra spacing between Twitter and News Articles
st.markdown("<br>", unsafe_allow_html=True)

# --------------------- PLACEHOLDER FOR OTHER PLATFORMS (WEBSITES) ---------------------
st.subheader("News Articles")
st.info("No data available for articles yet.")

# --------------------- MOCK SENTIMENT ANALYSIS ---------------------
def mock_sentiment_analysis(text):
    text_lower = text.lower()
    if "moon" in text_lower or "fire" in text_lower or "record" in text_lower:
        return {"sentiment": "Positive", "score": 0.8}
    elif "overpriced" in text_lower or "bad" in text_lower or "drops" in text_lower:
        return {"sentiment": "Negative", "score": -0.6}
    else:
        return {"sentiment": "Neutral", "score": 0.0}

# For demonstration, we use a short snippet from the data:
mock_text_for_analysis = "NVDA just reported record earnings, but some say it's overpriced."
analysis_result = mock_sentiment_analysis(mock_text_for_analysis)

# --------------------- AGENT RESPONSES ---------------------
agent_responses = {
    "Optimist": (
        "“Despite chatter about potential competition and headlines of a ‘$600B collapse,’ "
        "Nvidia remains a cornerstone in AI. Temporary dips are opportunities—especially given dominance in GPUs. "
        "Short-term volatility won’t overshadow the long-term growth story.”"
    ),
    "Pessimist": (
        "“Nvidia’s stock soared on AI hype, but negative headlines—competition, tariffs, and high valuations—suggest serious headwinds. "
        "Moreover, DeepSeek’s promise of operating with reduced computing power, combined with excessive volatility in the space, "
        "could undermine Nvidia’s market share. It’s better to remain cautious until these uncertainties are resolved.”"
    ),
    "Neutral": (
        "“While Nvidia has strong fundamentals and leads in the GPU market, rumors of new rivals and macro uncertainties are real. "
        "A balanced approach is prudent: neither chase the hype nor panic-sell on rumors without thorough research.”"
    ),
    "Degen": (
        "“I see immense opportunities in the volatility if you take calculated risks. Instead of making reckless bets, consider agile, tactical plays that adapt quickly to market signals and innovation trends—including developments like DeepSeek’s approach. "
        "Focus on dynamic strategies that capitalize on rapid price swings and market inefficiencies.”"
    ),
}

# --------------------- AGENTS DISPLAY ---------------------
st.markdown("---")
st.subheader("Agents' Views on Nvidia")

agent_names = ["Optimist", "Pessimist", "Neutral", "Degen"]
image_directory = "images/"

# Attempt to load agent images from local folder
agent_images = {
    agent: os.path.join(image_directory, f"{agent.lower()}.jpg")
    for agent in agent_names
}
agent_emojis = {
    "Optimist": "☀️",
    "Pessimist": "🌧️",
    "Neutral": "⚖️",
    "Degen": "🎲"
}

cols = st.columns(4)
for i, agent in enumerate(agent_names):
    with cols[i]:
        if os.path.exists(agent_images[agent]):
            # Slightly bigger image
            st.image(agent_images[agent], width=240)
        else:
            st.write(f"⚠️ Missing {agent} image")
        st.markdown(f"<div class='agent-heading'>{agent} {agent_emojis[agent]}</div>", unsafe_allow_html=True)
        st.write(agent_responses[agent])

# --------------------- FINAL CONSENSUS ---------------------
st.markdown("---")
st.subheader("Final Consensus - Slightly favors 'BUY'")

# Pre-defined scores based on each agent's view (0 = must sell, 100 = must buy)
agent_scores = {
    "Optimist": 80,
    "Pessimist": 30,
    "Neutral": 50,
    "Degen": 70,
}

final_consensus_score = round(sum(agent_scores.values()) / len(agent_scores))

# Add a commentary on how the agents debated and came to the consensus
consensus_commentary = (
    "After a detailed debate, the Optimist highlighted Nvidia's long-term growth potential, "
    "while the Pessimist warned of risks such as high volatility and reduced computing power demands from DeepSeek. "
    "The Neutral agent advised a balanced approach, and the Degen suggested tactical plays to capitalize on market inefficiencies. "
    "Taking into account all these viewpoints, they converged on a consensus score of **{score}** out of 100, "
    "where 100 indicates a 'must buy' and 0 indicates a 'must sell' signal."
).format(score=final_consensus_score)

st.markdown(
    f"After evaluating all viewpoints, the combined recommendation for **{selected_ticker}** is **{final_consensus_score}** out of 100.  \n\n{consensus_commentary}"
)
