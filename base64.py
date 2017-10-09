from string import ascii_uppercase, ascii_lowercase, digits

def base64(number):
    if number == 0:
        return "_"
    chars = ascii_uppercase + ascii_lowercase + digits + "-_"
    indexes = []
    power = 0
    final = ""
    while 64 ** power <= number:
        power += 1
    power -= 1
    while power > -1:
        maximum = number // (64 ** power)
        indexes.append(maximum)
        number -= maximum * (64 ** power)
        power -= 1
    for char in indexes:
        final += chars[char-1]
    return final
