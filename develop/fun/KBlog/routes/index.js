// exports.index = function (req, res) {
//     res.render('index', { title: "Express"})
// };

module.exports = function (app) {
    app.get('/', function (req, res) {
        res.render('index', { title: "Hello", test: ["hello", "world"]});
    });
};