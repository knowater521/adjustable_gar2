import torch as t
from torchvision import transforms 
import random
from hyper_parameters import *


def image_transforms(size=img_size):
    fr_transforms = transforms.Compose([
                        transforms.Resize(size), #大小
                        transforms.RandomCrop(cro_size), #随机裁剪
                        transforms.RandomHorizontalFlip(), #水平翻转
                        transforms.RandomVerticalFlip(), #垂直翻转
                        transforms.RandomRotation(angle), #角度调整
                        transforms.ColorJitter(brightness=0.05, contrast=0.1, saturation=0.3, hue=0.2), 
                        transforms.ToTensor(), 
                        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
                    ])
    return fr_transforms

def enhance_transforms():
    possibility = random.randint(0, 19)
    if possibility % 20 ==0:
        output_transforms = transforms.Compose([
                                    transforms.Resize(img_size), 
                                    transforms.CenterCrop(cro_size), 
                                    transforms.ToTensor(), 
                                    transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
                                   ])
        return output_transforms
    else:
        possibility2 = random.randint(0, 3)
        if possibility2%5==0:
            return image_transforms(224)
        elif possibility2%5==1:
            return image_transforms(245)
        elif possibility2%5==2:
            return image_transforms(274)
        elif possibility2%5==3:
            return image_transforms(316)


def transform_standard():
    output_transforms = transforms.Compose([
        transforms.Resize(img_size), 
        transforms.CenterCrop(cro_size), 
        transforms.ToTensor(), 
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        ])
    return output_transforms
    

