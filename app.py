from flask import Flask, render_template, request, jsonify
import os
import psycopg2

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    DATABASE_URL = 'postgres://qhkjicbidbltki:ff7899d0f2ef26bd2c754f6a7219d94b5c4d58de6073ad2d68d700eedb704473@ec2-44-197-128-108.compute-1.amazonaws.com:5432/d623bc8jc1utqt'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

#     # Execute a command: this creates a new table
#     cur.execute('DROP TABLE IF EXISTS books;')
#     cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
#                                      'title varchar (150) NOT NULL,'
#                                      'author varchar (50) NOT NULL,'
#                                      'pages_num integer NOT NULL,'
#                                      'review text,'
#                                      'date_added date DEFAULT CURRENT_TIMESTAMP);'
#                                      )

#     # Insert data into the table

    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('A Tale of Two Cities',
                 'Charles Dickens',
                 489,
                 'A great classic!')
                )


    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Anna Karenina',
                 'Leo Tolstoy',
                 864,
                 'Another great classic!')
                )
    conn.commit()

    cur.close()
    conn.close()
# Save and close the file.
    return '<h1>heo sahil padhiyar<h1>'

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


if __name__ == '__main__':
    app.run()
