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
if user_dna_sequence[0][1]>20:
    str1=string_1.replace("A","G")
    print(str1)
    
string_2=user_dna_sequence[1][2]
if user_dna_sequence[1][1]>20:
    str2=string_2.replace("A","G")
    print(str2)
    
string_3=user_dna_sequence[2][2]
if user_dna_sequence[2][1]>20:
    str3=string_3.replace("A","G")
    print(str3)
    
string_4=user_dna_sequence[3][2]
if user_dna_sequence[3][1]>20:
    str4=string_4.replace("A","G")
    print(str4)

