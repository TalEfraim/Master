import os
import cv2
from skimage.metrics import structural_similarity as ssim


def resize_and_compute_ssim(image1, image2):
    # Resize both images to a common size (e.g., 256x256)
    target_size = (256, 256)
    image1 = cv2.resize(image1, target_size)
    image2 = cv2.resize(image2, target_size)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate SSIM score
    ssim_score = ssim(gray1, gray2)
    return ssim_score

def main(golden_image_path, image_list):
    # Load the golden image
    golden_image = cv2.imread(golden_image_path)

    # Initialize a dictionary to store confidence levels for each image
    confidence_levels = {}

    # Iterate through the list of images and calculate SSIM scores
    for image_path in image_list:
        current_image = cv2.imread(image_path)
        ssim_score = resize_and_compute_ssim(golden_image, current_image)
        confidence_levels[image_path] = ssim_score

    return confidence_levels

Input_folder = r'C:\Users\talef\Pictures\Target detect project\Tal Efraim\train'
OrgDatasetImgs = [f for f in os.listdir(Input_folder) if f.endswith('.jpg')]
OrgDatasetList = []
for DatasetImg in OrgDatasetImgs:
    OrgDatasetList.append(os.path.join(Input_folder, DatasetImg))
image_list = OrgDatasetList

golden_image_path = os.path.join(Input_folder,'WIN_20230621_22_11_20_Pro.jpg')


confidence_levels = main(golden_image_path, image_list)
for image_path, confidence in confidence_levels.items():
    print(f"Image: {image_path}, SSIM Score: {confidence}")


#
#
# import cv2
# from skimage.metrics import structural_similarity as ssim
#
# def resize_and_compute_ssim(image1, image2):
#     # Resize both images to a common size (e.g., 256x256)
#     target_size = (256, 256)
#     image1 = cv2.resize(image1, target_size)
#     image2 = cv2.resize(image2, target_size)
#
#     # Convert images to grayscale
#     gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#
#     # Calculate SSIM score
#     ssim_score = ssim(gray1, gray2)
#     return ssim_score
#
# def main(golden_image_list, image_list):
#     # Initialize a dictionary to store confidence levels for each image pair
#     confidence_levels = {}
#
#     # Iterate through the lists of golden images and images and calculate SSIM scores
#     for golden_image_path, image_path in zip(golden_image_list, image_list):
#         golden_image = cv2.imread(golden_image_path)
#         current_image = cv2.imread(image_path)
#         ssim_score = resize_and_compute_ssim(golden_image, current_image)
#         confidence_levels[(golden_image_path, image_path)] = ssim_score
#
#     return confidence_levels
#
# if __name__ == "__main__":
#     # Provide lists of paths to the golden images and images to compare
#     golden_image_list = ["golden_image1.jpg", "golden_image2.jpg", "golden_image3.jpg"]
#     image_list = ["image1.jpg", "image2.jpg", "image3.jpg"]
#
#     # Calculate confidence levels for each pair of images (golden vs. current)
#     confidence_levels = main(golden_image_list, image_list)
#
#     # Print the confidence levels for each pair
#     for (golden_path, image_path), confidence in confidence_levels.items():
#         print(f"Golden Image: {golden_path}, Image: {image_path}, SSIM Score: {confidence}")
