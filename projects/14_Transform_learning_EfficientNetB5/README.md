# 🖼️ Transfer Learning EfficientNetB5 – Men vs Women Classification

## 📌 Overview
This project showcases transfer learning with EfficientNetB5 for high-performance men vs women image classification.  
Using a state-of-the-art architecture with large input sizes, this implementation achieves excellent accuracy with feature extraction and fine-tuning approaches.

---

## 📂 Project Structure

```
14_Transform_learning_EfficientNetB5/
├── notebook/
│   └── 14_Transform_learning_EfficientNetB5.ipynb  # Main implementation
```

---

## 🧠 Key Concepts
- Transfer learning with EfficientNetB5 (modern architecture)
- Large input resolution (456x456) for better performance
- Feature extraction and fine-tuning approaches
- Data augmentation (horizontal flip, rotation, zoom)
- Small batch size (8) due to large model and input size
- Binary classification with sigmoid activation
- Adam optimizer with careful learning rate management

---

## ✅ Result Summary
- **Base model**: EfficientNetB5 (ImageNet pre-trained)
- **Input size**: 456x456 RGB images (high resolution)
- **Dataset**: 2000 train, 400 validation, 400 test images
- **Batch size**: 8 (memory efficient)
- **Feature extraction test accuracy**: **0.938 (93.8%)**
- **Fine-tuning test accuracy**: **0.930 (93.0%)**
- **Best performance**: Feature extraction with EfficientNetB5

Confusion Matrix:

| Class | Performance |
|-------|-------------|
| Men   | Excellent classification |
| Women | Excellent classification |

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `tensorflow` / `keras` | EfficientNetB5 model, transfer learning |
| `matplotlib` | Training visualization |
| `numpy` | Data processing |

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the notebook:
   ```bash
   jupyter notebook notebook/14_Transform_learning_EfficientNetB5.ipynb
   ```

---

## 💡 Learnings

- Modern architectures like EfficientNet achieve state-of-the-art performance
- Higher input resolutions significantly improve accuracy
- Feature extraction often outperforms fine-tuning for smaller datasets
- EfficientNet's compound scaling provides excellent efficiency-accuracy trade-off
- Careful batch size management is crucial for large models

## 🚀 Future Improvements

- Experiment with even larger EfficientNet variants (B6, B7)
- Implement progressive resizing during training
- Add test-time augmentation for better inference
- Compare with other modern architectures (ConvNeXt, ViT)
- Implement advanced fine-tuning strategies (discriminative learning rates)