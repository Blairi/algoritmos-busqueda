
class Jugador:
    score = 0
    nickName = ""

    def __init__(self, score, nickName) -> None:
        self.score = score
        self.nickName = nickName

    def __str__(self) -> str:
        return f"score: {self.score}\nnickName: {self.nickName}"

    def getScore(self) -> int:
        return self.score

    def getNickName(self) -> str:
        return self.nickName
        
