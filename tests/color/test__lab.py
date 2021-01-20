#    _____           ______  _____ 
#  / ____/    /\    |  ____ |  __ \
# | |        /  \   | |__   | |__) | Caer - Modern Computer Vision
# | |       / /\ \  |  __|  |  _  /  Languages: Python, C, C++
# | |___   / ____ \ | |____ | | \ \  http://github.com/jasmcaus/caer
#  \_____\/_/    \_ \______ |_|  \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Caer Authors <http://github.com/jasmcaus>

import caer 
import cv2 as cv 
import os 

here = os.path.dirname(os.path.dirname(__file__))
img_path = os.path.join(here, 'data', 'green_fish.jpg')


def test_lab2rgb():
    cv_lab = cv.imread(img_path)

    rgb = caer.lab2rgb(cv_lab)

    assert len(rgb.shape) == 3 
    assert isinstance(rgb, caer.Tensor)
    assert rgb.is_rgb()


def test_lab2bgr():
    cv_lab = cv.imread(img_path)

    bgr = caer.lab2lab(cv_lab)

    assert len(bgr.shape) == 3 
    assert isinstance(bgr, caer.Tensor)
    assert bgr.is_bgr()

    
def test_lab2gray():
    cv_lab = cv.imread(img_path)

    gray = caer.lab2gray(cv_lab)

    assert len(gray.shape) == 2
    assert isinstance(gray, caer.Tensor)
    assert gray.is_gray()


def test_lab2hsv():
    cv_lab = cv.imread(img_path)

    hsv = caer.lab2hsv(cv_lab)

    assert len(hsv.shape) == 3 
    assert isinstance(hsv, caer.Tensor)
    assert hsv.is_hsv()


def test_lab2hls():
    cv_lab = cv.imread(img_path)

    hls = caer.lab2hls(cv_lab)

    assert len(hls.shape) == 3 
    assert isinstance(hls, caer.Tensor)
    assert hls.is_hls()