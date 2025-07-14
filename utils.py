from PIL import Image
import torch
import torchvision.transforms as transforms

ethnicity_labels = ['White', 'Black', 'Latino_Hispanic', 'East Asian', 'Southeast Asian', 'Indian', 'Middle Eastern']

def load_model(path='model/ethnicity_model.pt'):
    model = torch.load(path, map_location=torch.device('cpu'))
    model.eval()
    return model

def preprocess_image(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0)

def predict_ethnicity(model, image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
    return ethnicity_labels[predicted.item()]
