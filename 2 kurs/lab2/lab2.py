from abc import ABC, abstractmethod


class Pet(ABC):
    """Общий контракт для питомцев."""

    @abstractmethod
    def express(self) -> None:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getAge(self) -> int:
        pass

    @abstractmethod
    def getAgeInHumanYears(self) -> int:
        pass


class Animal(Pet):
    """Общие данные и поведение животных."""

    def __init__(self, name: str, age: int) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        if type(age) is not int:
            raise TypeError("Age must be an integer")

        if age < 0:
            raise ValueError("Age cannot be negative")

        self.__name = name
        self.__age = age

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    def happyBirthday(self) -> None:
        self.__age += 1

    @abstractmethod
    def express(self) -> None:
        pass

    @abstractmethod
    def getAgeInHumanYears(self) -> int:
        pass


class Parrot(Animal):
    """Попугай."""

    def getAgeInHumanYears(self) -> int:
        return self.getAge() * 5

    def express(self) -> None:
        print(f'{self.getName()}: "Hello!"')
        print(r'''   \
   (o>
\\_//)
 \_/_)
  _|_''')


class Turtle(Animal):
    """Черепаха."""

    def getAgeInHumanYears(self) -> int:
        age = self.getAge()

        if age <= 0:
            return 0

        return 15 + (age - 1) * 2

    def express(self) -> None:
        print(r'''  _____     ____
 /      \  |  o |
|        |/ ___\|
|_________/
|_|_| |_|_|''')


class Person:
    """Человек, у которого может быть питомец."""

    def __init__(self, name: str, pet=None) -> None:
        self.__name = name
        self.__pet = pet

    def setPet(self, pet) -> None:
        self.__pet = pet

    def getPetInfo(self) -> None:
        print("--------------------")
        pet = self.__pet

        if pet is None:
            print(f"{self.__name} has no pet yet")
            print("--------------------")
            return

        print(
            f"Pet for {self.__name} "
            f"is named {pet.getName()}"
        )
        print(
            f"Age: {pet.getAge()} year(s), "
            f"about {pet.getAgeInHumanYears()} human years"
        )
        print("And it expresses itself like this:")
        pet.express()
        print("--------------------")


def main() -> None:
    kesha = Parrot("Kesha", 2)
    zavala = Turtle("Zavala", 4)

    kesha.happyBirthday()

    jack = Person("Jack", kesha)
    john = Person("John")

    jack.getPetInfo()
    john.getPetInfo()

    john.setPet(zavala)
    john.getPetInfo()


if __name__ == "__main__":
    main()