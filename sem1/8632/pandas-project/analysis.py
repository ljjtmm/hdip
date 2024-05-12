#Import packages
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

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
        images_dir = os.path.join(script_dir, "images/histograms") 

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
        
        print("Histograms have been successfully generated, and writen to a folder within the images directory.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def generate_scatter_plots(dataset):
    """
    Generate scatter plots of each pair of variables.
    """

    try:
        # Get the directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__)) 

        # Create a subdirectory named "scatter_plots" 
        scatter_plots_dir = os.path.join(script_dir, "images/scatter_plots") 

        if not os.path.exists(scatter_plots_dir):
            os.makedirs(scatter_plots_dir)

        columns = dataset.columns[:-1]  # Exclude the target variable
        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):
                plt.figure()
                plt.scatter(dataset[columns[i]], dataset[columns[j]], c=dataset['target'], cmap='viridis')
                plt.xlabel(columns[i])
                plt.ylabel(columns[j])
                plt.title(f'Scatter plot of {columns[i]} vs {columns[j]}')
                plt.colorbar(label='Target')
                plt.savefig(os.path.join(scatter_plots_dir, f'{columns[i]}_{columns[j]}_scatter.png'))
                plt.close()
        
        print("Scatter plots have been successfully generated, and writen to a folder within the images directory.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def correlation_analysis(dataset):
    """
    Perform correlation analysis on the numeric columns of the dataset.
    """
    try:
        # Select only numeric columns
        numeric_columns = dataset.select_dtypes(include=['number'])

        # Calculate the correlation matrix
        correlation_matrix = numeric_columns.corr()

        # Visualize the correlation matrix as a heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Correlation Matrix')
        plt.show()
        
        print("Correlation analysis completed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    #Find the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    #Find the directory containing the dataset
    data_path = os.path.join(script_dir, 'data', 'iris_dataset.csv')

    #Read the data into a DatFrame
    data = pd.read_csv(data_path)

    #Solve for Task 1: Write the summary of the variables in the dataset to a file name of our choosing.
    summarise_variables(data, 'variables_summary.txt')

    #Solve for Task 2: Generate histograms
    generate_histograms(data)

    #Solve for Task 3: Generate scatter plots
    generate_scatter_plots(data)

    #Solve for Task 4 (Other analysis): Correlation analysis
    correlation_analysis(data)
    
if __name__ == '__main__':
    main()