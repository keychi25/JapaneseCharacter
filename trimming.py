# coding:utf-8

from PIL import Image
import sys
import os

args = sys.argv


def run_trimming(_image, _filename):
    img = _image
    rgbImage = img.convert('RGB')
    size = rgbImage.size

    tPix = 100000000
    bPix = -1
    lPix = -1
    rPix = -1

    # ピクセル操作
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = rgbImage.getpixel((x, y))
            rr, rg, rb = rgbImage.getpixel((size[0] - x-1, size[1] - y-1))

            # 色付きのピクセルかどうか（白もしくは白に近しい色を切り抜くため）
            if (r + g + b) < 600:
                if lPix == -1:
                    lPix = x
                if y < tPix:
                    tPix = y

            if (rr + rg + rb) < 600:
                if rPix == -1:
                    rPix = size[0] - x
                if size[1] - y > bPix:
                    bPix = size[1] - y

    print(tPix, lPix, bPix, rPix)

    try:
        trimImageFile = img.crop((lPix, tPix, rPix, bPix))  # トリミング
        trimImageFile.save('tmp/' + _filename, quality=100)  # 保存
    except:
        print('Error')
