#Import packages
import pandas as pd
import os
import matplotlib.pyplot as plt

def summarise_variables(data, output_file_name):
    """
    Summarise each variable in the dataset, and write to an output file.
    """

    try:
        # Write the output of the .describe() function for the DataFrame to the output file.
        with open(output_file_name, 'w') as f:
            f.write(round(data.describe(), 2).to_string())

        print(f"Summary file {output_file_name} successfully generated in script directory.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def generate_histograms(dataset):
    """
    Generate histograms of each variable and save them as PNG files in a directory within the script's directory.
    """

    try:
        # Get the directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__)) 

        # Create a subdirectory named "images" 
        images_dir = os.path.join(script_dir, "images") 

        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        # Generate the histograms, and exclude the target variable
        for column in dataset.columns[:-1]:  
            plt.figure()
            dataset[column].plot(kind='hist', bins=20, title=f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.savefig(os.path.join(images_dir, f'{column}_histogram.png'))
            plt.close()
        
        print("Histograms have been successfully generated, and writen to images directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")




def main():
    #Find the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    #Find the directory containing the dataset
    data_path = os.path.join(script_dir, 'data', 'iris_dataset.csv')

    #Read the data into a DatFrame
    data = pd.read_csv(data_path)

    #Write the summary of the variables in the dataset to a file name of our choosing.
    summarise_variables(data, 'variables_summary.txt')

    #Generate histograms
    generate_histograms(data)
    
if __name__ == '__main__':
    main()