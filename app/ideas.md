Data Series name and unit of measurement should be on the series object. Therefore a line graph should have at least one
series.

We should add data points to data server (and hence to the graph) in batches and not a data point at time to save on the
look up time for the appropriate graph to add it to

We don't have to read data about each translation of a car if the sim is going to be a long one. If we are looking
for aggregates (like average speed), we can sample at fixed intervals. This will reduce on the size of data in redis
