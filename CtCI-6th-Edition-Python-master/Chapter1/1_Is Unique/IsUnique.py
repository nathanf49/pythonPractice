# O(N)
import unittest


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # violates second optional requirement
    char_set = [False for _ in range(128)] #creates a list that defaults to false for each possible char in ASCII 128 to show if it has been found or not
    for char in string:
        val = ord(char) # finds where current char is in ascii 128 positioning
        if char_set[val]: #checks if that char has already been found
            # Char already found in string
            return False
        char_set[val] = True # sets to found

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
