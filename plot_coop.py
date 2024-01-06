import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import re
from scipy.optimize import curve_fit


def logistic(x, ymin, ymax, xmid, xscale):
    return ymin + (ymax - ymin)/(1 + np.exp(-xscale*(x-xmid)))
# Get a list of all data files



def extract_number(f):
    s = re.findall(r'\d+', f)
    return (int(s[0]) if s else -1, f)


# Get a list of all data files
files = glob.glob('output_*.txt')  # replace with your actual file path
files.sort(key=extract_number)

# Initialize lists to store data
coop_values = []
defacto_heuristics_values = []
uncertainties = []

# Loop over all files
for file in files:
    # Read the data from the file
    coop_dir = pd.read_csv(file, sep='\t')

    # Extract the 'coop' and 'defacto_heuristics' values and add them to the lists
    coop_values.extend([coop_dir['coop'].values])
    defacto_heuristics_values.extend([coop_dir['defacto_heuristics'].values])

    # Extract the degree of uncertainty from the filename and add it to the list
    uncertainty = (len(files))-1  # replace with your actual method

coop_dir = {}
for i in range(len(coop_values[0])):
    coop_dir[str(i)] = []
    for lst in coop_values:
        coop_dir[str(i)].append(lst[i])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

for key, values in coop_dir.items():
    x = list(range(len(values)))
    ax.plot(x, values, color='gray', alpha=0.1)
    ax.scatter(x, values, color='gray', alpha=0.1, s=5)

mean_values = [np.mean([coop_dir[key][i] for key in coop_dir]) for i in range(len(coop_dir['0']))]

# Create a cubic interpolation function
popt, pcov = curve_fit(logistic, range(len(mean_values)), mean_values)
xnew = np.linspace(0, len(mean_values)-1, num=100, endpoint=True)

# Calculate the y values for the logistic function
y_logistic = logistic(xnew, *popt)

# Add the logistic function to your plot
ax.plot(xnew, y_logistic, color='red', linewidth=2.0)
print(coop_dir)
# Add red points on the curve

ax.set_xlim(0, uncertainty)
ax.set_ylim(0, 1)

ax.set_xlabel("Uncertainty")
ax.set_ylabel("Cooperation")
plt.title("Cooperation at Different Levels of Uncertainty")

plt.show()
