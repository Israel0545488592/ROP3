import unittest
from custom_output import *


class Tests(unittest.TestCase):

    def test_prefreances(self):


        self.prefs = prefreances((4, 3, 2, 1))
        self.assertEqual(self.prefs.get_match(), -1)
        self.prefs.set_match(3)
        self.assertEqual(self.prefs.get_match(), 1)
        self.assertEqual(self.prefs[2], 2)

        self.prefs = prefreances({'4' : 4, '3' : 3, '2' : 2, 'hogaboga' : 1})
        self.assertEqual(self.prefs.get_match(), -1)
        self.prefs.set_match(3)
        self.assertEqual(self.prefs.get_match(), 1)
        self.assertEqual(self.prefs[2], 2)


    def test_outypes(self):

        girls = {'alice' :  ['bob', 'saeed', 'josh'],
                 'aliana':  ['saeed', 'josh', 'bob'],
                 'daniela': ['josh', 'saeed', 'bob']}

        boys =  {'bob' :  ['alice', 'aliana', 'daniela'],
                 'saeed': ['alice', 'aliana', 'bdanielaob'],
                 'josh':  ['daniela', 'alice', 'aliana']}

        self.graph = outype_setesfaction()
        self.graph.build(boys, girls)

        self.graph.match('bob', 'alice')
        self.assertEqual(self.graph.get('bob', first = True).get_match(), 0)

        print(self.graph.first_singles)
        print(self.graph.first_mached)




if __name__ == '__main__':



    '''girls = {'alice' :  ['bob', 'saeed', 'josh'],
                 'aliana':  ['saeed', 'josh', 'bob'],
                 'daniela': ['josh', 'saeed', 'bob']}

    boys =  {'bob' :  ['alice', 'aliana', 'daniela'],
                 'saeed': ['alice', 'aliana', 'bdanielaob'],
                 'josh':  ['daniela', 'alice', 'aliana']}

    graph = outype_setesfaction()
    graph.build(boys, girls)
    graph.match('bob', 'alice')'''

    unittest.main()