# 🖼️ AI-Based Image Caption Generator

## 📌 Project Overview

The AI-Based Image Caption Generator is a web application that uses Artificial Intelligence and Deep Learning to automatically generate meaningful textual descriptions for uploaded images.

The application accepts an image from the user and uses the BLIP image-captioning model to analyze the image and generate a caption.

---

## 🎯 Objective

The main objective of this project is to develop an AI-based application that can understand the visual content of an image and automatically generate a meaningful text description.

---

## 🚀 Features

- Upload JPG, JPEG, and PNG images
- Display the uploaded image
- Analyze the image using an AI model
- Automatically generate an image caption
- Simple and user-friendly web interface
- Fast caption generation after the model is loaded

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- BLIP
- PyTorch
- Pillow

---

## 🤖 AI Model

This project uses:

**Salesforce/blip-image-captioning-base**

BLIP is an image-language model that can be used for image captioning and other vision-language tasks.

---

## 🔄 Working Process

```text
Upload Image
     ↓
Streamlit Application
     ↓
Image Processing using Pillow
     ↓
BLIP AI Model
     ↓
Image Analysis
     ↓
Caption Generation
     ↓
Display Generated Caption