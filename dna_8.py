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

string_1=user_dna_sequence[0][2]
for index in range(19,len(string_1)):
    if string_1[19]=="G":

        print(user_dna_sequence[0])

string_2=user_dna_sequence[1][2]
for index in range(18,len(string_2)):
    if string_2[18]=="G":
        print(user_dna_sequence[1])

string_3=user_dna_sequence[2][2]
for index in range(18,len(string_3)):
    if string_3[18]=="G":
        print(user_dna_sequence[2])

string_4=user_dna_sequence[3][2]
for index in range(17,len(string_4)):
    if string_4[17]=="G":
        print(user_dna_sequence[3])
