# Wallpaper with Quotes (Windows)

This project randomly combines an image from the `images/` folder with one of the quotes from `background.py`, then saves the combined image to the `modified_images/` folder. Finally, the script sets the modified image as the desktop background (only on Windows).

## Example
![image](https://github.com/user-attachments/assets/55123233-f7f9-499e-96fd-35408da248f1)


## Folder Structure

- `images/`: Store all the images you want to use as wallpapers in this folder.
- `modified_images/`: This folder will store the modified version of the image with quotes applied. This gets purged before every run.
- `background.py`: The script that combines a random image and quote, then sets it as the desktop background.

## Setup Instructions

### 1. Create Folders:
   - Create a folder named `images` and another folder named `modified_images` in the project directory.
   - Place all the images you want to use as wallpapers inside the `images` folder.

### 2. Update Quotes:
   - Open `background.py`.
   - In the script, you will find a list of quotes. You can modify or add new quotes as you like.

### 3. Running the Script:
   - Run `background.py` to:
     1. Randomly select an image from the `images` folder.
     2. Randomly select a quote.
     3. Combine the image with the quote and save the result to `modified_images/`.
     4. Set the modified image as your desktop background (only works on Windows).
   
   To run the script, execute the following command:
   ```bash
   python background.py
```

## Other Notes
Insure Pillow is installed using: 
```bash
   pip install Pillow
```
