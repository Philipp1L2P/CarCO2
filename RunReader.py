from Reader import reader

csv_file_path = "csv-files/Test_production.csv"
typ = "2er"
roof = "Cabrio"
seat = "Leather"
motor = "E-Motor"

# Initialize an instance of the object Reader
myreader = reader.Reader(csv_file_path, typ, roof, seat, motor)
myreader = reader.Reader(csv_file_path, typ, roof, seat, motor)

# get the complete csv data
csv_data = myreader.get_data()

# Get the csv values
csv_values = myreader.return_csv_values(csv_data)

# get the specific CO2 values for roof, seat, motor
roof_co2 = myreader.get_roof_co2(csv_values)
seat_co2 = myreader.get_seat_co2(csv_values)
motor_co2 = myreader.get_motor_co2(csv_values)

# get the added CO2 values
sum = myreader.get_sum(roof_co2, seat_co2, motor_co2)
