source = u'qwertyuiopasdfghjklzxcvbnm'
key = '1234567890'
t = 'hello'

def encode(text, step):
    return text.translate(
        str.maketrans(source, source[step:] + source[:step])
    )
def decode(text, step):
    return text.translate(
        str.maketrans(source[step:] + source[:step], source)
    )