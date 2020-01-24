class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        SortingRobot.set_light_on(self)
        SortingRobot.swap_item(self)

        while SortingRobot.light_is_on(self):
            SortingRobot.set_light_off(self)

            while SortingRobot.can_move_right(self):
                SortingRobot.move_right(self)

                if SortingRobot.compare_item(self) == -1:
                    SortingRobot.swap_item(self)
                    
                elif SortingRobot.compare_item(self) == 1:
                    SortingRobot.set_light_on(self)

            while SortingRobot.can_move_left(self):

                if SortingRobot.compare_item(self) == 1:
                    SortingRobot.swap_item(self)

                elif SortingRobot.compare_item(self)==-1:
                    SortingRobot.set_light_on(self)

                SortingRobot.move_left(self)
                
        SortingRobot.swap_item(self) #PICKING BACK UP NONE
                
                


                



    #U- SORT ARRAY FROM SMALLEST TO LARGEST WITHOUT USING BUILT IN METHODS. ONLY USING THE FUNCTIONS(ESSENTIALLY METHODS) TO MOVE THE NUMBERS
    #P- INITIALLY YOU'RE HOLDING NOTHING(NONE), SWAP THAT WITH THE FIRST NUMBER(SWAP), SINCE YOU DO NOT WANT TO COMPARE IT WITH THE NONE YOU JUST SWAPPED IT WITH, MOVE RIGHT FIRST THEN.. 
        # WHITE BASE CASE IS TRUE LIGHT ON:
            #WHILE CAN MOVE RIGHT IS TRUE
            #   COMPARE:
                    #IF (-1) THE NUMBER YOU'RE HOLDING IS LESS, SWAP AND MOVE RIGHT
                    #ELIF(1) THE NUMBER YOU'RE HOLDING IS BIGGER, SIMPLY MOVE RIGHT
                    #ELIF(0) IF THEY'RE EQUAL, MOVE RIGHT
                    #ELIF(NONE) MOVE RIGHT, SWAP

    #PLAN B WHILE THE LIGHT IS ON

        # WHILE THE LIGHT IS OFF:
            #while can move right
                #COMPARE:
                    #IF (-1) THE NUMBER YOU'RE HOLDING IS LESS, SWAP, LIGHT ON AND MOVE RIGHT
                    #ELIF(1) THE NUMBER YOU'RE HOLDING IS BIGGER, SIMPLY MOVE RIGHT
                    #ELIF(0) IF THEY'RE EQUAL, MOVE RIGHT
                    #ELIF(NONE) SWAP, MOVE RIGHT
            # IF CAN MOVE RIGHT IS FALSE
                #WE'RE AT THE END, IF LIGHT IS ON, TURN IT OFF
            #WHILE CAN GO LEFT IS TRUE
                # IF CAN MOVE LEFT IS FALSE AND LIGHT IS ON, TURN IT OFF

        
            
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)