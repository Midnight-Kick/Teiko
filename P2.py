import csv
import matplotlib.pyplot as plt

# Initialize dictionaries to store data for responders and non-responders
cell_populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
responders = {pop: [] for pop in cell_populations}
non_responders = {pop: [] for pop in cell_populations}

# Maps to store sample responses and sample types
response_map = {}
sample_type_map = {}

# Read response and sample type data
with open('cell-count.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        response_map[row['sample']] = row['response']
        sample_type_map[row['sample']] = row['sample_type']

# Read relative cell counts and segregate by response (responder or non-responder)
with open('cell-count-relative.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sample = row['sample']
        if sample_type_map.get(sample) == 'PBMC':  # Only consider PBMC samples
            response = response_map.get(sample)
            population = row['population']
            percentage = float(row['percentage'])
            
            if response == 'y':  # Responders
                responders[population].append(percentage)
            elif response == 'n':  # Non-responders
                non_responders[population].append(percentage)

# Generate and save boxplots for each population
for pop in cell_populations:
    # Prepare data for boxplot (responders vs non-responders)
    data = [responders[pop], non_responders[pop]]
    
    # Create the boxplot
    plt.figure()
    plt.boxplot(data, labels=['Responders', 'Non-Responders'])
    plt.title(f'Boxplot of {pop} Relative Frequencies')
    plt.ylabel('Relative Frequency (%)')
    
    # Save the plot as a file (e.g., 'b_cell_boxplot.png')
    plt.savefig(f'{pop}_boxplot.png')
    plt.close()  # Close the plot to avoid display
