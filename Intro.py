import streamlit as st
from PIL import Image

# 🌸 Estilo personalizado femenino y delicado
st.markdown("""
    <style>
    /* Fondo general */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #fff6fb, #fbeeff, #fffaff);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffe6f7, #f5e4ff);
        color: #5b4b52;
        font-family: 'Poppins', sans-serif;
    }

    /* Títulos */
    h1, h2, h3, h4 {
        color: #c76ba4;
        font-family: 'Poppins', sans-serif;
    }

    /* Texto general */
    .stMarkdown, .stText {
        color: #5c4b51;
        font-family: 'Poppins', sans-serif;
    }

    /* Imágenes */
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0px 0px 10px rgba(235, 180, 210, 0.6);
    }

    /* Enlaces */
    a {
        color: #c76ba4 !important;
        text-decoration: none;
        font-weight: 600;
    }
    a:hover {
        color: #ff8ec6 !important;
    }

    /* Subtítulos */
    h3, h4 {
        border-bottom: 2px solid #ffd6ea;
        padding-bottom: 5px;
    }

    /* Divisor */
    hr {
        border: none;
        border-top: 2px dashed #f3b2d0;
    }
    </style>
""", unsafe_allow_html=True)


# 🌷 Título principal
st.title("🌸 Portafolio de aplicaciones con Inteligencia Artificial 🌸")

with st.sidebar:
    st.subheader("✨ Aplicaciones con Inteligencia Artificial ✨")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("Catalina Sanabria Monares")

# 🌼 Columnas principales
col1, col2, col3, col4, col5 = st.columns(5)

# --- COLUMNA 1 ---
with col1:
    st.subheader("💗 Intro")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
    url = "https://imultimod.streamlit.app/"
    st.write(f"Texto a voz: [Enlace]({url})")

    st.subheader("💗 Interfaz texto_voz")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

    st.subheader("💗 Interfaz voz_texto")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

# --- COLUMNA 2 ---
with col2: 
    st.subheader("💗 Interfaz OCR")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
    url = "https://traductor-ab0sp9f6fi.streamlit.app/"
    st.write(f"Voz a texto: [Enlace]({url})")

    st.subheader("💗 Analisis de Sentimiento")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
    url = "https://asistpy-csv.streamlit.app/"
    st.write(f"Datos: [Enlace]({url})")

    st.subheader("💗 Analisis de texto (ingles)")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
    url = "https://transcript-whisper.streamlit.app/"
    st.write(f"Transcriptor: [Enlace]({url})")

# --- COLUMNA 3 ---
with col3: 
    st.subheader("💗 Analisis de texto (español)")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

    st.subheader("💗 Reconocimiento de objeto en imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")
 
    st.subheader("💗 Reconocimiento de gestos")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

# --- COLUMNA 4 ---
with col4: 
    st.subheader("💗 Chat pdf")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

    st.subheader("💗 Interpretacion de imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")
 
    st.subheader("💗 Interfaz tactil")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

# --- COLUMNA 5 ---
with col5: 
    st.subheader("💗 Aplicacion de reconocimiento de bocetos")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

    st.subheader("💗 Control MQTT (Botones)")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")
 
    st.subheader("💗 Control MQTT (Voz)")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

# 🌷 Línea final decorativa
st.markdown("---")
st.markdown("<div style='text-align:center; color:#c76ba4;'>✨ Hecho con amor y curiosidad por Catalina ✨</div>", unsafe_allow_html=True)

