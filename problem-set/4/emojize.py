# install emojize first using pip install emoji in cmd or terminal

import emoji

msg = input("Input: ")
print(emoji.emojize(f"Output: {msg}", language="alias"))
