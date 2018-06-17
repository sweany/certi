# certi

## x509 certificate inventory tool

A tool to catalog x509 certificates. I am so tired of typing `echo | openssl s_client -connect host:port | openssl x509 -text -noout`.

Lofty goals for functionality:

* single connect mode
* scanning mode
* sniffing mode
* file mode
* directory mode
* machine-readable output--json perhaps
* storing certificate details in sqlite db
* listing and searching the stored certs for specific values
* reporting stats on stored certs
* HTML output
* JSON output


## Example

Single connect mode output.

```
$ ./certi host google.com
                 Subject: /C=US/ST=California/L=Mountain View/O=Google LLC/CN=*.google.com/
                  Issuer: /C=US/O=Google Trust Services/CN=Google Internet Authority G3/
           Serial Number: 5075331121231285666
                Key Size: 2048
     Signature Algorithm: sha256WithRSAEncryption
         Validity period: 20180523101658Z  20180815090900Z  valid

        extendedKeyUsage: TLS Web Server Authentication
          subjectAltName: DNS:*.google.com, DNS:*.android.com, DNS:*.appengine.google.com, DNS:*.cloud.google.com, DNS:*.db833953.google.cn, DNS:*.g.co, DNS:*.gcp.gvt2.com, DNS:*.google-analytics.com, DNS:*.google.ca, DNS:*.google.cl, DNS:*.google.co.in, DNS:*.google.co.jp, DNS:*.google.co.uk, DNS:*.google.com.ar, DNS:*.google.com.au, DNS:*.google.com.br, DNS:*.google.com.co, DNS:*.google.com.mx, DNS:*.google.com.tr, DNS:*.google.com.vn, DNS:*.google.de, DNS:*.google.es, DNS:*.google.fr, DNS:*.google.hu, DNS:*.google.it, DNS:*.google.nl, DNS:*.google.pl, DNS:*.google.pt, DNS:*.googleadapis.com, DNS:*.googleapis.cn, DNS:*.googlecommerce.com, DNS:*.googlevideo.com, DNS:*.gstatic.cn, DNS:*.gstatic.com, DNS:*.gvt1.com, DNS:*.gvt2.com, DNS:*.metric.gstatic.com, DNS:*.urchin.com, DNS:*.url.google.com, DNS:*.youtube-nocookie.com, DNS:*.youtube.com, DNS:*.youtubeeducation.com, DNS:*.yt.be, DNS:*.ytimg.com, DNS:android.clients.google.com, DNS:android.com, DNS:developer.android.google.cn, DNS:developers.android.google.cn, DNS:g.co, DNS:goo.gl, DNS:google-analytics.com, DNS:google.com, DNS:googlecommerce.com, DNS:source.android.google.cn, DNS:urchin.com, DNS:www.goo.gl, DNS:youtu.be, DNS:youtube.com, DNS:youtubeeducation.com, DNS:yt.be
     authorityInfoAccess: CA Issuers - URI:http://pki.goog/gsr2/GTSGIAG3.crt
OCSP - URI:http://ocsp.pki.goog/GTSGIAG3

    subjectKeyIdentifier: 8D:E1:DB:93:B7:40:69:F3:B9:21:CE:F1:2A:66:3B:7D:2F:7C:9C:8D
        basicConstraints: CA:FALSE
  authorityKeyIdentifier: keyid:77:C2:B8:50:9A:67:76:76:B1:2D:C2:86:D0:83:A0:7E:A6:7E:BA:4B

     certificatePolicies: Policy: 1.3.6.1.4.1.11129.2.5.3
Policy: 2.23.140.1.2.2
```


