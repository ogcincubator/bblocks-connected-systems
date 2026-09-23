<!-- generated -->
# TimeInstantOrNow

Time Instant

Converted from [`common/timeInstantOrNow.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/common/timeInstantOrNow.json) in the OGC API - Connected Systems repository.

## Differences from the source

This block differs from the upstream file (which should be fixed there too):

- Uses `anyOf` instead of `oneOf`: the string `now` also matches the `date-time` branch unless `format` is asserted, which made valid instances fail.

