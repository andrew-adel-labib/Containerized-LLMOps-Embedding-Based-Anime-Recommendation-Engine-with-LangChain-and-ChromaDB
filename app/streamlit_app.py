import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(
    page_title="Anime Recommender",
    page_icon="🎌", 
    layout="wide",
)

load_dotenv()

st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #533483);
    background-size: 400% 400%;
    animation: gradientShift 18s ease infinite;
    color: #f0f0f0;
    font-family: 'Poppins', sans-serif;
}}

@keyframes gradientShift {{
    0% {{background-position: 0% 50%;}}
    50% {{background-position: 100% 50%;}}
    100% {{background-position: 0% 50%;}}
}}

body::before {{
    content: "";
    background-image: url('7c01bb38-b615-49b7-a70b-85fdc57f8d94.png');
    background-size: cover;
    background-position: center;
    opacity: 0.15;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}}

.banner {{
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 10px;
    margin-bottom: 25px;
}}
.banner img {{
    height: 120px;
    border-radius: 12px;
    box-shadow: 0 0 25px rgba(255, 121, 198, 0.4);
    transition: transform 0.4s ease, box-shadow 0.4s;
}}
.banner img:hover {{
    transform: scale(1.1);
    box-shadow: 0 0 40px rgba(255, 121, 198, 0.7);
}}

h1 {{
    text-align: center;
    color: #ff79c6;
    text-shadow: 0 0 20px #ff79c655;
    font-weight: 800;
    letter-spacing: 1px;
}}

.subtitle {{
    text-align: center;
    color: #ffffff;
    font-size: 18px;
    margin-bottom: 20px;
}}

.stTextInput > div > div > input {{
    border: 2px solid #ff79c6;
    border-radius: 10px;
    background-color: #1e1e2e;
    color: #ffffff;
    padding: 10px;
    transition: 0.3s;
}}
.stTextInput > div > div > input:focus {{
    border-color: #8be9fd;
    box-shadow: 0 0 10px #8be9fd66;
}}

.anime-card {{
    background: rgba(40, 40, 60, 0.85);
    padding: 1.2em;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(255, 121, 198, 0.2);
    margin-top: 1em;
    transition: transform 0.3s ease, box-shadow 0.3s;
}}
.anime-card:hover {{
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(255, 121, 198, 0.4);
}}

.footer {{
    text-align: center;
    color: #aaa;
    font-size: 14px;
    margin-top: 30px;
}}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("🌙 Anime Recommender System")
st.markdown("<p class='subtitle'>Find your next anime journey 🌸</p>", unsafe_allow_html=True)
st.markdown("---")

query = st.text_input(
    "🎥 Enter your anime preferences",
    placeholder="e.g., light-hearted anime with a school setting"
)

if query:
    with st.spinner("🎯Fetching your personalized recommendations..."):
        response = pipeline.recommend(query)

        st.markdown("## 🌌 Recommended Anime")
        st.markdown("---")

        if isinstance(response, list):
            for anime in response:
                st.markdown(f"<div class='anime-card'>🎞️ <b>{anime}</b></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='anime-card'>{response}</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p class='footer'>✨ Built with ❤️ using Streamlit | Designed by Andrew Adel ✨</p>",
    unsafe_allow_html=True
)
