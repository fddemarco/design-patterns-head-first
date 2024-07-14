import abc

class Beverage(abc.ABC):
    """ Beverage is an abstract class, subclassed by all beverages offered
    in the coffee shop.

    Attributes
    ----------
    description : str
        The description instance variable is set in each subclass and holds a
        description of the bevreage, like "Most Excellent Dark Roast".
    """

    def __init__(self, description: str):
        self.description = description

    def get_description(self) -> str:
        """The get_description() method returns the description.

        Returns
        -------
        str
            _description_
        """        
        return self.description
    
    @abc.abstractmethod
    def cost(self) -> float:
        """The cost() method is abstract;
        subclasses need to define their own implementation.

        Returns
        -------
        float
            beverage cost
        """        
        ...


class HouseBlend(Beverage):
    def cost(self):
        ...


class DarkRoast(Beverage):
    def cost(self):
        ...


class Decaf(Beverage):
    def cost(self):
        ...


class Espresso(Beverage):
    def cost(self):
        ...


