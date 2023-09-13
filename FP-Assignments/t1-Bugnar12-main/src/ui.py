import functions

def adding(flight_list):
    code = input("code:")
    duration = int(input("duration:"))
    departure =input("departure:")
    destination = input("destination:")
    functions.add_flight(flight_list, code, duration, departure, destination)
    print(flight_list)

def delete(flight_list):
    code_input = input("Code to be deleted :")
    functions.delete_flight(flight_list, code_input)
    print(flight_list)

def show(flight_list):
    departure = input("This is the departure")
    functions.show_departure(flight_list, departure)

def start():
    flight_list = [
        {"code" : "0B3002", "duration" : "45", "departure" : "Cluj", "destination" : "London"},
        {"code": "0B1598", "duration": "100", "departure": "Bucuresti", "destination": "Cluj"},
        {"code": "123HO9", "duration": "150", "departure": "Cluj", "destination": "Madrid"},
        {"code": "A12BC2", "duration": "30", "departure": "Budapest", "destination": "Berlin"},
        {"code": "333KS2", "duration": "240", "departure": "Moskov", "destination": "Lisbon"}

    ]
    print("Menu:\n")
    print("1.Add a flight\n")
    print("2.Delete a flight\n")
    print("3.Show and sort\n")
    print("4.Modify time\n")
    print("The initial flight list is : \n")
    print(flight_list)


    while True:
        try:
            option = int(input(">"))
            if option == 1:
                print(adding(flight_list))
            elif option == 2:
                delete(flight_list)
            elif option == 3:
                pass
            elif option == 4:
                pass
            else:
                print("The value is not checkable")
        except ValueError as ve:
            print("Invalid input", ve)


start()


