Docker image for exporting power and volt for TP-link HS110 power plugs to InfluxDB

Build:  
docker build ./ -t hs110-exporter
Run:  
docker run -d -e DEVICE_IP="HS110_IP" -e INFLUX_IP="INFLUX_DB_IP" -e INFLUX_DB="INFLUX_DB" hs110-exporter

Optional arguments are INFLUX_PORT(defualt 8086) for influxdb port, and SLEEP_TIME(default 30) for how often it should send data.#   h s 1 1 0 - i n f l u x d b - e x p o r t e r  
 