

class Base:

    def __init__(self, uid: str):
        self._uid = uid

    @property
    def uid(self) -> str:
        return self._uid

