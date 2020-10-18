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

invalid_dna_0 = [ ]
invalid_dna_1 = [ ]
invalid_dna_2= [ ]
invalid_dna_3 = [ ]

invalid_dna = [ ]

for element in user_dna_sequence[0][2]:
    if (element not in dna_elements) and (element not in invalid_dna_0):
        invalid_dna_0.append(element)
#print(invalid_dna_0)

for element in user_dna_sequence[1][2]:
    if (element not in dna_elements) and (element not in invalid_dna_1):
        invalid_dna_1.append(element)
#print(invalid_dna_1)

for element in user_dna_sequence[2][2]:
    if (element not in dna_elements) and (element not in invalid_dna_2):
        invalid_dna_2.append(element)
#print(invalid_dna_2)

for element in user_dna_sequence[3][2]:
    if (element not in dna_elements) and (element not in invalid_dna_3):
        invalid_dna_3.append(element)
#print(invalid_dna_3)

invalid_dna.append(invalid_dna_0)
invalid_dna.append(invalid_dna_1)
invalid_dna.append(invalid_dna_2)
invalid_dna.append(invalid_dna_3)


#print(invalid_dna)

new_valid_dna_sequence_1= [ ]

for element in user_dna_sequence[0][2]:
    if element in dna_elements and (element not in invalid_dna):
        new_valid_dna_sequence_1.append(element)
print("Name:",user_dna_sequence[0][0],",","Age=",user_dna_sequence[0][1],",","New_DNA_Sequence=", new_valid_dna_sequence_1)

new_valid_dna_sequence_2= [ ]

for element in user_dna_sequence[1][2]:
    if element in dna_elements and (element not in invalid_dna):
        new_valid_dna_sequence_2.append(element)
print("Name:",user_dna_sequence[1][0],",","Age=",user_dna_sequence[1][1],",","New_DNA_Sequence=", new_valid_dna_sequence_2)

new_valid_dna_sequence_3= [ ]

for element in user_dna_sequence[2][2]:
    if element in dna_elements and (element not in invalid_dna):
        new_valid_dna_sequence_3.append(element)
print("Name:",user_dna_sequence[2][0],",","Age=",user_dna_sequence[2][1],",","New_DNA_Sequence=", new_valid_dna_sequence_3)

new_valid_dna_sequence_4= [ ]

for element in user_dna_sequence[3][2]:
    if element in dna_elements and (element not in invalid_dna):
        new_valid_dna_sequence_4.append(element)
print("Name:",user_dna_sequence[3][0],",","Age=",user_dna_sequence[3][1],",","New_DNA_Sequence=", new_valid_dna_sequence_4)











