## AgenticOpenCVDemo.py Explained

This file demonstrates basic OpenCV operations using Python. Below is a breakdown of the operations included:

### 1. Image Loading

The script starts by loading an image named `image.jpg`. Make sure to replace the placeholder image with your own. If the image cannot be read, the program exits.

```python
image = cv2.imread('image.jpg')
if image is None:
    print("Could not read image")
    exit()
```

### 2. Brightness Adjustment

The `change_brightness` function modifies the brightness of the image. It converts the image to the HSV color space, increases the V (Value) channel, and converts it back to BGR.

```python
def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
```

### 3. Contrast Adjustment

The `change_contrast` function adjusts the contrast of the image using CLAHE (Contrast Limited Adaptive Histogram Equalization). It converts the image to the LAB color space, applies CLAHE to the L (Lightness) channel, and converts it back to BGR.

```python
def change_contrast(img, level=1.0):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=level, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final
```

### 4. Hue Adjustment

The `change_hue` function modifies the hue of the image. It converts the image to the HSV color space, adds an angle to the H (Hue) channel, and converts it back to BGR.

```python
def change_hue(img, angle=10):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h = (h + angle) % 180
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
```

### 5. Edge Detection

The `detect_edges` function detects edges in the image using the Canny edge detector. It converts the image to grayscale and applies the Canny function.

```python
def detect_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges
```

### 6. Applying Operations and Displaying Images

Finally, the script applies these operations to the loaded image and displays the results using `cv2.imshow`.

```python
brightness_img = change_brightness(image, value=50)
contrast_img = change_contrast(image, level=3.0)
hue_img = change_hue(image, angle=30)
edge_img = detect_edges(image)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Brightness Image', brightness_img)
cv2.imshow('Contrast Image', contrast_img)
cv2.imshow('Hue Image', hue_img)
cv2.imshow('Edge Image', edge_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

Make sure you have OpenCV installed (`pip install opencv-python`) to run this script.
