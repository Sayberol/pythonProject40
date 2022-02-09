import pytest

from unittest.mock import MagicMock

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService
from demostration_solution.setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name="abc")
    director_2 = Director(id=2, name="bca")
    director_3 = Director(id=3, name="cba")

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock(return_value=None)
    director_dao.update = MagicMock(return_value=None)

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None
        # assert len(director) == 1

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": " Test",
        }

        director = self.director_service.create(director_d)
        assert director.id != None

    def test_delete(self):
        ret = self.director_service.delete(1)
        assert ret == None

    def test_update(self):
        director_d = {
            "id": 4,
            "name": " Test",
        }

        ret = self.director_service.update(director_d)
        assert ret == None
