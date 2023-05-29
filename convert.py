def hex_byte(h: str) -> bytes:
    return bytes.fromhex(h)


def byte_int(b: bytes) -> int:
    return int.from_bytes(b, 'big')


def hex_int(h: str) -> int:
    return byte_int(hex_byte(h))


def int_byte(i: int) -> bytes:
    return i.to_bytes(
        i.bit_length() + 7,
        'big',
    )


def byte_hex(b: bytes) -> str:
    return b.hex()


def str_byte(s: str) -> bytes:
    return s.encode(encoding='utf-8')


def byte_str(b: bytes) -> str:
    return b.decode(encoding='utf-8')
