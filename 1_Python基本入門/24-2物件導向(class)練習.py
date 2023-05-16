class BaseCRUD:
    data = [1,2,3,4,5,6,7,8,9,0]
    
    def read_data(self) -> list:
        return self.data


class EvenCRUD(BaseCRUD):
    
    def read_data(self) -> list:
        raw_data = super().read_data()

        return list(filter(lambda x: x % 2 == 0, raw_data))

e = EvenCRUD()
print(e.read_data())