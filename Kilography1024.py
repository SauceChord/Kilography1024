import cv2
import numpy as np
from PIL import Image
from reedsolo import RSCodec, ReedSolomonError
import sys

def lcg_shuffle(lst, seed, a=1664525, c=1013904223, m=2**32):
    arr = lst.copy()
    state = seed
    for i in range(len(arr)-1, 0, -1):
        state = (a * state + c) % m
        j = state % (i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def load_image(path):
    ycbcr = Image.open(path).convert("YCbCr")
    Y, Cb, Cr = ycbcr.split()
    Y_arr = np.array(Y, dtype=np.float32)
    return Y_arr, Cb, Cr

def find_slots(Y_arr, blocks_x, blocks_y, threshold=50, seed=1983):
    slots = []
    for by in range(blocks_y):
        for bx in range(blocks_x):
            block = Y_arr[by*8:by*8+8, bx*8:bx*8+8]
            dct = cv2.dct(block)
            energy = (
                abs(dct[2,3]) +
                abs(dct[3,2]) +
                abs(dct[3,3])
            )
            if energy < threshold:
                for (u, v) in [(1,1), (2,1), (1,2), (2,2)]:
                    slots.append((by, bx, u, v))
    return lcg_shuffle(slots, seed=seed)

def decode(stego):
    Yc_arr,_,_ = load_image(stego)
    H, W       = Yc_arr.shape
    blocks_y   = H // 8
    blocks_x   = W // 8

    coords = find_slots(Yc_arr, blocks_x, blocks_y, threshold=50, seed=1983)

    extracted_bits = []
    for bit_idx in range(len(coords)):
        by, bx, u, v = coords[bit_idx]
        block = Yc_arr[by*8:by*8+8, bx*8:bx*8+8]
        dct   = cv2.dct(block)
        coeff = dct[u, v]
        extracted_bits.append(1 if coeff >= 0 else 0)

    content_magic_bits = extracted_bits[:16]
    content_magic = int("".join(map(str, content_magic_bits)), 2)
    assert content_magic == 0xF00D, "IN XEN MANI fizzled!"
    content_length_bits = extracted_bits[16:32]
    content_length = int("".join(map(str, content_length_bits)), 2)
    content_bits = extracted_bits[32:32 + content_length * 8]

    extracted = bytearray()
    for i in range(0, len(content_bits), 8):
        byte = 0
        for b in content_bits[i:i+8]:
            byte = (byte << 1) | b
        extracted.append(byte)

    try:
        rsc = RSCodec(nsym=32)
        full_payload = rsc.decode(bytes(extracted))[0]
        filename_length = full_payload[0]
        filename = full_payload[1:1+filename_length].decode('utf-8')
        file_data = full_payload[1+filename_length:]
        with open(filename, "wb") as f:
            f.write(file_data)
        print(f"Unearthed tome: {filename}")
    except ReedSolomonError:
        print("Too many rumors to recover!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python kilography.py <image.jpg>")
    else:
        decode(sys.argv[1])