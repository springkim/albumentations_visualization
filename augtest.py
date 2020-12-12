import albumentations as A
import numpy as np
import cv2
import imageio
import os

from typeguard import function_name

size = 384
img = cv2.imread("kiwi.jpg")
img = cv2.resize(img, (size, size))
img2 = cv2.imread("bbosong.jpg")
img2 = cv2.resize(img2, (size, size))

augs = []
augs.append(A.Blur(p=1))
augs.append(A.CLAHE(p=1))
augs.append(A.ChannelDropout(p=1))
augs.append(A.ChannelShuffle(p=1))
augs.append(A.ColorJitter(p=1))
augs.append(A.Downscale(p=1))
augs.append(A.Equalize(p=1))
augs.append(A.FDA([img2], read_fn=lambda x: x, p=1))

augs.append(A.FancyPCA(p=1))
augs.append(A.GaussNoise(p=1))
augs.append(A.GaussianBlur(p=1))
augs.append(A.GlassBlur(p=1))
augs.append(A.HistogramMatching([img2], read_fn=lambda x: x, p=1))
augs.append(A.HueSaturationValue(p=1))
augs.append(A.IAAAdditiveGaussianNoise(p=1))
augs.append(A.IAAEmboss(p=1))

augs.append(A.IAAEmboss(p=1))
augs.append(A.IAASharpen(p=1))
augs.append(A.IAASuperpixels(p=1))
augs.append(A.ISONoise(p=1))
augs.append(A.InvertImg(p=1))
augs.append(A.MedianBlur(p=1))
augs.append(A.MotionBlur(p=1))
augs.append(A.MultiplicativeNoise(p=1))
augs.append(A.Posterize(p=1))

augs.append(A.RGBShift(p=1))
augs.append(A.RandomBrightnessContrast(p=1))
augs.append(A.RandomFog(p=1))

augs.append(A.RandomGamma(p=1))
augs.append(A.RandomRain(p=1))
augs.append(A.RandomShadow(p=1))
augs.append(A.RandomSnow(p=1))
augs.append(A.RandomSunFlare(p=1))
augs.append(A.Solarize(p=1))
augs.append(A.ToGray(p=1))
augs.append(A.ToSepia(p=1))

augs.append(A.CenterCrop(256, 256, p=1))
augs.append(A.CoarseDropout(p=1))
augs.append(A.Crop(0, 0, 256, 256, p=1))
augs.append(A.ElasticTransform(p=1))
augs.append(A.Flip(p=1))
augs.append(A.GridDistortion(p=1))
augs.append(A.GridDropout(p=1))
augs.append(A.HorizontalFlip(p=1))
augs.append(A.IAAAffine(p=1))
augs.append(A.IAACropAndPad(p=1))
augs.append(A.IAAFliplr(p=1))
augs.append(A.IAAFlipud(p=1))
augs.append(A.IAAPerspective(p=1))

augs.append(A.IAAPiecewiseAffine(p=1))
augs.append(A.OpticalDistortion(p=1))
augs.append(A.PadIfNeeded(256, 256, p=1))
augs.append(A.RandomCrop(256, 256, p=1))
augs.append(A.RandomGridShuffle(p=1))
augs.append(A.RandomResizedCrop(256, 256, p=1))
augs.append(A.RandomRotate90(p=1))


augs.append(A.RandomSizedCrop((256, size), 256, 256, p=1))
augs.append(A.Resize(256, 256, p=1))
augs.append(A.Rotate(p=1))
augs.append(A.ShiftScaleRotate(p=1))
augs.append(A.Transpose(p=1))
augs.append(A.VerticalFlip(p=1))

if not os.path.exists("img"):
    os.mkdir("img")
with open("Readme.md", "w") as fp:
    for aug in augs:
        function_name = aug.__str__().split('(')[0]
        print(function_name)
        transform = A.Compose([aug])
        with imageio.get_writer(f'img/{function_name}.gif', mode='I') as writer:
            for i in range(10):
                transformed = transform(image=img)
                transformed_img = transformed["image"]
                palette = np.zeros((size, size, 3), np.uint8)
                palette[0:transformed_img.shape[0], 0:transformed_img.shape[1]] = transformed_img
                out = cv2.hconcat([img, palette])
                out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
                writer.append_data(out)
        fp.write(f"# {function_name}\n")
        fp.write(f"```python\n{aug.__str__()}\n```\n")
        fp.write(f"![](img/{function_name}.gif)\n")
