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
    st.write("Primera aplicacion.")
    st.markdown("💗 [Ir a la aplicación](https://miprimeraappcatixx.streamlit.app/)")

with col2:
    st.subheader("💗 Texto a voz")
    st.image(Image.open("imagen2.jpg"))
    st.write("Convierte texto a audio")
    st.markdown("💗 [Ir a la aplicación]( https://pagina2profe.streamlit.app/)")

with col3:
    st.subheader("💗 Voz a Texto")
    st.image(Image.open("imagen3.jpg"))
    st.write("Convierte voz en texto usando IA.")
    st.markdown("💗 [Ir a la aplicación](https://pbeo6cxaxwky2mxj3cxj57.streamlit.app/)")

st.write("---")

# === FILA 2 ===
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("💗 Interfaz OCR ")
    st.image(Image.open("imagen4.jpg"))
    st.write("Reconocimiento optico de caracteres")
    st.markdown("💗 [Ir a la aplicación]( https://ocr-audio-sunwazxyy3htz7w8eqm7yn.streamlit.app/)")

with col5:
    st.subheader("💗 Analisis de Sentimiento")
    st.image(Image.open("imagen5.jpg"))
    st.write("Reconoce emociones de un texto")
    st.markdown("💗 [Ir a la aplicación](https://3uxhnpwvxuwdawcd85n3ee.streamlit.app/)")

with col6:
    st.subheader("💗 Analisis de texto (Ingles)")
    st.image(Image.open("imagen6.jpg"))
    st.write("Explora la relación entre los textos y una pregunta")
    st.markdown("💗 [Ir a la aplicación](https://aafml3fw2lsqviu7k6dyjm.streamlit.app/)")

st.write("---")

# === FILA 3 ===
col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("💗  Analisis de texto (Español)")
    st.image(Image.open("imagen7.jpg"))
    st.write("Analiza el texto puesto desde preguntas")
    st.markdown("💗 [Ir a la aplicación](https://uzvwnqkgpdvyafmupea9fu.streamlit.app/")

with col8:
    st.subheader("💗 Reconocimiento de Objetos")
    st.image(Image.open("imagen8.jpg"))
    st.write("Reconoce los objetos de una imagen")
    st.markdown("💗 [Ir a la aplicación](https://7gfmxhghfykz3hqwd5rtgw.streamlit.app/)")

with col9:
    st.subheader("💗 Reconocimiento de Gestos")
    st.image(Image.open("imagen9.jpg"))
    st.write("Interpreta movimientos usando visión computacional.")
    st.markdown("💗 [Ir a la aplicación](https://bzllgjxt9zzhxw72snvu7p.streamlit.app/)")

st.write("---")

# === FILA 4 ===
col10, col11, col12 = st.columns(3)

with col10:
    st.subheader("💗 Chat PDF")
    st.image(Image.open("imagen10.jpg"))
    st.write("Analiza el contenido de un documento PDF.")
    st.markdown("💗 [Ir a la aplicación](https://ajjmaezetnmmeds42r2ttl.streamlit.app/)")

with col11:
    st.subheader("💗 Interpretacion de imagen")
    st.image(Image.open("imagen11.jpg"))
    st.write("Análisis avanzado de imágenes con IA.")
    st.markdown("💗 [Ir a la aplicación](https://yz2rgx5rxrqsnrjbegaw8d.streamlit.app/)")

with col12:
    st.subheader("💗 Interfaz Tactil")
    st.image(Image.open("imagen12.jpg"))
    st.write("Puedes hacer dibujos en un tablero.")
    st.markdown("💗 [Ir a la aplicación](https://tablero-6pbavfx8iqfyobyfffug4g.streamlit.app/)")

st.write("---")

# === FILA 5 ===
col13, col14, col15 = st.columns(3)

with col13:
    st.subheader("💗 Reconocimiento de bocetos")
    st.image(Image.open("imagen13.jpg"))
    st.write("Analiza los dibujos que se hagan en el tablero.")
    st.markdown("💗 [Ir a la aplicación](https://drawrecog-htvmekqhjm2psqx3huthk9.streamlit.app/)")

with col14:
    st.subheader("💗 Control MQTT (Botones)")
    st.image(Image.open("imagen14.jpg"))
    st.write("Control de dispositivos mediante MQTT y botones.")
    st.markdown("💗 [Ir a la aplicación](https://sendcmqtt-cvddr5bndohn3vf69tazjd.streamlit.app/)")

with col15:
    st.subheader("💗 Control MQTT (Voz)")
    st.image(Image.open("imagen15.jpg"))
    st.write("Control de dispositivos mediante comandos de voz.")
    st.markdown("💗 [Ir a la aplicación] (https://ctrlvoice-cwg7b2khfj2a7r2q4trjtu.streamlit.app/)")

st.write("---")

# 🌸 Pie de página
st.markdown(
    "<p style='text-align:center; color:#b30086;'>💗 Fin del portafolio  💗</p>",
    unsafe_allow_html=True
)

