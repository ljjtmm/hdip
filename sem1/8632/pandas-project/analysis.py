#Import packages
import pandas as pd
import os

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



def main():
    #Find the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    #Find the directory containing the dataset
    data_path = os.path.join(script_dir, 'data', 'iris_dataset.csv')

    #Read the data into a DatFrame
    data = pd.read_csv(data_path)

    #Write the summary of the variables in the dataset to a file name of our choosing.
    summarise_variables(data, 'variables_summary.txt')

if __name__ == '__main__':
    main()