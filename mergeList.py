

arr_1 = [1, 4, 5, 10, 17, 20, 23, 26]
arr_2 = [2, 4, 6, 13, 14, 16, 21, 22]


# l_1 = len(arr_1)
# l_2 = len(arr_2)


# l = l_1 + l_2

# arr = []

# p_1 = 0
# p_2 = 0

# for x in range(l):
    
#     if(p_1 >= l_1):
#         arr.append(arr_2[p_2:])
#         break

#     if(p_2 >= l_2):
#         arr.append(arr_1[p_1:])
#         break
            
#     if(arr_1[p_1] < arr_2[p_2]):
#         arr.append(arr_1[p_1])
#         p_1 = p_1 + 1
#     else:
#         arr.append(arr_2[p_2])
#         p_2 = p_2 + 1
        
        
# print(arr)
# print(arr_1, arr_2)

i = 0
j = 0

arr = []

while len(arr_1) > i and len(arr_2) > j:
    if(arr_1[i] < arr_2[j]):
        arr.append(arr_1[i])
        i += 1
    else:
        arr.append(arr_2[j])
        j += 1
        
        
arr = arr + arr_1[i:] + arr_2[j:]

