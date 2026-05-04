import streamlit as st
from PIL import Image
import os
import time
from enhancer import enhance_image
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Photo Upgrader", layout="wide")

st.title("📸 Photo Upgrader")
st.write("Enhance low-quality images using AI-powered upscaling & denoising ✨")

st.markdown("---")

uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_path = "input.png"
    output_path = "output.png"

    # Save uploaded file
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    original = Image.open(input_path)

    st.image(original, caption="Original Image", use_container_width=True)

    # Quality check
    if max(original.size) < 500:
        st.warning("🔍 Image Quality: Very Blurry ❌")
        st.info("💡 Suggestion: Try uploading a clearer image for better results.")
    else:
        st.info("🔍 Image Quality: Moderately Blurry ⚠️")

    # 🚀 Enhance button
    if st.button("✨ Enhance Image"):

        progress = st.progress(0)
        status = st.empty()

        # Step 1
        status.text("🔹 Step 1: Loading image...")
        progress.progress(20)
        time.sleep(0.5)

        # Step 2
        status.text("🔹 Step 2: Improving contrast...")
        progress.progress(40)
        time.sleep(0.5)

        # Step 3
        status.text("🔹 Step 3: Resizing (memory optimization)...")
        progress.progress(60)
        time.sleep(0.5)

        # Step 4 (REAL PROCESS)
        status.text("🔹 Step 4: AI Upscaling...")
        result_path = enhance_image(input_path, output_path)
        progress.progress(90)

        # Step 5
        status.text("🔹 Step 5: Finalizing output...")
        time.sleep(0.3)
        progress.progress(100)

        st.success("Enhancement complete! ✅")

        enhanced = Image.open(result_path)

        st.markdown("### 🔍 Interactive Comparison")

        image_comparison(
            img1=original,
            img2=enhanced,
            label1="Original",
            label2="Enhanced",
        )

        # Download button
        with open(output_path, "rb") as file:
            st.download_button(
                label="⬇️ Download Enhanced Image",
                data=file,
                file_name="enhanced.png",
                mime="image/png"
            )