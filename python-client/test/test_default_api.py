"""
    Bundesagentur für Arbeit: Coachingangebote API

    Eine der größten Datenbanken zu Coaching-/Aktivierungsangeboten Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** ee971dcb-96fa-47b3-b2be-00863e4fc88b  **ClientSecret:** 1050e0b7-6db8-49e8-aff9-0e58e556681f  **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.coachingangebote.api.default_api import DefaultApi  # noqa: E501

from deutschland import coachingangebote


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aktivierungsangebote(self):
        """Test case for aktivierungsangebote

        Coaching-/Aktivierungsangebote  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
