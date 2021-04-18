import pandas as pd
import os



class Reader():
    def __init__(self, typ="2er", roof="Cabrio", seat="Cloth", motor="E-Motor", coating="Base"):
        self.typ = typ
        self.roof = roof
        self.seat = seat
        self.motor = motor
        self.coating = coating
        self.csv_directory = "csv-files/"

    def get_csv_list(self):
        # get the current path of the python_file (csv_writer.py)
        current_path = os.getcwd()

        # Merge the paths
        complete_csv_path = os.path.join(current_path, self.csv_directory)
        # Find all elements in the directory
        csv_file_list = os.listdir(complete_csv_path)
        return csv_file_list, self.csv_directory


    def get_csv_dir_path(self):
        # get the current path of the python_file (csv_writer.py)
        current_path = os.getcwd()

        # Merge the paths
        complete_csv_path = os.path.join(current_path, self.csv_directory)

        # Find all elements in the directory
        csv_file_list = os.listdir(complete_csv_path)

        # Return the path of the csv directory
        return complete_csv_path



    # From a given file name extract the csv data
    def get_data(self, csv_file_name):
        #print(f"csv_file_name: {csv_file_name}")

        # Get the path of the csv-files
        csv_dir_path = self.get_csv_dir_path()
        # print(f"csv_filepath: {csv_dir_path}")
        # Concatenate the path of the file_name and the directory
        csv_file_path = os.path.join(csv_dir_path, csv_file_name)
        # read the data
        #print(csv_file_path)
        csv_data = pd.read_csv(csv_file_path,
                               sep=",")
        return csv_data


    # Returns csv_values for a given configuration
    def return_csv_values(self, csv_data):
        reduced_csv_data = pd.DataFrame(csv_data).to_numpy()
        #print(reduced_csv_data)

        csv_values = []
        if self.typ == "2er" or self.typ == "twingo" or self.typ == "a4":
            for item in reduced_csv_data[0]:
                    csv_values.append(item)

        if self.typ == "3er" or self.typ == "clio" or self.typ == "a5":
            for item in reduced_csv_data[1]:
                    csv_values.append(item)

        if self.typ == "4er" or self.typ == "scenic" or self.typ == "a6":
            for item in reduced_csv_data[2]:
                    csv_values.append(item)
        return csv_values


    # Get the specific roof co2 value:
    def get_roof_co2(self, csv_values):
        if self.roof == "Roof":
            roof_co2 = csv_values[1]
        elif self.roof == "Cabrio":
            roof_co2 = csv_values[2]
        else:
            print("self.roof not found")
            return
        return roof_co2

    # Get the specific seat co2 value:
    def get_seat_co2(self, csv_values):
        if self.seat == "Leather":
            seat_co2 = csv_values[3]
        elif self.seat == "Cloth":
            seat_co2 = csv_values[4]
        else:
            print("self.seat not found")
            return
        return seat_co2

    # Get the specific motor co2 value:
    def get_motor_co2(self, csv_values):
        if self.motor == "E-Motor":
            motor_co2 = csv_values[5]
        elif self.motor == "H-Motor":
            motor_co2 = csv_values[6]
        elif self.motor == "V-Motor":
            motor_co2 = csv_values[7]
        else:
            print("self.motor not found")
            return
        return motor_co2

    # Get the specific coating co2 value:
    def get_coating_co2(self, csv_values):
        if self.coating == "Metallic":
            coating_co2 = csv_values[8]
        elif self.coating == "Base":
            coating_co2 = csv_values[9]
        else:
            print("self.coating not found")
            return
        return coating_co2

    # Calculate the sum for the whole production
    def get_sum(self, roof_co2, seat_co2, motor_co2, coating_co2):
        #print(coating_co2)
        sum = round(roof_co2 + seat_co2 + motor_co2 + coating_co2, 2)
        #print("sum {}".format(sum))
        return sum

    def calculate_csv_values(self, csv_file_name):
        csv_data = self.get_data(csv_file_name)
        csv_values = self.return_csv_values(csv_data)
        roof_co2 = self.get_roof_co2(csv_values)
        seat_co2 = self.get_seat_co2(csv_values)
        motor_co2 = self.get_motor_co2(csv_values)
        coating_co2 = self.get_coating_co2(csv_values)
        sum = self.get_sum(roof_co2, seat_co2, motor_co2, coating_co2)
        #print(f"roof_co2: {roof_co2}")
        return(roof_co2, seat_co2, motor_co2, coating_co2, sum)

    def calculate_all_values(self):
        csv_list, csv_directory = self.get_csv_list()
        mydict = {}
        my_value_list = []
        for csv_file_name in csv_list:
            (roof_co2, seat_co2, motor_co2, coating_co2, sum) = self.calculate_csv_values(csv_file_name)
            # print(f"roof_co2: {roof_co2}, seat_co2: {seat_co2}, motor_co2: {motor_co2}, sum:{sum}")
            splitted_file_name = csv_file_name.split(".")
            mydict[splitted_file_name[0]] = (roof_co2, seat_co2, motor_co2, coating_co2, sum)

        if "audi_Produktion" in mydict.keys():
            (audi_production_roof, audi_production_seat, audi_production_motor, audi_production_coating, audi_production_sum) = mydict.get(
                "audi_Produktion")
            my_value_list.append(audi_production_roof)
            my_value_list.append(audi_production_seat)
            my_value_list.append(audi_production_motor)
            my_value_list.append(audi_production_coating)
            my_value_list.append(audi_production_sum)
            # print(audi_production_roof, audi_production_seat, audi_production_motor, audi_production_sum)

        if "audi_Betrieb" in mydict.keys():
            (audi_usage_roof, audi_usage_seat, audi_usage_motor, audi_usage_coating, audi_usage_sum) = mydict.get("audi_Betrieb")
            my_value_list.append(audi_usage_roof)
            my_value_list.append(audi_usage_seat)
            my_value_list.append(audi_usage_motor)
            my_value_list.append(audi_usage_coating)
            my_value_list.append(audi_usage_sum)

        if "audi_Recycling" in mydict.keys():
            (audi_recycling_roof, audi_recycling_seat, audi_recycling_motor, audi_recycling_coating, audi_recycling_sum) = mydict.get(
                "audi_Recycling")
            my_value_list.append(audi_recycling_roof)
            my_value_list.append(audi_recycling_seat)
            my_value_list.append(audi_recycling_motor)
            my_value_list.append(audi_recycling_coating)
            my_value_list.append(audi_recycling_sum)
            #print(audi_recycling_roof, audi_recycling_seat, audi_recycling_motor, audi_recycling_sum)
        #########
        if "bmw_Produktion" in mydict.keys():
            (bmw_production_roof, bmw_production_seat, bmw_production_motor, bmw_production_coating, bmw_production_sum) = mydict.get(
                "bmw_Produktion")
            my_value_list.append(bmw_production_roof)
            my_value_list.append(bmw_production_seat)
            my_value_list.append(bmw_production_motor)
            my_value_list.append(bmw_production_coating)
            my_value_list.append(bmw_production_sum)
            #print(bmw_production_roof, bmw_production_seat, bmw_production_motor, bmw_production_sum)

        if "bmw_Betrieb" in mydict.keys():
            (bmw_usage_roof, bmw_usage_seat, bmw_usage_motor, bmw_usage_coating, bmw_usage_sum) = mydict.get("bmw_Betrieb")
            my_value_list.append(bmw_usage_roof)
            my_value_list.append(bmw_usage_seat)
            my_value_list.append(bmw_usage_motor)
            my_value_list.append(bmw_usage_coating)
            my_value_list.append(bmw_usage_sum)
            #print(bmw_usage_roof, bmw_usage_seat, bmw_usage_motor, bmw_usage_sum)

        if "bmw_Recycling" in mydict.keys():
            (bmw_recycling_roof, bmw_recycling_seat, bmw_recycling_motor, bmw_recycling_coating, bmw_recycling_sum) = mydict.get(
                "bmw_Recycling")
            my_value_list.append(bmw_recycling_roof)
            my_value_list.append(bmw_recycling_seat)
            my_value_list.append(bmw_recycling_motor)
            my_value_list.append(bmw_recycling_coating)
            my_value_list.append(bmw_recycling_sum)
           # print(bmw_recycling_roof, bmw_recycling_seat, bmw_recycling_motor, bmw_recycling_sum)

        #########
        if "renault_Produktion" in mydict.keys():
            (renault_production_roof, renault_production_seat, renault_production_motor, renault_production_coating,
             renault_production_sum) = mydict.get("renault_Produktion")
            my_value_list.append(renault_production_roof)
            my_value_list.append(renault_production_seat)
            my_value_list.append(renault_production_motor)
            my_value_list.append(renault_production_coating)
            my_value_list.append(renault_production_sum)
            #print(renault_production_roof, renault_production_seat, renault_production_motor, renault_production_sum)

        if "renault_Betrieb" in mydict.keys():
            (renault_usage_roof, renault_usage_seat, renault_usage_motor, renault_usage_coating, renault_usage_sum) = mydict.get(
                "renault_Betrieb")
            my_value_list.append(renault_usage_roof)
            my_value_list.append(renault_usage_seat)
            my_value_list.append(renault_usage_motor)
            my_value_list.append(renault_usage_coating)
            my_value_list.append(renault_usage_sum)
            #print(renault_usage_roof, renault_usage_seat, renault_usage_motor, renault_usage_sum)

        if "renault_Recycling" in mydict.keys():
            (renault_recycling_roof, renault_recycling_seat, renault_recycling_motor, renault_recycling_coating,
             renault_recycling_sum) = mydict.get("renault_Recycling")
            my_value_list.append(renault_recycling_roof)
            my_value_list.append(renault_recycling_seat)
            my_value_list.append(renault_recycling_motor)
            my_value_list.append(renault_recycling_coating)
            my_value_list.append(renault_recycling_sum)
            #print(renault_recycling_roof, renault_recycling_seat, renault_recycling_motor, renault_recycling_sum)

        return(my_value_list)

if __name__ == '__main__':
    Reader = Reader()

