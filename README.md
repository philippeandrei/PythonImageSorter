# Sort Images by Color

A tool for sorting images by their dominant colors, built by Philippe and Paul C.

## 🚀 Features

- Automatically generates a JSON file with color data for each image.
- Prevents duplicate entries by checking if the image is already in the JSON.
- Multithreaded for faster processing.

## 🛠️ Usage

1. Open the script and navigate to line 143.
2. Change the `folder_path` variable to the directory containing your images.
3. Use the modified version of `colorthief` included in this repo.

## 📦 Installation

To get started, install the necessary dependencies:

```bash
pip install colorthief
pip install pillow
```

## 🖼️ How it Works

The script scans through a folder of images, extracts dominant colors, and saves the data in a `data.json` file. It ensures no image is added twice and uses threading to optimize the process, speeding things up significantly.

![colorsort](https://github.com/Phi999/sort_imagesby_color/assets/72974980/3c091292-ca02-4f1c-beaf-61813fb5b285)

## 📝 TODO

- [ ] Improve algorithm efficiency.
- [ ] Compress `data.js`.
- [ ] Redesign the UI for a better user experience.
