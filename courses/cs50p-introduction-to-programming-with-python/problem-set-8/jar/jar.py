class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity test")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity test 1")
        if n + self.size > self.capacity:
            raise ValueError("Exceed capacity test 2")            
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies to remove test")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    ...


if __name__ == "__main__":
    main()