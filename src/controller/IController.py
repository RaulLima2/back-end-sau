from abc import ABC


class IController(ABC):

    @classmethod
    def store_data(self, data) -> bool:
        pass

    @classmethod
    def get_data(self) -> list:
        pass

    @classmethod
    def update_data(self, data) -> bool:
        pass

    @classmethod
    def delete_data(self, data) -> bool:
        pass

    @classmethod
    def search_data(self, data) -> list:
        pass
