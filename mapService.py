from executable import Map, BlockValue

class MapService:
    def __init__(self, path):
        self.map = Map(path)
    
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
        if(newX< 0 or newY <0 or newX> len(self.map.mapMatrixRepresentation[0]) or newY > len(self.map.mapMatrixRepresentation)):
            return False
        
        return True
    
    def playerPosition(self):
        return self.map.nodes[0]
    

if __name__ == '__main__' :
    print("----------------Start Position-----------------------")
    mapService = MapService("tutorialMap.xml")
    print(mapService.map)
    temp_node = mapService.playerPosition()
    temp_node.blocktype = BlockValue.BLOCKED
    print("---------------- Now Position -----------------------")
    print(mapService.map)
