import csv
import math

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

def mean(data):
    return sum(data) / len(data) if data else 0

def stdev(data, mean_value):
    return math.sqrt(sum((x - mean_value) ** 2 for x in data) / len(data))

for pop in cell_populations:
    mean_responder = mean(responders[pop])
    mean_non_responder = mean(non_responders[pop])
    stdev_responder = stdev(responders[pop], mean_responder)
    stdev_non_responder = stdev(non_responders[pop], mean_non_responder)

    print(f"Population: {pop}")
    print(f"  Responders - Mean: {mean_responder:.2f}, Stdev: {stdev_responder:.2f}")
    print(f"  Non-Responders - Mean: {mean_non_responder:.2f}, Stdev: {stdev_non_responder:.2f}")
