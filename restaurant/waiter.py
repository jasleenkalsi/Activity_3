class Waiter():
    """
    A class representing a Waiter.
    Attrs:
        __name (str): The name of the waiter. 
    """
    def __init__(self, name: str):
        """
        Initializes the Waiter class.
        Args:
            name (str): The name of the waiter. 
        """
        self.__name = name

    def __str__(self):
        """
        Returns a string representation of a Waiter instance.
        returns:
            string: A string representation of a Waiter instance.
        """
        return f"Waiter: {self.__name} is currently on duty."