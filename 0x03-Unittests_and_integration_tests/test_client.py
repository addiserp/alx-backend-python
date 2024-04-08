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

    def test_public_repos_url(self):
        """
            test_public_repos_url method to unit-test
            GithubOrgClient._public_repos_url.
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock
        ) as mock_property:
            mock_property.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )
