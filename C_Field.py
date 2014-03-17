class C_Field(Field):

    def __init__(self):
        #Status Leer 0, Kreuz 1, Kreis 2
        self.state = 0
        self.coordinates = None, None, None

    def on_init(self, coordinates):
        self.coordinates = coordinates

