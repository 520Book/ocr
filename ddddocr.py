# coding=utf-8

import io
import os
import base64
import json
import pathlib
import onnxruntime
from PIL import Image, ImageChops
import numpy as np
import cv2

def base64_to_image(img_base64):
    img_data = base64.b64decode(img_base64)
    return Image.open(io.BytesIO(img_data))

class DdddOcr(object):
    def __init__(self,  import_onnx_path: str = "", charsets_path: str = ""):
        self.__graph_path = os.path.join(os.path.dirname(__file__), 'ddddocr.onnx')
        self.__ort_session = onnxruntime.InferenceSession(self.__graph_path)

    def classification(self, img):
        if isinstance(img, bytes):
            image = Image.open(img)
        elif isinstance(img, str):
            image = base64_to_image(img)

        image = image.resize((int(image.size[0] * (64 / image.size[1])), 64), Image.ANTIALIAS).convert('L')
        image = np.array(image).astype(np.float32)
        image = np.expand_dims(image, axis=0) / 255
        image = (image - 0.5) / 0.5
                
        ort_inputs = {'input1': np.array([image]).astype(np.float32)}
        ort_outs = self.__ort_session.run(None, ort_inputs)
        
        result = []
        numDict = {
            4733: '0',  4018 : '1', 2851 : '2',  309 : '3',   3606 : '4', 
            5223 : '5', 13 : '6',   6794 : '7',  4919 : '8',  4725 : '9',
            7266: 'a',    5461: 'A',
            4393: 'b',   1204 : 'B',
            1151: 'c',   7961 : 'C',
            6810: 'd',   3128 : 'D',
            5428 : 'e', 2547: 'E',
            55: 'f',     311 : 'F',
            5690: 'g',   598 : 'G',
            7412: 'h',   1965 : 'H',
            782: 'i',    6554 : 'I',
            4730: 'j',   7216 : 'J',            
            5737: 'k',   2113 : 'K',
            2457: 'l',   210 : 'L',            
            320: 'm',    7844 : 'M',
            1503: 'n',   901 : 'N',
            4429 : 'o', 3157 : 'O',
            209 : 'p', 2341 : 'P',
            1849 : 'Q',
            297 : 'Y',
            306 : 'w',
            521 : 'X',
            689 : 'x',
            897 : 'T',
            1073 : 'v',
            2185 : 'W',
            2376 : 'r',
            2621 : 'Z',
            2714 : 's',
            3073 : 'z',
            4102 : 't',
            4588 : 'u',
            5629 : 'R',
            5855 : 'S',
            6887 : 'V',
            7576 : 'q',
            7712 : 'U',
            7877 : 'y',
        } 

        last_item = 0
        for item in ort_outs[0][0]:
            if item == last_item:
                continue
            else:
                last_item = item
            if item != 0:
                result.append(numDict.get(item))
        return ''.join(result)