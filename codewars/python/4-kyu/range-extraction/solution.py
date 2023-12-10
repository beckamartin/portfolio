def solution(args):
    sequence = args
    counter = []
    output = ""

    for i in range(len(sequence)):
        counter.append(sequence[i])

        if i + 1 == len(sequence) or sequence[i] + 1 != sequence[i+1]:
            if len(counter) == 1:
                if output == "":
                    output += (str(counter[0]))

                else:
                    output += (f",{str(counter[0])}")
            
            elif len(counter) < 3:
                if output == "":
                    output += (",".join(str(x) for x in counter))
                
                else:
                    output += (f",{(','.join(str(x) for x in counter))}")

            else:
                if output == "":
                    output += (f"{counter[0]}-{counter[-1]}")

                else:
                    output += (f",{counter[0]}-{counter[-1]}")

            counter = []

    return output