from class_rules import Rules


class ImplementorClass(metaclass=Rules):
    test_attr = "class attribute for Implementor class"
    _test_attr = "class attribute for Implementor class"
    est_attr12 = "class attribute for Implementor class"

    def __init__(self):
        self._priv = "private class attribute"

    def ethod1(self):
        """ doc string for method1 """
        print("Method 1")

if __name__ == "__main__":
    imp_obj = ImplementorClass()
    print("omp_obj is: ", imp_obj)
    # print("__dict__ : ", imp_obj.__dict__)