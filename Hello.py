import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import pprint
import sqlite3

# Function to generate data
def generate_data():

    x1_start_date = datetime(2023, 1, 1)
    x4_end_date = datetime(2023, 1, 10)
    delta = timedelta(days=1)
    x1 = [x1_start_date + i * delta for i in range(10)]
    y1 = np.sin(np.linspace(0, 2 * np.pi, 10))

    x2 = np.linspace(0, 10, 100)
    y2 = np.cos(x2)

    x3 = np.linspace(0, 15, 150)
    y3 = np.sin(x3)

    x4_start_date = datetime(2023, 1, 1)
    x4_end_date = datetime(2023, 1, 20)
    x4_delta = timedelta(days=1)
    x4 = [x4_start_date + i * x4_delta for i in range(20)]
    y4 = np.cos(np.linspace(0, 2 * np.pi, 20))

    return x1, y1, x2, y2, x3, y3, x4, y4

# Function to create and display the plot
def plot_data(x1, y1, x2, y2, x3, y3, x4, y4):
    # Create a figure with four axes objects
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))  # 2x2 grid of subplots

    # Plot using the first axes ('ax1')
    ax1.plot(x1, y1, marker='o', linestyle='-', label='Sine Wave')
    ax1.set_xlabel('Timestamp (ax1)')
    ax1.set_ylabel('Y-axis label (ax1)')
    ax1.legend()

    # Rotate x-axis labels for ax1 by 45 degrees
    ax1.set_xticks(x1)  # Set the x-axis tick positions
    ax1.set_xticklabels([dt.strftime("%Y-%m-%d") for dt in x1], rotation=45)  # Set the x-axis tick labels

    # Plot using the second axes ('ax2')
    ax2.plot(x2, y2, label='Cosine Wave', color='red', linestyle='--')
    ax2.set_xlabel('X-axis label (ax2)')
    ax2.set_ylabel('Y-axis label (ax2)')
    ax2.legend()

    # Rotate x-axis labels for ax2 by 45 degrees
    ax2.set_xticks(ax2.get_xticks())  # Set the x-axis tick positions
    ax2.set_xticklabels([str(round(label, 2)) for label in ax2.get_xticks()], rotation=45)  # Set the x-axis tick labels

    # Plot using the third axes ('ax3')
    ax3.plot(x3, y3, label='Sine Wave')
    ax3.set_xlabel('X-axis label (ax3)')
    ax3.set_ylabel('Y-axis label (ax3)')
    ax3.legend()

    # Rotate x-axis labels for ax3 by 45 degrees
    ax3.set_xticks(ax3.get_xticks())  # Set the x-axis tick positions
    ax3.set_xticklabels([str(round(label, 2)) for label in ax3.get_xticks()], rotation=45)  # Set the x-axis tick labels

    # Plot using the fourth axes ('ax4')
    ax4.plot(x4, y4, label='Cosine Wave', color='green', linestyle='-.')
    ax4.set_xlabel('Timestamp (ax4)')
    ax4.set_ylabel('Y-axis label (ax4)')
    ax4.legend()

    # Rotate x-axis labels for ax4 by 45 degrees
    ax4.set_xticks(x4)  # Set the x-axis tick positions
    ax4.set_xticklabels([dt.strftime("%Y-%m-%d") for dt in x4], rotation=45)  # Set the x-axis tick labels

    # Adjust subplot layout to prevent overlap
    fig.tight_layout()

    # Display the figure using Streamlit
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title('Data Plotting')
    
    # Generate data
    x1, y1, x2, y2, x3, y3, x4, y4 = generate_data()

    print(x4, y4)
    a = list(zip(x4,y4))
    for i,v in enumerate(a):
        print(i,v)    

    # Plot the data
    plot_data(x1, y1, x2, y2, x3, y3, x4, y4)

if __name__ == "__main__":
    main()


    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
