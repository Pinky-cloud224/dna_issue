user_dna_sequence = [
[
"Roksana Kozlova", 18, "GTTAGCCGACTTGGCXCTTT"
],
[
"Roza Kiseleva", 19, "ATTTGGCGAATTGGCCTTT"
],
[
"Kliment Volkov", 27, "ATTTGACCAATTGZGCAAA"
],
[
"Afanas Morozov", 22, "ATTTGACCGATTNGGCAA"
],
]

dna_elements = ["A", "T", "G", "C"]

arr=[]
for element in user_dna_sequence:
    if (element[1]>18)and (element[1]<25):
        arr.append(element)
#print(arr)

arr_1=[ ]
for element in arr[0][2]:
    arr_1.append(element)
#print(arr_1)
arr_1.reverse()
#print(arr_1)


dna_string_1=" "
for element in arr_1:
    dna_string_1+=element
print(dna_string_1)

arr_2=[ ]
for element in arr[1][2]:
    arr_2.append(element)
#print(arr_2)
arr_2.reverse()
#print(arr_2)
    
dna_string_2=" "
for element in arr_2:
    dna_string_2+=element
print(dna_string_2)



arr_2=[ ]
for element in arr[1][2]:
    arr_2.append(element)
#print(arr_2)
