def get_parking_spots_in_column(n_spots: int, 
                                first_parking_spot: list, 
                                height_of_spot: int, 
                                traffic_islands_spot: list = [], 
                                break_spots: list = [], 
                                traffic_island_height: int = 30, 
                                break_height: int = 30) -> list:
    '''
    Function that returns the parking spots in a column
    Parameters:
    n_spots (int): The number of parking spots in the column
    first_parking_spot (list): The first parking spot in the column
    height_of_spot (int): The height of the parking spot
    traffic_islands_spot (list): The list of parking spots where the traffic islands are present
    break_spots (list): The list of parking spots where the break is present
    traffic_island_height (int): The height of the traffic island
    break_height (int): The height of the break

    Returns:
    list: The list of parking spots in the column

    '''


    parkings_spots = []
    curr_spot = first_parking_spot
    for i in range(n_spots):
        if i in traffic_islands_spot:
            curr_spot = [curr_spot[0], curr_spot[1] + traffic_island_height, curr_spot[2], curr_spot[3]]
        if i in break_spots:
            curr_spot = [curr_spot[0], curr_spot[1] + break_height, curr_spot[2], curr_spot[3]]

        parkings_spots.append(curr_spot)
        curr_spot = [curr_spot[0], curr_spot[1] + height_of_spot, curr_spot[2], curr_spot[3]]

    return parkings_spots


