from flask import Flask, render_template, request, jsonify
import cloudinary
import cloudinary.uploader
import cloudinary.api

app = Flask(__name__)

# 🚀 Configuración Cloudinary
cloudinary.config( 
  cloud_name = "dmsjguosm", 
  api_key = "221341567895561", 
  api_secret = "Acxisi79tMdlx0H7kRdMPDbwEM0"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    result = cloudinary.uploader.upload(file, folder="capturas")
    return jsonify(result)

@app.route("/list", methods=["GET"])
def list_images():
    resources = cloudinary.api.resources(type="upload", prefix="capturas", max_results=30)
    urls = [res["secure_url"] for res in resources["resources"]]
    return jsonify(urls)

if __name__ == "__main__":
    app.run(debug=True)


