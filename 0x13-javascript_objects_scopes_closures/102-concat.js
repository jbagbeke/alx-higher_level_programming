#!/usr/bin/node

const fs = require('fs');

const content1 = fs.readFileSync(process.argv[2], 'UTF8');
const content2 = fs.readFileSync(process.argv[3], 'UTF8');

const concat = content1 + content2;

fs.writeFileSync(process.argv[4], concat);
