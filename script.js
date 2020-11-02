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
                         { "data": "time" },
                         { "data": "title" },
                         { "data": "open_again" },
                         { "data": "conference_url" }
                       ],
            "order": [[ 4, "desc" ]], // sort by open_again
            "pageLength": 100
			} );
});
