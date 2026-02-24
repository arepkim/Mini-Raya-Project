import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# --- INITIALIZATION & CONFIG ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def configure_gemini():
    """Initializes the Google Gemini API client."""
    if not API_KEY or API_KEY == "your_api_key_here":
        st.error("⚠️ GEMINI_API_KEY is missing. Please update your `.env` file.")
        st.stop()
    genai.configure(api_key=API_KEY)

def apply_custom_css():
    """Applies festive styling for a clean, modern UI."""
    st.markdown("""
        <style>
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        }
        
        /* Input card styling */
        .stTextInput, .stSelectbox, .stTextArea {
            border-radius: 12px !important;
        }

        /* Button styling */
        div.stButton > button:first-child {
            background: linear-gradient(90deg, #166534 0%, #15803d 100%);
            color: white;
            padding: 12px 24px;
            border-radius: 12px;
            border: none;
            font-size: 1.1rem;
            font-weight: 600;
            width: 100%;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(22, 101, 52, 0.2);
        }

        /* Result container styling */
        .greeting-card {
            background: #ffffff;
            padding: 2.5rem;
            border-radius: 20px;
            border-left: 8px solid #16a34a;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
            color: #14532d;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-top: 2rem;
            white-space: pre-wrap;
        }
        </style>
    """, unsafe_allow_html=True)

# --- CORE LOGIC ---
def get_model_response(name, tone, details):
    """
    Calls the Gemini API to generate a culturally relevant Hari Raya greeting.
    Uses 'gemini-flash-latest' for the best balance of speed and availability.
    """
    model = genai.GenerativeModel("gemini-flash-latest")
    
    # Context-aware instructions for different tones
    tone_map = {
        "Formal": "Highly respectful, polite, and elegant (suitable for elders or professional settings).",
        "Funny": "Witty, playful, and light-hearted (mentions of ketupat, lemang, and festive food).",
        "Poetic (Pantun)": "Must include a classic 4-line Malay pantun followed by a sincere modern wish.",
        "Casual": "Relaxed, warm, and friendly (natural 'santai' conversational style)."
    }

    prompt = f"""
    You are a festive culture expert. Craft a warm and authentic Hari Raya Aidilfitri greeting for: {name}.
    
    Style Guidelines:
    - Tone: {tone_map.get(tone, "Warm and sincere")}
    - Context: {details if details else "A general wish for forgiveness and celebration."}
    
    Requirements:
    1. Language: Use a natural, expressive mix of Malay and English (Malaysian/Singaporean vernacular).
    2. Essential Phrase: Include "Selamat Hari Raya Aidilfitri, Maaf Zahir dan Batin".
    3. Emotion: Ensure it feels human-written, festive, and heartfelt.
    4. Format: Do not include meta-text (like "Here is your greeting"). Start directly with the wish.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Oops! Something went wrong: {str(e)}"

# --- MAIN APP LAYOUT ---
def main():
    st.set_page_config(
        page_title="Hari Raya Greeting AI",
        page_icon="🌙",
        layout="centered"
    )
    
    apply_custom_css()
    configure_gemini()

    # Header section
    st.title("✨ AI Hari Raya Greeting Generator")
    st.markdown("##### *Create thoughtful and festive Eid al-Fitr wishes in seconds.*")
    st.divider()

    # Input section
    col1, col2 = st.columns(2)
    with col1:
        recipient = st.text_input("👤 To who?", placeholder="Name or nickname...")
    with col2:
        tone = st.selectbox("🎭 Mood/Tone", ["Casual", "Funny", "Formal", "Poetic (Pantun)"])
    
    extra_details = st.text_area(
        "📝 Personal Touch (Optional)", 
        placeholder="e.g. Mention the rendang, apologize for being away, or a shared memory."
    )

    # Action & Output section
    if st.button("🌙 Generate My Greeting"):
        if not recipient:
            st.warning("Please tell us who the greeting is for! 👤")
        else:
            with st.spinner("✨ Crafting your festive wish with AI..."):
                final_greeting = get_model_response(recipient, tone, extra_details)
                
                st.markdown("### 🕊️ Your Festive Greeting:")
                st.markdown(f'<div class="greeting-card">{final_greeting}</div>', unsafe_allow_html=True)
                
                # Feedback options
                st.caption("💡 *Tip: You can copy and paste this into WhatsApp, Telegram, or Instagram!*")

    # Footer
    st.divider()
    st.caption("🌙 Built with Google Gemini 2.5 Flash | Streamlit v1.30+")

if __name__ == "__main__":
    main()
