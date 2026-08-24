import streamlit as st
st.markdown('<h1 class="hero-title">HELLO</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-badge">
        TEST BADGE
    </div>

    <h1 class="hero-title">
        Your next trip
    </h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-badge">
        TEST BADGE
    </div>

    <h1 class="hero-title">
        Your next trip,<br>
        planned intelligently.
    </h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-badge">
        TEST BADGE
    </div>

    <h1 class="hero-title">
        Your next trip
    </h1>
</div>
""", unsafe_allow_html=True)

import streamlit as st

st.markdown(
    '<div class="hero"><div class="hero-badge">TEST BADGE</div><h1 class="hero-title">Your next trip</h1></div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero">
    <div class="hero-badge">TEST BADGE</div>
    <h1 class="hero-title">Your next trip</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-badge">TEST BADGE</div>
    <h1 class="hero-title">Your next trip,<br>planned intelligently.</h1>
</div>
""", unsafe_allow_html=True)

hero_html = """
<div class="hero">
    <div class="hero-badge">✦ AI-POWERED TRAVEL PLANNER</div>
    <h1 class="hero-title">Your next trip,<br><span>planned intelligently.</span></h1>
    <p class="hero-subtitle">Tell us where you want to go, when you want to travel, and what kind of experience you're looking for. Our AI agents will handle the rest.</p>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

import streamlit as st

st.markdown(
    "<div>ONE</div><h1>TWO</h1><p>THREE</p>",
    unsafe_allow_html=True
)

import streamlit as st

x = """
<div>ONE</div>
<h1>TWO</h1>
<p>THREE</p>
"""

st.markdown(x, unsafe_allow_html=True)

hero_html = """
<div class="hero">
    <div class="hero-badge">✦ AI-POWERED TRAVEL PLANNER</div>
    <h1 class="hero-title">Your next trip,<br><span>planned intelligently.</span></h1>
    <p class="hero-subtitle">Tell us where you want to go, when you want to travel, and what kind of experience you're looking for. Our AI agents will handle the rest.</p>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

st.markdown("""
<style>
.hero {
    text-align: center;
    padding: 65px 20px 35px 20px;
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
    max-width: 650px;
    margin: 24px auto 0 auto;
    color: #858585;
    font-size: 17px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

