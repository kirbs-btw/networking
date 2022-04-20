def encrypt(msg):
    dic = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    PRIV_KEY = open("key.txt", "r").readlines()[0]
    pos = 0

    message_ENCRYPTED = ""

    for i in msg:
        index = dic.index(i)
        shift = dic.index(PRIV_KEY[pos])
        new_letter_index = index + shift + 1
        message_ENCRYPTED += str(dic[new_letter_index])
        pos += 1

    return message_ENCRYPTED

if __name__ == '__main__':
    message = "schwanz schwaz schwanz"

    print(encrypt(message))
