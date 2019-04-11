request = require('request'),
cheerio = require('cheerio');

	request({url: 'https://www.taringa.net/', enconding: 'binary'},function(err, resp, body){
		if(!err && resp.statusCode == 200){
			console.log(body);
			/*var $ = cheerio.load(body);
			$('main').each(function(){
				var titulo = $(this).html();
				console.log(titulo);
			})*/
			
		}

	});