class RomanNumerals():
    def to_roman(val):
        roman_m = val // 1000
        val = val % 1000

        roman_cm = val // 900
        val = val % 900

        roman_d = val // 500
        val = val % 500

        roman_cd = val // 400
        val = val % 400

        roman_c = val // 100
        val = val % 100

        roman_xc = val // 90
        val = val % 90

        roman_l = val // 50
        val = val % 50

        roman_xl = val // 40
        val = val % 40

        roman_x = val // 10
        val = val % 10

        roman_ix = val // 9
        val = val % 9

        roman_v = val // 5
        val = val % 5

        roman_iv = val // 4
        val = val % 4

        roman_i = val // 1

        return ("M" * roman_m) + ("CM" * roman_cm) + ("D" * roman_d) + ("CD" * roman_cd) + ("C" * roman_c) + ("XC" * roman_xc) + ("L" * roman_l) + ("XL" * roman_xl) + ("X" * roman_x) + ("IX" * roman_ix) + ("V" * roman_v) + ("IV" * roman_iv) + ("I" * roman_i)
        
    def from_roman(roman_num):
        result = 0
        i = 0

        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i + 2] == "CM":
                result += 900
                i += 2

            elif i + 1 < len(roman_num) and roman_num[i:i + 2] == "CD":
                result += 400
                i += 2

            elif i + 1 < len(roman_num) and roman_num[i:i + 2] == "XC":
                result += 90
                i += 2

            elif i + 1 < len(roman_num) and roman_num[i:i + 2] == "XL":
                result += 40
                i += 2

            elif i + 1 < len(roman_num) and roman_num[i:i + 2] == "IX":
                result += 9
                i += 2
            
            elif i + 1 < len(roman_num) and roman_num[i:i + 2] == "IV":
                result += 4
                i += 2
            
            else:
                char = roman_num[i]

                if char == "M":
                    result += 1000

                elif char == "D":
                    result += 500

                elif char == "C":
                    result += 100

                elif char == "L":
                    result += 50

                elif char == "X":
                    result += 10  

                elif char == "V":
                    result += 5
                    
                elif char == "I":
                    result += 1

                i += 1

        return result