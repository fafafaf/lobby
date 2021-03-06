__author__ = 'Sheeo'

from fa import check
from fa.game_version import GameVersion
from fa.featured import Mod
from git import Version

VALID_GAME_VERSION_INFO = {
    "engine": Version('FAForever/binary-patch', 'master'),
    "game": Mod("faf", Version('FAForever/fa.git', '3636', None, '791035045345a4c597a92ea0ef50d71fcccb0bb1')),
    "mods": [],
    "map": {"name": "scmp_0009", "version": "builtin"}
}


def test_check_game_verifies_game_version(application):
    assert check.game(application, GameVersion(VALID_GAME_VERSION_INFO))


def test_check_game_without_engine(application):
    invalid_version = VALID_GAME_VERSION_INFO.copy()
    invalid_version.pop('engine')
    assert not check.game(application, GameVersion(invalid_version))


def test_check_game_without_game(application):
    invalid_version = VALID_GAME_VERSION_INFO.copy()
    invalid_version.pop('game')
    assert not check.game(application, GameVersion(invalid_version))

