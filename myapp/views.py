from django.shortcuts import render
import os
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

# def register(request):
#     return render(request, 'myapp/register.html')

def register(request):
    # Path to the image inside static/images directory
    plot_file_path = os.path.join('images', 'plot.png')
    return render(request, 'myapp/register.html', {'plot_file_path': plot_file_path})



def dashboard(request):
    return render(request, 'myapp/dashboard.html')

def mylogin(request):
    return render(request, 'myapp/mylogin.html')

def profilemanagement(request):
    return render(request, 'myapp/profilemanagement.html')


def plot_view(request):
    # Path to the image inside static/images directory
    plot_file_path = os.path.join('images', 'plot.png')
    return render(request, 'myapp/plot.html', {'plot_file_path': plot_file_path})



# def plot_chart(request, bus_id):
#     # Step 1: Load Data
#     data = pd.read_csv("data/CAN_DATA.csv")

#     # Step 2: Convert 'can_time' to datetime
#     data['can_time'] = pd.to_datetime(data['can_time'], format='%d/%m/%Y %H:%M:%S')

#     # Step 3: Group by Bus ID and count data points
#     bus_data_counts = data[data['can_param'] == 'Battery SOC']['vehicleid'].value_counts()


#     bus_id = request.GET.get('bus_id_input', bus_id)

#     # Calculate total number of data points and buses
#     total_data_points = bus_data_counts.sum()
#     total_buses = len(bus_data_counts)

#     # Create the bar chart
#     fig, ax = plt.subplots(figsize=(10, 6))
#     bars = ax.bar(bus_data_counts.index, bus_data_counts.values, color='b')


#     # Pass the bus_id to the template for display
#     context = {
#         'bus_id': bus_id,
#         # ... other context data for the template ...
#     }

#     # Annotate the height of each bar
#     for bar in bars:
#         height = bar.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(bar.get_x() + bar.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')

#     # Set labels and title
#     ax.set_xlabel('Bus ID')
#     ax.set_ylabel('Number of Data Points')
#     ax.set_title('Number of Data Points from Each Bus')

#     # Create the corner note
#     corner_note = f'Total Data Points: {total_data_points}\nTotal Buses: {total_buses}'

#     # Annotate the corner note on the graph just above it
#     ax.annotate(corner_note, xy=(0.02, 0.98), xycoords='axes fraction', fontsize=10,
#                 ha='left', va='top', bbox=dict(boxstyle="round, pad=0.4", edgecolor="black", facecolor="white"))

#     # Save the plot to a file (optional)
#     plt.savefig(os.path.join(os.getcwd(), 'static', 'graph.png'))
#     plot_filename = os.path.join(settings.MEDIA_ROOT, 'plot.png')
#     plt.savefig(plot_filename)

#     # Show the plot
#     plt.close(fig)  # Close the plot to free up resources

#     #-----------------------------
#     with open(plot_filename, 'rb') as plot_file:
#         response = HttpResponse(plot_file.read(), content_type='image/png')
#         response['Content-Disposition'] = 'inline; filename=plot.png'
#         return response

#     #-------------------------------


#     return HttpResponse("Plot generated successfully!")
#     return render(request, 'chart.html')
#     return render(request, 'plotchart.html', context)   


#------------------------------------------#------------------------------------------
#------------------------------------------#------------------------------------------

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.conf import settings

# def plot_chart(request):
#     bus_id = request.GET.get('bus_id_input', None)

#     if bus_id is not None and bus_id != '':
#         # Path to the 'CAN_DATA.csv' file inside the 'data' folder
#         data_file_path = os.path.join(settings.BASE_DIR, 'data', 'CAN_DATA.csv')

#         # Step 1: Load Data
#         data = pd.read_csv(data_file_path)

#         # Filter data based on the provided bus_id and can_param
#         filtered_data = data[(data['vehicleid'] == int(bus_id)) & (data['can_param'] == 'Battery SOC')]

#         # Log the filtered_data
#         print(filtered_data)  # This will print the filtered data to the console for debugging purposes

#         # Check if filtered_data is not empty
#         if not filtered_data.empty:
#             # Your code to generate the plot using Matplotlib
#             fig, ax = plt.subplots(figsize=(10, 6))
#             ax.plot(filtered_data['can_time'], filtered_data['can_value'])  # Modify column names based on your CSV structure

#             # Save the plot to a file
#             plot_filename = os.path.join(settings.MEDIA_ROOT, 'plot.png')
#             plt.savefig(plot_filename)
#             plt.close()  # Close the plot to free up resources

#             plot_file_path = os.path.join(settings.MEDIA_URL, 'plot.png')
#         else:
#             # Handle the case where filtered_data is empty
#             plot_file_path = None
#     else:
#         plot_file_path = None

#     # Pass the plot_file_path to the template
#     context = {
#         'plot_file_path': plot_file_path
#     }

#     return render(request, 'myapp/plotchart.html', context)


#------------------------------------------#------------------------------------------
#------------------------------------------#------------------------------------------

import os
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.conf import settings

def plot_chart(request):
    bus_id = request.GET.get('bus_id_input', None)

    if bus_id is not None and bus_id != '':
        # Path to the 'CAN_DATA.csv' file inside the 'data' folder
        data_file_path = os.path.join(settings.BASE_DIR, 'data', 'CAN_DATA.csv')

        # Step 1: Load Data
        data = pd.read_csv(data_file_path)

        # Filter data based on the provided bus_id and can_param
        filtered_data = data[(data['vehicleid'] == int(bus_id)) & (data['can_param'] == 'Battery SOC')]

        # Check if filtered_data is not empty
        if not filtered_data.empty:
            # Your code to generate the plot using Matplotlib
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(filtered_data['can_time'], filtered_data['can_val'])  # Modify column names based on your CSV structure

            # Save the plot to a file
            plot_filename = os.path.join(settings.MEDIA_ROOT, 'plot.png')
            plt.savefig(plot_filename)
            plt.close()  # Close the plot to free up resources

            plot_file_path = os.path.join(settings.MEDIA_URL, 'plot.png')
        else:
            # Handle the case where filtered_data is empty
            plot_file_path = None
    else:
        plot_file_path = None

    # Pass the plot_file_path to the template
    context = {
        'plot_file_path': plot_file_path
    }

    return render(request, 'myapp/plotchart.html', context)


#---------------------------------------------------------------


# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from django.shortcuts import render
# from django.conf import settings

# def plot_chart(request, bus_id=None):
#     if bus_id:
#         data_file_path = os.path.join(settings.BASE_DIR, 'data', 'CAN_DATA.csv')
#         data = pd.read_csv(data_file_path)
#         filtered_data = data[(data['vehicleid'] == int(bus_id)) & (data['can_param'] == 'Battery SOC')]

#         if not filtered_data.empty:
#             fig, ax = plt.subplots(figsize=(10, 6))
#             ax.plot(filtered_data['can_time'], filtered_data['can_val'])
#             plot_filename = os.path.join(settings.MEDIA_ROOT, 'plot.png')
#             plt.savefig(plot_filename)
#             plt.close()

#             plot_file_path = os.path.join(settings.MEDIA_URL, 'plot.png')
#         else:
#             plot_file_path = None
#     else:
#         plot_file_path = None

#     context = {
#         'plot_file_path': plot_file_path
#     }

#     return render(request, 'myapp/plotchart.html', context)
