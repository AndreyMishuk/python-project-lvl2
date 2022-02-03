#!/usr/bin/env python

from gendiff.scripts.parsers import parser_file2dict


def test_parser_file2dict():
    dict_parser = parser_file2dict('./tests/fixtures/file1.yml')
    assert dict_parser == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }
