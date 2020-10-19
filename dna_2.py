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

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

for element in user_dna_sequence[0][2]:
    if element==dna_elements[0]:
        count_1 +=1
print(dna_elements[0],"=",count_1)


for element in user_dna_sequence[1][2]:
    if element==dna_elements[1]:
        count_2 +=1
print(dna_elements[1],"=",count_2)

for element in user_dna_sequence[2][2]:
    if element==dna_elements[2]:
        count_3 +=1
print(dna_elements[2],"=",count_3)

for element in user_dna_sequence[3][2]:
    if element==dna_elements[3]:
        count_4 +=1
print(dna_elements[3],"=",count_4)



