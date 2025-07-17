# Week 01 – Age and Gender Dataset Collection

## 👩‍💻 Task Summary

For Week 1, I curated a labeled dataset for age and gender classification using the UTKFace dataset. A total of **558 images** were organized into six categories:

- child_male (100)
- child_female (100)
- adult_male (98)
- adult_female (100)
- aged_male (80)
- aged_female (80)

## 📁 Dataset Structure

Images were organized using age and gender labels from filenames and split into age ranges:

- **Children:** 1–17 years
- **Adults:** 18–60 years
- **Aged:** 61–100 years

To ensure **diversity and fairness**, each category was further divided into **five racial groups**:

- `0/` → White
- `1/` → Black
- `2/` → Indian
- `3/` → Asian
- `4/` → Others

Each subfolder contains ~20 images per race (where available), equally distributed across all categories.

## 🛠️ Tools & Method

- Used a **custom Python script** to filter, rename, and organize images.
- Skipped images with poor clarity or incorrect labels.
- Ensured consistency in file naming and folder hierarchy for future model training.

## Submitted By:
**Syeda Shanzay Shah**

