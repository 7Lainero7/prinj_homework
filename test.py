import easyocr

from main import read_text_from_photo


def test_read_text_from_photo():
    reader = easyocr.Reader(['ru', 'en'])
    tested_text = "G R Е Е N\nNLN\n6 е3 nBX\n"

    text = read_text_from_photo(reader, "test_photo.jfif")

    assert text == tested_text
