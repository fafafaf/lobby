from fa.game_version import GameVersion
from fa.featured import Mod
from git import Repository, Version

import pytest

__author__ = 'Sheeo'

TEST_GAME_VERSION = Version('FAForever/fa', '3634', None, '791035045345a4c597a92ea0ef50d71fcccb0bb1')
TEST_SIM_MOD = Mod("test-mod", Version('FAForever/test_sim_mod', 'some-branch', None, 'some-hash'))

VALID_BINARY_PATCH = Version('FAForever/binary-patch', 'master')

VALID_GAME_VERSION_INFO = {
    "engine": Version('FAForever/binary-patch', 'master'),
    "game": Mod("faf", TEST_GAME_VERSION),
    "mods": [TEST_SIM_MOD],
    "map": {"name": "scmp_0009", "version": "builtin"}
}

UNTRUSTED_GAME_VERSION = VALID_GAME_VERSION_INFO.copy()
UNTRUSTED_GAME_VERSION["game"] = Mod("faf", Version("fa", "3678", "http://example.com/test.git"))


@pytest.fixture(scope='function')
def version():
    return VALID_GAME_VERSION_INFO.copy()


def test_game_version_can_be_created_from_valid_dict():
    assert GameVersion(VALID_GAME_VERSION_INFO).is_valid


def test_game_version_requires_valid_binary_patch_version(version):
    version.pop('engine')
    assert not GameVersion(version).is_valid
    version['engine'] = {"a": "b"}
    assert not GameVersion(version).is_valid


def test_game_version_requires_valid_featured_mods(version):
    version.pop('game')
    assert not GameVersion(version).is_valid
    version['game'] = []
    assert not GameVersion(version).is_valid


def test_game_version_requires_existing_featured_mods(version):
    version['game'] = Mod("non-existing-featured-mod", Version('example', 'example'))
    assert not GameVersion(version).is_valid


def test_game_version_is_unstable_iff_contains_unstable_pointer(version):
    assert not GameVersion(version).is_stable


def test_game_version_with_stable_pointers_is_stable(version):
    version['engine'] = Version('FAForever/binary-patch', 'master', None, 'a41659780460fd8829fce87b479beaa8ac78e474')
    assert GameVersion(version).is_stable


def test_game_version_is_trusted_iff_all_repos_are_trusted(version):
    assert GameVersion(version).is_trusted


def test_game_version_untrusted_urls(version):
    assert GameVersion(UNTRUSTED_GAME_VERSION).untrusted_urls == ["http://example.com/test.git"]

