# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q



from itertools import groupby, starmap


def file_encode(a, b):
    with open(a) as file1, open (b, 'a') as file2: 
        for i in file1:
            for let, amount in groupby(i):
                file2.write("".join([f"{len(list(amount))}{let}"]))

def file_decode(c):
    with open(c) as file1, open(a, 'a') as file2:
        
        for i in file1:   
            temp = ''     
            my_list = []  
            for char in i.strip():        
                if char.isdigit(): 
                    temp += char 
                else:             
                    temp = int(temp) 
                    my_list.append([temp, char]) 
                    temp = '' 
            file2.write("".join(starmap(lambda m, n: m * n, my_list))) 

#a = input("Enter the name of the file with text: ")
a = "text_words.txt"
#b = input("Enter the name of the file to record: ")
b = "text_code_words.txt"
#c = input("Enter the name of the file to decode: ")
c = "text_code_words.txt"

file_encode(a, b)
file_decode(c)