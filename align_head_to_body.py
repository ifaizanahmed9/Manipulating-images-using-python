from PIL import Image
import numpy as np
import os
import cv2

def align_head_to_body(joined,output_path):
    # Read the input image
    img = Image.open('shirt_pant.png')

    # Convert the image into a numpy array
    img_array = np.array(img)

        # Detect the head region using HoughCircles method of OpenCV
    img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, dp=1, minDist=100,
                               param1=50, param2=30, minRadius=50, maxRadius=150)
    head_cx, head_cy, head_r = circles[0][0]

    # Define the body region as the remaining part of the image
    body_left = 0
    body_top = int(head_cy + head_r)
    body_right = img.width
    body_bottom = img.height


        # Crop the head and body regions from the image
    head_img = img.crop((head_cx - head_r, head_cy - head_r, head_cx + head_r, head_cy + head_r))
    body_img = img.crop((body_left, body_top, body_right, body_bottom))

    # Calculate the offset to align the head to the center of the body
    offset_x = int((body_right - body_left - 2 * head_r) / 2)
    offset_y = int(head_r)

    # Create a new image with the aligned head and body regions
    new_img = Image.new("RGBA", (img.width, img.height), (0, 0, 0, 0))
    new_img.paste(body_img, (0, 0))
    new_img.paste(head_img, (offset_x, offset_y), mask=head_img)

    # Save the final image to the output path
    new_img.save('output_path')
