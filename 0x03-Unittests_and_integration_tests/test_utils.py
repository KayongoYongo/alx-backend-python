#!/usr/bin/env python3
"""Unit test for utils"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Unittest.

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """UnitTest
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,\
                        expected_exception_message):
        """_summary_
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJSON

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """UnitTest
        """
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
