from executable import Map, BlockValue

class MapService:
    def __init__(self, path):
        self.map = Map(path)
        self.playerPositionIndex = 0
    
    def isMoveValid(self, move):
        startNode = self.playerPosition()
        newX = startNode.x
        newY = startNode.y
        match move:
            case "right":
                newX += 1
            case "left":
                newX -= 1
            case "up":
                newY -= 1
            case "down":
                newY += 1
        numberOfCol = len(self.map.mapMatrixRepresentation[0])
        numberOfRows = len(self.map.mapMatrixRepresentation)
        isOutOfBounds = newX< 0 or newY <0 or newX> numberOfCol or newY > numberOfRows
        if(isOutOfBounds):
            return False
        
        nextStepNodeList = [n for n in self.map.nodes if (n.x == newX and n.y == newY)]
        nextStepNode = nextStepNodeList[0]      
        if(nextStepNode.blocktype == BlockValue.BLOCKED):
            return False
        
        return True
    
    def playerPosition(self):
        return self.map.nodes[self.playerPositionIndex]
    

if __name__ == '__main__' :
    print("----------------Start Position-----------------------")
    mapService = MapService("tutorialMap.xml")
    print(mapService.map)
    temp_node = mapService.playerPosition()
    temp_node.blocktype = BlockValue.BLOCKED
    print("---------------- Now Position -----------------------")
    print(mapService.map)
