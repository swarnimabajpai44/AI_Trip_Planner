import streamlit as st
import requests
import datetime

# ============================================================
# CONFIGURATION
# ============================================================

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="TripWise AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #111827 50%,
            #172554 100%
        );
    }

    /* Main content width */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Main title */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(
            90deg,
            #38bdf8,
            #818cf8,
            #c084fc
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #cbd5e1;
        margin-bottom: 2.5rem;
    }

    /* Feature cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        height: 140px;
        transition: all 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);
        border-color: rgba(129, 140, 248, 0.7);
        background: rgba(255, 255, 255, 0.10);
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 8px;
    }

    .feature-title {
        color: white;
        font-size: 1rem;
        font-weight: 600;
    }

    .feature-description {
        color: #94a3b8;
        font-size: 0.85rem;
    }

    /* AI response container */
    .response-container {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 25px;
        margin-top: 30px;
    }

    /* Section heading */
    .section-title {
        color: #f8fafc;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🌍 TripWise AI")

    st.markdown(
        """
        Your intelligent AI travel companion.

        Plan trips, discover destinations,
        check weather, calculate expenses,
        and convert currencies.
        """
    )

    st.divider()

    st.markdown("### 🧭 What I can help with")

    st.markdown(
        """
        ✈️ **Trip Planning**

        📍 **Places to Visit**

        🌤️ **Weather Information**

        💰 **Travel Expenses**

        💱 **Currency Conversion**
        """
    )

    st.divider()

    st.markdown("### 💡 Example Questions")

    st.caption("Plan a 5-day trip to Goa")

    st.caption("What is the weather in Paris?")

    st.caption("Calculate my travel budget for Bali")

    st.caption("Convert ₹50,000 to USD")

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌍 TripWise AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'Your intelligent travel companion — plan smarter, explore better.'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# FEATURE CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🗺️</div>
            <div class="feature-title">Smart Itineraries</div>
            <div class="feature-description">
                Personalized travel plans
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🌤️</div>
            <div class="feature-title">Live Weather</div>
            <div class="feature-description">
                Check destination weather
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">💰</div>
            <div class="feature-title">Budget Planning</div>
            <div class="feature-description">
                Estimate your travel costs
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">📍</div>
            <div class="feature-title">Explore Places</div>
            <div class="feature-description">
                Discover amazing destinations
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# CHAT HISTORY
# ============================================================

st.markdown(
    '<div class="section-title">💬 Your Travel Assistant</div>',
    unsafe_allow_html=True,
)

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "✈️ Ask me to plan your next adventure..."
)


# ============================================================
# PROCESS USER REQUEST
# ============================================================

if user_input:

    # --------------------------------------------------------
    # Add user message to chat history
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    # Display user message immediately

    with st.chat_message("user"):
        st.markdown(user_input)


    # --------------------------------------------------------
    # Call FastAPI Backend
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("✨ Your AI travel agent is planning your trip..."):

            try:

                # Keep the same API format as your existing backend

                payload = {
                    "question": user_input
                }

                response = requests.post(
                    f"{BASE_URL}/query",
                    json=payload,
                    timeout=120,
                )


                # ------------------------------------------------
                # Successful Response
                # ------------------------------------------------

                if response.status_code == 200:

                    answer = response.json().get(
                        "answer",
                        "No answer returned.",
                    )

                    # Display AI response

                    st.markdown(answer)


                    # Add AI response to conversation history

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                        }
                    )


                # ------------------------------------------------
                # Backend Error
                # ------------------------------------------------

                else:

                    error_message = (
                        f"⚠️ The travel agent could not process "
                        f"your request.\n\n"
                        f"Backend response: {response.text}"
                    )

                    st.error(error_message)


            # ----------------------------------------------------
            # Connection / Request Error
            # ----------------------------------------------------

            except requests.exceptions.ConnectionError:

                error_message = (
                    "🔌 **Unable to connect to the travel agent.**\n\n"
                    "Please make sure your FastAPI backend is running "
                    "on `http://localhost:8000`."
                )

                st.error(error_message)


            except requests.exceptions.Timeout:

                st.error(
                    "⏳ The request took too long. "
                    "Please try again."
                )


            except Exception as e:

                st.error(
                    f"❌ Something went wrong: {str(e)}"
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🌍 TripWise AI · Powered by AI Agents and LangGraph
        <br>
        Always verify travel information, prices, operating hours,
        and travel requirements before your trip.
    </div>
    """,
    unsafe_allow_html=True,
)