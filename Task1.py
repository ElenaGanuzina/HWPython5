# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def word_arr(num, word="абв"):
    my_list = []
    for i in range(num):
        rand_words = sample(word, k=3)
        my_list.append("".join(rand_words))
    return " ".join(my_list)


def get_out(arr):
    return " ".join(arr.replace("абв", "").split())


num = int(input("Number of words: "))
arr = word_arr(num, "абв")
print(arr)
print(get_out(arr))
