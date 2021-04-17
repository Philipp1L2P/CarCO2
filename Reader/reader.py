import pandas as pd
import os



class Reader():
    def __init__(self, csv_file_location, typ, roof, seat, motor):
        self.csv_file_location = csv_file_location
        self.typ = typ
        self.roof = roof
        self.seat = seat
        self.motor = motor

    # From a given file name extract the csv data
    def get_data(self):
        current_path = os.getcwd()

        csv_filepath = os.path.join(current_path, self.csv_file_location)
        # print(csv_filepath)
        csv_data = pd.read_csv(csv_filepath,
                               sep=",")
        return csv_data


    # Returns csv_values for a given configuration
    def return_csv_values(self, csv_data):
        reduced_csv_data = pd.DataFrame(csv_data).to_numpy()
        print(reduced_csv_data)

        csv_values = []
        if self.typ == "2er":
            for item in reduced_csv_data[0]:
                    #print("item: {}".format(item))
                    csv_values.append(item)
        return csv_values


    # Get the specific roof co2 value:
    def get_roof_co2(self, csv_values):
        if self.roof == "Roof":
            roof_co2 = csv_values[1]
        else:
            roof_co2 = csv_values[2]
        return roof_co2

    # Get the specific seat co2 value:
    def get_seat_co2(self, csv_values):
        if self.seat == "Leather":
            seat_co2 = csv_values[3]
        else:
            seat_co2 = csv_values[4]
        return seat_co2

    # Get the specific motor co2 value:
    def get_motor_co2(self, csv_values):
        if self.motor == "E-Motor":
            motor_co2 = csv_values[5]
        elif self.motor == "H-Motor":
            motor_co2 = csv_values[6]
        else:
            motor_co2 = csv_values[7]
        return motor_co2

    # Calculate the sum for the whole production
    def get_sum(self, roof_co2, seat_co2, motor_co2):
        sum = roof_co2 + seat_co2 + motor_co2
        print("sum {}".format(sum))
        return sum

if __name__ == '__main__':
    csv_file_location = "Test_production.csv"
    Reader = Reader("2er", "Cabrio", "Leather", "E-Motor")
    csv_data = Reader.get_data(csv_file_location)
    csv_values = Reader.return_csv_values(csv_data)
    roof_co2 = Reader.get_roof_co2(csv_values)
#    print("roof.co2: {}".format(roof_co2))
    seat_co2 = Reader.get_seat_co2(csv_values)
    motor_co2 = Reader.get_motor_co2(csv_values)
    sum = Reader.get_sum(roof_co2, seat_co2, motor_co2)

