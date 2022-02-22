import unittest

def reverseArray(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list

def isPalindrome(stri):
    for x in range (int((len(stri))/2)):
        if (stri[x] == stri[((len(stri))-1) - x]):
            return True;

def coin(num):
    quarter = num//25
    count = num - (25*(num//25))
    dime = count//10
    count = count - (10*(count//10))
    nickel = count//5
    count = count - (5*(count//5))
    penny = count
    return quarter, dime, nickel, penny

def recursiveFactorial(num):
    total = 1
    if (num == 0):
        return 1
    else:
        for x in range(num, 0, -1):
            total *=x
    return total

class revereseArrayTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseArray([1,2,3]),[3,2,1])
    def testTwo(self):
        self.assertEqual(reverseArray([4,5,6,7]),[7,6,5,4])
    def testThree(self):
        self.assertEqual(reverseArray([8,9,10,11,12]),[12, 11, 10, 9, 8])
    def setUp(self):
        print('Running Setup')
    def tearDown(self):
        print('Running tear down tasks')

    class isPalindromeTest(unittest.TestCase):
        def testOne(self):
            self.assertEqual(isPalindrome('racecar'),True)
        def testTwo(self):
            self.assertTrue(isPalindrome('fish'))
        def testThree(self):
            self.assertFalse(isPalindrome('danger'))
        def testFour(self):
            self.assertTrue(isPalindrome('level'))
        def testFive(self):
            self.assertFalse(isPalindrome('madam'))
        def setUp(self):
            print('Running Setup')
        def tearDown(self):
            print('Running tear down tasks')

class isCoinTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coin(87), (3,1,0,2))
    def testTwo(self):
        self.assertEqual(coin(99), (3,1,0,2))
    def testThree(self):
        self.assertTrue(coin(87))
    def testFour(self):
        self.assertFalse(coin(87))
    def testFive(self):
        self.assertEqual(coin(87), (4,1,0,5))
    def setUp(self):
        print('Running Setup')
    def tearDown(self):
        print('Running tear down tasks')

class recursiveFactorialTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(recursiveFactorial(3), 6)
    def testTwo(self):
        self.assertTrue(recursiveFactorial(4))
    def testThree(self):
        self.assertFalse(recursiveFactorial(5))

if __name__ == '__main__':
    unittest.main()