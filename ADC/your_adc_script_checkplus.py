import rotate_me
import final_5_3_function

# Read the current orientation from the "current_state.txt" file
current_orientation = rotate_me.read_orientation_from_file("current_state.txt")

# Define the target orientation
target_orientation = (20,10,150)

# Calculate the correction needed to get from the current orientation to the 
# target orientation by calling the calculate_rotation() function
corrections = final_5_3_function.calculate_rotation(current_orientation, target_orientation)
print("The rotation corrections are:", corrections)

# Call the rotate_me.main() function with the calculated corrections
rotate_me.main(corrections)


