var express = require('express');
var superagent = require('superagent');
var cheerio = require('cheerio');
var app = express();

app.get('/', function(req, res, next) {
    superagent.get('https://cnodejs.org/')
        .end(function(err, sres) {
            if (err) {
                next(err);
            }
            var items = [];
            var $ = cheerio.load(sres.text);
            $('#topic_list .topic_title').each(function(idx, element) {
                var $element = $(element);
                items.push({
                  title: $element.attr('title'),
                  href: 'http://cnodejs.org' + $element.attr('href')
                });
            });

            res.send(items);
        });
});

app.listen(3000);
