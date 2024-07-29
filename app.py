from flask import Flask, render_template, request, redirect, url_for, flash
import bcrypt  # For password hashing (install with pip)

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Replace with your actual user authentication logic (e.g., database lookup)
        hashed_password_from_db = b"$2b$12$Gzhm5rD123456789abcdefghijklmnopqrstuv"  # Example

        if bcrypt.checkpw(password.encode(), hashed_password_from_db):
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password.", "error")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
