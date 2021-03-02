'''Instantiate by defining the init
and the functionality of each parameter'''
class DrivingComputer:
    def __init__(self, car, start=False,
                 alert=False, driving=False):
        self.car = car
        self.start = start
        self.alert = alert
        self.driving = driving

    #Putting the car in motion
    def run(self):
        if self.start:
            print(f'Alert {self.car}: '
                  f'fasten your seat belt.')
            return
        if not self.start:
            print(f'{self.car} off.')
            return

    #Starting the car engine
    def starting(self):
        if self.start:
            print(f'The {self.car} is already '
                  f'started')
            return
        print(f'Starting the {self.car}, welcome!')
        self.start = True

    #Turn off the car engine
    def turn_off(self):
        if not self.start:
            print(f'{self.car} is off and stopped')
            return
        print(f'{self.car} to switch off')
        self.start = False