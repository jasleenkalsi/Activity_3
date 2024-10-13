class Chef():
    """
    A class representing a Chef.
    Attrs:
        __name (str): The name of the chef. 
    """
    def __init__(self, name: str):
        """
        Initializes the Chef class.
        Args:
            name (str): The name of the chef. 
        """
        self.__name = name

    def __str__(self):
        """
        Returns a string representation of a Chef instance.
        returns:
            string: A string representation of a Chef instance.
        """
        return f"Chef: {self.__name} is currently employed at the Restaurant."
