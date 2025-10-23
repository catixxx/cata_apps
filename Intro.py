import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de Aplicaciones con Inteligencia Artificial",
    page_icon="💗",
    layout="wide",
)

# 🌸 Estilos visuales corregidos (centrado, imágenes iguales, tipografía consistente)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffe6f2;
    color: #5a004f;
    font-family: 'Poppins', sans-serif;
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
    text-align: center;
    font-family: 'Poppins', sans-serif;
}

/* Imágenes uniformes */
.stImage > img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 15px;
    width: 300px !important;
    height: 400px !important;
    object-fit: cover !important;
    object-position: center !important;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

/* Botones rosados */
button, .stButton>button {
    background-color: #ffb3d9 !important;
    color: #5a004f !important;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    display: block;
    margin: 0 auto;
    transition: 0.3s;
}

button:hover {
    background-color: #ff99cc !important;
    transform: scale(1.05);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🌸 Título principal
st.markdown("<h1>💗 Portafolio de Aplicaciones con Inteligencia Artificial 💗</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Catalina Sanabria Monares</h4>", unsafe_allow_html=True)
st.write("---")

# === FILA 1 ===
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💗 Introducción")
    st.image(Image.open("imagen1.jpg"))
    st.write("Presentación general del portafolio.")
    st.markdown("💗 [Ir a la aplicación](https://intro1.streamlit.app/)")

with col2:
    st.subheader("💗 Introducción 2")
    st.image(Image.open("imagen2.jpg"))
    st.write("Segunda práctica introductoria.")
    st.markdown("💗 [Ir a la aplicación](https://intro2.streamlit.app/)")

with col3:
    st.subheader("💗 Voz a Texto")
    st.image(Image.open("imagen3.jpg"))
    st.write("Convierte voz en texto usando IA.")
    st.markdown("💗 [Ir a la aplicación](https://voz-texto.streamlit.app/)")

st.write("---")

# === FILA 2 ===
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("💗 Aplicación de Reconocimiento de Bocetos")
    st.image(Image.open("imagen4.jpg"))
    st.write("Usa RAG para procesar información desde un documento PDF.")
    st.markdown("💗 [Ir a la aplicación](https://chatpdf-cc.streamlit.app/)")

with col5:
    st.subheader("💗 Clasificador de Imágenes")
    st.image(Image.open("imagen5.jpg"))
    st.write("Reconoce objetos en imágenes usando un modelo IA.")
    st.markdown("💗 [Ir a la aplicación](https://clasificador-imagenes.streamlit.app/)")

with col6:
    st.subheader("💗 Generador de Texto GPT")
    st.image(Image.open("imagen6.jpg"))
    st.write("Genera texto automáticamente con inteligencia artificial.")
    st.markdown("💗 [Ir a la aplicación](https://generador-gpt.streamlit.app/)")

st.write("---")

# === FILA 3 ===
col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("💗 Análisis de Sentimientos")
    st.image(Image.open("imagen7.jpg"))
    st.write("Detecta emociones en textos escritos.")
    st.markdown("💗 [Ir a la aplicación](https://sentimientos.streamlit.app/)")

with col8:
    st.subheader("💗 Generador de Imágenes IA")
    st.image(Image.open("imagen8.jpg"))
    st.write("Crea imágenes a partir de texto con IA generativa.")
    st.markdown("💗 [Ir a la aplicación](https://imagenes-ia.streamlit.app/)")

with col9:
    st.subheader("💗 Chatbot Asistente")
    st.image(Image.open("imagen9.jpg"))
    st.write("Asistente virtual conversacional basado en GPT.")
    st.markdown("💗 [Ir a la aplicación](https://chatbot-ia.streamlit.app/)")

st.write("---")

# === FILA 4 ===
col10, col11, col12 = st.columns(3)

with col10:
    st.subheader("💗 Detección de Objetos")
    st.image(Image.open("imagen10.jpg"))
    st.write("Identifica objetos en tiempo real con visión por computadora.")
    st.markdown("💗 [Ir a la aplicación](https://deteccion-objetos.streamlit.app/)")

with col11:
    st.subheader("💗 Recomendador de Películas")
    st.image(Image.open("imagen11.jpg"))
    st.write("Sugiere películas según tus preferencias.")
    st.markdown("💗 [Ir a la aplicación](https://recomendador-peliculas.streamlit.app/)")

with col12:
    st.subheader("💗 Traductor Multilingüe")
    st.image(Image.open("imagen12.jpg"))
    st.write("Traduce textos automáticamente a varios idiomas.")
    st.markdown("💗 [Ir a la aplicación](https://traductor-ia.streamlit.app/)")

st.write("---")

# === FILA 5 ===
col13, col14, col15 = st.columns(3)

with col13:
    st.subheader("💗 Detección de Emociones en Rostros")
    st.image(Image.open("imagen13.jpg"))
    st.write("Analiza expresiones faciales con redes neuronales.")
    st.markdown("💗 [Ir a la aplicación](https://emociones-faciales.streamlit.app/)")

with col14:
    st.subheader("💗 Generador de Música")
    st.image(Image.open("imagen14.jpg"))
    st.write("Crea melodías automáticas usando IA musical.")
    st.markdown("💗 [Ir a la aplicación](https://musica-ia.streamlit.app/)")

with col15:
    st.subheader("💗 Análisis de Datos")
    st.image(Image.open("imagen15.jpg"))
    st.write("Visualiza y analiza datos con ayuda de IA.")
    st.markdown("💗 [Ir a la aplicación](https://analisis-datos.streamlit.app/)")

st.write("---")

# 🌸 Pie de página
st.markdown(
    "<p style='text-align:center; color:#b30086;'>💗 Portafolio creado con amor y creatividad 💗</p>",
    unsafe_allow_html=True
)

