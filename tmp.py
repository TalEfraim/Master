import cv2
import dlib
import os


# Here are the steps to try each option:
#
# 1. Adjust the face detector: In this updated code, the default dlib face detector is used. You can adjust the parameters of the detectMultiScale function in the OpenCV Haar cascade section to improve face detection for images where faces are looking aside. Try experimenting with the scaleFactor, minNeighbors, and minSize parameters to achieve better results.
#
# 2. Use OpenCV's Haar cascades: If the default dlib face detector fails to detect faces, an alternative approach using OpenCV's Haar cascades is attempted. The Haar cascade model haarcascade_frontalface_default.xml is loaded, and the detectMultiScale function is used to detect faces in the grayscale image. You may need to adjust the parameters of detectMultiScale to improve face detection for your specific images.
#
# 3. Face alignment: If both the default dlib face detector and the Haar cascades fail to detect faces, the code suggests using face alignment techniques. This part of the code assumes you have a face alignment library and a pre-trained shape predictor model (shape_predictor_68_face_landmarks.dat). You'll need to replace 'path/to/shape_predictor_68_face_landmarks.dat' with the actual path to your shape predictor model file. Once you have the face landmarks, you can apply face alignment techniques (such as affine transformations) to align the face before drawing the bounding box label.




def draw_face_boxes(images_folder, output_folder):
    # Load the face detector model
    face_detector = dlib.get_frontal_face_detector()

    # Loop through the images in the folder
    for root, _, files in os.walk(images_folder):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                # Read the image file
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path)

                # Convert the image to grayscale for face detection
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Detect faces in the image using the default face detector
                faces = face_detector(gray)

                # If no faces are detected, try a different face detector
                if len(faces) == 0:
                    # Use OpenCV's Haar cascades for face detection
                    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                # If still no faces are detected, try face alignment techniques
                if len(faces) == 0:
                    # Perform face alignment using a face alignment library of your choice
                    # This example uses dlib's face landmarks and affine transformations
                    predictor_path = 'path/to/shape_predictor_68_face_landmarks.dat'
                    predictor = dlib.shape_predictor(predictor_path)
                    dlib_faces = dlib.get_face_chips(image, [face.rect for face in faces], size=256)

                    for dlib_face in dlib_faces:
                        landmarks = predictor(image, dlib_face)
                        # Perform face alignment using the face landmarks
                        # ...
                        # Add code here to align the face using the landmarks
                        # ...

                # Draw bounding box labels around the faces
                for face in faces:
                    x, y, w, h = face.left(), face.top(), face.width(), face.height()
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Save the image with face bounding box labels
                output_path = os.path.join(output_folder, file)
                cv2.imwrite(output_path, image)

def train_cascade_classifier(positive_images_path, negative_images_path):
    # Set up paths and parameters
    output_model_file = 'trained_model.svm'
    annotations_file = 'annotations.xml'

    # Collect positive sample filenames
    positive_sample_filenames = []
    for root, _, files in os.walk(positive_images_path):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                positive_sample_filenames.append(os.path.join(root, file))

    # Collect negative sample filenames
    negative_sample_filenames = []
    for root, _, files in os.walk(negative_images_path):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                negative_sample_filenames.append(os.path.join(root, file))

    # Create annotations file
    with open(annotations_file, 'w') as f:
        for filename in positive_sample_filenames:
            f.write(filename + ' 1 0 0 24 24\n')

    # Set up options for training
    options = dlib.simple_object_detector_training_options()
    options.add_left_right_image_flips = True
    options.C = 5
    options.num_threads = 4
    options.be_verbose = True

    # Train the cascade classifier
    detector = dlib.train_simple_object_detector(annotations_file, output_model_file, options)

    # Save the trained model
    detector.save(output_model_file)

    # Remove the annotations file
    os.remove(annotations_file)


positive = r'C:\Users\talef\Pictures\Target detect project\Tal Efraim\Negative-Positive\p'
negative = r'C:\Users\talef\Pictures\Target detect project\Tal Efraim\Negative-Positive\n'

draw_face_boxes(images_folder=positive, output_folder='C:\Python codes\positive faces')

# train_cascade_classifier(positive_images_path=positive, negative_images_path=negative)
