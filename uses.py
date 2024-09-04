import re

# arr = [1, 2, 3, 4, 3, 2, 1]


def find_even(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
    return -1


# find_even(arr)

# str = "abcde"


def split_pair(str):
    new = []
    for i in range(0, len(str), 2):
        pair = str[i : i + 2]
        if len(pair) == 1:
            pair += "_"
        new.append(pair)
    return new


# split_pair(str)

# panag = "murcielago"


def panagrama(panag):
    (
        print("Panagrama")
        if len(
            [
                i
                for i, char in enumerate(panag)
                if char.lower() in ["a", "e", "i", "o", "u"]
            ]
        )
        == 5
        else None
    )


# panagrama(panag)

# w = "murcielago"
# w = "murielagos"


def get_middle(w):
    if len(w) % 2 != 0:
        p = w[len(w) // 2]
        print(p)
    else:
        p = w[(len(w) // 2) - 1 : (len(w) // 2) + 1]
        print(p)


# get_middle(w)

# number = 10


def solution(number):
    total = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            total += x
        elif x <= 0:
            return 0
    return total


# solution(number)

# pig = "Pig latin is cool !"


def pig_it(text):
    words = text.split()
    new_words = []
    for word in words:
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            new_words.append(new_word)
        else:
            new_words.append(word)
    return " ".join(new_words)


# pig_it(pig)

# s = "abaa"


def count(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# count(s)

# arr = [":D", ":~)", ";~D", ":)"]


def count_smileys(arr):
    count = 0
    smiles = [
        r":-\)",
        r":-D",
        r":~\)",
        r":~D",
        r";-\)",
        r";-D",
        r";~\)",
        r";~D",
        r":\)",
        r";\)",
        r":D",
        r";D",
    ]

    for text in arr:
        for sm in smiles:
            smile = re.search(sm, text)
            if smile:
                count += 1
    return print(count)
    # return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


# count_smileys(arr)

# snail_map = [[1, 2, 3], [6, 5, 4], [6, 5, 4], [9, 8, 7]]


def snail(snail_map):
    if not snail_map:
        return []

    result = []
    top, bottom, left, right = 0, len(snail_map) - 1, 0, len(snail_map[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(snail_map[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(snail_map[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(snail_map[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(snail_map[i][left])
            left += 1

    return result


# snail(snail_map)
