import easyocr

import streamlit as st


def is_string(variable): return isinstance(variable, str)


def read_text_from_photo(reader, photo):
    detection = reader.readtext(photo)
    text = ""
    for row in detection:
        for el in row:
            if is_string(el):
                text += el + "\n"
    return text


reader = easyocr.Reader(['ru', 'en'])
st.title("Загрузка фотографии, с которой вы хотите получить текст")
st.write("Тестовая ссылка:")
st.write("https://static1.wow2print.com/storage/65/gallery/image/1896205816629f8ee1d12786.96956893.webp")
photo = st.text_input("Вставьте url фотографии")
st.button("Обработать")
if photo:
    st.image(photo)
    st.title("Вывод текста, считанного с фотографии")
    text = read_text_from_photo(reader, photo)
    if text:
        st.write("Вывод текста выглядит так:")
        st.write(text)
    else:
        st.write("Нейросети не удалось распознать текст")
