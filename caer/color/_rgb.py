#    _____           ______  _____ 
#  / ____/    /\    |  ____ |  __ \
# | |        /  \   | |__   | |__) | Caer - Modern Computer Vision
# | |       / /\ \  |  __|  |  _  /  Languages: Python, C, C++
# | |___   / ____ \ | |____ | | \ \  http://github.com/jasmcaus/caer
#  \_____\/_/    \_ \______ |_|  \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Caer Authors <http://github.com/jasmcaus>


import cv2 as cv 

from ..adorad import Tensor, to_tensor_, _convert_to_tensor_and_rename_cspace
from ._constants import RGB2BGR, RGB2GRAY, RGB2HSV, RGB2LAB, RGB2HLS

__all__ = [
    'rgb2bgr',
    'rgb2gray',
    'rgb2hsv',
    'rgb2lab',
    'rgb2hls'
]

def _is_rgb_image(img):
    img = to_tensor_(img)
    # return img.is_rgb()
    return img.is_rgb() or (len(img.shape) == 3 and img.shape[-1] == 3)


def rgb2bgr(img) -> Tensor:
    r"""
        Converts an RGB image to its BGR version.

    Args:
        img (Tensor): Valid RGB image array
    
    Returns:
        BGR image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This function converts an RGB image to its BGR counterpart')

    im = cv.cvtColor(img, RGB2BGR)
    return _convert_to_tensor_and_rename_cspace(im, 'bgr')


def rgb2gray(img) -> Tensor:
    r"""
        Converts an RGB image to its Grayscale version.

    Args:
        img (Tensor): Valid RGB image array
    
    Returns:
        Grayscale image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This function converts an RGB image to its Grayscale counterpart')
    
    im = cv.cvtColor(img, RGB2GRAY)
    return _convert_to_tensor_and_rename_cspace(im, 'gray')


def rgb2hsv(img) -> Tensor:
    r"""
        Converts an RGB image to its HSV version.

    Args:
        img (Tensor): Valid RGB image array
    
    Returns:
        HSV image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This function converts an RGB image to its HSV counterpart')
    
    im = cv.cvtColor(img, RGB2HSV)
    return _convert_to_tensor_and_rename_cspace(im, 'hsv')


def rgb2hls(img) -> Tensor:
    r"""
        Converts an RGB image to its HLS version.

    Args:
        img (Tensor): Valid RGB image array
    
    Returns:
        HLS image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This function converts an RGB image to its HLS counterpart')
    
    im = cv.cvtColor(img, RGB2HLS)
    return _convert_to_tensor_and_rename_cspace(im, 'hls')


def rgb2lab(img) -> Tensor:
    r"""
        Converts an RGB image to its LAB version.

    Args:
        img (Tensor): Valid RGB image array
    
    Returns:
        LAB image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not _is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This function converts an RGB image to its LAB counterpart')

    im = cv.cvtColor(img, RGB2LAB)
    return _convert_to_tensor_and_rename_cspace(im, 'lab')