def get_parking_spots_in_column(n_spots, first_parking_spot, height_of_spot, traffic_islands_spot, 
                                break_spots, traffic_island_height, break_height):

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


def get_all_parking_spots():
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



    return all_spots