
import cv2

# Load an image
image = cv2.imread('image.jpg')

if image is None:
    print("Could not read image")
    exit()

# Change brightness
def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# Change contrast
def change_contrast(img, level=1.0):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=level, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final

# Change hue
def change_hue(img, angle=10):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h = (h + angle) % 180
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# Edge detection
def detect_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges


# Apply the operations
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


