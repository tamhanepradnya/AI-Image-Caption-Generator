import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Image Caption Generator",
    page_icon="🖼️",
    layout="centered"
)

# -------------------------------
# Custom Styling
# -------------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .caption-box {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-top: 15px;
        font-size: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.markdown(
    '<div class="main-title">🖼️ AI-Based Image Caption Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Upload an image and let Artificial Intelligence generate a meaningful caption.'
    '</div>',
    unsafe_allow_html=True
)

# -------------------------------
# Load BLIP Model
# -------------------------------
@st.cache_resource
def load_model():

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    return processor, model


# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.header("📌 About the Project")

    st.write(
        "This application uses the BLIP "
        "(Bootstrapping Language-Image Pre-training) "
        "model to generate captions for uploaded images."
    )

    st.write("### Technologies")

    st.write("""
    • Python  
    • Streamlit  
    • Hugging Face Transformers  
    • BLIP  
    • PyTorch  
    • Pillow
    """)

# -------------------------------
# Load Model
# -------------------------------
with st.spinner("Loading AI model..."):
    processor, model = load_model()

# -------------------------------
# Image Upload
# -------------------------------
st.subheader("📤 Upload an Image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

# -------------------------------
# Process Image
# -------------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.write("")

    # -------------------------------
    # Generate Caption Button
    # -------------------------------
    if st.button("✨ Generate Caption", use_container_width=True):

        with st.spinner("AI is analyzing the image..."):

            inputs = processor(
                images=image,
                return_tensors="pt"
            )

            output = model.generate(
                **inputs,
                max_new_tokens=50
            )

            caption = processor.decode(
                output[0],
                skip_special_tokens=True
            )

        st.success("Caption Generated Successfully!")

        st.subheader("📝 Generated Caption")

        st.markdown(
            f'<div class="caption-box">"{caption}"</div>',
            unsafe_allow_html=True
        )

else:

    st.info("👆 Please upload an image to generate a caption.")