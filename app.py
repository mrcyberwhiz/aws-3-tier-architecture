from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, render_template_string, redirect, url_for
import mysql.connector


app = Flask(__name__)
CORS(app)

# Add your Database connection details in the below three lines
db_config = {
    "host": "threetadb.cpy40aks2h2b.ap-south-1.rds.amazonaws.com",  
    "user": "admin",
    "password": "Admin123#",
    "database": "threetadatabase"
}

@app.route('/login', methods=['GET'])
def login():
    url = "http://backendlb-1940925447.ap-south-1.elb.amazonaws.com/booksawindex.html"
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users LIMIT 1;")  # Adjust query as needed
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return redirect(url)
        else:
            return jsonify({"message": "No users found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)