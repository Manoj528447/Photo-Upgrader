# 📸 Photo Upgrader

Enhance low-quality images using AI-powered upscaling, denoising, and smart preprocessing.

---

## 🚀 Features

- 🔍 AI Image Enhancement using RealESRGAN  
- 🧠 Smart Brightness Correction (adaptive)  
- 🧼 Noise Reduction  
- 🔼 Image Upscaling  
- 📊 Interactive Before vs After Comparison  
- ⚡ Step-by-step Processing UI (Streamlit)  
- 💾 Download Enhanced Image  

---

## 🧠 How It Works

This project uses a hybrid pipeline:

### 1. Preprocessing
- Detect image brightness  
- Apply correction only if needed  
- Resize image to prevent memory issues  

### 2. AI Enhancement
- RealESRGAN deep learning model  
- Super-resolution + denoising  

### 3. Post Processing
- Convert formats  
- Display results  
- Enable download  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- OpenCV  
- PyTorch  
- RealESRGAN  
- BasicSR  

---

## 📦 Installation

### 1. Clone repository

```bash
git clone https://github.com/Manoj528447/Photo-Upgrader.git
cd Photo-Upgrader
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add model weights

Download the model file:  
👉 RealESRGAN_x4plus.pth  

Place it inside:
```
weights/RealESRGAN_x4plus.pth
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
AI-Photo-Upgrader/
│
├── app.py              # Streamlit UI
├── enhancer.py         # AI processing logic
├── requirements.txt
├── README.md
├── weights/
│   └── RealESRGAN_x4plus.pth
```

---

## 🧪 Usage

1. Upload an image  
2. Click **Enhance Image**  
3. View enhanced result with comparison  
4. Download the enhanced image  

---

## ⚡ Optimization

To improve performance on CPU:

- Images are resized before processing  
- Upscaling factor reduced to 2x  
- Memory-safe tiling (`tile=128`) is used  

---

## ⚠️ Limitations

- Extremely blurry or overexposed images may not fully recover details  
- CPU-based processing may be slower  
- High-resolution images are resized for memory safety  

---

## 🚀 Future Improvements

- GPU acceleration support  
- Better color correction  
- Batch image processing  
- Web deployment  

---

## 👨‍💻 Author

**Manoj Prasad**  
MCA Graduate | AI Enthusiast  

---