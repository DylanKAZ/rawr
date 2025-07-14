from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text_top_y = request.form.get("text_top_y", "50px")
        text_bottom_y = request.form.get("text_bottom_y", "50px")
        selected_color = request.form.get("selected_color", "black")
    else:
        text_top_y = "50px"
        text_bottom_y = "50px"
        selected_color = "black"

    return render_template(
        "index.html",
        text_top_y=text_top_y,
        text_bottom_y=text_bottom_y,
        selected_color=selected_color
    )

if __name__ == "__main__":
    app.run(debug=True)
