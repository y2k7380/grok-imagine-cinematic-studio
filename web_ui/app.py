#!/usr/bin/env python3
"""
Grok Imagine Cinematic Studio — Enhanced Streamlit Web UI v3.5.4
With Live Grok 4.3 API Integration + Role Card Support
"""

import streamlit as st
from datetime import datetime
import json
import os
from pathlib import Path
from openai import OpenAI

# ===================== CONFIG =====================
AGENTS_DIR = Path("../references/agents")  # Adjust if running from different location

# ===================== GROK API INTEGRATION =====================
def get_grok_client():
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        api_key = st.session_state.get("xai_api_key", "")
    if not api_key:
        return None
    return OpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1"
    )

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Grok Imagine Cinematic Studio v3.5",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cinematic CSS
st.markdown("""
<style>
    .main { background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%); }
    .stApp { color: #e0e0ff; }
    .stButton>button {
        background: linear-gradient(90deg, #6a00ff, #00d4ff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 28px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #00d4ff;
    }
    .metric-card {
        background: rgba(30, 30, 60, 0.8);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #4a4a8a;
    }
    .agent-card {
        background: #1f1f3a;
        border-radius: 10px;
        padding: 12px;
        margin: 6px 0;
        border-left: 4px solid #00d4ff;
    }
</style>
""", unsafe_allow_html=True)

# ===================== HEADER =====================
st.title("🎥 Grok Imagine Cinematic Studio v3.5")
st.markdown("**22-Agent Professional Film Production System** • Powered by Grok 4.3 Beta + Full Role Cards")

# ===================== SIDEBAR =====================
with st.sidebar:
    st.header("🎬 Production Crew (22 Agents)")
    st.success("✅ All 22 Agents + Role Cards Online")

    with st.expander("View All Agents", expanded=False):
        agents_full = [
            "Studio Director", "Mega Production Architect",
            "Director of Photography", "Post-Production Color Grading Supervisor", "Production Designer / Set Decorator",
            "Performance & Emotion Director", "Identity Lock Specialist", "Narrative Arc & Pacing Strategist",
            "Sequence Director", "Cinematic Sequence Extender",
            "Continuity & Consistency Guardian", "Quality Assurance Guardian",
            "Imagine Prompt Master", "Workflow & Quota Optimizer",
            "Sonic Architect Native Audio Virtuoso", "Foley Sound Design Specialist",
            "Stunt & Action Choreographer", "VFX & SFX Supervisor",
            "Key Art & Poster Designer", "Trailer & Teaser Director", "Localization & Subtitle Specialist",
            "ErosForge NSFW Director (opt-in)"
        ]
        for agent in agents_full:
            st.markdown(f"• {agent}")

    # Role Cards Browser
    with st.expander("📋 Browse Role Cards", expanded=False):
        if AGENTS_DIR.exists():
            role_cards = sorted([f.stem for f in AGENTS_DIR.glob("*.md")])
            selected_card = st.selectbox("Select Role Card", role_cards)
            if selected_card:
                card_path = AGENTS_DIR / f"{selected_card}.md"
                if card_path.exists():
                    st.markdown(f"**{selected_card.replace('_', ' ')}**")
                    content = card_path.read_text()[:1500]
                    st.markdown(content + "...")
        else:
            st.warning("references/agents/ not found")

    st.divider()
    st.subheader("⚙️ Production Settings")

    genre = st.selectbox("Genre", ["Sci-Fi", "Psychological Horror", "Action", "Drama", "Cyberpunk", "Epic Fantasy", "Thriller", "Intimate Drama"])
    director = st.selectbox("Director Signature",
        ["Denis Villeneuve", "Christopher Nolan", "David Fincher", "Roger Deakins", "Zack Snyder", "Default Cinematic"])
    aspect_ratio = st.selectbox("Aspect Ratio", ["16:9 (Cinematic)", "2.39:1 (Anamorphic)", "9:16 (Vertical)", "1:1 (Square)"])
    quality = st.select_slider("Quality", ["Standard", "High", "Ultra", "IMAX"])
    duration = st.slider("Target Duration (seconds)", 15, 180, 60, step=5)
    complexity = st.select_slider("Complexity", ["Low", "Medium", "High", "Extreme"])

    # Live Cost Simulator
    st.subheader("💰 Live Cost Estimate")
    multipliers = {"Low": 1, "Medium": 2, "High": 4, "Extreme": 7}
    est_cost = round(duration * multipliers[complexity] * 0.85, 2)
    est_tokens = int(est_cost * 1250)

    col1, col2 = st.columns(2)
    col1.metric("Est. Cost", f"${est_cost}")
    col2.metric("Tokens", f"{est_tokens:,}")

