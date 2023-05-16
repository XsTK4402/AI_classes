class veh():
    name = "交通工具"
    def __init__(self, c: str) -> None:
        self.tires = c
    

#繼承

class cars(veh):
    name = "汽車"

    def move(self) -> None:
        print(f"這個{self.name}有{self.tires}而且跑起來了~")


class airplain(veh):
    name = "飛機"

    def move(self) -> None:
        print(f"這個{self.name}有{self.tires}而且飛起來了~")

    
my_car = cars("四輪")
my_car.move()  # 輸出：這個汽車有四輪而且跑起來了~