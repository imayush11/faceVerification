import cv2


def image_to_blob(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError("Could not load the image. Please check the image path.")

    # Encode the image to a binary format (JPEG)
    _, buffer = cv2.imencode('.jpg', image)

    # Convert the buffer to bytes and return
    blob = buffer.tobytes()

    return blob


if __name__ == "__main__":
    img_path = '../images/jolie_1.jpg'
    blob_object = image_to_blob(img_path)
    print("BLOB object created successfully.", blob_object)

