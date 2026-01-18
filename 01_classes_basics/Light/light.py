class Light:
    def __init__(self, name):
        self.name = name
        self.__is_on = False
    
    def turn_on(self):
        if self.__is_on:
            return
        self.__is_on = True
    
    def turn_off(self):
        if not self.__is_on:
            return
        self.__is_on = False
    
    def toggle(self):
        self.__is_on = not self.__is_on
    
    def __str__(self):
        return(
            f"Light: {self.name} | Status: {'on' if self.__is_on else 'off'}"
        )
