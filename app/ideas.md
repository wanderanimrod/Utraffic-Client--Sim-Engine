** Create a web-client facing API that will translate requests for objects' properties into requests for data points
from the data server. So, we can create the API versioned such that a request to
/v1/vehicles/0?fields=acceleration,velocity returns all acceleration and velocity data points for a vehicle with id=0

Ensure javascript opens a persistent connection to the server for fetching the same kind of data through the lifetime
of the simulation (test this)

Try out semantic UI

Here's the link to the js-fiddle with the live d3.js graph http://jsfiddle.net/NbeXY/

Data Series name and unit of measurement should be on the series object. Therefore a line graph should have at least one
series.

We don't have to read data about each translation of a car if the sim is going to be a long one. If we are looking
for aggregates (like average speed), we can sample at fixed intervals. This will reduce on the size of data in redis,
and therefore the memory footprint of the application suite

FUTURE IMPROVEMENTS
--------------------------

** Use [Reverse Ajax / Comet](http://blog.jamieisaacs.com/2010/08/27/comet-with-nginx-and-jquery/) programming to turn
the whole information passing architecture on its head. The simulator pushes state changes to the Sim-Client Engine and
the Sim-Client Engine crunches the data and pushes ready data to the browser-based Visualiser. Interesting!!!
