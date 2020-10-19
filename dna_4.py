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
    if element[1]<20:
        arr.append(element)
#print(arr)

arr[0][2]=arr[0][2].replace("G","A")
arr[0][2]=arr[0][2].replace("T","C")
print(arr[0][2])

arr[1][2]=arr[1][2].replace("G","A")
arr[1][2]=arr[1][2].replace("T","C")
print(arr[1][2])
