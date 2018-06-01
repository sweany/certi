# certi

## x509 certificate inventory tool

A tool to catalog x509 certificates. I am so tired of typing `echo | openssl s_client -connect host:port | openssl x509 -text -noout`.

Lofty goals for functionality:

* single connect mode
* scanning mode
* sniffing mode
* file mode
* directory mode
* logging to syslog
* storing certificate details in sqlite db
* reporting on stored certs


## Example

Single connect mode output.

```
$ ./certi google.com
-----BEGIN CERTIFICATE-----
MIIISjCCBzKgAwIBAgIIBnpXTgVozHowDQYJKoZIhvcNAQELBQAwVDELMAkGA1UE
BhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczElMCMGA1UEAxMc
R29vZ2xlIEludGVybmV0IEF1dGhvcml0eSBHMzAeFw0xODA1MTUyMTAyMDhaFw0x
ODA4MDcxOTUzMDBaMGYxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlh
MRYwFAYDVQQHDA1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKDApHb29nbGUgTExDMRUw
EwYDVQQDDAwqLmdvb2dsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQC6aPoxoMT6WSGiYoTeEHWZoFT7G8OctN9A+CKsnU3eKpBtJglCim2KuvQk
HXrmPqJIz9IPoJd7Q5Ep1dwWl8z5Yp35B1hqwalJyK9NZBquf9kpv9k8cgoJKmS/
trpkrHZWAz32iqLF5+A3V42HPDVGUvdbdNxZjrKgnTuzfF53irah756EKnmHNg5c
aHUv6zG7nHxuZETyQ1qv3OoDx2XzzUSQ7pkdLGpMUFvYoYQa6r3UE88DByrTFgmE
GtR/48S7XxT65Ho6lTEPK7T265I+tcsWCyRYZeNdKq85Zbb1BoYB0eopVfhsQp5K
gft33wP9NOUje+ZDlwdlJtDjv8itAgMBAAGjggUMMIIFCDATBgNVHSUEDDAKBggr
BgEFBQcDATCCA+EGA1UdEQSCA9gwggPUggwqLmdvb2dsZS5jb22CDSouYW5kcm9p
ZC5jb22CFiouYXBwZW5naW5lLmdvb2dsZS5jb22CEiouY2xvdWQuZ29vZ2xlLmNv
bYIUKi5kYjgzMzk1My5nb29nbGUuY26CBiouZy5jb4IOKi5nY3AuZ3Z0Mi5jb22C
FiouZ29vZ2xlLWFuYWx5dGljcy5jb22CCyouZ29vZ2xlLmNhggsqLmdvb2dsZS5j
bIIOKi5nb29nbGUuY28uaW6CDiouZ29vZ2xlLmNvLmpwgg4qLmdvb2dsZS5jby51
a4IPKi5nb29nbGUuY29tLmFygg8qLmdvb2dsZS5jb20uYXWCDyouZ29vZ2xlLmNv
bS5icoIPKi5nb29nbGUuY29tLmNvgg8qLmdvb2dsZS5jb20ubXiCDyouZ29vZ2xl
LmNvbS50coIPKi5nb29nbGUuY29tLnZuggsqLmdvb2dsZS5kZYILKi5nb29nbGUu
ZXOCCyouZ29vZ2xlLmZyggsqLmdvb2dsZS5odYILKi5nb29nbGUuaXSCCyouZ29v
Z2xlLm5sggsqLmdvb2dsZS5wbIILKi5nb29nbGUucHSCEiouZ29vZ2xlYWRhcGlz
LmNvbYIPKi5nb29nbGVhcGlzLmNughQqLmdvb2dsZWNvbW1lcmNlLmNvbYIRKi5n
b29nbGV2aWRlby5jb22CDCouZ3N0YXRpYy5jboINKi5nc3RhdGljLmNvbYIKKi5n
dnQxLmNvbYIKKi5ndnQyLmNvbYIUKi5tZXRyaWMuZ3N0YXRpYy5jb22CDCoudXJj
aGluLmNvbYIQKi51cmwuZ29vZ2xlLmNvbYIWKi55b3V0dWJlLW5vY29va2llLmNv
bYINKi55b3V0dWJlLmNvbYIWKi55b3V0dWJlZWR1Y2F0aW9uLmNvbYIHKi55dC5i
ZYILKi55dGltZy5jb22CGmFuZHJvaWQuY2xpZW50cy5nb29nbGUuY29tggthbmRy
b2lkLmNvbYIbZGV2ZWxvcGVyLmFuZHJvaWQuZ29vZ2xlLmNughxkZXZlbG9wZXJz
LmFuZHJvaWQuZ29vZ2xlLmNuggRnLmNvggZnb28uZ2yCFGdvb2dsZS1hbmFseXRp
Y3MuY29tggpnb29nbGUuY29tghJnb29nbGVjb21tZXJjZS5jb22CGHNvdXJjZS5h
bmRyb2lkLmdvb2dsZS5jboIKdXJjaGluLmNvbYIKd3d3Lmdvby5nbIIIeW91dHUu
YmWCC3lvdXR1YmUuY29tghR5b3V0dWJlZWR1Y2F0aW9uLmNvbYIFeXQuYmUwaAYI
KwYBBQUHAQEEXDBaMC0GCCsGAQUFBzAChiFodHRwOi8vcGtpLmdvb2cvZ3NyMi9H
VFNHSUFHMy5jcnQwKQYIKwYBBQUHMAGGHWh0dHA6Ly9vY3NwLnBraS5nb29nL0dU
U0dJQUczMB0GA1UdDgQWBBT9ofZPfn4qIvG4Ut7yMzzW++uOiDAMBgNVHRMBAf8E
AjAAMB8GA1UdIwQYMBaAFHfCuFCaZ3Z2sS3ChtCDoH6mfrpLMCEGA1UdIAQaMBgw
DAYKKwYBBAHWeQIFAzAIBgZngQwBAgIwMQYDVR0fBCowKDAmoCSgIoYgaHR0cDov
L2NybC5wa2kuZ29vZy9HVFNHSUFHMy5jcmwwDQYJKoZIhvcNAQELBQADggEBADIM
Utov5beiI6qyrq8/A6u+2QOyaiIqkVfCJuftikTJnwhIRBkWRXoQHyUq/TORuZIp
3SfubVoyz2ZdsqYfqsJQlSlAWhWRb7nk2KVbDncq143t5DZo2dPAaU5WFKbQ1gLR
rrZDidya96rJB5NUlpKAbcBPjkSFt2ID9gcg7yAt6398GAyQ/Q8Qjc0kwoNBwmZX
XC1epP3yVIBFmHf5F6PJfeZIohq6wTTLEIcioM2izHhf0B8XKYYtM89NhSAq6jB1
oO2ZzJdOcZHD6o/We2+gS5RuuOD21BZinIX7uiajtHorJetbcXU/h0uvJvsHUtqi
ojFrRbS2PetQXrm9ZWg=
-----END CERTIFICATE-----

<X509Name object '/C=US/ST=California/L=Mountain View/O=Google LLC/CN=*.google.com'>
<X509Name object '/C=US/O=Google Trust Services/CN=Google Internet Authority G3'>
466781503996087418
b'sha256WithRSAEncryption'
b'20180515210208Z'
b'20180807195300Z'
b'extendedKeyUsage' TLS Web Server Authentication
b'subjectAltName' DNS:*.google.com, DNS:*.android.com, DNS:*.appengine.google.com, DNS:*.cloud.google.com, DNS:*.db833953.google.cn, DNS:*.g.co, DNS:*.gcp.gvt2.com, DNS:*.google-analytics.com, DNS:*.google.ca, DNS:*.google.cl, DNS:*.google.co.in, DNS:*.google.co.jp, DNS:*.google.co.uk, DNS:*.google.com.ar, DNS:*.google.com.au, DNS:*.google.com.br, DNS:*.google.com.co, DNS:*.google.com.mx, DNS:*.google.com.tr, DNS:*.google.com.vn, DNS:*.google.de, DNS:*.google.es, DNS:*.google.fr, DNS:*.google.hu, DNS:*.google.it, DNS:*.google.nl, DNS:*.google.pl, DNS:*.google.pt, DNS:*.googleadapis.com, DNS:*.googleapis.cn, DNS:*.googlecommerce.com, DNS:*.googlevideo.com, DNS:*.gstatic.cn, DNS:*.gstatic.com, DNS:*.gvt1.com, DNS:*.gvt2.com, DNS:*.metric.gstatic.com, DNS:*.urchin.com, DNS:*.url.google.com, DNS:*.youtube-nocookie.com, DNS:*.youtube.com, DNS:*.youtubeeducation.com, DNS:*.yt.be, DNS:*.ytimg.com, DNS:android.clients.google.com, DNS:android.com, DNS:developer.android.google.cn, DNS:developers.android.google.cn, DNS:g.co, DNS:goo.gl, DNS:google-analytics.com, DNS:google.com, DNS:googlecommerce.com, DNS:source.android.google.cn, DNS:urchin.com, DNS:www.goo.gl, DNS:youtu.be, DNS:youtube.com, DNS:youtubeeducation.com, DNS:yt.be
b'authorityInfoAccess' CA Issuers - URI:http://pki.goog/gsr2/GTSGIAG3.crt
OCSP - URI:http://ocsp.pki.goog/GTSGIAG3

b'subjectKeyIdentifier' FD:A1:F6:4F:7E:7E:2A:22:F1:B8:52:DE:F2:33:3C:D6:FB:EB:8E:88
b'basicConstraints' CA:FALSE
b'authorityKeyIdentifier' keyid:77:C2:B8:50:9A:67:76:76:B1:2D:C2:86:D0:83:A0:7E:A6:7E:BA:4B

b'certificatePolicies' Policy: 1.3.6.1.4.1.11129.2.5.3
Policy: 2.23.140.1.2.2
```


