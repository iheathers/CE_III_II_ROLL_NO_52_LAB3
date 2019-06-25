import unittest
from binary_search import BinarySearchTree

class BinarySearchTestcase(unittest.TestCase):
        def test_bst(self):
            bst = BinarySearchTree()

            bst.addNode(20,"Computer")
            self.assertEqual(bst.size(),1)

            bst.addNode(10 ,"laptop")
            self.assertEqual(bst.size(),2)

            bst.addNode(15,"PDA")
            self.assertEqual(bst.size(),3)

            bst.addNode(40,"android")
            self.assertEqual(bst.size(),4)

            self.assertListEqual(bst.inOrderTraverse(),[10,15,20,40])

            self.assertListEqual(bst.preOrderTraverse(),[20,10,15,40])

            self.assertListEqual(bst.postOrderTraverse(),[10,15,40,20])



if __name__ == "__main__":
    unittest.main()