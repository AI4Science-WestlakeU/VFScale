# VFScale: Intrinsic Reasoning through Verifier-Free Test-time Scalable Diffusion Model (ICLR 2026)
Here is the official implementation for **VFScale: Intrinsic Reasoning through Verifier-Free Test-time Scalable Diffusion Model**. 

[[paper](https://openreview.net/forum?id=8ta0xgtsJK)][[arXiv](https://arxiv.org/abs/2502.01989)]

We introduce we introduce the Verifier-free Test-time Scalable Diffusion Model (VFScale) to achieve scalable intrinsic reasoning, which equips number-of-sample test-time scaling with the intrinsic energy function of diffusion models as the verifier.
**Trained with Maze tasks of up to 6x6, VFScale can generalize to solve much harder 15x15 Maze tasks, with larger test-time compute resulting in higher accuracy:**
<a href="https://github.com/AI4Science-WestlakeU/VFScale/tree/main/assets/maze_scalability.png">
  <img src="https://raw.githubusercontent.com/AI4Science-WestlakeU/VFScale/main/assets/maze_scalability.png" align="center" width="800">
</a>

**Framework of VFScale:**
<a href="https://github.com/AI4Science-WestlakeU/VFScale/tree/main/assets/figure1.jpg">
  <img src="https://raw.githubusercontent.com/AI4Science-WestlakeU/VFScale/main/assets/figure1.jpg" align="center" width="800">
</a>
## 1. Environment Setup

```bash
conda env create -f environment.yml
conda activate VFScaleEnv
pip install -e .
```

## 2. Dataset and checkpoints
The datasets and checkpoints can be downloaded from this [link](https://drive.google.com/drive/folders/1ZfPdkQ4DpEukOxRn6S47ADV3TXTnr6xk?usp=drive_link).

## 3. Training
To train the model, run the following command
```bash
sh scripts/Maze_train.sh
```
```bash
sh scripts/Sudoku_train.sh
```
## 4. Inference

```bash
sh scripts/Maze_inference.sh
```
```bash
sh scripts/Sudoku_inference.sh
```

## Citation
If you find our work and/or our code useful, please cite us via:

```bibtex
@inproceedings{
zhang2026vfscale,
title={{VFS}cale: Intrinsic Reasoning through Verifier-Free Test-time Scalable Diffusion Model},
author={Tao Zhang and Jia-Shu Pan and Ruiqi Feng and Tailin Wu},
booktitle={The Fourteenth International Conference on Learning Representations},
year={2026},
url={https://openreview.net/forum?id=8ta0xgtsJK}
}
```
