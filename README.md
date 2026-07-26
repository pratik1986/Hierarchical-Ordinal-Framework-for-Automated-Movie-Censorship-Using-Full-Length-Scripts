# Hierarchical-Ordinal-Framework-for-Automated-Movie-Censorship-Using-Full-Length-Scripts
Official implementation of the hierarchical ordinal framework for automated movie censorship using full-length scripts. Includes preprocessing, TF-IDF, HLSTM, Hierarchical BERT, Longformer, ordinal regression, evaluation pipeline, and reproducible experiments for MPAA movie certification prediction

## Overview

Automatic movie age rating prediction is an ordinal classification problem where the target classes follow a natural ordering:

**G → PG → PG-13 → R → NC-17**

This repository presents a reproducible framework for predicting MPAA age ratings directly from **full-length English movie scripts** using hierarchical neural architectures and traditional machine learning models.

The repository includes:

- Dataset preparation utilities
- Data preprocessing pipeline
- Training notebooks
- Public datasets
- Pretrained models
- Experimental outputs

---

# Repository Structure

```text
.
├── dataset_used/
│   Dataset documentation and download links
│
├── notebooks/
│   Training notebooks for all experiments
│
├── preprocessing/
│   Dataset preparation and preprocessing utilities
│
├── published_paper_author_version/
│   Author version of the published paper
│
├── trained_models/
│   Links to pretrained Hugging Face models
│
├── LICENSE
└── README.md
```

---

# Implemented Models

The following architectures were evaluated.

| Architecture | Balanced | Unbalanced |
|--------------|:--------:|:----------:|
| TF-IDF + MLP | ✓ | ✓ |
| Hierarchical LSTM | ✓ | ✓ |
| Hierarchical BERT | ✓ | ✓ |
| Hierarchical Longformer | ✓ | ✓ |

---

# Public Datasets (Use under CC BY-NC-SA 4.0)

## Balanced Dataset (250 Scripts)

https://huggingface.co/datasets/pratikkalamkar/Balanced_Hollywood_Movies_Scripts_Age_Rating_Dataset_250

- 250 English movie scripts
- Five MPAA rating classes
- 50 scripts per class

---

## Unbalanced Dataset (1,142 Scripts)

https://huggingface.co/datasets/pratikkalamkar/UnBalanced_Hollywood_Movies_Scripts_Age_Rating_Dataset_1142

- 1,142 English movie scripts
- Original MPAA class distribution

---

# Pretrained Models

Eight pretrained models are available on Hugging Face.

### Balanced Models

- TF-IDF + MLP
- Hierarchical LSTM
- Hierarchical BERT
- Hierarchical Longformer

### Unbalanced Models

- TF-IDF + MLP
- Hierarchical LSTM
- Hierarchical BERT
- Hierarchical Longformer

See **trained_models/README.md** for download links.

---

# Experimental Workflow

1. Dataset collection
2. Script preprocessing
3. Feature extraction
4. Model training
5. Ordinal classification
6. Threshold calibration
7. Performance evaluation

---

# Evaluation Metrics

The following evaluation metrics are reported:

- Accuracy
- Precision
- Recall
- F1-score
- Mean Absolute Error (MAE)
- ROC Curve
- Precision–Recall Curve
- Confusion Matrix

---

# Requirements

Main libraries

- Python 3.10+
- TensorFlow / Keras
- PyTorch
- Hugging Face Transformers
- Scikit-learn
- Pandas
- NumPy
- Matplotlib

---

# Citation

If you use this repository, datasets, or pretrained models, please cite:

```bibtex
@inproceedings{kalamkar2025hierarchical,
  title={Hierarchical Ordinal Framework for Automated Movie Censorship Using Full-Length Scripts},
  author={Kalamkar, Pratik N. and Peddi, Prasad and Sharma, Y. K.},
  booktitle={Proceedings of IEEE GCAT},
  year={2025}
}
```

---

# Related Resources

- dataset_used/README.md
- trained_models/README.md

---

# Author

**Dr. Pratik N. Kalamkar**

GitHub

https://github.com/pratik1986

Hugging Face

https://huggingface.co/pratikkalamkar

---

# License

Licensed under the Apache License 2.0.
