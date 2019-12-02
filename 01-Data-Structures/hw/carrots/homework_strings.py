import matplotlib.pyplot as plt
import re
""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# Counts the number of nucleotides
def count_nucleotides(gene_list):
    count_of_nucleotides = dict.fromkeys(['A', 'C', 'G', 'T'], 0)
    for line in gene_list:
        for nucleide in 'ACGT':
            count_of_nucleotides[nucleide] += line.count(nucleide)
    return count_of_nucleotides

# Plot histogram for dna statistics
def histogram(values, title, x='', y=''):
    plt.figure(title)
    plt.title(title)
    plt.bar(list(values.keys()), values.values())
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    plt.show()


# Show dna statistics in histogram and write statistic to nucleotides.txt file
def dna_statistics(dna_file):
    # read the file dna_file
    dna = open(dna_file, "r")

    # Count number of nucleotides for gene
    description = []
    count_of_nucleotides_list = []
    gene_info = []

    for line in dna.readlines():
        if '>' in line:
            description.append(line.lstrip('>').rstrip('\n'))
            if len(gene_info):
                count_of_nucleotides_list.append(count_nucleotides(gene_info))
                del gene_info[:]
        else:
            gene_info.append(line.rstrip('\n'))

    count_of_nucleotides_list.append(count_nucleotides(gene_info))
    statistic = dict(zip(description, count_of_nucleotides_list))

    # Close dna file
    dna.close()

    # Write statistics to the nucleotide.txt file
    nucleotide = open("nucleotides.txt", "w")

    for key, var in statistic.items():
        nucleotide.write(key + ':' + '\n')
        for element, count in var.items():
            nucleotide.write(element + '-' + str(count) + ' ')
        nucleotide.write('\n')

    # Close nucleotide file
    nucleotide.close()

    # Plot histogram
    xlabel = 'Nucleotides'
    ylabel = 'Frequency'
    for var, key in statistic.items():
        histogram(key, var, xlabel, ylabel)



# Translate from dna to rna and write result to rna.fasta file
def translate_from_dna_to_rna(dna_file):
    # Read the file dna_file
    dna = open(dna_file, "r")

    # Open rna file
    rna = open("rna.fasta", "w")
    for line in dna.readlines():
        if '>' in line:
            rna.write(line)
        else:
            rna.write(line.replace('T', 'U'))

    # Close dna file
    dna.close()

    # Close rna file
    rna.close()

# Translate rna to protein
def translate_rna_to_protein(rna_file):
    # Open rna_codon_table.txt
    rna_table = open("./files/rna_codon_table.txt", "r")

    rna_dict = {}
    for line in rna_table.readlines():
        rna_dict.update(zip(line.split()[::2], line.split()[1::2]))

    # Close rna_table file
    rna_table.close()

    # Open rna.fasta file
    rna_file = open(rna_file, "r")

    # Open protein.fasta
    protein = open("protein.fasta", "w")
    for line in rna_file.readlines():
        if '>' in line:
            protein.write(line)
        else:
            #rna_list = re.findall(r'.{3}', line) # Еще один способ с помощью регулярных выражений.
            rna_list = [line[i:i + 3] for i in range(0, len(line), 3)]
            del rna_list[-1]
            protein_line = ''.join(rna_dict[s] for s in rna_list)
            protein.write(protein_line.replace('Stop', '') + '\n')

    # Close protein.fasta file
    protein.close()

    # Close rna.fasta file
    rna_file.close()


dna_statistics("./files/dna.fasta")

translate_from_dna_to_rna("./files/dna.fasta")

translate_rna_to_protein("rna.fasta")