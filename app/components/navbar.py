import streamlit as st

def navbar():
    st.markdown("""
        <style>
            .navbar {
                background-color: #0E1117;
                padding: 0.5rem;
                color: white;
                font-size: 18px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .navbar-title {
                font-weight: bold;
                color: #00FFAA;
            }
        </style>
        <div class="navbar">
            <div class="navbar-title">📊 DataVisionIA360</div>
            <div>Big Data • AI • Business Intelligence</div>
        </div>
    """, unsafe_allow_html=True)

