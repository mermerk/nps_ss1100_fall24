def calculate_rotation(current_orientation, desired_orientation):
    """
    ChatGPT assisted with function creation
    """

    rotate_x = desired_orientation[0] - current_orientation[0]
    rotate_y = desired_orientation[1] - current_orientation[1]
    rotate_z = desired_orientation[2] - current_orientation[2]

    return(rotate_x, rotate_y, rotate_z)
