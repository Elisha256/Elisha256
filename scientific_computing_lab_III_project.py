# MASENO UNIVERSITY; DEPARTMENT OF PHYSICS ANND MATERIAL SCIENCE
# BACHELOR'S IN SCIENCE(PHYSICS)
# ADMISSION NUMBER : SC/00014/018
# NAME: KIDENGE ELISHA ODHIAMBO
# LECTURER: DR. HENRY OTUNGA
# UNIT: SPH 331 : SCIENTIFIC COMPUTING LAB III


# ATICKER_TIMER PROJECT 1 : A PYTHON PROGRAM ON THE TICKER_TIMER_EXPERIMENT

alien_O = {'x_position': 0, 'y_position': 25 , 'speed': 'medium'}
print("Original x_position: " + str(alien_O['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_O['speed'] == 'slow':
   x_increment = 1
elif alien_O['speed'] == 'medium':
   x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus increnment.
alien_O['x_position'] = alien_O['x_position'] + x_increment

print("New x_position: " + str(alien_O['x_position']))