Certificate list output
```
$ ./certi list
   1 2018-06-17 06:27:36  google.com:443 ()
        2048 bit  sha256WithRSAEncryption  20180523101658Z => 20180815090900Z  valid
        Subject: /C=US/ST=California/L=Mountain View/O=Google LLC/CN=*.google.com/
        Issuer: /C=US/O=Google Trust Services/CN=Google Internet Authority G3/
        subjectAltName: DNS:*.google.com, DNS:*.android.com, DNS:*.appengine.google.com, DNS:*.cloud.google.com, DNS:*.db833953.google.cn, DNS:*.g.co, DNS:*.gcp.gvt2.com, DNS:*.google-analytics.com, DNS:*.google.ca, DNS:*.google.cl, DNS:*.google.co.in, DNS:*.google.co.jp, DNS:*.google.co.uk, DNS:*.google.com.ar, DNS:*.google.com.au, DNS:*.google.com.br, DNS:*.google.com.co, DNS:*.google.com.mx, DNS:*.google.com.tr, DNS:*.google.com.vn, DNS:*.google.de, DNS:*.google.es, DNS:*.google.fr, DNS:*.google.hu, DNS:*.google.it, DNS:*.google.nl, DNS:*.google.pl, DNS:*.google.pt, DNS:*.googleadapis.com, DNS:*.googleapis.cn, DNS:*.googlecommerce.com, DNS:*.googlevideo.com, DNS:*.gstatic.cn, DNS:*.gstatic.com, DNS:*.gvt1.com, DNS:*.gvt2.com, DNS:*.metric.gstatic.com, DNS:*.urchin.com, DNS:*.url.google.com, DNS:*.youtube-nocookie.com, DNS:*.youtube.com, DNS:*.youtubeeducation.com, DNS:*.yt.be, DNS:*.ytimg.com, DNS:android.clients.google.com, DNS:android.com, DNS:developer.android.google.cn, DNS:developers.android.google.cn, DNS:g.co, DNS:goo.gl, DNS:google-analytics.com, DNS:google.com, DNS:googlecommerce.com, DNS:source.android.google.cn, DNS:urchin.com, DNS:www.goo.gl, DNS:youtu.be, DNS:youtube.com, DNS:youtubeeducation.com, DNS:yt.be

   2 2018-06-17 06:27:48  gmail.com:443 ()
        2048 bit  sha256WithRSAEncryption  20180523100400Z => 20180815090900Z  valid
        Subject: /C=US/ST=California/L=Mountain View/O=Google LLC/CN=mail.google.com/
        Issuer: /C=US/O=Google Trust Services/CN=Google Internet Authority G3/
        subjectAltName: DNS:mail.google.com, DNS:inbox.google.com

   3 2018-06-17 06:28:01  github.com:443 ()
        2048 bit  sha256WithRSAEncryption  20180508000000Z => 20200603120000Z  valid
        Subject: /businessCategory=Private Organization/UNDEF=US/UNDEF=Delaware/serialNumber=5157550/C=US/ST=California/L=San Francisco/O=GitHub, Inc./CN=github.com/
        Issuer: /C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert SHA2 Extended Validation Server CA/
        subjectAltName: DNS:github.com, DNS:www.github.com

   4 2018-06-17 06:28:19  bing.com:443 ()
        2048 bit  sha256WithRSAEncryption  20170720174708Z => 20190710174708Z  valid
        Subject: /CN=www.bing.com/
        Issuer: /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/OU=Microsoft IT/CN=Microsoft IT TLS CA 5/
        subjectAltName: 


4 certificates listed.
```

Stats output

```
$ ./certi stats
4 certificates

===== Key Sizes
    4  2048

===== Signature Algorithms
    4  sha256WithRSAEncryption

===== Issuers
    2  /C=US/O=Google Trust Services/CN=Google Internet Authority G3/
    1  /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/OU=Microsoft IT/CN=Microsoft IT TLS CA 5/
    1  /C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert SHA2 Extended Validation Server CA/

===== Days until expiration
    2  31-60
    2  90+

===== Month of expiration
    2  2018-08
    1  2019-07
    1  2020-06

===== Ports
    4  443
```
