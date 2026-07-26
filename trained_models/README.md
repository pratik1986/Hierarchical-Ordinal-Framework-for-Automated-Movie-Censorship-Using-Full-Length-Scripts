# Pretrained Models

This repository provides links to the pretrained models accompanying the paper:

> **Hierarchical Ordinal Framework for Automated Movie Censorship Using Full-Length Scripts**
> IEEE GCAT 2025

The models are hosted on Hugging Face for convenient download and reuse.

---

## Balanced Models

| Model | Hugging Face |
|------|------|
| TF-IDF + MLP | https://huggingface.co/pratikkalamkar/moviecert-tfidf-balanced |
| Hierarchical LSTM | https://huggingface.co/pratikkalamkar/moviecert-hlstm-balanced |
| Hierarchical BERT | https://huggingface.co/pratikkalamkar/moviecert-hbert-balanced |
| Hierarchical Longformer | https://huggingface.co/pratikkalamkar/moviecert-hlongformer-balanced |

---

## Unbalanced Models

| Model | Hugging Face |
|------|------|
| TF-IDF + MLP | https://huggingface.co/pratikkalamkar/moviecert-tfidf-unbalanced |
| Hierarchical LSTM | https://huggingface.co/pratikkalamkar/moviecert-hlstm-unbalanced |
| Hierarchical BERT | https://huggingface.co/pratikkalamkar/moviecert-hbert-unbalanced |
| Hierarchical Longformer | https://huggingface.co/pratikkalamkar/moviecert-hlongformer-unbalanced |

---

## Model Summary

| Architecture | Balanced | Unbalanced |
|--------------|:--------:|:----------:|
| TF-IDF + MLP | ✓ | ✓ |
| Hierarchical LSTM | ✓ | ✓ |
| Hierarchical BERT | ✓ | ✓ |
| Hierarchical Longformer | ✓ | ✓ |

All models were trained for automatic MPAA age rating prediction from full-length English movie scripts.

The repositories contain the trained model weights together with the files required for inference (where applicable).

---

## Citation

If you use these models in your research, please cite:

```bibtex
@inproceedings{kalamkar2025hierarchical,
  title={Hierarchical Ordinal Framework for Automated Movie Censorship Using Full-Length Scripts},
  author={Kalamkar, Pratik N. and Peddi, Prasad and Sharma, Y. K.},
  booktitle={Proceedings of IEEE GCAT},
  year={2025}
}
```
