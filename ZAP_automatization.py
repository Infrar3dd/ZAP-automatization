from zapv2 import ZAPv2
import time
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ZAP automatization script')
    parser.add_argument('-a','--address', help='IP-address of the aim')
    parser.add_argument('-p','--port', help='ZAP port')
    args = parser.parse_args()

    try:
        zap = ZAPv2(apikey='your-api-key', proxies={'http': 'http://localhost:'+str(args.port)})

        scan_id = zap.spider.scan("http://"+str(args.address))
        while int(zap.spider.status(scan_id)) < 100:
            time.sleep(1) 

        scan_id = zap.ascan.scan("http://"+str(args.address))
        while int(zap.ascan.status(scan_id)) < 100:
            time.sleep(5)

        with open('report.html', 'w') as f:
            f.write(zap.core.htmlreport())

        print("The end of scanning: report.html")
    except:
        print("\nSomething went wrong!!!")
