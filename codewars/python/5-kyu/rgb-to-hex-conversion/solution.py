def rgb(r, g, b):
    def convert(x):
        if x == 10: return "A"
        elif x == 11: return "B"
        elif x == 12: return "C"
        elif x == 13: return "D"
        elif x == 14: return "E"
        elif x == 15: return "F"
        else: return f"{x}"

    hex = ""
        
    for rgb in (r, g, b):
        if rgb < 0:
            hex = hex + str(0) + str(0)
        elif rgb >= 255:
            hex = hex + "F" + "F"
        elif rgb >= 0 and rgb < 255:
            first_number = convert(rgb // 16)
            second_number = convert(rgb % 16)
            hex = hex + str(first_number) + str(second_number)

    return hex