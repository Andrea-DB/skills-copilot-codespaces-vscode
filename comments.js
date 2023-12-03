// Create a web server
var http = require('http'),
    fs = require('fs'),
    qs = require('querystring');

// Create the server
var server = http.createServer(function(req, res) {
    // Check the request
    if (req.method === 'POST') {
        // Read the form data
        var body = '';
        req.on('data', function(data) {
            body += data;
        });
        req.on('end', function() {
            // Parse the form data
            var form = qs.parse(body);
            // Read the comments file
            fs.readFile('comments.txt', function(err, data) {
                if (err) throw err;
                var comments = JSON.parse(data);
                // Add the comment to the comments array
                comments.push(form.comment);
                // Write the comments back to the file
                fs.writeFile('comments.txt', JSON.stringify(comments), function(err) {
                    if (err) throw err;
                    // Redirect to the comments page
                    res.writeHead(302, {
                        'Location': 'http://localhost:3000/comments.html'
                    });
                    res.end();
                });
            });
        });
    }
}).listen(3000);