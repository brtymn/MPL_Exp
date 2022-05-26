import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Plotter function for convenience.
def Plot1():
    # Read the CSV file that contains the data and import it to Python as a Pandas Dataframe.
    df = pd.read_csv("PE_data.csv")

    #print(df.to_string())

    # Pass the head strings for easier plotting.
    x_data_head = ["Voltage, 365 nm", "Voltage, 405 nm", "Voltage, 436 nm", "Voltage, 546 nm", "Voltage, 577 nm"]
    y_data_head = ["Current, 365 nm", "Current, 405 nm", "Current, 436 nm", "Current, 546 nm", "Current, 577 nm"]
    # Pass the wavelength strings for easier plotting.
    wavelength = ["365 nm", "405 nm", "436 nm", "546 nm", "577 nm"]
    # Loop over all data series.
    for i in range(len(x_data_head)):
        # Plot the data on top of each other.
        x = df[x_data_head[i]]
        y =  df[y_data_head[i]]
        plt.scatter(x, y,s=50, label=wavelength[i])
        fit = np.poly1d(np.polyfit(x, y, 6))
        plt.plot(x, fit(x))
    # Initialize the legends.
    plt.legend()
    # Initialize the labels.
    plt.xlabel("Voltage, V")
    plt.ylabel("Current, A")
    # Initialize the title.
    plt.title("Voltage vs Photocurrent Measurement Results")
    plt.axhline(0, color = "black")
    plt.axvline(0, color = "black")
    plt.show()


def Plot2():
    x_arr = [365, 405, 436, 546, 577]
    y_arr = [-1.944, -1.55, -1.331, -0.784, -0.683]

    plt.scatter(x_arr, y_arr, c="Red", label="Data")
    fit = np.polyfit(x_arr, y_arr, 1)
    poly = np.poly1d(fit)
    print(poly)
    plt.plot(x_arr, poly(x_arr), label="Linear Fit")
    plt.errorbar(x_arr, y_arr, 0.1, fmt = 'o',color = 'orange',
            ecolor = 'lightgreen', elinewidth = 5, capsize=10, label="Error")
    plt.xlabel("Wavelength, nm")
    plt.ylabel("Stopping Voltage, V")
    plt.title("Wavelength vs Stopping Voltage Measurement Results")
    plt.legend()
    plt.show()

# Run the plotters.
Plot1()
Plot2()
