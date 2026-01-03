import unittest
import xml.etree.ElementTree as ET
from mapService import MapService

class TestXmlParserMethods(unittest.TestCase):

    def test_isMoveValid_WhenRuningIntoBlocked_returnsFalse(self) :
        #arange
        mapService = MapService("tutorialMap.xml")
        
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
