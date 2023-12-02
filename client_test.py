import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 10, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 20, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_none(self):
        self.assertRaises(Exception, getDataPoint, [])
        self.assertRaises(Exception, getDataPoint, {})
        self.assertRaises(Exception, getDataPoint, 5)
        quotes = [
            {'top_as': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'pric': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'siz': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestam': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bi': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'pric': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'siz': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'i': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stoc': 'DEF'},
        ]
        for quote in quotes:
            self.assertRaises(Exception, getDataPoint, quote)

    def test_getDataPoint_negative(self):
        quotes = [
            {'top_ask': {'price': -121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': -121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertRaises(Exception, getDataPoint, quote)

    def test_getRatio_is_zero(self):
        self.assertRaises(Exception, getDataPoint, 5, 0)
        self.assertRaises(Exception, getDataPoint, 0, 5)

    def test_getRatio_negative(self):
        self.assertRaises(Exception, getDataPoint, -5, 5)
        self.assertRaises(Exception, getDataPoint, 5, -5)
        self.assertRaises(Exception, getDataPoint, -5, -5)


if __name__ == '__main__':
    unittest.main()
