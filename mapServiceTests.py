import unittest
import xml.etree.ElementTree as ET
from mapService import MapService
from executable import BlockValue

def movePlayerLeftOfBlockedPosition(mapService):
     mapService.map.nodes[0].blocktype = BlockValue.PASSTHROUGH
     mapService.map.nodes[6].blocktype = BlockValue.PLAYER
     mapService.playerPositionIndex = 6
     print(mapService.map)     

class TestXmlParserMethods(unittest.TestCase):

    def test_isMoveValid_WhenRuningIntoBlocked_returnsFalse(self) :
        #arange
        mapService = MapService("tutorialMap.xml")
        movePlayerLeftOfBlockedPosition(mapService)
        
        #act
        actual = mapService.isMoveValid("right")

        #assert
        self.assertFalse(actual)

    def test_isMoveValid_WhenRuningIntoPassthroguh_returnsTrue(self) :
        #arange
        mapService = MapService("tutorialMap.xml")
        
        #act
        actual = mapService.isMoveValid("right")

        #assert
        self.assertTrue(actual)
    
    def test_playerPosition_returnsPlayerPositionNode(self):
        #arange
        mapService = MapService("tutorialMap.xml")

        #act
        actual = mapService.playerPosition()

        #act
        self.assertEqual(actual.x, 0)
        self.assertEqual(actual.y, 0)
    
if __name__ == '__main__':
    unittest.main()
