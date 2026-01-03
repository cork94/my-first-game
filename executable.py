import xml.etree.ElementTree as ET
from enum import Enum

class Map:
    def __init__(self, path):
        loadMapXml = ET.parse(path)

        self.name = loadMapXml.findall("./Name")
        nodesXml = loadMapXml.findall("./Nodes/Node")
        self.nodes = []
        for nodeXml in nodesXml:
            x = nodeXml.findtext("X")
            y = nodeXml.findtext("Y")
            blockValue = nodeXml.findtext("Value")
            self.nodes.append(Node(x,y,blockValue))
        
        self.mapMatrixRepresentation = []
    
    def __str__(self) :
        if len(self.nodes) == 0:
            return f"{self.name} has no nodes."
        
        rows = []
        for node in self.nodes:
            rowsLen = len(rows)
            coordY = int(node.y)
            if(rowsLen-1 < coordY):
                rows.append([])
            match node.blocktype:
                case BlockValue.PASSTHROUGH:
                    rows[coordY].append('O')
                case BlockValue.BLOCKED:
                    rows[coordY].append('X')
                case BlockValue.POINT:
                    rows[coordY].append('1')
                case BlockValue.SPECIALPOINT:
                    rows[coordY].append('2')
                case BlockValue.PLAYER:
                    rows[coordY].append('P')
        
        self.mapMatrixRepresentation = rows
        matrixText = ""
        for row in rows:
            for ele in row:
                matrixText += f"{ele} "
            matrixText += "\n"
            
        return matrixText

class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        
        valUp = val.upper()
        self.blocktype = BlockValue.__members__.get(valUp)

        if self.blocktype is None:
            raise ValueError("Invalid BlockType")

class BlockValue(Enum):
    PASSTHROUGH  = 1
    BLOCKED = 2
    POINT = 3
    SPECIALPOINT = 4
    PLAYER = 5


loadMapXml = ET.parse("tutorialMap.xml")
map = Map("tutorialMap.xml")
print("----------------Start Position-----------------------")
print(map)
    