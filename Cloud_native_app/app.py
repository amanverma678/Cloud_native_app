import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    message = None
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!!!"
    return render_template("system_monitor.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# f" CPU utilization {cpu_metric} and Memory utilization is {mem_metric}"