# Movement of drone in square trajectory 

import time

# Create flyt_python navigation class instance
from flyt_python import api
drone = api.navigation(timeout=120000)  

# at least 3sec sleep time for the drone interface to initialize properly

time.sleep(3)

# Take Off Sequence
print 'taking off'
drone.take_off(5.0)

# Holding a position
drone.position_hold()

# Path Travel Sequence 
print ' going along the global setpoints'
drone.position_set_global(23.19578, 79.90200, 5)
drone.position_set_global(23.19578, 79.90207, 5)
drone.position_set_global(23.19572, 79.90207, 5)
drone.position_set_global(23.19572, 79.90200, 5)

# Landing Sequence
print 'Landing'
drone.land(async=False)

# Shutdown Sequence
drone.disconnect()

