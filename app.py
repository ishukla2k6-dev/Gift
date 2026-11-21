import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Private Gift for Aprajita ✨",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit header, footer, and padding for a full-screen experience
st.markdown(
    """
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
        iframe {border: none !important; width: 100vw !important; height: 100dvh !important; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

def to_data_uri(file_path: str, mime_type: str) -> str:
    path = Path(file_path)
    if not path.exists():
        return file_path
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

html_code = Path("index.html").read_text(encoding="utf-8")

# Inline local media so Streamlit's sandboxed iframe loads everything seamlessly
replacements = {
    'src="video_1.mp4"': f'src="{to_data_uri("video_1.mp4", "video/mp4")}"',
    'src="download.png"': f'src="{to_data_uri("download.png", "image/png")}"',
    'catImageFile: "download.png"': f'catImageFile: "{to_data_uri("download.png", "image/png")}"',
    'src="music.mp3"': f'src="{to_data_uri("music.mp3", "audio/mpeg")}"',
}

for target, replacement in replacements.items():
    html_code = html_code.replace(target, replacement)

components.html(html_code, height=900, scrolling=False)