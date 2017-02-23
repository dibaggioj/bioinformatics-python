import sys
import fileinput

ASTHMA_SEQUENCE = "CGCGC"

argv = list(sys.argv)

print argv[0]
print argv[1]
print argv[2]

output_file = open(argv[2], 'w+')
strand_index = -1
# people = {}
asthma_patients = []
asthma_patients_string = ""

for line in fileinput.input(argv[1]):
    name_dna = line.split(', ')
    if len(name_dna) == 2:
        person = name_dna[0]
        sequence = name_dna[1].replace('\n', '')
        # people[person] = sequence
        if ASTHMA_SEQUENCE in sequence:
            asthma_patients.append(person)
            asthma_patients_string += person + '\n'

output_file.write(asthma_patients_string)

print asthma_patients
