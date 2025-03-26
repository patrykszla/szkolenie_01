def connect(**opcje):  # ** agrumenty nazwane, keywords arg, słownikowe!!
    print(opcje)


connect(test='test')


def all_args(*args, **kwargs):
    print(args, kwargs)

all_args('test', a='taaaa')
