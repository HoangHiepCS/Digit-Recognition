import torch
import torchvision.transforms as transforms
from PIL import Image

def preprocess_image(frame):
    # Chuyển sang grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Resize ảnh về kích thước mà mô hình yêu cầu (giả sử là 28x28)
    resized = cv2.resize(gray, (28, 28))
    
    # Chuyển sang  dạng tensor
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    image_tensor = transform(Image.fromarray(resized))

    image_tensor = image_tensor.unsqueeze(0)

    return image_tensor
