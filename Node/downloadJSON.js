var requestify = require('requestify');

var fs = require('fs');
fs.writeFile('./JSON/time-conversion.js', 'var k = [', encoding='utf8', function (err) {
    if (err) throw err;
});

for(var i = 0; i < 900; i+=100) {
requestify.get('https://www.hackerrank.com/rest/contests/master/challenges/time-conversion/leaderboard/filter?offset='+i.toString+'&limit=100&language=cpp14&filter_kinds=language&include_practice=true&_=1475252434304')
  .then(function(response) {
      // Get the response body (JSON parsed or jQuery object for XMLs)
      fs.appendFile('./JSON/time-conversion.js', JSON.stringify(response.getBody())+',', encoding='utf8', function (err) {
    if (err) throw err;
});
//console.log(response.getBody());
  }
);
console.log(i);
}