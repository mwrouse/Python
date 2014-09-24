"""
    Program: 8_2class.py
    Author: Michael Rouse
    Date: 12/12/13
    Description: TV class for challenge8_2.py
"""

class Television(object):
    """ TV Class """
    def __init__(self, channel=3, volume=25):
        self.__channel = channel
        self.__volume = volume
 
    def __str__(self):
        """ Print channel and volume info """
        info = "\nTV Information: \n\tChannel: " + str(self.__channel) + """\n\tVolume: """ + str(self.__volume) + "\n"
        
        return info

    def change_channel(self, channel=3):
        """ Change to a specified channel """
        # Check to see if the channel is within a valid range
        if channel in range(0, 101):
            # Change to that channel
            self.__channel = channel
        else:
            # Inform user of invalid channel
            print("Channel number is not within valid range. Try again.")

    def change_volume(self, modifier=1):

        # If self.__volume + modifier goes over 100 then set modifier to the amount needed to get to 100
        if (self.__volume + modifier) > 100:
            modifier = 100 - self.__volume

        # If self.__volume + modifier goes below 0 then set modifier to the amount needed to get to 0
        if (self.__volume + modifier) < 0:
            modifier = 0 - self.__volume

        # Double check to make sure the volume won't go over 100 or below 0
        if (self.__volume + modifier) in range(0, 101):
                if modifier < 0:
                    print("Decreasing volume by " + str(modifier * -1) + "...")

                elif modifier > 0:
                    print("Increasing volume by " + str(modifier) + "...")

                # Apply modifier to the volume
                self.__volume += modifier
            
        
