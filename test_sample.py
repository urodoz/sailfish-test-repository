import unittest
import redis

class TestRedis(unittest.TestCase):

  def test_redis_connection(self):

      r = redis.StrictRedis(host='redis', port=6379, db=0)
      result_set = r.set('foo', 'bar')

      self.assertEqual(True, result_set)

      item_from_redis = r.get('foo')

      self.assertEqual("bar", item_from_redis)

if __name__ == '__main__':
    unittest.main()