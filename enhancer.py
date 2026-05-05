import os
import urllib.request
import torch
import cv2
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet

# Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

MODEL_URL = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/RealESRGAN_x4plus.pth"
MODEL_PATH = "weights/RealESRGAN_x4plus.pth"

def load_model():
    os.makedirs("weights", exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        print("Downloading model weights...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Download complete!")

    model = RRDBNet(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_block=23,
        num_grow_ch=32,
        scale=4
    )

    upsampler = RealESRGANer(
        scale=4,
        model_path=MODEL_PATH,
        model=model,
        tile=128,
        tile_pad=10,
        pre_pad=0,
        half=False
    )

    return upsampler


def enhance_image(input_path, output_path, progress_callback=None):

    # STEP 1
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)
    if progress_callback:
        progress_callback("Step 1: Reading image...", 10)

    # STEP 2
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = gray.mean()

    if brightness < 110:
        img = cv2.convertScaleAbs(img, alpha=1.05, beta=3)

    if progress_callback:
        progress_callback("Step 2: Brightness correction...", 25)

    # STEP 3
    max_size = 400
    h, w = img.shape[:2]

    if max(h, w) > max_size:
        scale = max_size / max(h, w)
        img = cv2.resize(img, (int(w * scale), int(h * scale)))

    if progress_callback:
        progress_callback("Step 3: Resizing...", 40)

    # STEP 4
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if progress_callback:
        progress_callback("Step 4: Preparing for AI...", 55)

    # 🔥 LOAD MODEL HERE (fixes freezing)
    upsampler = load_model()

    # STEP 5
    output, _ = upsampler.enhance(img, outscale=2)
    if progress_callback:
        progress_callback("Step 5: AI Upscaling...", 85)

    # STEP 6
    cv2.imwrite(output_path, cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
    if progress_callback:
        progress_callback("Step 6: Done!", 100)

    return output_path