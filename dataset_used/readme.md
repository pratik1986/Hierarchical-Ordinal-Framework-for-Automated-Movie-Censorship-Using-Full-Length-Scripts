# Datasets

This repository uses two publicly available English movie script datasets accompanying the paper:

> **Hierarchical Ordinal Framework for Automated Movie Censorship Using Full-Length Scripts**
> IEEE GCAT 2025

The datasets are hosted on Hugging Face.

---

## Balanced Dataset

**Balanced Hollywood Movies Scripts Age Rating Dataset (250 Scripts)**

https://huggingface.co/datasets/pratikkalamkar/Balanced_Hollywood_Movies_Scripts_Age_Rating_Dataset_250

### Statistics

- 250 English movie scripts
- Five MPAA age-rating classes
- 50 scripts per class
- Suitable for balanced classification experiments

Classes:

- G
- PG
- PG-13
- R
- NC-17

---

## Unbalanced Dataset

**Hollywood Movies Scripts Age Rating Dataset (1,142 Scripts)**

https://huggingface.co/datasets/pratikkalamkar/UnBalanced_Hollywood_Movies_Scripts_Age_Rating_Dataset_1142

### Statistics

- 1,142 English movie scripts
- Original MPAA distribution
- Reflects real-world class imbalance

Classes:

- G
- PG
- PG-13
- R
- NC-17

---

## Dataset Usage

The balanced dataset was used to evaluate model performance under equal class representation.

The unbalanced dataset was used to investigate the effect of naturally imbalanced class distributions on automatic movie age-rating prediction.

Both datasets were used throughout the experiments reported in the paper.

---

## Related Models

Pretrained models trained on these datasets are available in the `models/` directory and on Hugging Face.
