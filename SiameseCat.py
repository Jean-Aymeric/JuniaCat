from Cat import Cat


class SiameseCat(Cat):
    def __init__(self, state: str, name: str):
        super().__init__(state, name)

    def display(self) -> None:
        print(" ^_^")
        print("(" + Cat.getEyesFromState(self.State) + ")")
        print(" (" + "\"" * 5 + ")~")
        print("  °°  °°")
