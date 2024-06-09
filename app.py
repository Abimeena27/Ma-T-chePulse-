from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management and flash messages

# Dummy credentials for demonstration purposes
users={
    'Abi': 'aurora$',
    'MD':'@md46',
    'Jeni':'#reach_jeni',
    'rakhana':'Pik@@chuuu*'
}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Basic validation
        if not username or not password:
            flash('Please enter both username and password', 'error')
        elif username in users and users[username]==password:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
