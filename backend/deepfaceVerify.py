from deepface import DeepFace

# Model names: "VGG-Face", "Google FaceNet", "OpenFace", "DeepID", "Dlib"


def verify_face(img1, img2):
    result = DeepFace.verify(
        img1,
        img2,
        model_name="VGG-Face"
    )
    return result["verified"]


if __name__ == "__main__":
    result = verify_face(
        "../images/jolie_1.jpg",
        "../images/jolie_2.jpg"
    )
    print(result)

