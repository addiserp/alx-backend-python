#!/usr/bin/env python3
"""
Tests for client.py
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
        a class TestGithubOrgClient that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org, expected_res, mock_function):
        """
            Use @patch as a decorator to make sure get_json is called
            once with the expected argument
        """
        mock_function.return_value = MagicMock(return_value=expected_res)
        google_client = GithubOrgClient(org)
        self.assertEqual(google_client.org(), expected_res)
        mock_function.assert_called_once_with("https://api.github.com/orgs/{}"
                                              .format(org))
