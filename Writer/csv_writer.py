import pandas as pd
import numpy as np
import os

brands = ['bmw', 'audi','renault', 'mercedes']
LCA = ['Produktion', 'Recycling', 'Betrieb']
bmw_names = ['2er', '3er', '4er']
audi_names = ['a4', 'a5', 'a6']
renault_names = ['twingo', 'clio', 'scenic'] # There must be the same amount of elements in each names list


def save_csv_files():
    # get the current path of the python_file (csv_writer.py)
    current_path = os.getcwd()

    # get the parent directory
    parent_directory = os.path.dirname(current_path)

    # Set the name of the csv-files-directory
    csv_directory = "csv-files/"

    # Merge the paths
    complete_csv_path = os.path.join(parent_directory, csv_directory)

    # Return the path of the csv directory
    return complete_csv_path


if __name__ == "__main__":

    for item in brands:
        for element in LCA:
            if item == 'bmw': #item == 'bmw':
                index_list=bmw_names
            elif item == 'audi':
                index_list = audi_names
            elif item == 'renault':
                index_list = renault_names
            else:
                print("car name not defined")
                break

            title = ['Dach', 'Cabrio', 'Leder', 'Stoff', 'Motor E', 'Motor H', 'Motor V', 'Metallic',
                     'Base']

            my_numpy_array = np.random.rand(len(index_list), len(title))
            my_numpy_array = np.around(my_numpy_array, decimals=2)

            df = pd.DataFrame(my_numpy_array , columns=title, index=index_list)  # naming title as column

            # Save the csv files in the csv-files
            save_csv_path = os.path.join(save_csv_files(), f"{item}_{element}.csv")
            df.to_csv(save_csv_path)
