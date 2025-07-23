# 🩺 Kidney Stone Image Segmentation using Image Processing (PIL)

This project performs image segmentation on a CT Kidney dataset to highlight and isolate different kidney conditions such as **Normal**, **Cyst**, **Tumor**, and **Stone** using traditional image processing techniques in Python. The segmentation masks are visualized with overlays to emphasize regions of interest.

## 📁 Dataset

**Name:** CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone  
**Structure:**
```
Imagedata/
└── CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/
    ├── Normal/
    ├── Cyst/
    ├── Tumor/
    └── Stone/
```

Each subfolder contains `.jpg` images representing the corresponding class.

## 🧰 Steps Performed

1. 📦 **Zip Extraction**  
   - The dataset `Imagedata.zip` is extracted into a working directory.

2. 🖼 **Image Loading & Resizing**  
   - All images are resized to **256×256** pixels for uniformity.

3. ✨ **Image Enhancement**  
   - Performed using:
     - Contrast adjustment
     - Median denoising
     - Histogram equalization

4. 🧠 **Image Segmentation**  
   - Basic thresholding is used to create binary masks.
   - Optionally remove unwanted rectangular areas from masks.

5. 🎨 **Color Overlay**  
   - Segmented binary masks are colorized (e.g., red) and transparently overlaid on the original images for visualization.

## 📌 Sample Output

> Example visualizations (shown in the notebook):
- Original Image  
- Segmented Binary Mask  
- Overlay with Transparent Colored Mask

## 🧪 Requirements

```bash
pip install pillow
```

(Optional) For interactive exploration:
```bash
pip install notebook
```

## ▶️ Usage

Ensure `Imagedata.zip` is present, then:

```bash
# Run the notebook
jupyter notebook 'CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone.ipynb'
```

Or use a standalone script (if available):

```bash
python kidney_segmentation.py
```

## 📍 Notes

- No deep learning involved — only traditional image processing.
- Ideal for structured grayscale medical images.
- Exclusion rectangles can filter out noisy sections.

## 📁 Repository

🔗 [GitHub Repo](https://github.com/M-ArslanArshad/kidney_stone_image_segmention)

## 🧑‍💻 Author

**M Arslan Arshad**  
Ml/AI Enthusiast | Computer Vision Researcher

