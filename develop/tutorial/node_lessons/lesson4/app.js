var express = require('express');
var superagent = require('superagent');
var cheerio = require('cheerio');
var eventproxy = require('eventproxy');
var app = express();

app.get('/', function(req, res, next) {
    var cnodeUrl = 'https://cnodejs.org/';
    superagent.get(cnodeUrl)
        .end(function(err, sres) {
            if (err) {
                next(err);
            }
            var topicUrls = [];
           

            var $ = cheerio.load(sres.text);
            $('#topic_list .topic_title').each(function(idx, element) {
                var $element = $(element);
                topicUrls.push(
                  'https://cnodejs.org' + $element.attr('href')
                );
            });

            var ep = eventproxy();

            ep.after('user_html', topicUrls.length, function (users) {
                users = users.map(function (userPair) {
                    var topic = userPair[0];
                    var userHtml = userPair[1];
                    var $ = cheerio.load(userHtml);

                    topic['score'] = $('.big').text();
                    return topic;
                });
                res.set({'content-type': 'application/json; charset=utf-8'});
                res.end(JSON.stringify({ 'final': users }, null, 4));
            } )

            ep.after('topic_html', topicUrls.length, function(topics) {
                topics = topics.map(function (topicPair) {
                    var topicUrl = topicPair[0];
                    var topicHtml = topicPair[1];
                    var $ = cheerio.load(topicHtml);

                    return ({
                      title: $('.topic_full_title').text().trim(),
                      href: topicUrl,
                      comment1: $('.reply_content').eq(0).text().trim(),
                      author: $('.changes').find('span a').text(),
                      author_url: 'https://cnodejs.org/user/' + $('.changes').find('span a').text()
                    });
                });
                console.log(topics);
                topics.forEach(function (topic) {
                    console.log('access ' + topic['author_url']);
                    superagent.get(topic['author_url']).end(function (err, res) {
                        if (err) {
                            next(err);
                        }
                        ep.emit('user_html', [topic, res.text]);
                        // console.log('done');
                    });
                });
                
                // res.set({'content-type': 'application/json; charset=utf-8'});
                // res.end(JSON.stringify({ 'final': topics }, null, 4));


            });

            topicUrls.forEach(function (topicUrl) {
                superagent.get(topicUrl).end(function (err, res) {
                    if (err) {
                        next(err);
                    }
                    ep.emit('topic_html', [topicUrl, res.text]);
                });
            });



            // res.send(topicUrl);
        });
});

app.listen(3000);
