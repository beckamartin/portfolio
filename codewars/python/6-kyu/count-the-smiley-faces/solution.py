def count_smileys(arr):
    import re

    smiles = 0

    for i in arr:
        if matches := re.search(r"^(:|;){1}(-|~)?(\)|D){1}$", i):
            smiles += 1

    return smiles