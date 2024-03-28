class FacesException(Exception):
    def __init__(self, message="Face could not be recognized"):
        self.message = message
        super().__init__(self.message)
