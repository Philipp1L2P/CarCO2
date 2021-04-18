from Reader import reader
import pandas as pd
import os


typ = "scenic"  # possible types: "2er", "3er", "4er", "twingo", "clio", "scenic", "a4", "a5", "a6"
roof = "Cabrio"  # "Cabrio" or "Roof"
seat = "Leather"  # "Leather" or "Cloth"
motor = "E-Motor"  # "E-Motor", "V-Motor", "H-Motor"
paint = "Base"  # "Metallic" or "Base"


# Initialize an instance of the object Reader
myreader = reader.Reader(typ, roof, seat, motor)

# value list stores all variables
value_list = myreader.calculate_all_values()

audi_production_roof = value_list[0]
audi_production_seat = value_list[1]
audi_production_motor = value_list[2]
audi_production_coating = value_list[3]
audi_production_sum = value_list[4]

audi_usage_roof = value_list[5]
audi_usage_seat = value_list[6]
audi_usage_motor = value_list[7]
audi_usage_coating = value_list[8]
audi_usage_sum = value_list[9]

audi_recycling_roof = value_list[10]
audi_recycling_seat = value_list[11]
audi_recycling_motor = value_list[12]
audi_recycling_coating = value_list[13]
audi_recycling_sum = value_list[14]

bmw_production_roof = value_list[15]
bmw_production_seat = value_list[16]
bmw_production_motor = value_list[17]
bmw_production_coating = value_list[18]
bmw_production_sum = value_list[19]

bmw_usage_roof = value_list[20]
bmw_usage_seat = value_list[21]
bmw_usage_motor = value_list[22]
bmw_usage_coating = value_list[23]
bmw_usage_sum = value_list[24]

bmw_recycling_roof = value_list[25]
bmw_recycling_seat = value_list[26]
bmw_recycling_motor = value_list[27]
bmw_recycling_coating = value_list[28]
bmw_recycling_sum = value_list[29]

renault_production_roof = value_list[30]
renault_production_seat = value_list[31]
renault_production_motor = value_list[32]
renault_production_coating = value_list[33]
renault_production_sum = value_list[34]

renault_usage_roof = value_list[35]
renault_usage_seat = value_list[36]
renault_usage_motor = value_list[37]
renault_usage_coating = value_list[38]
renault_usage_sum = value_list[39]

renault_recycling_roof = value_list[40]
renault_recycling_seat = value_list[41]
renault_recycling_motor = value_list[42]
renault_recycling_coating = value_list[43]
renault_recycling_sum = value_list[44]

