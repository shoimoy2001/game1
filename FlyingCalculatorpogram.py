#Flying Calculator simulator based on GUI
from breezypythongui import EasyFrame
from math import sqrt

class AircraftMinimumSafeClimbRateCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=350, height=300, title="Aircraft Minimum Safe Climb Rate Calculator")

        self.label1 = self.addLabel(text="Enter The obstruction height (m):  ", row=0, column=0)
        self.obstructionHeight = self.addFloatField(value=0.0, row=0, column=1, state="normal", width=10, precision=2)

        self.label2 = self.addLabel(text="Enter The distance to obstruction from the point to Takeoff (m):  ", row=1, column=0)
        self.takeoffDistance = self.addFloatField(value=0.0, row=1, column=1, width=10, precision=2)

        self.label3 = self.addLabel(text="Enter ground speed of the Aircraft (Km/H): ", row=2, column=0)
        self.velocityField = self.addIntegerField(value=0, state="normal", row=2, column=1, width=10)

        self.label4 = self.addLabel(text="Aircraft altitude above obstruction (m):   ", row=3, column=0)
        self.altitudeField = self.addFloatField(value=0.0, row=3, column=1, width=10, state="readonly", precision=2)

        self.label5 = self.addLabel(text="Minimum Safe Climb Rate (m/s):   ", row=4, column=0)
        self.climbRate = self.addFloatField(value=0.0, row=4, column=1, width=10, state="readonly", precision=2)

        self.calculateBtn = self.addButton(text="Calculate", row=5, column=0, command=self.calculateBtnClick)
        self.clearBtn = self.addButton(text="Clear", row=5, column=1, command=self.clearBtnClick, state="disabled")

    def calculateBtnClick(self):
        try:
            obstruction_height = self.obstructionHeight.getNumber()+10
            #you can increase the safe height you desire I just added 10
            takeoff_distance = self.takeoffDistance.getNumber()
            ground_velocity = self.velocityField.getNumber()

            # Ensure non-zero velocity to avoid division by zero
            if ground_velocity == 0:
                raise ValueError("Ground velocity must be greater than 0")

            if takeoff_distance == 0:
                raise ValueError("Takeoff distance to the point of obstruction must be greater than 0")

            # Following the Pythagorean Theorem
            final_distance = sqrt(obstruction_height**2 + takeoff_distance**2)

            # Time to reach obstruction with conversion factor
            time = (final_distance)/(ground_velocity/3.6)

            # Altitude and climb rate calculations
            final_height = (obstruction_height/time)
        
            

            # Set the calculated values to the fields
            self.altitudeField.setNumber(obstruction_height)
            self.climbRate.setNumber(final_height)

            # Enable the clear button
            self.clearBtn["state"] = "normal"
            self.calculateBtn["state"] = "disabled"
        
        except ValueError as e:
            self.messageBox(title="ERROR", message=str(e))

    def clearBtnClick(self):
        # Reset the fields for the next calculation
        self.obstructionHeight.setNumber(0.0)
        self.takeoffDistance.setNumber(0.0)
        self.velocityField.setNumber(0)
        self.altitudeField.setNumber(0.0)
        self.climbRate.setNumber(0.0)

        # Disable the clear button
        self.clearBtn["state"] = "disabled"
        self.calculateBtn["state"] = "normal"

def main():
    AircraftMinimumSafeClimbRateCalculator().mainloop()

if __name__ == "__main__":
    main()
