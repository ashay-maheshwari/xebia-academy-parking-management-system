from datetime import date
today = date.today()
# dd/mm/YY
date_today = today.strftime("%d/%m/%Y")

def bike_parking(bike_no, rate, latest_parking_slots):
    """
    :param bike_no: Registration number of the bike
    :param rate: rate of parking in INR
    :param latest_parking_slots: fetch the latest parking spots available in the database
    :return: JSON response with bike_no, date, parking time, parking slot address
    """

    # Dictionary to be provided with response
    parking_response_dict = {
        "Vehicle Registration No" : bike_no,
        "Parking Rate" : rate,
        "Date" : date_today
    }

    levels = list(latest_parking_slots.keys())
    parking_found = 0

    # Remove _id key from the list
    levels.remove("_id")

    for level in levels:

        # Look for a spot in Motorcycle section first
        motorcycle_spots = list(latest_parking_slots[level]["MotorcycleSpots"].keys())
        for row in motorcycle_spots:

            if len(latest_parking_slots[level]["MotorcycleSpots"][row]) == 0:
                print("No parking found")
            else:
                parking_found = 1
                print(latest_parking_slots[level]["MotorcycleSpots"][row])

                parking_response_dict["Level"] = level
                parking_response_dict["Slot Category"] = "Motorcycle Slot"
                parking_response_dict["Row"] = row
                parking_response_dict["Spot"] = ""

                return parking_response_dict

        # Look for a parking in compact spot
        compact_spots = list(latest_parking_slots[level]["CompactSpots"].keys())
        for row in compact_spots:
            if len(latest_parking_slots[level]["CompactSpots"][row]) == 0:
                print("No parking found")
            else:
                parking_found = 1
                parking_response_dict["Level"] = level
                parking_response_dict["Slot Category"] = "Compact Slot"
                parking_response_dict["Row"] = row
                parking_response_dict["Spot"] = ""

                return parking_response_dict

        # Look for a parking in large spot
        large_spots = list(latest_parking_slots[level]["LargeSpots"].keys())
        for row in large_spots:
            if len(latest_parking_slots[level]["LargeSpots"][row]) == 0:
                print("No parking found")
            else:
                parking_found = 1
                parking_response_dict["Level"] = level
                parking_response_dict["Slot Category"] = "Large Slot"
                parking_response_dict["Row"] = row
                parking_response_dict["Spot"] = ""

                return parking_response_dict

