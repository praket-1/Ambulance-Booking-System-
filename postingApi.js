const express = require('express');
const mysql = require('mysql2');

const app = express();
const port = 3000;

app.use(express.json()); // To parse JSON data

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'zxcvbnm',
    database: 'ambu',
});
app.post('/postData', (req, res) => {
    const formData = req.body;

    const sql = 'INSERT INTO users SET';

    db.query(sql, formData, (err) => {
        if (err) {
            console.error('MySQL Error:', err);
            res.status(500).json({ error: 'Internal Server Error' });
        } else {
            res.json({ success: true });
        }
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
