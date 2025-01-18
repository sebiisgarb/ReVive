import torch
from torchvision import transforms
from PIL import Image
import os

class ImageRestorer:
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = torch.load(model_path, map_location=self.device)
        self.model.eval()

    def restore_image(self, input_path, output_path):
        # Încarcă imaginea
        img = Image.open(input_path).convert("RGB")

        # Transformare pentru model
        transform = transforms.Compose([transforms.ToTensor()])
        img_tensor = transform(img).unsqueeze(0).to(self.device)

        # Rulează modelul
        with torch.no_grad():
            restored_tensor = self.model(img_tensor)

        # Conversie înapoi la imagine
        restored_img = transforms.ToPILImage()(restored_tensor.squeeze(0).cpu())
        restored_img.save(output_path)
        return output_path
