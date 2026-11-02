const fs = require('fs');
const data = JSON.parse(fs.readFileSync('c:/Users/pc/Desktop/menu/menu_data_default_1.json', 'utf8'));

// Read viewer.html and extract the <script> block
const html = fs.readFileSync('c:/Users/pc/Desktop/menu/viewer.html', 'utf8');
console.log('Read viewer.html, length:', html.length);

