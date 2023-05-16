# a = input()

# A = a.count("U")
# B = a.count("D")
# C = a.count("L")
# D = a.count("R")

# if A == B and C == D:
#     print("Y")
# else:
#     print("N")


class Robot():
    #location = [0, 0]

    def __init__(self, action: str) -> None:
        self.location = [0, 0]
        for a in action:
            if a == "U":
                self.Up()
            elif a == "D":
                self.Down()
            elif a == "R":
                self.Right()
            elif a == "L":
                self.Left()

    def Up(self) -> None:
        self.location[1] += 1

    def Down(self) -> None:
        self.location[1] -= 1

    def Right(self) -> None:
        self.location[0] += 1

    def Left(self) -> None:
        self.location[0] -= 1

    def is_original(self) -> bool:
        return self.location == [0, 0]


r = Robot("RRDDLLUU")

print(r.location)
print(r.is_original())
