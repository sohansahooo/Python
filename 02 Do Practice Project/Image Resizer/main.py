import cv2

# Read the image
img = cv2.imread("ruk-jara.jpg", cv2.IMREAD_UNCHANGED)

# Check if the image was successfully loaded
if img is None:
    print("Error: Could not open or find the image.")
else:
    # Resize the image
    scale_percent = 50  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim)

    # Save the resized image
    cv2.imwrite("ruk-jara-resized.jpg", resized)

    # Display the original and resized images
    cv2.imshow("Original Image", img)
    cv2.imshow("Resized Image", resized)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Resized image saved as ruk-jara-resized.jpg")
