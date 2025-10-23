import streamlit as st
from PIL import Image

st.set_page_config(page_title="Aplicaciones IA", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center; color: #C71585;'>🌸 Galería de Aplicaciones con Inteligencia Artificial 🌸</h1>
    <p style='text-align: center;'>Explora diferentes proyectos interactivos desarrollados con herramientas de IA y diseño creativo.</p>
    """,
    unsafe_allow_html=True
)

# ---- Filas de tarjetas ----
col1, col2, col3 = st.columns(3)

# --------- COLUMNA 1 ----------
with col1:
    st.subheader("💗 Aplicación de reconocimiento de bocetos")
    image = Image.open("Chat_pdf.png")
    st.image(image, width=150)
    st.write("Una app que usa RAG para analizar contenido de un PDF.")
    st.write("[Abrir app](https://chatpdf-cc.streamlit.app/)")

    st.subheader("💗 Clasificación de flores")
    image = Image.open("flowers.png")
    st.image(image, width=150)
    st.write("Modelo entrenado para identificar tipos de flores a partir de una imagen.")
    st.write("[Abrir app](https://flowers-cc.streamlit.app/)")

    st.subheader("💗 Estilo artístico con IA")
    image = Image.open("art_style.png")
    st.image(image, width=150)
    st.write("Transforma tus fotos en obras de arte con distintos estilos artísticos.")
    st.write("[Abrir app](https://artstyle-cc.streamlit.app/)")

    st.subheader("💗 Asistente de recetas inteligentes")
    image = Image.open("chef.png")
    st.image(image, width=150)
    st.write("Escribe los ingredientes que tengas y genera una receta única.")
    st.write("[Abrir app](https://smartchef-cc.streamlit.app/)")

    st.subheader("💗 Reconocimiento facial básico")
    image = Image.open("face_recognition.png")
    st.image(image, width=150)
    st.write("Una herramienta para detectar rostros en fotografías.")
    st.write("[Abrir app](https://faceai-cc.streamlit.app/)")

# --------- COLUMNA 2 ----------
with col2:
    st.subheader("💗 Análisis de sentimientos")
    image = Image.open("sentiment.png")
    st.image(image, width=150)
    st.write("Analiza textos y detecta emociones positivas o negativas.")
    st.write("[Abrir app](https://sentiment-cc.streamlit.app/)")

    st.subheader("💗 Detección de objetos")
    image = Image.open("object_detect.png")
    st.image(image, width=150)
    st.write("Modelo que identifica distintos objetos en imágenes.")
    st.write("[Abrir app](https://objectdetect-cc.streamlit.app/)")

    st.subheader("💗 Generador de poemas")
    image = Image.open("poem.png")
    st.image(image, width=150)
    st.write("Crea poemas únicos a partir de una palabra o tema.")
    st.write("[Abrir app](https://poemai-cc.streamlit.app/)")

    st.subheader("💗 Traductor multilingüe")
    image = Image.open("translator.png")
    st.image(image, width=150)
    st.write("Traduce texto entre varios idiomas usando IA.")
    st.write("[Abrir app](https://translator-cc.streamlit.app/)")

    st.subheader("💗 Generador de voces")
    image = Image.open("voice.png")
    st.image(image, width=150)
    st.write("Convierte texto en voz con diferentes tonos y acentos.")
    st.write("[Abrir app](https://voiceai-cc.streamlit.app/)")

# --------- COLUMNA 3 ----------
with col3:
    st.subheader("💗 Generador de imágenes")
    image = Image.open("image_gen.png")
    st.image(image, width=150)
    st.write("Crea imágenes a partir de descripciones escritas.")
    st.write("[Abrir app](https://imagegen-cc.streamlit.app/)")

    st.subheader("💗 Clasificador de frutas")
    image = Image.open("fruit.png")
    st.image(image, width=150)
    st.write("Reconoce qué fruta aparece en la imagen.")
    st.write("[Abrir app](https://fruitai-cc.streamlit.app/)")

    st.subheader("💗 Detector de emociones faciales")
    image = Image.open("emotion.png")
    st.image(image, width=150)
    st.write("Identifica emociones humanas a partir de expresiones faciales.")
    st.write("[Abrir app](https://emotion-cc.streamlit.app/)")

    st.subheader("💗 Analizador de audio")
    image = Image.open("audio.png")
    st.image(image, width=150)
    st.write("Analiza audios para extraer información y clasificar sonidos.")
    st.write("[Abrir app](https://audio-cc.streamlit.app/)")

    st.subheader("💗 Generador de música")
    image = Image.open("music.png")
    st.image(image, width=150)
    st.write("Crea música con base en tus emociones o descripciones.")
    st.write("[Abrir app](https://musicai-cc.streamlit.app/)")
