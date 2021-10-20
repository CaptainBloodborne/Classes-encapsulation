class Field:
    def __init__(self):
        self.__value = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


if __name__ == "__main__":
    # Check if this code is working
    field = Field()
    field.set_value(123)
    print(field.get_value())
