import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de Aplicaciones con Inteligencia Artificial",
    page_icon="💗",
    layout="wide",
)

# Estilo rosado
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffe6f2;
    color: #5a004f;
}
[data-testid="stHeader"] {
    background: none;
}
h1, h2, h3, h4, h5, h6 {
    color: #b30086;
    text-align: center;
    font-family: 'Poppins', sans-serif;
}
p, li {
    color: #5a004f;
}
button, .stButton>button {
    background-color: #ffb3d9 !important;
    color: #5a004f !important;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}
button:hover {
    background-color: #ff99cc !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Título principal
st.markdown("<h1>💗 Portafolio de Aplicaciones con Inteligencia Artificial 💗</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Angie Estrella Espinosa Valdez 💗</h4>", unsafe_allow_html=True)
st.write("---")

# === FILA 1 ===
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💗 Introducción")
    image = Image.open("imagen1.jpg")
    st.image(image, width=190)
    st.write("Presentación general del portafolio.")
    url = "https://intro1.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col2:
    st.subheader("💗 Introducción 2")
    image = Image.open("imagen2.jpg")
    st.image(image, width=190)
    st.write("Segunda práctica introductoria.")
    url = "https://intro2.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col3:
    st.subheader("💗 Voz a Texto")
    image = Image.open("imagen3.jpg")
    st.image(image, width=190)
    st.write("Convierte voz en texto usando IA.")
    url = "https://voz-texto.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

st.write("---")

# === FILA 2 ===
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("💗 Aplicación de Reconocimiento de Bocetos")
    image = Image.open("imagen4.jpg")
    st.image(image, width=190)
    st.write("Usa RAG para procesar información desde un documento PDF.")
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col5:
    st.subheader("💗 Clasificador de Imágenes")
    image = Image.open("imagen5.jpg")
    st.image(image, width=190)
    st.write("Reconoce objetos en imágenes usando un modelo IA.")
    url = "https://clasificador-imagenes.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col6:
    st.subheader("💗 Generador de Texto GPT")
    image = Image.open("imagen6.jpg")
    st.image(image, width=190)
    st.write("Genera texto automáticamente con inteligencia artificial.")
    url = "https://generador-gpt.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

st.write("---")

# === FILA 3 ===
col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("💗 Análisis de Sentimientos")
    image = Image.open("imagen7.jpg")
    st.image(image, width=190)
    st.write("Detecta emociones en textos escritos.")
    url = "https://sentimientos.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col8:
    st.subheader("💗 Generador de Imágenes IA")
    image = Image.open("imagen8.jpg")
    st.image(image, width=190)
    st.write("Crea imágenes a partir de texto con IA generativa.")
    url = "https://imagenes-ia.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col9:
    st.subheader("💗 Chatbot Asistente")
    image = Image.open("imagen9.jpg")
    st.image(image, width=190)
    st.write("Asistente virtual conversacional basado en GPT.")
    url = "https://chatbot-ia.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

st.write("---")

# === FILA 4 ===
col10, col11, col12 = st.columns(3)

with col10:
    st.subheader("💗 Detección de Objetos")
    image = Image.open("imagen10.jpg")
    st.image(image, width=190)
    st.write("Identifica objetos en tiempo real con visión por computadora.")
    url = "https://deteccion-objetos.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col11:
    st.subheader("💗 Recomendador de Películas")
    image = Image.open("imagen11.jpg")
    st.image(image, width=190)
    st.write("Sugiere películas según tus preferencias.")
    url = "https://recomendador-peliculas.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col12:
    st.subheader("💗 Traductor Multilingüe")
    image = Image.open("imagen12.jpg")
    st.image(image, width=190)
    st.write("Traduce textos automáticamente a varios idiomas.")
    url = "https://traductor-ia.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

st.write("---")

# === FILA 5 ===
col13, col14, col15 = st.columns(3)

with col13:
    st.subheader("💗 Detección de Emociones en Rostros")
    image = Image.open("imagen13.jpg")
    st.image(image, width=190)
    st.write("Analiza expresiones faciales con redes neuronales.")
    url = "https://emociones-faciales.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col14:
    st.subheader("💗 Generador de Música")
    image = Image.open("imagen14.jpg")
    st.image(image, width=190)
    st.write("Crea melodías automáticas usando IA musical.")
    url = "https://musica-ia.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

with col15:
    st.subheader("💗 Análisis de Datos")
    image = Image.open("imagen15.jpg")
    st.image(image, width=190)
    st.write("Visualiza y analiza datos con ayuda de IA.")
    url = "https://analisis-datos.streamlit.app/"
    st.write(f"💗 [Ir a la aplicación]({url})")

st.write("---")

# Pie de página
st.markdown(
    "<p style='text-align:center; color:#b30086;'>💗 Portafolio creado con amor y creatividad 💗</p>",
    unsafe_allow_html=True
)
