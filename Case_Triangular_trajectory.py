# Movement of a drone in triangular trajectory

import time

# Create flyt_python navigation class instance
from flyt_python import api
drone = api.navigation(timeout=120000) 

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

# Take off Sequence
print 'taking off'
drone.take_off(10.0)

# Hold Position
print 'holding position'
drone.position_hold() 

print 'Setting zero velocity along all direction '
drone.velocity_set(0, 0, 0, relative=False)

# Path Travel Sequence
print ' going along the global setpoints'
drone.position_set_global(23.19581, 79.90200, 10)
drone.position_set_global(23.19576, 79.90209, 10)
drone.position_set_global(23.19572, 79.90200, 10)


# Landing Sequence
print 'Landing'
drone.land(async=True)

# Shutdown Sequence
drone.disconnect()
