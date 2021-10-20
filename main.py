class Field:
    def __init__(self):
        self.__value = None

    def set_field(self, value):
        self.__value = value

    def get_field(self):
        return self.__value


if __name__ == "__main__":
    # Check if this code is working
    field = Field()
    field.set_field(123)
    print(field.get_field())
