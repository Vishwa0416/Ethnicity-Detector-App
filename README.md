# 🧬 Ethnicity Detector App

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)
![PyTorch](https://img.shields.io/badge/Powered%20By-PyTorch-blue?logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A lightweight, Streamlit-based web app that uses the **FairFace deep learning model** to detect faces and predict **ethnicity** from uploaded images. This project lays the foundation for future enhancements such as **age estimation** and **height prediction**.

---

## ✨ Features

- 📤 **Upload Image**: Upload photos containing one or more human faces.
- 🧠 **Ethnicity Prediction**: Uses FairFace to detect and classify faces into one of several ethnicity categories.
- 🖼️ **Real-Time Face Detection**: Automatically detects all faces in an image and displays predictions.
- 🌐 **Web-Based Interface**: Clean and interactive UI powered by Streamlit.
- 🔧 **Future-Ready**: Modular code structure — easily extendable to include age and height estimation using additional models.

---

## 📸 Demo

![App Demo](https://user-images.githubusercontent.com/your-gif-or-image-link.gif)


---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python ≥ 3.8 installed. Then install the required dependencies:


---

# 📁 Project Structure
bash
Copy
Edit
Ethnicity-Detector-App/
│
├── model/
│   ├── res34_fair_align_multi_4_20190809.pt     # (Deleted from repo history to reduce size)
│   └── res34_fair_align_multi_7_20190809.pt     # (Deleted from repo history)
│
├── app.py                # Main Streamlit app
├── utils.py              # Preprocessing and prediction utilities
├── .gitignore
└── README.md
---

