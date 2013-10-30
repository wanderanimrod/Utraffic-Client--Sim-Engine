from unittest import TestCase
import app
from data_access.database import get_db


class AppTest(TestCase):

    def test_should_create_a_database_object_with_a_connection_to_redis(self):
        db = get_db()
        self.assertIsNotNone(db)

    def test_should_maintain_connection_to_the_same_db_over_multiple_calls_to_get_db(self):
        db_returned_by_first_call = get_db()
        db_returned_by_second_call = get_db()
        self.assertEquals(db_returned_by_first_call, db_returned_by_second_call)

    def test_should_maintain_state_across_multiple_calls_to_get_db(self):
        key_to_maintain = 'name'
        value_to_maintain = 'Nimrod'
        db_returned_by_first_call = get_db()
        db_returned_by_first_call.set(key_to_maintain, value_to_maintain)
        db_returned_by_second_call = get_db()
        returned_value = db_returned_by_second_call.get(key_to_maintain)
        self.assertEquals(returned_value, value_to_maintain)