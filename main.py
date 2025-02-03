from flask import Flask, render_template_string, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Gmail Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'harunkirtau@gmail.com'  # Gmail adresinizi yazın
app.config['MAIL_PASSWORD'] = 'wyar qtua pchq khup'  # Google App Password
mail = Mail(app)

# HTML templates
login_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="/login" method="post">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Login</button>
    </form>
    {% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
</body>
</html>
"""

survey_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Survey</title>
</head>
<body>
    <h1>Tanıma Testi</h1>
    <form action="/submit-survey" method="post">
        <h2>1. Beni ne kadar tanıyorsun?</h2>
        <input type="radio" name="question1" value="Sen kimsin" required> Sen kimsin<br>
        <input type="radio" name="question1" value="Eh tanıyorum"> Eh tanıyorum<br>
        <input type="radio" name="question1" value="Orta"> Orta<br>
        <input type="radio" name="question1" value="Seviyorum"> Seviyorum<br>
        <input type="radio" name="question1" value="Aşkımmmm"> Aşkımmmm<br>

        <h2>2. Tanıdığın kadarıyla ?</h2>
        <input type="radio" name="question2" value="Keşke olmasan da gitsen" required> Keşke olmasan da gitsen<br>
        <input type="radio" name="question2" value="Fark etmiyor"> Fark etmiyor<br>
        <input type="radio" name="question2" value="Kral ya iyi çocuksun"> Kal ya iyi çocuksun<br>
        <input type="radio" name="question2" value="Lazımsın"> Lazımsın<br>
        <input type="radio" name="question2" value="Sensiz bir hayat düşünemem"> Sensiz bir hayat düşünemem<br>

        <h2>3. Seni rahatsız eden bir durumum oldu mu ?</h2>
        <input type="radio" name="question3" value="Hayır" required> Hayır<br>
        <input type="radio" name="question3" value="Evet"> Evet<br>

        <button type="submit">Gönder</button>
    </form>
</body>
</html>
"""

success_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Mailini kontrol et!</h1>
</body>
</html>
"""

@app.route('/')
def login_page():
    return render_template_string(login_template)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    if password == '1234':  # Şifrenizi buraya yazın
        return render_template_string(survey_template)
    else:
        flash('Hatalı şifre, tekrar deneyin!')
        return redirect(url_for('login_page'))

@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')

    # E-posta gönderme
    msg = Message('Hatunluk Sonuçları',
                  sender='harunkirtau@gmail.com',  # Gmail adresinizi yazın
                  recipients=['arikpelin@icloud.com'])  # Alıcı adres
    msg.body = f"""
    1. Beni ne kadar seviyorsun? Cevap: {question1}
    2. Hayatında olmamdan ne kadar memnunsun? Cevap: {question2}
    3. Ne kadar kızsan da yanımda mısın? Cevap: {question3}

    Anket sonuçların burada.Belki tatmin eder belki etmez... Herkes kendini en iyi bildiği şekilde yapar sürprizini. Ben bunu biliyorum. 

    """
    mail.send(msg)

    return render_template_string(success_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
