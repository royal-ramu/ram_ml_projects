import sys
print(sys.executable)
from flask import Flask, request, render_template
import numpy as np
import pickle
import os

app = Flask(__name__)

#  Load Model 
MODEL_PATH = os.path.join("model", "fertilizer_recom.pkl")

with open(MODEL_PATH, "rb") as f:
    saved = pickle.load(f)

model = saved["model"] #ml model random forest
scaler = saved["scaler"] #scaler during training
soil_encode = saved["soil_encoder"] #label encoder for soil type
crop_encode = saved["crop_encoder"]
fert_encode = saved["fertilizer_encoder"]
# Route

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            #  numeric inputs
            temp = float(request.form["temp"])
            moist = float(request.form["moist"])
            rain = float(request.form["rain"])
            ph = float(request.form["ph"])
            nitro = float(request.form["nitro"])
            phos = float(request.form["phos"])
            pot = float(request.form["pot"])
            car = float(request.form["car"])
            # categorical inputs
            soil = request.form["soi"]
            crop = request.form["cro"]
            # Encode soil and crop
            soil_value = soil_encode.transform([soil])[0]
            crop_value = crop_encode.transform([crop])[0]

            # Prepare feature vector
            x = np.array([[temp, moist, rain, ph,nitro, phos, pot, car,soil_value, crop_value]])
                           
            # Scale and predict
            x_scaled = scaler.transform(x)
            pred = model.predict(x_scaled)[0]

            # Decode fertilizer prediction
            prediction = fert_encode.inverse_transform([pred])[0]

            return render_template("result.html", prediction=prediction)

        except Exception as e:
            error_text = f"Error: {e}"
            return render_template("result.html", prediction=error_text)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
