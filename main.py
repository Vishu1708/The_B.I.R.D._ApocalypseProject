from flask import Flask, render_template, request

string_ = ["bird", "birD", "biRd","bIrd","Bird","BirD","BiRd","BIrd","bIrD","bIRd","biRD","bIRD","BiRD","BIrD","BIRd","BIRD"]

""" Encode """
def encode(text, Cypher, key1, Roman="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!@#$%^&*()-_[]{} '\"", length=83):
    encoded = ""
    for letter in text:
        index = Roman.index(letter)
        if index + key1 >= length:
            index = index + key1 - length
        else:
            index = index + key1
        encoded = encoded + Cypher[index]
    return encoded

def decode(text, Cypher, key1, Roman="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!@#$%^&*()-_[]{} '\"", length=83):
    decoded = ""
    for letter in text:
        index = (Cypher.index(letter)) - key1
        decoded = decoded + (Roman[index])
    return decoded

def keys(key):
    [first, second] = key.split("_")
    first = int(first)
    new = second + Roman.split(second)[1] + Roman.split(second)[0]
    while (first > length):
        first = first - length
    return new, first

""" Fixed """
Roman = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!@#$%^&*()-_[]{} '\""
length = len(Roman)
app = Flask(__name__)


@app.route('/')
def first_page() -> 'html':
    return render_template('input_page.html',the_title="Beware, the Spies are everywhere!!")

@app.route('/process', methods=['POST'])
def process_text():
    text = request.form['Text']
    key = request.form['Key']
    action = request.form['Dropdown']
    cypher, key1 = keys(key)
    for strings_ in string_:
        if strings_ in text:
            return render_template('image.html', the_title="I SEE YOU!")
    if action == 'encode':
        result = encode(text, cypher, key1)
    else:
        result = decode(text, cypher, key1)
    return render_template('result.html', the_title="Even the walls have ears", action=action, result=result)

app.run(debug=True, port=5020)