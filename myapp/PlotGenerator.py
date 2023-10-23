import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
data = pd.read_csv("CAN_DATA.csv")

# Step 2: Convert 'can_time' to datetime
data['can_time'] = pd.to_datetime(data['can_time'], format='%d/%m/%Y %H:%M:%S')

# Step 3: Group by Bus ID and count data points
bus_data_counts = data[data['can_param'] == 'Battery SOC']['vehicleid'].value_counts()

# Calculate total number of data points and buses
total_data_points = bus_data_counts.sum()
total_buses = len(bus_data_counts)

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(bus_data_counts.index, bus_data_counts.values, color='b')

# Annotate the height of each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Set labels and title
ax.set_xlabel('Bus ID')
ax.set_ylabel('Number of Data Points')
ax.set_title('Number of Data Points from Each Bus')



# Create the corner note
corner_note = f'Total Data Points: {total_data_points}\nTotal Buses: {total_buses}'

# Annotate the corner note on the graph just above it
ax.annotate(corner_note, xy=(0.02, 0.98), xycoords='axes fraction', fontsize=10,
            ha='left', va='top', bbox=dict(boxstyle="round, pad=0.4", edgecolor="black", facecolor="white"))



# Step 3: Save the plot as an image inside static/images directory
plot_file_path = os.path.join('static', 'images', 'plot.png')
plt.savefig(plot_file_path)
plt.close()  

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
