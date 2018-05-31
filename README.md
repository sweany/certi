# certi

## x509 certificate inventory tool

A tool to catalog x509 certificates. I am so tired of typing `echo | openssl s_client -connect host:port | openssl x509 -text -noout`.

Lofty goals for functionality:

* single connect mode
* scanning mode
* sniffing mode
* file mode
* directory mode


