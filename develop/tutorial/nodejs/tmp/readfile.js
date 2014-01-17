var fs = require("fs");
// fs.readFile('content.txt', 'utf-8', function (err, data) {
//     if (err) {
//         console.log(err);
//     } else{
//         console.log(data);
//     }
// });
var content = fs.readFileSync('content.txt', 'utf-8');
console.log(content);

console.log('end.');
