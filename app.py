import streamlit as st
from PIL import Image
from utils import load_model, preprocess_image, predict_ethnicity

st.set_page_config(page_title="Ethnicity Detector", layout="centered")
st.title("🧬 Ethnicity Detection from Photo")

uploaded_file = st.file_uploader("Upload a clear photo of a person's face", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    model = load_model()
    img_tensor = preprocess_image(image)
    prediction = predict_ethnicity(model, img_tensor)

    st.success(f"Predicted Ethnicity: **{prediction}**")
