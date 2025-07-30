def encoded_caesar(str, k):
    alphabet_lower = {}
    for i in range(0, 26):
        letters = chr(ord("a") + i)
        alphabet_lower[letters] = i + 1  # dict_name[key] = value

    alphabet_upper = {}
    for i in range(26):
        letters = chr(ord("A") + i)
        alphabet_upper[letters] = i + 1

    lis = []
    cases_lis = []
    for i in str:
        if i == " ":
            lis.append(" ")
            cases_lis.append(" ")
        elif i in alphabet_lower:
            if alphabet_lower[i] + k > 26:
                newNume = alphabet_lower[i] - (26 - k)
                lis.append(newNume)
                cases_lis.append("lower")
            else:
                newNume = alphabet_lower[i] + k
                lis.append(newNume)
                cases_lis.append("lower")
        elif i in alphabet_upper:
            if alphabet_upper[i] + k > 26:
                newNume = alphabet_upper[i] - (26 - k)
                lis.append(newNume)
                cases_lis.append("upper")
            else:
                newNume = alphabet_upper[i] + k
                lis.append(newNume)
                cases_lis.append("upper")

    print(lis)

    encoded_str = []
    for i, case in zip(lis, cases_lis):  # xử lý từng cặp (hoặc bộ) phần tử tương ứn
        if case == " ":
            encoded_str.append(" ")
        elif case == "lower":
            for key, val in alphabet_lower.items():
                if val == i:
                    encoded_str.append(key)
        elif case == "upper":
            for key, val in alphabet_upper.items():
                if val == i:
                    encoded_str.append(key)

    encoded_str = "".join(encoded_str)
    return encoded_str


def decoded_caesar(str, k):
    alphabet_lower = {}
    for i in range(0, 26):
        letters = chr(ord("a") + i)
        alphabet_lower[letters] = i + 1  # dict_name[key] = value

    alphabet_upper = {}
    for i in range(26):
        letters = chr(ord("A") + i)
        alphabet_upper[letters] = i + 1

    lis = []
    cases_lis = []

    for i in str:
        if i == " ":
            lis.append(" ")
            cases_lis.append(" ")
        if i != " " and alphabet_lower[i] - k < 1:
            newNume = alphabet_lower[i] + (26 - k)
            lis.append(newNume)
            cases_lis.append("lower")
        elif i != " " and alphabet_lower[i] - k > 1:
            newNume = alphabet_lower[i] - k
            lis.append(newNume)
            cases_lis.append("lower")

    decoded_str = []
    for i, case in zip(lis, cases_lis):  # xử lý từng cặp (hoặc bộ) phần tử tương ứn
        if case == " ":
            decoded_str.append(" ")
        if case == "lower":
            for key, val in alphabet_lower.items():
                if val == i:
                    decoded_str.append(key)
        elif case == "upper":
            for key, val in alphabet_upper.items():
                if val == i:
                    decoded_str.append(key)

    decoded_str = "".join(decoded_str)
    print(decoded_str)
    return decoded_str


def meaning_brute_force(str_li, words_list):
    raw_texts = str_li.split()

    clean = []
    score = 0

    for word in raw_texts:
        words = word.lower()
        clean.append(words)

    print(clean)
    for w in clean:
        if w in words_list:
            score += 1

    return score


import pandas as pd


plaintext = "hello world fromvietnamz"
encode = encoded_caesar(plaintext, 17)
print(encode)

df = pd.read_csv(
    "C:/Users/ngkho/OneDrive/Máy tính/Projects/cryptography/caesar-cipher/unigram_freq.csv"
)
words_eng_common = set(df["word"].astype(str).str.lower())


best_score = -1
best_case = ""  #
best_shift = 0

for i in range(26):
    decode = decoded_caesar(encode, i)
    score = meaning_brute_force(decode, words_eng_common)
    if score > best_score:
        best_score = score
        best_case = decode
        best_shift = i

print(best_case)
print(best_shift)
