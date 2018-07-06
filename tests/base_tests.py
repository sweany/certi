# -*- coding: utf-8 -*
import unittest
from mock import MagicMock
import ssl
from certi import getcert, cert_print
from io import StringIO
import sys

mock_cert_pem = """
-----BEGIN CERTIFICATE-----
MIIDmTCCAoGgAwIBAgIJAK2Hwgt1SjWFMA0GCSqGSIb3DQEBCwUAMGMxCzAJBgNV
BAYTAlVTMQswCQYDVQQIDAJDQTERMA8GA1UEBwwITm8gUGxhY2UxETAPBgNVBAoM
CE5vIFBsYWNlMQ0wCwYDVQQLDAROb25lMRIwEAYDVQQDDAlsb2NhbGhvc3QwHhcN
MTgwNzA2MjAwMTQzWhcNNDUxMTIxMjAwMTQzWjBjMQswCQYDVQQGEwJVUzELMAkG
A1UECAwCQ0ExETAPBgNVBAcMCE5vIFBsYWNlMREwDwYDVQQKDAhObyBQbGFjZTEN
MAsGA1UECwwETm9uZTESMBAGA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0B
AQEFAAOCAQ8AMIIBCgKCAQEAtznMt9eybOSGzSi0WZrXBQCTIgKvRD5Rco82YIqH
fe/9yffVjsHahq4k+aZg8JfmMVwQrFpapgy+D/zvMN4BYnDAGgqEFSuLgIGpWIxp
zzZ6FX45bjNCrknBC7r+okwX41y+psQg0j1dD3ca3Y4ypvMF7zOiNsf0F5AuarlE
6/VhXaTqd0X4jQ9j4tSKHVSVOI1fgDpgLTggaDdGPWkLo+0SCrtnWT36gDStJvZx
X95BShc6qf2AIbzCcxGRuBN0tN53WVxHyRWseCV+Wj06vsUOkXFYzn7slzJWO7Vt
s1kfUQh9JUMgUq5SUfM5BfIqVHOElBl8W7FwdA+iurOQBQIDAQABo1AwTjAdBgNV
HQ4EFgQUroEZ6zvN6ogzFmWDGRBdUhSfU9QwHwYDVR0jBBgwFoAUroEZ6zvN6ogz
FmWDGRBdUhSfU9QwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAnoDQ
I33q3ya9mqfJp+dktgAZi9u1GP8UlDCCm6KyMjzVFtVa2TRkgaVSouBJdpdCPcnV
rxFcyTpXQoNbiKBVh7693mnkyftRZCV+og/fFjWwJkJCHtlmDrRwmRF3mifYd9oP
m8yCzi67PH1GhUtXgwGV5H/cTLYy+5ZIa+ukOGDgigg/k6l/074QSbsu+wBdKOxy
kafQzaWRCuq7yDMTLHUBsbEwdKjYLOyoXHheCfPy6ZfaHa6MCip41CTrRWcTJdph
ou0Y1Lq5cus+KaJx+RRpy51bZfnxqqatf/Wc+T7kmxZeCcM8Hvr6MhcAw+yGrxzk
OxZ4O3kp+VhksuIg3g==
-----END CERTIFICATE-----
"""

mock_cert = """                 Subject: /C=US/ST=CA/L=No Place/O=No Place/OU=None/CN=localhost/
                  Issuer: /C=US/ST=CA/L=No Place/O=No Place/OU=None/CN=localhost/
           Serial Number: 12504176244885697925
                Key Size: 2048  
     Signature Algorithm: sha256WithRSAEncryption  
         Validity period: 20180706200143Z  20451121200143Z  valid
           SHA256 Digest: EF:73:DF:28:65:52:ED:6F:19:54:9A:20:25:55:D2:24:62:F9:BC:D7:B3:80:37:61:C5:50:87:3B:35:D3:33:7A
             SHA1 Digest: CD:29:99:8F:13:F4:7D:F7:9A:AC:16:25:35:11:E9:C9:C5:B6:15:4C

	No basicConstraints extension

    subjectKeyIdentifier: AE:81:19:EB:3B:CD:EA:88:33:16:65:83:19:10:5D:52:14:9F:53:D4
  authorityKeyIdentifier: keyid:AE:81:19:EB:3B:CD:EA:88:33:16:65:83:19:10:5D:52:14:9F:53:D4


"""

class CertiTests(unittest.TestCase):
    def setUp(self):
        ssl.get_server_certificate = MagicMock(return_value=mock_cert_pem)

    def test_get_cert(self):
        cert = getcert('127.0.0.1', 443)
        self.assertEqual(mock_cert_pem, cert)

    def test_print_cert(self):
        cert = getcert('127.0.0.1', 443)
        out = StringIO()
        sys.stdout = out
        cert_print(cert)
        sys.stdout = sys.__stdout__

        self.assertMultiLineEqual(mock_cert, out.getvalue())

    def tearDown(self):
        pass