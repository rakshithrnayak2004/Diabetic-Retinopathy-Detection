# 👁️ Diabetic Retinopathy Detection Using Deep Learning (ImageNet vs ResNet)

This project focuses on automated **Diabetic Retinopathy (DR) detection** using deep learning.  
Two powerful models — **ResNet** and **ImageNet (Transfer Learning)** — were compared for classifying retinal fundus images.  

After experimentation, the **ImageNet-based model achieved 96% accuracy**, outperforming **ResNet’s 92%**.

---

## 🧠 Overview

Diabetic Retinopathy (DR) is a diabetes complication that affects the eyes and can lead to blindness.  

This project aims to develop an automated system that classifies the severity of DR using deep learning, helping in **early detection and prevention of vision loss**.

---

## 🚀 Features

- 🧩 Comparison between **ResNet and ImageNet transfer learning models**
- 🩺 ImageNet model achieved **96% accuracy** — selected as the final classifier
- 🧠 Multi-class classification of diabetic retinopathy (**5 stages**)
- 🧾 Flask-based web app for uploading and predicting images
- 📊 Visualization of training accuracy, loss, and confusion matrix
- 💾 Trained model saved as `imagenet_dr_model.pt` for deployment

---

## 🏗️ Architecture & Workflow

- **Dataset** — APTOS 2019 Blindness Detection  
- **Preprocessing** — Image resizing (224×224), normalization, and data augmentation  

### Model Training
- **ResNet**: Baseline model (**92% accuracy**)  
- **ImageNet (Transfer Learning)**: Fine-tuned model (**96% accuracy ✅**)  

### Evaluation
- Accuracy  
- Loss  
- F1-score  
- Confusion matrix  

### Deployment
- Flask web application with a simple interface  

---

## 📊 Model Comparison

| Model | Training Accuracy | Validation Accuracy | Remarks |
|------|------------------|--------------------|--------|
| ResNet | 92% | 84% | Strong baseline |
| ImageNet (Transfer Learning) | **96%** | **90%** | ✅ Best performing model |

The ImageNet fine-tuned model showed **excellent generalization and stability** across all DR stages.

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | HTML5, CSS3, Bootstrap |
| Backend | Python (Flask) |
| Deep Learning Framework | PyTorch |
| Model Architectures | ResNet, ImageNet |
| Dataset | APTOS 2019 Blindness Detection |
| IDE/Tools | Google Colab, VS Code |
| Version Control | Git & GitHub |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rakshithrnayak2004/Diabetic-Retinopathy-Detection.git
