// exports.index = function (req, res) {
//     res.render('index', { title: "Express"})
// };

module.exports = function (app) {
    app.get('/', function (req, res) {
        res.render('index', { title: "Home Page"} );
    });

    app.get('/reg', function (req, res) {
        res.render('reg', { title: "Registry" });
    });

    app.get('/login', function (req, res) {
        res.render('login', { title: "Login" });
    });

    app.get('/post', function (req, res) {
        res.render('post', { title: "Post" });
    });

    app.get('/login', function (req, res) {
    });
};