def get_all_parking_spots() -> list[list[int]]:
    '''
    Returns a list of all parking spots in the parking lot
    '''
    height = 32
    break_height = 34
    traffic_island_height = 35
    all_spots = []

    # First column
    first_column_parking_spot = [86, 391, 65, 28]
    first_column_rows = 19
    first_column_traffic_islands = [6]
    first_column_break_spots = [6]
    first_column = get_parking_spots_in_column(n_spots=first_column_rows, first_parking_spot=first_column_parking_spot, height_of_spot=height,
                                                  traffic_islands_spot=first_column_traffic_islands, break_spots=first_column_break_spots, 
                                                  traffic_island_height=32, break_height=break_height)
    all_spots.extend(first_column)

    # Second column
    second_column_parking_spot = [151, 135, 65, 28]
    second_column_rows = 27
    second_column_traffic_islands = [14]
    second_column_break_spots = [14]
    second_column = get_parking_spots_in_column(n_spots=second_column_rows, first_parking_spot=second_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=second_column_traffic_islands, break_spots=second_column_break_spots,
                                                    traffic_island_height=traffic_island_height, break_height=break_height)
    all_spots.extend(second_column)

    # Third column
    third_column_parking_spot = [320, 135, 65, 28]
    third_column_rows = 28
    third_column_traffic_islands = [15]
    third_column_break_spots = []
    third_column = get_parking_spots_in_column(n_spots=third_column_rows, first_parking_spot=third_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=third_column_traffic_islands, break_spots=third_column_break_spots,
                                                    traffic_island_height=traffic_island_height, break_height=break_height)
    all_spots.extend(third_column)

    # Fourth column
    fourth_column_parking_spot = [385, 135, 65, 28]
    fourth_column_rows = 28
    fourth_column_traffic_islands = [15]
    fourth_column_break_spots = []
    fourth_column = get_parking_spots_in_column(n_spots=fourth_column_rows, first_parking_spot=fourth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=fourth_column_traffic_islands, break_spots=fourth_column_break_spots,
                                                    traffic_island_height=traffic_island_height, break_height=break_height)
    
    all_spots.extend(fourth_column)

    #Fifth column
    fifth_column_parking_spot = [550, 260, 65, 28]
    fifth_column_rows = 23
    fifth_column_traffic_islands = [10]
    fifth_column_break_spots = [4]
    fifth_column = get_parking_spots_in_column(n_spots=fifth_column_rows, first_parking_spot=fifth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=fifth_column_traffic_islands, break_spots=fifth_column_break_spots,
                                                    traffic_island_height=30, break_height=break_height)
    all_spots.extend(fifth_column)

    # Sixth column
    sixth_column_parking_spot = [615, 260, 65, 28]
    sixth_column_rows = 23
    sixth_column_traffic_islands = [10]
    sixth_column_break_spots = [4]
    sixth_column = get_parking_spots_in_column(n_spots=sixth_column_rows, first_parking_spot=sixth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=sixth_column_traffic_islands, break_spots=sixth_column_break_spots,
                                                    traffic_island_height=30, break_height=break_height)
    all_spots.extend(sixth_column)

    # Seventh column
    seventh_column_parking_spot = [780, 164, 65, 28]
    seventh_column_rows = 27
    seventh_column_traffic_islands = [14]
    seventh_column_break_spots = []
    seventh_column = get_parking_spots_in_column(n_spots=seventh_column_rows, first_parking_spot=seventh_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=seventh_column_traffic_islands, break_spots=seventh_column_break_spots,
                                                    traffic_island_height=29, break_height=break_height)
    all_spots.extend(seventh_column)

    # Eighth column
    eighth_column_parking_spot = [845, 164, 65, 28]
    eighth_column_rows = 25
    eighth_column_traffic_islands = [14]
    eighth_column_break_spots = []
    eighth_column = get_parking_spots_in_column(n_spots=eighth_column_rows, first_parking_spot=eighth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=eighth_column_traffic_islands, break_spots=eighth_column_break_spots,
                                                    traffic_island_height=28, break_height=break_height)
    all_spots.extend(eighth_column)

    # Ninth column
    ninth_column_parking_spot = [990, 215, 65, 28]
    ninth_column_rows = 21
    ninth_column_traffic_islands = [9]
    ninth_column_break_spots = [6]
    ninth_column = get_parking_spots_in_column(n_spots=ninth_column_rows, first_parking_spot=ninth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=ninth_column_traffic_islands, break_spots=ninth_column_break_spots,
                                                    traffic_island_height=28, break_height=28)
    all_spots.extend(ninth_column)

    # Tenth column
    tenth_column_parking_spot = [1065, 215, 65, 28]
    tenth_column_rows = 21
    tenth_column_traffic_islands = [9]
    tenth_column_break_spots = [6]
    tenth_column = get_parking_spots_in_column(n_spots=tenth_column_rows, first_parking_spot=tenth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=tenth_column_traffic_islands, break_spots=tenth_column_break_spots,
                                                    traffic_island_height=28, break_height=28)
    all_spots.extend(tenth_column)

    # Eleventh column
    eleventh_column_parking_spot = [1220, 150, 65, 28]
    eleventh_column_rows = 24
    eleventh_column_traffic_islands = [12]
    eleventh_column_break_spots = []
    eleventh_column = get_parking_spots_in_column(n_spots=eleventh_column_rows, first_parking_spot=eleventh_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=eleventh_column_traffic_islands, break_spots=eleventh_column_break_spots,
                                                    traffic_island_height=28, break_height=28)
    all_spots.extend(eleventh_column)

    # Twelfth column
    twelfth_column_parking_spot = [1293, 150, 65, 28]
    twelfth_column_rows = 24
    twelfth_column_traffic_islands = [12]
    twelfth_column_break_spots = []
    twelfth_column = get_parking_spots_in_column(n_spots=twelfth_column_rows, first_parking_spot=twelfth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=twelfth_column_traffic_islands, break_spots=twelfth_column_break_spots,
                                                    traffic_island_height=26, break_height=28)
    all_spots.extend(twelfth_column)

    # Thirteenth column
    thirteenth_column_parking_spot = [1450, 150, 65, 28]
    thirteenth_column_rows = 23
    thirteenth_column_traffic_islands = [11]
    thirteenth_column_break_spots = [8]
    thirteenth_column = get_parking_spots_in_column(n_spots=thirteenth_column_rows, first_parking_spot=thirteenth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=thirteenth_column_traffic_islands, break_spots=thirteenth_column_break_spots,
                                                    traffic_island_height=26, break_height=28)
    all_spots.extend(thirteenth_column)

    # Fourteenth column
    fourteenth_column_parking_spot = [1525, 150, 65, 28]
    fourteenth_column_rows = 23
    fourteenth_column_traffic_islands = [11]
    fourteenth_column_break_spots = [8]
    fourteenth_column = get_parking_spots_in_column(n_spots=fourteenth_column_rows, first_parking_spot=fourteenth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=fourteenth_column_traffic_islands, break_spots=fourteenth_column_break_spots,
                                                    traffic_island_height=26, break_height=28)
    all_spots.extend(fourteenth_column)

    # Fifteenth column
    fifteenth_column_parking_spot = [1675, 147, 65, 28]
    fifteenth_column_rows = 24
    fifteenth_column_traffic_islands = [12]
    fifteenth_column_break_spots = []
    fifteenth_column = get_parking_spots_in_column(n_spots=fifteenth_column_rows, first_parking_spot=fifteenth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=fifteenth_column_traffic_islands, break_spots=fifteenth_column_break_spots,
                                                    traffic_island_height=27, break_height=break_height)
    all_spots.extend(fifteenth_column)

    # Sixteenth column
    sixteenth_column_parking_spot = [1780, 180, 65, 28]
    sixteenth_column_rows = 23
    sixteenth_column_traffic_islands = [11]
    sixteenth_column_break_spots = []
    sixteenth_column = get_parking_spots_in_column(n_spots=sixteenth_column_rows, first_parking_spot=sixteenth_column_parking_spot, height_of_spot=height,
                                                    traffic_islands_spot=sixteenth_column_traffic_islands, break_spots=sixteenth_column_break_spots,
                                                    traffic_island_height=27, break_height=break_height)
    all_spots.extend(sixteenth_column)


    return all_spots


def get_parking_spots_for_cropped():
    height = 59
    spots = []

    # First column
    first_column_parking_spot = [50, 1, 150, 55]
    first_column_rows = 7
    first_column = get_parking_spots_in_column(n_spots=first_column_rows, first_parking_spot=first_column_parking_spot, height_of_spot=height)
    spots.extend(first_column)

    # Second column
    second_column_parking_spot = [200, 1, 150, 55]
    second_column_rows = 7
    second_column = get_parking_spots_in_column(n_spots=second_column_rows, first_parking_spot=second_column_parking_spot, height_of_spot=height)
    spots.extend(second_column)
    

    return spots
