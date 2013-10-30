** Create a web-client facing API that will translate requests for objects' properties into requests for data points
from the data server. So, we can create the API versioned such that a request to
/get_data?object=vehicle&id=0&property=acceleration returns all acceleration data points for a vehicle with id=0

Try out semantic UI

Here's the link to the js-fiddle with the live d3.js graph http://jsfiddle.net/NbeXY/

Data Series name and unit of measurement should be on the series object. Therefore a line graph should have at least one
series.

We don't have to read data about each translation of a car if the sim is going to be a long one. If we are looking
for aggregates (like average speed), we can sample at fixed intervals. This will reduce on the size of data in redis,
and therefore the memory footprint of the application suite
