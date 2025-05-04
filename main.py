# # import os
# # from dotenv import load_dotenv
# # from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# # #--------------------------------------agents ka setup---------------------------------------------#
# # load_dotenv()

# # set_tracing_disabled(disabled=True)

# # OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# # if not OPENROUTER_API_KEY:
# #     raise Exception("OPENROUTER_API_KEY is not set!")

# # #--------------------------------------agents ka instance---------------------------------------------#
# # client = AsyncOpenAI(
# #     api_key = OPENROUTER_API_KEY,
# #     base_url ="https://openrouter.ai/api/v1",
# # )
# # agent = Agent(
# #     model=OpenAIChatCompletionsModel(model='deepseek/deepseek-chat-v3-0324:free',openai_client=client),
# #     name='zartasha agent',
# #     instructions='you are a helpful assistant',
# # )

# # #----------------------------agents ko chalaya-------------------------------------------
# # res = Runner.run_sync(agent,"what is the capital of Pakistan?")

# # print(res.final_output)


# # app.py
# import os
# import asyncio
# from dotenv import load_dotenv
# import streamlit as st
# from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# load_dotenv()
# set_tracing_disabled(disabled=True)

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# if not OPENROUTER_API_KEY:
#     st.error("OPENROUTER_API_KEY is not set!")
#     st.stop()

# st.title("💬 Ask Zartasha Agent")
# user_input = st.text_input("Enter your question:")

# if user_input:
#     with st.spinner("Thinking..."):
#         client = AsyncOpenAI(
#             api_key=OPENROUTER_API_KEY,
#             base_url="https://openrouter.ai/api/v1",
#         )
#         agent = Agent(
#             model=OpenAIChatCompletionsModel(
#                 model='deepseek/deepseek-chat-v3-0324:free',
#                 openai_client=client
#             ),
#             name='zartasha agent',
#             instructions='you are a helpful assistant',
#         )

#         # Use asyncio.run instead of run_sync
#         response = asyncio.run(Runner.run(agent, user_input))
#         st.success(response.final_output)

import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# Load environment variables
load_dotenv()

# Support both local and deployment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or st.secrets.get("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    st.error("❌ OPENROUTER_API_KEY is missing. Please check your .env or Streamlit secrets.")
    st.stop()

# Disable tracing (optional)
set_tracing_disabled(disabled=True)

# Setup OpenRouter client
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

# Get Agent instance with tone
def get_agent(tone):
    return Agent(
        model=OpenAIChatCompletionsModel(
            model='deepseek/deepseek-chat-v3-0324:free',
            openai_client=client
        ),
        name='Zartasha Agent',
        instructions=f'You are a helpful assistant who answers in a {tone.lower()} tone.'
    )

# UI Setup
st.set_page_config(page_title="Zartasha Agent", layout="centered")
st.title("🤖 Ask My Agent")

# Session state
if "history" not in st.session_state:
    st.session_state.history = []
if "pinned" not in st.session_state:
    st.session_state.pinned = []

# Sidebar - Chat configuration
st.sidebar.title("🧠 Chat Settings")
mode = st.sidebar.selectbox("Select Chat Mode", ["General Knowledge", "Programming Help", "Casual Chat"])
tone = st.sidebar.radio("Response Tone", ["Formal", "Neutral", "Friendly"])

# Suggested prompts
st.markdown("### 🔮 Suggested Questions")
suggested_qs = [
    "What is AI?",
    "How to reverse a list in Python?",
    "What is the capital of France?",
    "Tell me a joke.",
]
cols = st.columns(2)
for i, q in enumerate(suggested_qs):
    with cols[i % 2]:
        if st.button(q):
            st.session_state.suggested_input = q

# Run Agent
def run_query(query):
    agent = get_agent(tone)
    return asyncio.run(Runner.run(agent, query))

# Input field
user_input = st.text_input("💬 Enter your question:", value=st.session_state.get("suggested_input", ""))
submit = st.button("Ask")

# Handle submission
if submit and user_input:
    with st.spinner("💭 Thinking..."):
        try:
            result = run_query(user_input)
            output = result.final_output
            st.session_state.history.append((user_input, output))
            st.success("✅ Answer generated!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    st.session_state.suggested_input = ""

# Current response
if st.session_state.history:
    st.subheader("💡 Latest Answer")
    latest_q, latest_a = st.session_state.history[-1]
    st.markdown(f"**Q:** {latest_q}")
    st.markdown(f"**A:** {latest_a}")

    if st.button("📌 Pin this answer"):
        st.session_state.pinned.append((latest_q, latest_a))

    st.info(f"📝 Word Count: {len(latest_a.split())} | 🧠 Tokens: ~{int(len(latest_a.split()) * 1.3)}")

# Pinned responses
if st.session_state.pinned:
    st.subheader("📌 Pinned Answers")
    for q, a in st.session_state.pinned:
        st.markdown(f"**📍Q:** {q}")
        st.markdown(f"**A:** {a}")
        st.markdown("---")

# Chat history
if len(st.session_state.history) > 1:
    st.subheader("📜 Chat History")
    for i, (q, a) in enumerate(reversed(st.session_state.history[:-1]), 1):
        with st.container():
            st.markdown(f"**{i}. Q:** {q}")
            st.markdown(f"**A:** {a}")
            st.markdown("---")
