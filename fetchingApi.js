const express = require('express');
const mysql = require('mysql2');

const app = express();
const port = 5000;

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'zxcvbnm',
    database: 'ambu',
});

app.get('/getData', (req, res) => {
    const sql = 'SELECT * FROM users';

    db.query(sql, (err, result) => {
        if (err) {
            console.error('MySQL Error:', err);
            res.status(500).json({ error: 'Internal Server Error' });
        } else {
            res.json(result);
        }
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://127.0.0.1:5000/users:${port}`);})
