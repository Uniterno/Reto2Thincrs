from db.migrations import create_db
import os


class TestClassInstance:
    path = './db/db_oltp.db'

    def initialize(self) -> bool:
        return create_db(self.path)

    def test_initialize(self):
        assert not os.path.isfile(self.path) & (self.initialize() == True) == True

    def test_not_initialize(self):
        assert os.path.isfile(self.path) == True
