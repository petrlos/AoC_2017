class Particle:

    def __init__(self, partNr, numbers):
        self.partNr = partNr
        self.location = numbers[0:3]
        self.velocity = numbers[3:6]
        self.acceleration = numbers[6:9]
        self.distance = sum([abs(x) for x in self.location])
        self.active = True

    def __str__(self):
        return "Nr.:{0}: distance: {1}".format(self.partNr, self.distance)
        #return "Nr.{0}, coords: {1}, vel: {2}, acc: {3}".format(self.partNr, self.location, self.velocity, self.acceleration)

    def stepByOne(self):
        self.velocity = [x + y for x, y in zip(self.velocity, self.acceleration)]
        self.location = [x + y for x, y in zip(self.velocity, self.location)]
        self.distance = sum([abs(x) for x in self.location])

