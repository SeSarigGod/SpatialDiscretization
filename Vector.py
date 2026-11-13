def str_consists(test_str: str, comp_str: str) -> bool:
    return all(char in comp_str for char in test_str)

class Vector2[_T]:
    def __init__(self, x: _T = None, y: _T = None) -> None:
        if x is None:
            self.x = self.default_values[0]
        else:
            self.x = x

        if y is None:
            self.y = self.default_values[1]
        else:
            self.y = y

    def __init_subclass__(cls, /, default_values: tuple[_T, _T], **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.default_values = default_values
        cls.x: _T = default_values[0]
        cls.y: _T = default_values[1]

    def __getattribute__(self, name: str) -> list[_T] | tuple[_T,...] | _T:
        if str_consists(name, "xy") and len(name) > 1:
            return tuple([super().__getattribute__(char) for char in name])
        else:
            return super().__getattribute__(name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __add__(self, other) -> Vector2:
        if isinstance(other, self.__class__):
            return self.__class__(self.x + other.x, self.y + other.y)
        else:
            try:
                if len(other) == 2:
                    return self.__class__(self.x + other[0], self.y + other[1])
                else:
                    raise TypeError(f"multi-element operand types must match length of vector for +: '{self.__class__.__name__}: 2' and '{type(other).__name__}: {len(other)}'")
            except TypeError:
                pass
            except Exception as e:
                raise e
            try:
                return self.__class__(self.x + other, self.y + other)
            except TypeError:
                raise TypeError(f"unsupported operand type(s) for +: '{self.__class__.__name__}' and '{type(other).__name__}'")
            except Exception as e:
                raise e

    def __radd__(self, other) -> Vector2:
        return self.__add__(other)

    def __iadd__(self, other) -> Vector2:
        if isinstance(other, self.__class__):
            self.x += other.x
            self.y += other.y
            return self
        else:
            try:
                if len(other) == 2:
                    self.x += other[0]
                    self.y += other[1]
                    return self
                else:
                    raise TypeError(f"multi-element operand types must match length of vector for +: '{self.__class__.__name__}: 2' and '{type(other).__name__}: {len(other)}'")
            except TypeError:
                pass
            except Exception as e:
                raise e
            try:
                self.x += other
                self.y += other
                return self
            except TypeError:
                raise TypeError(f"unsupported operand type(s) for +: '{self.__class__.__name__}' and '{type(other).__name__}'")
            except Exception as e:
                raise e

class Vector2i(Vector2[int], default_values=(0, 0)):
    pass

class Vector2f(Vector2[float | int], default_values=(0.0, 0.0)):
    pass


test_vector_1 = Vector2f()
test_vector_2 = Vector2f(1.0, 2.0)
print(test_vector_1 + test_vector_2)
print(test_vector_2 + 1)