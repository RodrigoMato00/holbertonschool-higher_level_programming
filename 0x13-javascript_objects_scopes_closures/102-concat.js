#!/usr/bin/node
const ftw = require('fs');
ftw.writeFileSync(process.argv[4], ftw.readFileSync(process.argv[2], 'utf8') + ftw.readFileSync(process.argv[3], 'utf8'));
