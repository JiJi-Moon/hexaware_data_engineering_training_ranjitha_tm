from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Healthcare Appointment Management Platform"

@app.route("/health")
def health():
    return "Appointment Service Healthy"

@app.route("/appointment-status")
def appointment_status():
    return "Appointment Confirmed"

@app.route("/doctor-availability")
def doctor_availability():
    return "Doctor Available"

if __name__ == "__main__":
    app.run()
