# streamlit user interface
import streamlit as st
import requests
import json
from typing import Any


# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Trip Planner AI",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

API_URL = "http://127.0.0.1:8000/travel"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       GLOBAL
    ------------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 50% -10%,
                rgba(70, 90, 120, 0.18),
                transparent 35%
            ),
            #050505;
        color: #f5f5f5;
    }

    .main {
        background: #050505;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* -------------------------------------------------------
       HERO
    ------------------------------------------------------- */

    .hero {
        width: 100%;
        text-align: center;
        padding: 65px 20px 35px 20px;
        box-sizing: border-box;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 999px;
        background: rgba(255,255,255,0.04);
        color: #a8a8a8;
        font-size: 13px;
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    }

    .hero-title {
        font-size: clamp(42px, 6vw, 78px);
        line-height: 0.95;
        font-weight: 800;
        letter-spacing: -4px;
        margin: 0;
        color: #ffffff;
    }

    .hero-title span {
        background: linear-gradient(
            90deg,
            #ffffff,
            #8e9fff,
            #70d6ff
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        display: block;
        width: 100%;
        max-width: 700px;
        margin: 24px auto 0 auto !important;
        padding: 0 important;
        color: #858585;
        font-size: 17px;
        line-height: 1.6;
        text-align: center !important;
    }


    /* -------------------------------------------------------
       INPUT AREA
    ------------------------------------------------------- */

    .input-label {
        color: #cfcfcf;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    div[data-testid="stTextArea"] textarea {
        background: #101010 !important;
        color: #ffffff !important;
        border: 1px solid #292929 !important;
        border-radius: 18px !important;
        padding: 18px !important;
        font-size: 16px !important;
        resize: vertical !important;
        box-shadow:
            inset 0 0 0 1px rgba(255,255,255,0.01),
            0 10px 40px rgba(0,0,0,0.25);
    }

    div[data-testid="stTextArea"] textarea:focus {
        border-color: #6675ff !important;
        box-shadow:
            0 0 0 1px #6675ff,
            0 0 35px rgba(102,117,255,0.12) !important;
    }

    div[data-testid="stTextArea"] textarea::placeholder {
        color: #666666 !important;
    }


    /* -------------------------------------------------------
       BUTTON
    ------------------------------------------------------- */

    .stButton > button {
        width: 100%;
        height: 52px;
        border: none !important;
        border-radius: 14px !important;
        background:
            linear-gradient(
                135deg,
                #6675ff,
                #8368ff
            ) !important;
        color: white !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        transition: all 0.2s ease !important;
        box-shadow:
            0 10px 30px rgba(102,117,255,0.20);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow:
            0 14px 35px rgba(102,117,255,0.35);
    }


    /* -------------------------------------------------------
       SUGGESTION CARDS
    ------------------------------------------------------- */

    .suggestion {
        background: #0d0d0d;
        border: 1px solid #1d1d1d;
        border-radius: 14px;
        padding: 16px;
        color: #a3a3a3;
        font-size: 13px;
        min-height: 75px;
    }

    .suggestion strong {
        color: #e7e7e7;
        display: block;
        margin-bottom: 6px;
    }


    /* -------------------------------------------------------
       RESULT CONTAINERS
    ------------------------------------------------------- */

    .result-card {
        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.045),
                rgba(255,255,255,0.015)
            );
        border: 1px solid #242424;
        border-radius: 20px;
        padding: 28px;
        margin-top: 25px;
        box-shadow:
            0 20px 60px rgba(0,0,0,0.30);
    }

    .result-title {
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #777777;
        margin-bottom: 12px;
    }

    .answer {
        color: #eeeeee;
        font-size: 17px;
        line-height: 1.8;
    }


    /* -------------------------------------------------------
       METRICS
    ------------------------------------------------------- */

    .metric-card {
        background: #0d0d0d;
        border: 1px solid #202020;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
    }

    .metric-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }

    .metric-label {
        color: #686868;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        color: #f0f0f0;
        font-size: 15px;
        font-weight: 600;
        margin-top: 5px;
    }


    /* -------------------------------------------------------
       JSON / DATA
    ------------------------------------------------------- */

    div[data-testid="stJson"] {
        background: #090909 !important;
        border: 1px solid #202020 !important;
        border-radius: 14px !important;
    }

    .data-box {
        background: #0b0b0b;
        border: 1px solid #1d1d1d;
        border-radius: 14px;
        padding: 18px;
    }


    /* -------------------------------------------------------
       TABS
    ------------------------------------------------------- */

    button[data-baseweb="tab"] {
        color: #777777 !important;
        font-weight: 600 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ffffff !important;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #6675ff !important;
    }


    /* -------------------------------------------------------
       FOOTER
    ------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #4f4f4f;
        font-size: 12px;
        padding-top: 60px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def pretty_json(data: Any):
    """Safely display JSON-like API data."""
    if data is None:
        st.info("No data returned.")
        return

    if isinstance(data, str):
        try:
            parsed = json.loads(data)
            st.json(parsed)
        except Exception:
            st.markdown(
                f'<div class="data-box">{data}</div>',
                unsafe_allow_html=True,
            )
    else:
        st.json(data)


def make_api_request(message: str):
    """Send request to FastAPI backend."""

    payload = {
        "message": message,
        "thread_id": None,
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            timeout=180,
        )

        try:
            data = response.json()
        except Exception:
            return None, f"Invalid response from API: {response.text}"

        if response.status_code != 200:
            return None, data.get(
                "error",
                f"API returned status {response.status_code}",
            )

        return data, None

    except requests.exceptions.ConnectionError:
        return None, (
            "Could not connect to the Trip Planner API. "
            "Make sure FastAPI is running on http://127.0.0.1:8000"
        )

    except requests.exceptions.Timeout:
        return None, "The request timed out. Your trip planner may still be processing."

    except Exception as e:
        return None, str(e)


def render_metric(icon, label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO
# ============================================================

hero_html = """
<div class="hero">
    <div class="hero-badge">✦ AI-POWERED TRAVEL PLANNER</div>
    <h1 class="hero-title">Your next trip,<br><span>planned intelligently.</span></h1>
    <p class="hero-subtitle">Tell us where you want to go, when you want to travel, and what kind of experience you're looking for. Our AI agents will handle the rest.</p>
</div>
"""

st.markdown(hero_html,unsafe_allow_html=True)


# ============================================================
# INPUT
# ============================================================

st.markdown(
    '<div class="input-label">WHERE DO YOU WANT TO GO?</div>',
    unsafe_allow_html=True,
)

user_message = st.text_area(
    label="Trip request",
    label_visibility="collapsed",
    placeholder=(
        "Example: Plan a 7-day trip to Japan from Mumbai for 2 people "
        "in October. I want a mix of Tokyo, Kyoto and Osaka with "
        "comfortable hotels and good local food."
    ),
    height=140,
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    plan_clicked = st.button(
        "✦  Plan My Trip",
        use_container_width=True,
    )


# ============================================================
# QUICK PROMPTS
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        text-align:center;
        color:#555;
        font-size:12px;
        margin-bottom:12px;
        text-transform:uppercase;
        letter-spacing:1px;
    ">
        Need inspiration?
    </div>
    """,
    unsafe_allow_html=True,
)

q1, q2, q3 = st.columns(3)

with q1:
    st.markdown(
        """
        <div class="suggestion">
            <strong>🏝️ Beach Escape</strong>
            Plan a relaxing tropical vacation with beautiful beaches.
        </div>
        """,
        unsafe_allow_html=True,
    )

with q2:
    st.markdown(
        """
        <div class="suggestion">
            <strong>🏔️ Adventure</strong>
            Find an unforgettable mountain and adventure itinerary.
        </div>
        """,
        unsafe_allow_html=True,
    )

with q3:
    st.markdown(
        """
        <div class="suggestion">
            <strong>🏙️ City Explorer</strong>
            Discover food, culture and iconic city experiences.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# API CALL
# ============================================================

if plan_clicked:

    if not user_message.strip():
        st.warning("Please tell me something about the trip you want to plan.")

    else:

        with st.status(
            "Planning your trip...",
            expanded=True,
        ) as status:

            st.write("🔎 Understanding your travel request...")
            st.write("✈️ Searching for flight options...")
            st.write("🏨 Finding suitable hotels...")
            st.write("🗺️ Building your itinerary...")

            data, error = make_api_request(
                user_message.strip()
            )

            if error:
                status.update(
                    label="Trip planning failed",
                    state="error",
                    expanded=True,
                )

            else:
                status.update(
                    label="Your trip is ready ✨",
                    state="complete",
                    expanded=False,
                )

        # ----------------------------------------------------
        # ERROR
        # ----------------------------------------------------

        if error:

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-title">Something went wrong</div>
                    <div class="answer">
                        {error}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.stop()

        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        if data.get("success") is False:

            st.error(
                data.get(
                    "error",
                    "The trip planner returned an error.",
                )
            )

            st.stop()

        # Save result
        st.session_state["trip_result"] = data


# ============================================================
# RESULTS
# ============================================================

if "trip_result" in st.session_state:

    result = st.session_state["trip_result"]

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # TOP METRICS
    # --------------------------------------------------------

    travellers = result.get("travellers", "—")
    thread_id = result.get("thread_id", "—")

    m1, m2, m3 = st.columns(3)

    with m1:
        render_metric(
            "✈️",
            "Flights",
            "Ready",
        )

    with m2:
        render_metric(
            "🏨",
            "Hotels",
            "Ready",
        )

    with m3:
        render_metric(
            "👥",
            "Travellers",
            str(travellers),
        )

    # --------------------------------------------------------
    # MAIN ANSWER
    # --------------------------------------------------------

    answer = result.get(
        "answer",
        "No final answer was returned.",
    )

    st.markdown(
        f"""
        <div class="result-card">

            <div class="result-title">
                Your Personalized Trip
            </div>

            <div class="answer">
                {answer}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # TABS
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    tab_flight, tab_hotel, tab_itinerary, tab_travellers = st.tabs(
        [
            "✈️ Flights",
            "🏨 Hotels",
            "🗺️ Itinerary",
            "👥 Travellers",
        ]
    )

    # --------------------------------------------------------
    # FLIGHTS
    # --------------------------------------------------------

    with tab_flight:

        st.markdown(
            """
            <div class="result-card">

                <div class="result-title">
                    Flight Results
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        pretty_json(
            result.get("flight_result")
        )

    # --------------------------------------------------------
    # HOTELS
    # --------------------------------------------------------

    with tab_hotel:

        st.markdown(
            """
            <div class="result-card">

                <div class="result-title">
                    Hotel Results
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        pretty_json(
            result.get("hotel_result")
        )

    # --------------------------------------------------------
    # ITINERARY
    # --------------------------------------------------------

    with tab_itinerary:

        st.markdown(
            """
            <div class="result-card">

                <div class="result-title">
                    Day-by-Day Itinerary
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        itineary = result.get("itineary")

        if isinstance(itineary, str):
            st.markdown(itineary)
        else:
            pretty_json(itineary)

    # --------------------------------------------------------
    # TRAVELLERS
    # --------------------------------------------------------

    with tab_travellers:

        st.markdown(
            """
            <div class="result-card">

                <div class="result-title">
                    Traveller Information
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        pretty_json(
            travellers
        )

    # --------------------------------------------------------
    # THREAD
    # --------------------------------------------------------

    with st.expander("Developer information"):

        st.code(
            f"Thread ID: {thread_id}",
            language="text",
        )

        st.caption(
            "This ID can later be used to persist and continue conversations."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Trip Planner AI · Powered by your FastAPI multi-agent backend
    </div>
    """,
    unsafe_allow_html=True,
)
