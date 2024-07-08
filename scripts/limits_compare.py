import matplotlib.pyplot as plt
import sys
import json

with open('/afs/cern.ch/user/c/ccarriva/ZZHH/operators.json', 'r') as file:
    data = json.load(file)
coefficients = {key: value['best limit'] for key, value in data.items() if value['turn'] == 'on'}

def parse_interval(interval):
    """Parse an interval from string format to a tuple of floats."""
    try:
        if interval == '-' or not interval.strip('[]'):
            return (0, 0)  # Handle cases where there is no interval.
        low, high = interval.strip('[]').split(',')
        return float(low), float(high)
    except ValueError:
        print(f"Error parsing interval: {interval}")
        return (0, 0)

def read_user_intervals(filename):
    user_intervals = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split(':')
                if len(parts) < 2:
                    print("Skipping line, incorrect format:", line)
                    continue
                wc_description = parts[0].strip()
                interval = parts[1].strip()
                if "no unitarity" in wc_description:
                    wc = wc_description.split()[0]
                    user_intervals[wc] = interval
                    print(f"Reading {wc}: {interval}")  # Debug print
        return user_intervals
    except FileNotFoundError:
        print(f"Error: File not found {filename}")
        return user_intervals
    except Exception as e:
        print(f"An error occurred: {e}")
        return user_intervals

def plot_intervals(user_intervals):
    with open('/afs/cern.ch/user/c/ccarriva/ZZHH/operators.json', 'r') as file:
        data2 = json.load(file)
    labels = [key for key, value in data2.items() if value['turn'] == 'on']
    table_intervals = [parse_interval(coefficients[key]) for key in labels]
    user_parsed_intervals = [parse_interval(user_intervals.get(key, "-")) for key in labels]
    x = range(len(labels))  
    width = 0.25  # Bar width
    process = sys.argv[1]
    
    fig, ax = plt.subplots()
    rects1 = ax.barh([pos - width/2 for pos in x], [intv[1] - intv[0] for intv in table_intervals],
                     width, left=[intv[0] for intv in table_intervals], label='Best limits')
    rects2 = ax.barh([pos + width/2 for pos in x], [intv[1] - intv[0] for intv in user_parsed_intervals],
                     width, left=[intv[0] for intv in user_parsed_intervals], label=f'{process}', color='#FF8565')

    ax.axvline(x=0, color='grey', linestyle='--')
    ax.set_xlabel('Interval @95%CL')
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.legend(loc='upper right')
    
    ax.set_xlim(-25, 25)

    fig.tight_layout()
    plt.savefig(f'/afs/cern.ch/user/c/ccarriva/ZZHH/Output/{process}/limits_compare_{process}.png') 

process = sys.argv[1]
user_input_intervals = read_user_intervals(f'/afs/cern.ch/user/c/ccarriva/ZZHH/Output/{process}/results_{process}.txt')
plot_intervals(user_input_intervals)

