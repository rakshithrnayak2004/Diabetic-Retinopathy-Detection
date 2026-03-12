import os
import torch
import timm
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for
from flask import Flask, render_template, url_for


app = Flask(__name__)

# Create a directory for uploads
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the model
MODEL_PATH = r"deit_base_patch16_224_9.pt"
device = torch.device("cpu")

model = timm.create_model('deit_base_patch16_224', pretrained=False, num_classes=5)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()

# Image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Label mapping
label_map = {
    0: "No DR",
    1: "Mild DR",
    2: "Moderate DR",
    3: "Severe DR",
    4: "Proliferative DR"
}

uploaded_file_path = None  # Store uploaded file path

@app.route("/")
@app.route("/home")  # Add this line
def home():
    return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    global uploaded_file_path
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("test.html", error="No file uploaded")

        file = request.files["file"]
        if file.filename == "":
            return render_template("test.html", error="No selected file")

        uploaded_file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(uploaded_file_path)

        return redirect(url_for("predict"))

    return render_template("test.html")

@app.route("/predict")
def predict():
    global uploaded_file_path
    if not uploaded_file_path:
        return redirect(url_for("test"))

    image = Image.open(uploaded_file_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        prediction = label_map[predicted.item()]

    return render_template("predict.html", prediction=prediction, image_url=uploaded_file_path)

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")




if __name__ == "__main__":
    app.run(debug=True)
