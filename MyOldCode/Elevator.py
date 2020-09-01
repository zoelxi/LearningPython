class Elevator:
    '''Represents a simple elevator'''

    def __init__(self, startFloor, startDoorsOpen):
        '''Elevator(startFloor, startDoorsOpen) -> Elevator
        Constructs an Elevator
        startFloor: int giving the starting floor
        startDoorsOpen: bool giving the starting doors 
                    (True = 'open')'''
        self.floor = startFloor  # store floor attribute
        self.doorsOpen = startDoorsOpen  # store doors attribute
        self.passengers = []

    def __str__(self):
        '''str(Elevator) -> str
        Returns a string giving the floor and state of the doors.'''
        answer = 'doors '         # will contain string to return
        if self.doorsOpen:        # if doors open
            answer += 'open'      # say so
        else:                     # if doors closed
            answer += 'closed'    # say that too
        answer += ', floor '      # this is in every answer
        answer += str(self.floor) # add floor number
        if len(self.passengers) != 0:
            answer += ', passengers '
            for passenger in self.passengers:
                answer += passenger + ', '
            answer = answer[:-2]
        return answer

    def open_doors(self):
        '''Elevator.open_doors()
        Opens the doors by setting doors attribute to True.'''
        self.doorsOpen = True # set doors to open

    def close_doors(self):
        '''Elevator.close_doors()
        Closes the doors by setting doors attribute to False.'''
        self.doorsOpen = False # set doors to closed

    def go_up(self):
        '''Elevator.go_up()
        Goes up by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor += 1              # increase floor by 1

    def go_down(self):
        '''Elevator.go_down()
        Goes down by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor -= 1              # decrease floor by 1

    def go_to_floor(self, destination):
        '''Elevator.go_to_floor(int)
        Closes doors, moves to destination, and opens doors.'''
        if self.doorsOpen:               # if doors are open
            self.close_doors()           # close 'em
        while self.floor != destination: # if not at destination
            if self.floor < destination: # if below
                self.go_up()             # go up 1 floor
            else:                        # if above
                self.go_down()           # go down 1 floor
        self.open_doors()                # open doors

    def get_on(self,passengersOn):
        if self.doorsOpen:
            self.passengers.extend(passengersOn)
        else:
            print('Please wait until the doors are open!')

    def get_off(self,passengersOff):
        if self.doorsOpen:
            for passenger in passengersOff:
                self.passengers.remove(passenger)
        else:
            print('Please wait until the doors are open!')

e = Elevator(5,False)
print(e)
e.get_on(['Chloe'])
print(e)
e.open_doors()
print(e)
e.get_on(['Chloe'])
print(e)
e.go_to_floor(7)
print(e)
e.get_on(['Rosa'])
print(e)
e.go_to_floor(8)
print(e)
e.get_on(['Sophia'])
print(e)
e.go_to_floor(1)
print(e)
e.get_off(['Chloe','Rosa','Sophia'])
print(e)
