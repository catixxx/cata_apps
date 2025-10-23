import streamlit as st
from PIL import Image

# 🌸 CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Portafolio de Aplicaciones con IA", page_icon="💗", layout="wide")

# 🌷 ESTILO PERSONALIZADO (rosado suave con detalles femeninos)
st.markdown("""
    <style>
    /* Fondo general */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ffe6f9, #ffd9ec, #fff0f7);
    }

    /* Títulos */
    h1, h2, h3, h4 {
        color: #b13a8b;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
    }

    /* Subtítulo (nombre) */
    .nombre {
        color: #d16fa7;
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
    }

    /* Cards */
    .card {
        background-color: white;
        border-radius: 20px;
        box-shadow: 0px 4px 10px rgba(255, 180, 230, 0.5);
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease-in-out;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 6px 15px rgba(230, 140, 200, 0.7);
    }

    /* Imágenes */
    .card img {
        border-radius: 15px;
        width: 100%;
        height: 200px;
        object-fit: cover;
    }

    /* Botones */
    .boton {
        background-color: #ffb6d9;
        color: white;
        border: none;
        padding: 8px 20px;
        border-radius: 10px;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
        text-decoration: none;
        transition: background-color 0.3s ease-in-out;
        display: inline-block;
        margin-top: 10px;
    }
    .boton:hover {
        background-color: #ff8cc9;
        color: white;
    }

    /* Texto general */
    p {
        color: #6d4b5b;
        font-family: 'Poppins', sans-serif;
    }

    </style>
""", unsafe_allow_html=True)

# 🌸 TÍTULO PRINCIPAL
st.markdown("<h1 style='text-align: center;'>💗 Portafolio de Aplicaciones con Inteligencia Artificial 💗</h1>", unsafe_allow_html=True)
st.markdown("<p class='nombre'>Catalina Sanabria Monares 🌷</p>", unsafe_allow_html=True)
st.write("---")

# 🌼 CONTENEDOR DE TARJETAS
col1, col2, col3 = st.columns(3)

# --- COLUMNA 1 ---
with col1:
    st.markdown("""
        <div class="card">
            <img src="https://i.pinimg.com/originals/ee/09/a4/ee09a4d0e1e5fa0e078a8f4f434836ed.jpg" alt="Intro">
            <h3>💖 Introducción</h3>
            <p>Presentación general del portafolio.</p>
            <a href="https://imultimod.streamlit.app/" target="_blank" class="boton">🌸 Ir a la aplicación</a>
        </div>
    """, unsafe_allow_html=True)

# --- COLUMNA 2 ---
with col2:
    st.markdown("""
        <div class="card">
            <img src="https://i.pinimg.com/originals/d3/6c/a5/d36ca5f17b7cf97d6c8ecf132ac99ad2.jpg" alt="Intro 2">
            <h3>💖 Introducción 2</h3>
            <p>Segunda práctica introductoria.</p>
            <a href="https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/" target="_blank" class="boton">🌸 Ir a la aplicación</a>
        </div>
    """, unsafe_allow_html=True)

# --- COLUMNA 3 ---
with col3:
    st.markdown("""
        <div class="card">
            <img src="https://i.pinimg.com/originals/9a/b4/1c/9ab41c0f0e26b5e4acb8e18e3472b2c7.jpg" alt="Voz a Texto">
            <h3>💖 Voz a Texto</h3>
            <p>Convierte voz en texto (traductor).</p>
            <a href="https://traductor-ab0sp9f6fi.streamlit.app/" target="_blank" class="boton">🌸 Ir a la aplicación</a>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 🌸 SEGUNDA FILA DE TARJETAS
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
        <div class="card">
            <img src="https://i.pinimg.com/originals/d2/59/9c/d2599cf0909b3b9cecc0ef8c7995a1d9.jpg" alt="OCR">
            <h3>💖 OCR</h3>
            <p>Reconocimiento de texto en imágenes.</p>
            <a href="https://vision2-gpt4o.streamlit.app/" target="_blank" class="boton">🌸 Ir a la aplicación</a>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
        <div class="card">
            <img src="https://i.pinimg.com/originals/16/63/bf/1663bfa88a7f74e54dcb278a1a58a47c.jpg" alt="Analisis">
            <h3>💖 Análisis de Sentimiento</h3>
            <p>Detecta emociones en texto.</p>
            <a href="https://asistpy-csv.streamlit.app/" target="_blank" class="boton">🌸 Ir a la aplicación</a>
        </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
        <div class="card">
            <img src="https://i.pinimg.com/originals/d5/bb/a7/d5bba7b52e61b04de3e9b926bdce1ee9.jpg" alt="Chat PDF">
            <h3>💖 Chat PDF</h3>
            <p>Consulta documentos usando IA.</p>
            <a href="https://chatpdf-cc.streamlit.app/" target="_blank" class="boton">🌸 Ir a la aplicación</a>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align:center; color:#b13a8b;'>💗 Gracias por visitar mi portafolio 💗</p>", unsafe_allow_html=True)

