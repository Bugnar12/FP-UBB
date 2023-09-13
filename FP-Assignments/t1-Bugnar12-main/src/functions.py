def create_flight(code, duration, departure, destination):
    return [code, duration, departure, destination]

def get_code(flight):
    return flight[0]

def get_duration(flight):
    return flight[1]

def get_departure(flight):
    return flight[2]

def get_destination(flight):
    return flight[3]

def set_code(flight, new_code):
    flight[0] = new_code

def set_duration(flight, new_duration):
    flight[1] = new_duration

def set_departure(flight, new_departure):
    flight[2] = new_departure

def set_destination(flight, new_destination):
    flight[3] = new_destination

def add_flight(flight_list, new_code1, new_duration1, new_departure1, new_destination1):
    try:
            new_flight = create_flight()
            new_code = set_code(new_flight, new_code1)
            new_duration = set_duration(new_flight, new_duration1)
            new_departure = set_departure(new_flight, new_departure1)
            new_destination = set_destination(new_flight, new_destination1)
            new_flight = create_flight(new_code, new_duration, new_departure, new_destination)
            flight_list.append(new_flight)
            return flight_list
    except ValueError as ve:
        print("invalid input", ve)


def delete_flight(flight_list, code_given):
    try:
        for flight in flight_list:
            if(get_code(flight) != code_given):
                raise ValueError("Code is not in the list")
            else:
                del flight_list[flight]
                break
    except ValueError as ve:
        print("Invalid input", ve)


def show_departure(flight_list, given_departure):
    try:
        new_flights = []
        for flight in flight_list:
            if get_departure(flight) == given_departure:
                new_flights.append(flight)
    except ValueError as ve:
        print("Invalid input", ve)


def sort_list(flight_list):

    for flight in flight_list:
        for i in range(0, len(flight_list) - 2):
            for j in range(i + 1, len(flight_list) - 1):
                if flight[i] > flight[j]:
                    flight[i], flight[j] = flight[j], flight[i]


def sort_destination(flight_list, given_destination):
    for flight in flight_list:
        if get_destination(flight) == given_destination:
            sort_list(flight_list)


def test_flight():
    flight = create_flight()

    assert get_code(flight) == "AOS231"
    assert get_duration(flight) == 45
    assert get_departure(flight) == "Cluj"
    assert get_destination(flight) == "Brasov"

    create_flight("AOS231", 45, "Cluj", "Brasov")






