from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = 'e90f0995b50a47638fa613c88452ba84'
endpoint = 'https://20240105.cognitiveservices.azure.com/'

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

#画像の説明
print("===== Describe of image - remote =====")
read_image_url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"

descripiton_results = computervision_client.describe_image(read_image_url)
print("Description of remote image: ")
if (len(descripiton_results.captions) == 0):
    print("No descripition detected.")
else:
    for caption in descripiton_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence*100))


#画像カテゴリの取得
print("==== Categorize an image - remote ====")
remote_image_feature = ["categories"]
categorize_results_remote = computervision_client.analyze_image(read_image_url, remote_image_feature)

print("Categories from remote image: ")
if (len(categorize_results_remote.categories) == 0 ):
    print("No categories detected")
else:
    for category in categorize_results_remote.categories:
        print("'{}' with confidence{:.2f}%".format(category.name, category.score * 100))

#画像タグの取得
print("==== Tag an image -remote ====")

tags_result_remote = computervision_client.tag_image(read_image_url)
print("tag in the remote image:")
if (len(tags_result_remote.tags) == 0):
    print("No tags detected")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

#オブジェクトの検出
print("==== Detect Objects -remote ====")
detect_objects_results = computervision_client.detect_objects(read_image_url)

print("Detecting objects in remote image:")
if len(detect_objects_results.objects) == 0:
    print ("No objects detected")
else:
    for object in detect_objects_results.objects:
        print("object at location {}, {}, {}, {}".format(
        object.rectangle.x, object.rectangle.x + object.rectangle.w, \
        object.rectangle.y, object.rectangle.y + object.rectangle.h))    


#ローカルファイルに対応させる
local_image_path = 'test.jpeg'
local_image = open(local_image_path, "rb")

print("==== Detect Objects -local ====")
detect_objects_results_remote = computervision_client.detect_objects_in_stream(local_image)

print("Detecting objects in local image:")
if len(detect_objects_results_remote.objects) == 0:
    print ("No objects detected")
else:
    for object in detect_objects_results_remote.objects:
        print("object at location {}, {}, {}, {}".format(
        object.rectangle.x, object.rectangle.x + object.rectangle.w, \
        object.rectangle.y, object.rectangle.y + object.rectangle.h))    
print()
'''
END - Read File - remote
'''

print("End of Computer Vision quickstart.")