# ===================== MAIN CONTENT =====================
st.header("📝 Project Brief")

story = st.text_area(
    "Describe your cinematic vision",
    placeholder="A cyberpunk detective chases a rogue AI through neon-drenched Tokyo rooftops at midnight...",
    height=150
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Generate Master Prompt", use_container_width=True):
        if story:
            prompt = f"""# Grok Imagine Cinematic Studio v3.5 — ACTIVATED

**Project:** {story[:100]}...
**Genre:** {genre}
**Director Signature:** {director}
**Duration:** {duration}s | **Quality:** {quality}
**Aspect Ratio:** {aspect_ratio}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

You are now running the full **22-agent** Grok Imagine Cinematic Studio v3.5 with Role Cards loaded from `references/agents/`.

Please begin by confirming activation and building a detailed Production Bible.
"""
            st.code(prompt, language="markdown")
            st.success("✅ Ready-to-paste prompt generated!")
        else:
            st.warning("Please enter a story description first.")

with col2:
    if st.button("🎬 Simulate Full Production", use_container_width=True):
        if story:
            with st.spinner("Engaging all 22 agents + Role Cards..."):
                import time
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.015)
                    progress.progress(i + 1)

            st.balloons()
            st.success("✅ Production Complete! (Simulated)")

            st.subheader("📊 Production Analytics")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Consistency", "96%")
            m2.metric("Emotional Impact", "94%")
            m3.metric("Visual Coherence", "98%")
            m4.metric("QA Score", "✅ GO")

            st.info("All clips passed 16-point QA. Ready for final delivery. (This is a simulation — use real Grok API for actual generation)")
        else:
            st.warning("Enter a project description first.")

with col3:
    if st.button("📄 Export Production Bible", use_container_width=True):
        if story:
            bible = {
                "title": story[:60] + "...",
                "genre": genre,
                "director_signature": director,
                "duration": f"{duration}s",
                "quality": quality,
                "aspect_ratio": aspect_ratio,
                "created": datetime.now().isoformat(),
                "agents": 22,
                "role_cards": "references/agents/",
                "status": "Production Ready"
            }
            st.download_button(
                label="⬇️ Download production_bible.json",
                data=json.dumps(bible, indent=2),
                file_name="production_bible.json",
                mime="application/json"
            )
            st.success("Production Bible ready for download!")
        else:
            st.warning("Please describe your project first.")

# ===================== GROK API SECTION =====================
st.divider()
st.header("🔌 Grok API Integration (Live)")

col_api1, col_api2 = st.columns([2, 1])

with col_api1:
    api_key_input = st.text_input(
        "XAI API Key (or set XAI_API_KEY env var)",
        type="password",
        placeholder="xai-...",
        key="xai_api_key"
    )

with col_api2:
    if st.button("🔑 Test Connection", use_container_width=True):
        client = get_grok_client()
        if client:
            try:
                response = client.chat.completions.create(
                    model="grok-4.3",
                    messages=[{"role": "user", "content": "Say 'Connection successful'"}],
                    max_tokens=10
                )
                st.success("✅ Connected to Grok 4.3!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Connection failed: {e}")
        else:
            st.warning("Please enter your XAI API key")

# Grok-Powered Cinematic Prompt Generator
st.subheader("🎬 Generate Cinematic Prompt with Grok 4.3")

if st.button("✨ Generate with Real Grok API", use_container_width=True):
    if not story:
        st.warning("Please enter a project description above first.")
    else:
        client = get_grok_client()
        if not client:
            st.error("Please enter your XAI API key above.")
        else:
            with st.spinner("Grok 4.3 is crafting your cinematic prompt using Role Card best practices..."):
                try:
                    response = client.chat.completions.create(
                        model="grok-4.3",
                        messages=[
                            {"role": "system", "content": "You are a world-class cinematic director and prompt engineer for Grok Imagine Cinematic Studio v3.5. Use professional Role Card thinking."},
                            {"role": "user", "content": f"Create a highly detailed, cinematic prompt for this project: {story}. Include camera angles, lighting motivation, mood, visual style, and emotional temperature. Reference the 22-agent system where relevant."}
                        ],
                        max_tokens=900,
                        temperature=0.75
                    )
                    generated_prompt = response.choices[0].message.content

                    st.success("✅ Grok 4.3 generated high-quality cinematic prompt!")
                    st.text_area("Generated Cinematic Prompt", generated_prompt, height=220)
                    st.code(generated_prompt, language="markdown")

                except Exception as e:
                    st.error(f"API Error: {str(e)}")

# Footer
st.divider()
st.caption("Grok Imagine Cinematic Studio v3.5.4 • 22 Agents + Full Role Cards • Live Grok 4.3 API • June 2026 • SuperGrokPro Recommended")
