import torch
import cv2
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet

# Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Model architecture
model = RRDBNet(
    num_in_ch=3,
    num_out_ch=3,
    num_feat=64,
    num_block=23,
    num_grow_ch=32,
    scale=4
)

# Upsampler (memory safe)
upsampler = RealESRGANer(
    scale=4,
    model_path='weights/RealESRGAN_x4plus.pth',
    model=model,
    tile=128,
    tile_pad=10,
    pre_pad=0,
    half=False
)


def enhance_image(input_path, output_path, progress_callback=None):

    # STEP 1: Read image
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)

    if progress_callback:
        progress_callback("Step 1: Reading image...", 10)

    # STEP 2: Smart brightness fix (ONLY if dark)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = gray.mean()

    if brightness < 110:
        img = cv2.convertScaleAbs(img, alpha=1.05, beta=3)

    if progress_callback:
        progress_callback("Step 2: Brightness correction...", 25)

    # STEP 3: Resize (prevent memory crash)
    max_size = 400
    h, w = img.shape[:2]

    if max(h, w) > max_size:
        scale = max_size / max(h, w)
        img = cv2.resize(img, (int(w * scale), int(h * scale)))

    if progress_callback:
        progress_callback("Step 3: Resizing...", 40)

    # STEP 4: Convert BGR → RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if progress_callback:
        progress_callback("Step 4: Preparing for AI...", 55)

    # STEP 5: AI Upscaling
    output, _ = upsampler.enhance(img, outscale=2)

    if progress_callback:
        progress_callback("Step 5: AI Upscaling...", 85)

    # STEP 6: Save image
    cv2.imwrite(output_path, cv2.cvtColor(output, cv2.COLOR_RGB2BGR))

    if progress_callback:
        progress_callback("Step 6: Done!", 100)

    return output_path