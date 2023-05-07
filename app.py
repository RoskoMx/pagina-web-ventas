from pathlib import Path
import streamlit as st
from PIL import Image 

#Ajustes de rutas
this_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
assets_dir = this_dir / "assets"
styles_dir = this_dir / "styles"
css_file = styles_dir / "main.css"

#Ajustes generales. Editar con los datos de tu producto
stripe_chekout_url = "url de stripe"
contact_email = "tu email"
product_name = "nombre del producto"
product_tagline = "Lema del producto"
demo_video_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
product_description = """
Esta es la descripción del producto digital que prentendemos vender en nuestra landing page. Vamos a poner a continuación algunos puntos interesantes a saber sobre nuestro producto:

- Punto 1
- Punto 2
- Punto 3
- Punto 4

***esto es un ejemplo de texto en negrita***
"""

#Ajustes visuales de la página. No es necestario editar nada
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#Ajustes de la página. No es necestario editar nada
st.set_page_config(
    page_title= product_name,
    page_icon= ":star:",
    layout= "centered",
    initial_sidebar_state= "collapsed", 
)

local_css(css_file)


#SECCIÓN PRINCIPAL. No es necesario editar nada
st.header(product_name)
st.subheader(product_tagline)
left_column, right_column = st.columns((2,1))
with left_column:
    st.text("")
    st.write(product_description)
    st.markdown(
        f'<a href="{stripe_chekout_url}" class="button">👉🏼 Comprar aquí</a>',
        unsafe_allow_html=True,
    )

with right_column:
    product_image = Image.open(assets_dir / "product_image.png")
    st.image(product_image, width=450) 


#SECCIÓN DE CARACTERÍSTICAS. Editar cabeceras y descripciones de las características de tu producto
st.write("")
st.write("---")
st.subheader(":rocket: Características")


features = {
    "feature_1.png": ["cabecera de la característica 1",
    "Aquí vendría la descripción de la característica 1",],
    "feature_2.png": ["cabecera de la característica 2",
    "Aquí vendría la descripción de la característica 2",],
    "feature_3.png": ["cabecera de la característica 3",
    "Aquí vendría la descripción de la característica 3",],
}


for image, description in features.items():
    image = Image.open(assets_dir / image)
    st.write("")
    left_column, right_column = st.columns(2) 
    left_column.image(image, use_column_width=True)
    right_column.subheader(f"**{description[0]}**")
    right_column.write(description[1])


#SECCIÓN DEMO VÍDEO. Editar con el enlace de tu vídeo de demostración. Si no tienes puedes eliminar esta sección
st.write("")
st.write("---")
st.subheader(":tv: Demo video")
st.video(demo_video_url, format="video/mp4", start_time=0)

#SECCIÓN FAQ. Editar con las preguntas frecuentes de tu producto
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "¿Pregunta 1?": "Respuesta 1",
    "¿Pregunta 2?": "Respuesta 2",
    "¿Pregunta 3?": "Respuesta 3",
    "¿Pregunta 4?": "Respuesta 4",
    "¿Pregunta 5?": "Respuesta 5",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


#SECCION DE CONTACTO. Aqui no necesitas editar nada pero en ajustes generales debes indicar tu email de contacto
st.write("")
st.write("---")
st.subheader(":mailbox: Tienes alguna duda? Contacta con nosotros")

contact_form = f"""
<form action="https://formsubmit.co/{contact_email}" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Tu nombre" required>
     <input type="email" name="email" placeholder = "Tu email" required>
    <textarea name="message" placeholder = "Tu mensaje aquí" required></textarea>
     <button type="submit" class ="button" >Enviar ✉️</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True) 

