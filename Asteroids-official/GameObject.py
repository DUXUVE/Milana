from abc import ABC

class GameObject(ABC):
    @abstractmetod
    def update(self):
        ...
        
    @abstractmetod
    def draw(self):
        ...