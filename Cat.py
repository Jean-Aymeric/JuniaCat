from abc import ABC, abstractmethod

from util import classproperty


class Cat(ABC):
    __DEFAULT_STATE = "Sleeping"
    __DEFAULT_NAME = "Minou"
    __NUMBER_OF_LIVES = 9
    __state: str
    __name: str
    __numberOfLives: int

    def __init__(self, state: str, name: str):
        if name == "":
            self.__name = self.__DEFAULT_NAME
        else:
            self.__name = name
        if state == "":
            self.__state = self.__DEFAULT_STATE
        else:
            self.__state = state
        self.__numberOfLives = self.__NUMBER_OF_LIVES

    @classmethod
    def getEyesFromState(cls, state: str):
        if state == "Sleeping":
            return "- -"
        elif state == "Awake":
            return "o o"
        else:
            return "x x"

    @abstractmethod
    def display(self) -> None:
        pass

    def die(self) -> None:
        if self.__state == "Dead":
            return
        self.__numberOfLives -= 1
        if self.__numberOfLives == 0:
            self.__state = "Dead"

    def sleep(self) -> None:
        if self.__state == "Dead":
            return
        self.__state = "Sleeping"

    def wakeUp(self) -> None:
        if self.__state == "Dead":
            return
        self.__state = "Awake"

    @property
    def State(self) -> str:
        return self.__state

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, name: str) -> None:
        self.__name = name

    @property
    def NumberOfLives(self) -> int:
        return self.__numberOfLives

    @classproperty
    def NumberOfLives(cls) -> int:
        return cls.__NUMBER_OF_LIVES
