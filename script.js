$(document)
    .ready(function() {
        $.ajax({
            url: 'https://raw.githubusercontent.com/tintinnabulate/intergroup-dashboard/master/output.json',
            method: 'get',
            dataType: 'json',
            success: function(data) {
                var exampleTable = $('#example')
                    .DataTable({
                      data: data,
                      "columns": [
                                   { "data": "code"},
                                   { "data":  "day" },
                                   { "data":  "hearing" },
                                   { "data":  "lat" },
                                   { "data":  "lng" },
                                   { "data":  "postcode" },
                                   { "data":  "time" },
                                   { "data":  "duration" },
                                   { "data":  "title" },
                                   { "data":  "wheelchair" },
                                   { "data":  "covid_open_status" },
                                   { "data":  "detail" },
                                   { "data":  "conference_url" }
                                 ]
					} );
				} });
			} );
