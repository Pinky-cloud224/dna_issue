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
c=string_1[0]+string_1[1],string_1[2]+string_1[3]+string_1[4],string_1[5]+string_1[6]+string_1[7],string_1[8]+string_1[9]+string_1[10],string_1[11]+string_1[12]+string_1[13],string_1[14]+string_1[15]+string_1[16],string_1[17]+string_1[18]+string_1[19]
print("Person-1:",c)

count=0

for element in c:
    if element=="AAA":
        count+=1
print("AAA","=",count)

string_2=user_dna_sequence[1][2]
d=string_2[0],string_2[1]+string_2[2]+string_2[3],string_2[4]+string_2[5]+string_2[6],string_2[7]+string_2[8]+string_2[9],string_2[10]+string_2[11]+string_2[12],string_2[13]+string_2[14]+string_2[15],string_2[16]+string_2[17]+string_2[18]

print("Person-2:",d)

count_1=0

for element in d:
    if element=="AAA":
        count_1+=1
print("AAA","=",count_1)

string_3=user_dna_sequence[2][2]
e=string_3[0],string_3[1]+string_3[2]+string_3[3],string_3[4]+string_3[5]+string_3[6],string_3[7]+string_3[8]+string_3[9],string_3[10]+string_3[11]+string_3[12],string_3[13]+string_3[14]+string_3[15],string_3[16]+string_3[17]+string_3[18]
print("Person-3:",e)

count_2=0

for element in e:
    if element=="AAA":
        count_2+=1
print("AAA","=",count_2)

string_4=user_dna_sequence[3][2]
f=string_4[0],string_4[1]+string_4[2]+string_4[3],string_4[4]+string_4[5]+string_4[6],string_4[7]+string_4[8]+string_4[9],string_4[10]+string_4[11]+string_4[12],string_4[13]+string_4[14]+string_4[15],string_4[16]+string_4[17]
print("Person-4:",f)

count_3=0

for element in f:
    if element=="AAA":
        count_3+=1
print("AAA","=",count_3)




