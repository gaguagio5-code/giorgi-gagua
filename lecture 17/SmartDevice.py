class SmartDevice:
    def __init__(self, brend):
        self.brend = brend
        self.__is_on = False

    @property
    def is_on(self):
        return self.__is_on
    def turn_on(self):
        if not self.__is_on:
            print(f"{self.brend} is turning on...")
        else:
            self.__is_on = True
            print(f"{self.brend} is already on.")

    def turn_off(self):
        if self.__is_on:
            print(f"{self.brend} is turning off...")
        else:
            self.__is_on = False
            print(f"{self.brend} is already off.")

class SmartLight(SmartDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)
        self.brightness = brightness  

    @property
    def brightness(self):
        return self.__brightness
    @brightness.setter
    def brightness(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        self.__brightness = value
    def turn_on(self):
        super().turn_on()
        print(f"{self.brend} light is now on with brightness {self.brightness}%.")
light = SmartLight("Philips", 75)
print(light.is_on)  # Output: False
light.turn_on()  # Output: "Philips is turning on..." and "Philips light is now on with brightness 75%."
print(light.is_on)  # Output: True
light.turn_off()  # Output: "Philips is turning off..."
print(light.is_on)  # Output: False
    