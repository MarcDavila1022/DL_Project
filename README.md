# Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise  
**Christopher Cheng, Marc Davila, Ryan Lee, Benjamin Tang, Oscar Wang**  

---

## Introduction
This repository contains our re-implementation of *Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise* by Arpit Bansal, Eitan Borgnia, Hong-Min Chu, Jie S. Li, Hamid Kazemi, Furong Huang, Micah Goldblum, Jonas Geiping, and Tom Goldstein. The paper challenges the traditional notion that random noise is necessary for diffusion models, proposing instead that deterministic degradations like blurring and pixelation can also lead to high-quality image restoration (and also generation, but we do not focus on that). Our goal is to validate these findings on MNIST and CIFAR-10 datasets.

## Chosen Result
We focus on reproducing **Algorithm 2** of the paper, which is mathematically proven to achieve high-quality reconstructions even when the restoration operator is imperfect. We use this in our validation of the inversion of deterministic degradations on MNIST and CFAR-10, such as:
- Deblurring
- Super-resolution
- Inpainting

For reference, see Figure 3 (Deblurring), Figure 5 (Super-resolution), and Figure 4 (Inpainting) in the original paper.  

## GitHub Contents
The structure of the GitHub follows the requirements from class:
```
- code/: A directory containing your re-implementation code, along with any necessary
configuration files or scripts.
- data/: A directory containing the datasets used for training and evaluation, or a
README with instruction on how to obtain the dataset.
- results/: A directory containing the results of your re-implementation, including any
generated figures, tables, or log files.
- poster/: A directory containing a PDF of the poster used for your in-class presentations.
- report/: A directory containing a PDF of the final report submitted.
```

## Reimplementation Details
We used a U-Net architecture with residual blocks, self-attention, and sinusoidal positional embeddings. Training was performed on Google Colab A100 GPUs, using:
- **Optimizer:** Adam (`lr=2e-5`, `batch_size=32`)
- **Degradations:** Gaussian blur for deblurring, halving resolution for super-resolution
- **Metrics:** Frechet Inception Distance (FID), Structural Similarity Index (SSIM), Root Mean Squared Error (RMSE)

We initially attempted to recreate the model from scratch but later referenced the authors' GitHub for architectural consistency.

The most notable changes is the decrease in training steps from 700,000 to 200,000 for deblurring and super-resolution, and 5,000 for inpainting.

## Reproduction Steps
We suggest using Google Colab as well. Thus, download the `.ipynb` files from the `./code/` folder, and open them in Google Colab. Make sure to use A100 GPUs if you can. Running all the cells should work out of the box, as it will install all necessary dependencies and pull the datasets from the web.

## Results
Our reimplementation successfully inverts several deterministic degradations, confirming the core claims of the paper. Although our results are promising, they fall short of the paper's reported FID, SSIM, and RMSE metrics due to limited training steps (200K vs. 700K). We anticipate that extending training would bridge this gap.

## Conclusions
We validated that cold diffusion can be a viable alternative to noise-based diffusion, inverting deterministic transformations like blurring and pixelation with high fidelity. Our experiments highlight the robustness of Algorithm 2 and open doors for noise-free applications in generative modeling. We also learned the importance of designing before coding: we tried to dive straight into the code, but got terrible results as we realized we completely oversimplified the architecture.

## References
- Bansal, A., Borgnia, E., Chu, H.-M., Li, J. S., Kazemi, H., Huang, F., Goldblum, M., Geiping, J., & Goldstein, T. (2022). *Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise*. arXiv preprint arXiv:2208.09392. [arXiv link](https://doi.org/10.48550/arXiv.2208.09392)
- Sun, Jennifer, et al. (2025). *Week 7: Diffusion Models*. [Cornell CS4782 Lecture Notes](https://www.cs.cornell.edu/courses/cs4782/2025sp/slides/pdf/week9_1_slides.pdf)

## Aknowledgements
This project serves as the authors' final project for Cornell University's CS 5782: Intro to Deep Learning. We thank Professor Sun and Professor Weinberger as well as the entire course staff for a great semester!

We used ChatGPT-4o for generating graphs, as well as assistance with with preliminary testing. Final code is ours and the key architectures align with that of the paper.
