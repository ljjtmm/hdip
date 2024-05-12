import os
from sklearn.datasets import load_iris
import pandas as pd

def fetch_and_save_iris_dataset(output_dir="data"):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the Iris dataset
    iris = load_iris()

    # Convert the data to a pandas DataFrame
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    iris_df['target_names'] = iris.target_names[iris.target]

    # Write the dataset to a CSV file
    output_file = os.path.join(output_dir, "iris_dataset.csv")
    iris_df.to_csv(output_file, index=False)

    print("Iris dataset saved to:", output_file)

if __name__ == "__main__":
    fetch_and_save_iris_dataset()
