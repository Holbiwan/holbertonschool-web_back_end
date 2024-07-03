#!/usr/bin/env python3
"""Module for testing client """

import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Testing Github Org Client Class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_json):
        """Test Org Method"""
        client = GithubOrgClient(test_org)
        client.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org}"
        )

    def test_public_repos_url(self):
        """Testing Public Repos Url Method"""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value={'repos_url': 'holberton'}
        ) as mock_get:
            test_json = {"repos_url": 'holberton'}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(
                test_return,
                mock_get.return_value.get("repos_url")
            )

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """Testing public repos Method"""
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/"
        ) as mock_pub:
            test_client = GithubOrgClient("holberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Testing has_license method"""
        test_class = GithubOrgClient('test')
        result = test_class.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Testing _public_repos_url method"""
        # Mock the org property to return a known payload
        mock_org.return_value = {"repos_url": "http://example.com/repos"}

        test_class = GithubOrgClient('test')
        url = test_class._public_repos_url
        expected_url = "http://example.com/repos"

        self.assertEqual(url, expected_url)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """testing public repos """

    def test_public_repos_with_license(self):
        """testing public with license"""

if __name__ == '__main__':
    unittest.main()
