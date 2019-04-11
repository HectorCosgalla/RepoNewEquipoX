var request = require('request');
var scraper = require('facebook-nologin-scraper');
 
request('https://www.facebook.com/zuck',
  {
    headers: {
      'user-agent': 'curl/7.47.0',
      'accept-language': 'en-US,en',
      'accept': '*/*'
    }
  }, function (error, response, body) {
    if (error) {
      throw (error);
    }
    if (response.statusCode === 200) {
      var result = scraper(body);
      console.log(JSON.stringify(result, null, 2));
    } else {
      console.log('HTTP Error: ' + response.statusCode);
    }
});