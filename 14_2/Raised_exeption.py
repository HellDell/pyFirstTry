class GroupLimitError(Exception):

    def __init__(self, message="A group cannot contain more than 10 students!"):
        self.message = message
        super().__init__(self.message)