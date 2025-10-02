from flask import Flask, render_template, request, jsonify
import cloudinary
import cloudinary.uploader

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

if __name__ == "__main__":
    app.run(debug=True)


