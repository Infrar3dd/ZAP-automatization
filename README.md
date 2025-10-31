# ZAP-automatization

```python
$ python3 ZAP_automatization.py --help                
  usage: ZAP_automatization.py [-h] [-a ADDRESS] [-p PORT]

  ZAP automatization script

  options:
    -h, --help            show this help message and exit
    -a, --address ADDRESS
                          IP-address of the aim
    -p, --port PORT       ZAP port

```

## Example

I will test it on Hacksudo - Thor. The result is in the result.html
```bash
$ ./zap.sh -daemon -host 0.0.0.0 -port 8080 -config api.disablekey=true
$ python3 ZAP_automatization.py -a 192.168.1.41 -p 8080
  The end of scanning: report.html

```
