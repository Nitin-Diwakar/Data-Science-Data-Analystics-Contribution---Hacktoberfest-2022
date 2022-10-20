
import cv2
import numpy as np

from sklearn.cluster import MiniBatchKMeans

clusters =40

#loading the image
image=cv2.imread("image/avengers.jpg")
h,w = image.shape[:2]

#conversion to L*a*b gamut for perptual meaning
image=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)

#reshape the image into a feature vector for k-means
image=image.reshape((image.shape[0]* image.shape[1],3))

#Creating a Quantized image using K-means
cls= MiniBatchKMeans(n_clusters=clusters)
labels = cls.fit_predict(image)
quantized= cls.cluster_centers_.astype("uint8")[labels]

#Reshape the feature vectors back to images
quantized=quantized.reshape((h,w,3))
image=image.reshape((h,w,3))

#Convert from L*a*b to RGB
quantized = cv2.cvtColor(quantized,cv2.COLOR_LAB2RGB,cv2.CV_8U)
image =cv2.cvtColor(image,cv2.COLOR_LAB2RGB,cv2.CV_8U)

#saving the image
cv2.imwrite(f"Color_Quantized_{clusters}.jpg", np.hstack([image,quantized]))