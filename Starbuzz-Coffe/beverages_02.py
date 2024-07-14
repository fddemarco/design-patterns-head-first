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


class HouseBlendWithSteamedMilkAndMocha(Beverage):
    def cost(self):
        ...


class DarkRoastWithSteamedMilkAndMocha(Beverage):
    def cost(self):
        ...


class DecafWithSteamedMilkAndMocha(Beverage):
    def cost(self):
        ...


class EspressoWithSteamedMilkAndMocha(Beverage):
    def cost(self):
        ...


class HouseBlendWithSteamedMilkAndCaramel(Beverage):
    def cost(self):
        ...


class DarkRoastWithSteamedMilkAndCaramel(Beverage):
    def cost(self):
        ...


class DecafWithSteamedMilkAndCaramel(Beverage):
    def cost(self):
        ...


class EspressoSteamedMilkAndCaramel(Beverage):
    def cost(self):
        ...

class HouseBlendWithSoyAndMocha(Beverage):
    def cost(self):
        ...


class DarkRoastWithSoyAndMocha(Beverage):
    def cost(self):
        ...


class DecafWithSoyAndMocha(Beverage):
    def cost(self):
        ...


class EspressoSoyAndMocha(Beverage):
    def cost(self):
        ...


class HouseBlendWithWhipAndSoy(Beverage):
    def cost(self):
        ...


class DarkRoastWithWhipAndSoy(Beverage):
    def cost(self):
        ...


class DecafWithWhipAndSoy(Beverage):
    def cost(self):
        ...


class EspressoWithWhipAndSoy(Beverage):
    def cost(self):
        ...
