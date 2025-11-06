from flask import Flask, render_template, request, jsonify
import cx_Oracle

app = Flask(__name__)

# --------------------------------------------------
# Home route → Login page
# --------------------------------------------------
@app.route("/")
def home():
    return render_template("login.html")

# --------------------------------------------------
# Signup page route
# --------------------------------------------------
@app.route("/signup")
def signup_page():
    return render_template("signup.html")

# --------------------------------------------------
# Handle signup form submission
# --------------------------------------------------
@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("email")  # using email as username
    password = request.form.get("password")
    email = request.form.get("email")

    try:
        # Connect to Oracle
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
        connection = cx_Oracle.connect(user="prags", password="121", dsn=dsn)
        cursor = connection.cursor()

        # Check if user already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = :1", (username,))
        count, = cursor.fetchone()
        if count > 0:
            cursor.close()
            connection.close()
            return jsonify({"status": "fail", "message": "User already exists!"})

        # Insert new user (no hashing, plain text password)
        cursor.execute(
            "INSERT INTO users (username, password_hash, email) VALUES (:1, :2, :3)",
            (username, password, email)
        )
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"status": "success", "message": "Account created successfully!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# --------------------------------------------------
# Handle login verification
# --------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    try:
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
        connection = cx_Oracle.connect(user="prags", password="121", dsn=dsn)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = :1 AND password_hash = :2",
            (username, password)
        )
        count, = cursor.fetchone()
        cursor.close()
        connection.close()

        if count > 0:
            return jsonify({"status": "success", "message": "Login successful!"})
        else:
            return jsonify({"status": "fail", "message": "Invalid credentials."})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
