# 🐱🐶 AlexNet CNN – Cat vs Dog Classification

## 📌 Overview
This project implements **AlexNet convolutional neural network architecture** for binary image classification of **cats vs dogs**. Using a large dataset of cat and dog images, the model learns to distinguish between these two animal classes with high accuracy.

---

## 📂 Project Structure

```
10_AlexNet_cat_vs_dog/
├── 10_AlexNet_cat_vs_dog.ipynb     # Main notebook with AlexNet implementation
├── data_cleaning.ipynb             # Data preprocessing and cleaning
├── src/
│   └── dataset.py                  # Dataset utilities
├── train/                          # Training images (ignored)
├── val/                            # Validation images (ignored)
├── test/                           # Test images (ignored)
└── data/                           # Dataset (ignored by .gitignore)
```

---

## 🧠 Key Concepts
- Binary image classification (cats vs dogs)
- AlexNet architecture adapted for custom dataset
- Image preprocessing and resizing (180x180)
- Data validation and cleaning
- Large-scale image dataset handling
- Transfer learning concepts
- RGB image processing (3 channels)

---

## ✅ Result Summary
- **Dataset size**: 17,333 training images, 4,944 validation images, 2,484 test images
- **Architecture**: AlexNet with 21.5M+ parameters
- **Image preprocessing**: Resizing to 180x180, normalization
- **Training features**: Dropout regularization, data augmentation ready

The notebook includes comprehensive data validation to ensure clean training data.

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `tensorflow.keras` | AlexNet model and image processing |
| `numpy` | Array operations |
| `matplotlib` | Image visualization |
| `os` | File system operations |

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install tensorflow numpy matplotlib
   ```
2. Prepare dataset (ensure images are in train/val/test folders)
3. Launch the notebook:
   ```bash
   jupyter notebook 10_AlexNet_cat_vs_dog.ipynb
   ```

---

## 💡 Learnings

- Handling large image datasets requires careful preprocessing
- Data validation is crucial for training stability
- AlexNet can be adapted for custom classification tasks
- RGB images require 3-channel input processing
- Deep networks need substantial computational resources

## 🚀 Future Improvements

- Complete the full training cycle and evaluate final accuracy
- Implement data augmentation (rotation, flipping, zoom)
- Add more preprocessing techniques
- Experiment with learning rate scheduling
- Compare with other architectures like ResNet or VGG
- Add model checkpointing and early stopping