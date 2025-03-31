import csv
import matplotlib.pyplot as plt

cell_populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
responders = {pop: [] for pop in cell_populations}
non_responders = {pop: [] for pop in cell_populations}

response_map = {}
sample_type_map = {}

with open('cell-count.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        response_map[row['sample']] = row['response']
        sample_type_map[row['sample']] = row['sample_type']

with open('cell-count-relative.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sample = row['sample']
        if sample_type_map.get(sample) == 'PBMC': 
            response = response_map.get(sample)
            population = row['population']
            percentage = float(row['percentage'])
            
            if response == 'y': 
                responders[population].append(percentage)
            elif response == 'n': 
                non_responders[population].append(percentage)

for pop in cell_populations: 
    data = [responders[pop], non_responders[pop]]
    
    plt.figure()
    plt.boxplot(data, labels=['Responders', 'Non-Responders'])
    plt.title(f'Boxplot of {pop} Relative Frequencies')
    plt.ylabel('Relative Frequency (%)')
    plt.show()
