import csv

# Define cell populations
cell_populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

# Load data
data = []
with open('cell-count.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sample = row['sample']
        counts = {pop: int(row[pop]) for pop in cell_populations}
        total_count = sum(counts.values())
        for pop, count in counts.items():
            percentage = (count / total_count) * 100 if total_count > 0 else 0
            data.append([sample, total_count, pop, count, percentage])

# Save output
with open('cell-count-relative.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['sample', 'total_count', 'population', 'count', 'percentage'])
    writer.writerows(data)
