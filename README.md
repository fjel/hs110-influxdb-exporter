## Docker image for exporting power and volt for TP-link HS110 power plugs to InfluxDB

Build:  
```bash
docker build ./ -t hs110-exporter
```
Run:  
```bash
docker run -d -e DEVICE_IP="HS110_IP" -e INFLUX_IP="INFLUX_DB_IP" -e INFLUX_DB="INFLUX_DB" hs110-exporter
```

Optional arguments are INFLUX_PORT(default 8086) for influxdb port, and SLEEP_TIME(default 30) for how often it should send data.
