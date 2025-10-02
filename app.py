from flask import Flask, render_template, request, jsonify
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

# 🚀 Configuración Cloudinary
cloudinary.config( 
  cloud_name = "TU_CLOUD_NAME", 
  api_key = "TU_API_KEY", 
  api_secret = "TU_API_SECRET"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    result = cloudinary.uploader.upload(file)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


