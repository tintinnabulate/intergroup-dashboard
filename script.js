$(document)
    .ready(function() {
		$('#example').dataTable( {
        	"ajax": {
            "url": 'https://raw.githubusercontent.com/tintinnabulate/intergroup-dashboard/master/output.json',
            "type": "GET",
            "cache": true,
            "complete":
				function(xhr, status) {
					console.log(xhr.responseText);
                    console.log(status);
				}
            },
            "columns": [
                         { "data": "code"},
                         { "data": "day" },
                         { "data": "hearing" },
                         { "data": "lat" },
                         { "data": "lng" },
                         { "data": "postcode" },
                         { "data": "time" },
                         { "data": "duration" },
                         { "data": "title" },
                         { "data": "wheelchair" },
                         { "data": "covid_open_status" },
                         { "data": "detail" },
                         { "data": "conference_url" }
                       ],
			} );
});
