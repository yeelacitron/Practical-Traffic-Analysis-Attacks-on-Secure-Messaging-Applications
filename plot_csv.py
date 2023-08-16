import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def display(file_name):
    #Step 1 : Load the data from the CSV file
    data = pd.read_csv(file_name)

    # Extract "Time" and "Length" values from the DataFrame as numpy arrays
    time_values = data["Time"].astype(float).to_numpy()
    length_values = data["Length"].astype(int).to_numpy()

    plot_time_per_len(time_values,length_values)
    
    plot_time_per_len_groupby(time_values,length_values)

    plot_pdf(time_values)

    plot_packet_per_1_sec(data,time_values)
    

def plot_time_per_len(time_values,length_values):
    # Plot the data as bars
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.bar(time_values, length_values)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Packet Size (bytes)")
    plt.title("Packet Size vs. Time")
    plt.grid(axis="y")  # Add grid lines only to the y-axis
    plt.show()
    
def plot_time_per_len_groupby(time_values, length_values):
    # Plot the data as bars
    plt.figure(figsize=(10, 6))  # Set the figure size

    # Group packets sent within 0.7 seconds and calculate their total length
    grouped_time = []
    grouped_length = []
    current_time = time_values[0]
    current_length = 0

    for time, length in zip(time_values, length_values):
        if time - current_time <= 0.7:
            current_length += length
        else:
            grouped_time.append(current_time)
            grouped_length.append(current_length)
            current_time = time
            current_length = length

    plt.bar(grouped_time, grouped_length, width=0.7)  # Use width to indicate the time interval
    plt.xlabel("Time (seconds)")
    plt.ylabel("Total Packet Size (bytes)")
    plt.title("Total Packet Size vs. Time (Packets Sent within 0.7 seconds)")
    plt.grid(axis="y")  # Add grid lines only to the y-axis
    plt.show()
    
def plot_pdf(time_values):
    # Calculate the time differences between packets
    time_diff = time_values[1:] - time_values[:-1]

    # Calculate the histogram
    hist, bin_edges = np.histogram(time_diff, bins=20, density=True)
    bin_width = bin_edges[1] - bin_edges[0]
    normalized_hist = hist / hist.sum()

    # Plot the Histogram of Inter-Message Delays
    plt.figure(figsize=(10, 6))
    plt.bar(bin_edges[:-1], normalized_hist, width=bin_width, alpha=0.5, edgecolor='blue', fill=False, label="Histogram of Inter-Message Delays")

    plt.xlabel("Time Difference")
    plt.ylabel("Normalized Probability Density")
    plt.title("Histogram of Inter-Message Delays")
    plt.legend()
    plt.show()
    
def plot_packet_per_1_sec(data,time_values):
    # Convert time to one-second intervals and sum the number of packets for each interval
    time_intervals = pd.cut(time_values, bins=int(time_values.max() ) + 1, labels=False)
    packets_per_interval = data.groupby(time_intervals)['No.'].count()

    # Create a new DataFrame with the time intervals and normalized packets
    result_data = pd.DataFrame({'Time': (packets_per_interval.index ).astype(float), 'Packets': packets_per_interval})

    # Plotting the data
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(result_data['Time'].values, result_data['Packets'].values, marker='o', linestyle='-')
    plt.xlabel('Time (Seconds)')
    plt.ylabel('packets per interval')
    plt.title('Number of Packets in one-Second Intervals')
    plt.grid(True)
    plt.show()
    
    
display("object_30sec_abi_phone.csv")