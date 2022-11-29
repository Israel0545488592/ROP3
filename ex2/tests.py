import unittest
from custom_output import *
from typing import List


class Tests(unittest.TestCase):

    def test_prefreances(self):


        self.prefs = prefreances((4, 3, 2, 1))
        self.assertEqual(self.prefs.get_match(), -1)
        self.prefs.set_match(3)
        self.assertEqual(self.prefs.get_match(), 2)
        self.assertEqual(self.prefs[2], 1)

        self.prefs = prefreances({'4' : 4, '3' : 3, '2' : 2, 'hogaboga' : 1})
        self.assertEqual(self.prefs.get_match(), -1)
        self.prefs.set_match(3)
        self.assertEqual(self.prefs.get_match(), 2)
        self.assertEqual(self.prefs[2], 1)


    def test_outypes(self):

        outypes : List[outype] = [setesfaction(), matches()]

        for out in outypes:

            girls = {'alice' :  ['bob', 'saeed', 'josh'],
                     'aliana':  ['saeed', 'josh', 'bob'],
                     'daniela': ['josh', 'saeed', 'bob']}

            boys =  {'bob' :  ['alice', 'aliana', 'daniela'],
                     'saeed': ['alice', 'aliana', 'daniela'],
                     'josh':  ['daniela', 'alice', 'aliana']}

            self.graph = out
            self.graph.build(boys, girls)

            self.assertEqual(len(self.graph.first_singles), 3)
            self.assertEqual(len(self.graph.second_singles), 3)
            self.assertEqual(len(self.graph.first_mached), 0)
            self.assertEqual(len(self.graph.second_mached), 0)

            self.graph.match('bob', 'alice')
            self.assertEqual(self.graph.get('bob').get_match(), 2)
            self.assertEqual(self.graph.get('alice').get_match(), 2)
            self.assertEqual(len(self.graph.first_mached), 1)
            self.assertEqual(len(self.graph.first_singles), 2)
            self.assertEqual(len(self.graph.second_mached), 1)
            self.assertEqual(len(self.graph.second_singles), 2)

            self.graph.match('saeed', 'daniela')
            self.assertEqual(self.graph.get('saeed').get_match(), 0)
            self.assertEqual(self.graph.get('daniela').get_match(), 1)
            self.assertEqual(len(self.graph.first_mached), 2)
            self.assertEqual(len(self.graph.first_singles), 1)
            self.assertEqual(len(self.graph.second_mached), 2)
            self.assertEqual(len(self.graph.second_singles), 1)

            # decupleing
            self.graph.match('saeed', 'aliana')
            self.assertEqual(self.graph.get('saeed').get_match(), 1)
            self.assertEqual(self.graph.get('daniela').get_match(), -1)
            self.assertEqual(self.graph.get('aliana').get_match(), 2)
            self.assertEqual(len(self.graph.first_mached), 2)
            self.assertEqual(len(self.graph.first_singles), 1)
            self.assertEqual(len(self.graph.second_mached), 2)
            self.assertEqual(len(self.graph.second_singles), 1)

            # rejection
            self.graph.match('daniela', 'bob')
            self.assertEqual(self.graph.get('bob').get_match(), 2)
            self.assertEqual(self.graph.get('daniela').get_match(), -1)
            self.assertEqual(len(self.graph.first_mached), 2)
            self.assertEqual(len(self.graph.first_singles), 1)
            self.assertEqual(len(self.graph.second_mached), 2)
            self.assertEqual(len(self.graph.second_singles), 1)

            self.graph.match('daniela', 'josh')
            self.assertEqual(self.graph.get('daniela').get_match(), 2)
            self.assertEqual(self.graph.get('josh').get_match(), 2)
            self.assertEqual(len(self.graph.first_mached), 3)
            self.assertEqual(len(self.graph.first_singles), 0)
            self.assertEqual(len(self.graph.second_mached), 3)
            self.assertEqual(len(self.graph.second_singles), 0)

            print('final results:', self.graph.extract_result())




if __name__ == '__main__':

    unittest.main()