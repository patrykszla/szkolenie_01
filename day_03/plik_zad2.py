import chardet

# with open('test.log', 'r', encoding="utf-8") as fh:
#     raw_data = fh.read()
#
# print(raw_data)

# rb odczyt binarnie
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
print(type(raw_data))
result = chardet.detect(raw_data)
print(result)
print(type(result))
encoding = result['encoding']
print("Znalezione kodowanie znaków:", encoding)

print(raw_data.decode(encoding=encoding))