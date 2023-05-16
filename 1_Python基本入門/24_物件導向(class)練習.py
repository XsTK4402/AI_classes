# user_id = 蛇型
# UserId = 駝峰


class Chair():  # 定義類別、設計稿
    name = "椅子"
    def __init__(self, c: str) -> None:
        self.color = c
    
    def seat(self) -> None:
        print(f"這個{self.color}的{self.name}好舒服~")

chair_a = Chair("Red")

chair_b = Chair("Green")


#繼承

class Sofa(Chair):
    name = "沙發"
    pass

    def lay(self) -> None:
        print(f"這個{self.color}的{self.name}可以躺~")

    def seat(self) -> None:
        super().seat()
        print("ZZZZZ")


sofa_a = Sofa("black")

sofa_a.lay()