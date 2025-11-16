# ZAP-automatization

ZAP-automatization project for PSB infromation security school test

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

### ⚠️ Disclaimer ⚠️

This software and proof-of-concept code is provided **for educational and research purposes only**. 

*   The author (infrar3d) is **not responsible** for any misuse or damage caused by this program.
*   **Do not use** against any systems without explicit **prior permission**.
*   Use of this tools for attacking targets without consent is **illegal**.

You are responsible for obeying all applicable laws. **Use ethically and responsibly.**
