from typing import Literal

from PIL import Image
import numpy as np

TYPE_BO = Literal['little', 'big']


# converters
#   to bytes

def bytearr_byte(ba: bytearray) -> bytes:
    return bytes(ba)


def byte_bytearr(b: bytes) -> bytearray:
    return bytearray(b)


def strip_leading_null_bytes(b: (bytes, bytearray)) -> bytes:
    if isinstance(b, bytearray):
        ba = b
    else:
        ba = byte_bytearr(b)

    for idx, _b in enumerate(ba):
        if _b != 0:
            return bytearr_byte(ba[idx:])


def hex_byte(h: str, strip: bool = False) -> bytes:
    b = bytes.fromhex(h)

    if strip:
        return strip_leading_null_bytes(b)

    return b


def str_byte(s: str, enc: str = 'utf-8', strip: bool = False) -> bytes:
    b = s.encode(encoding=enc)

    if strip:
        return strip_leading_null_bytes(b)

    return b


def int_byte(i: int, size: int = None, bo: TYPE_BO = 'big', strip: bool = True) -> bytes:
    if size is None:
        size = i.bit_length() + 7

    b = i.to_bytes(size, bo)

    if strip:
        return strip_leading_null_bytes(b)

    return b


#   to int

def byte_int(b: bytes, bo: TYPE_BO = 'big') -> int:
    return int.from_bytes(b, bo)


def hex_int(h: str) -> int:
    return byte_int(hex_byte(h))


#  to str

def byte_hex(b: bytes) -> str:
    return b.hex()


def byte_str(b: bytes, enc: str = 'utf-8') -> str:
    return b.decode(encoding=enc)


def int_hex(i: int) -> str:
    return byte_hex(int_byte(i))


# data visualisation

def to_img(pixel_fnc, data: list, appendix: str, x: int, y: int):
    pixels = np.zeros((y, x, 3), dtype=np.uint8)
    pixel_fnc(data=data, pixels=pixels)
    image = Image.fromarray(pixels)
    image.save(f'test_{appendix}.png')


def hex_to_img(data: list, pixels: np.ndarray):
    for y, d in enumerate(data):
        for x, h in enumerate(str(d)):
            c = int(h) * 16
            pixels[y, x] = [c, c, c]


def hex_to_bin_to_img(data: list, pixels: np.ndarray):
    for y, d in enumerate(data):
        for x, b in enumerate(bin(d)[2:]):
            c = 64 if b == '0' else 240
            pixels[y, x] = [c, c, c]


def bin_to_img(data: list, pixels: np.ndarray):
    for y, d in enumerate(data):
        if d.startswith('0b'):
            d = d[2:]

        for x, b in enumerate(d):
            c = 64 if b == '0' else 240
            pixels[y, x] = [c, c, c]
