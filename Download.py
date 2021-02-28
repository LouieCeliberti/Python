from urllib import request

google_stock_url = "https://speed.hetzner.de/100MB.bin"


def dowload_stocker_data(cvs_url):
        response = request.urlopen(cvs_url)
        cvs = response.read()
        cvs_str = str(cvs)
        lines = cvs_str.split("\\n")
        desk_file = r'googlestockdata.bin'
        fx = open(desk_file, "w")
        for line in lines:
            fx.write(line + "\n")
        fx.close()


dowload_stocker_data(google_stock_url)