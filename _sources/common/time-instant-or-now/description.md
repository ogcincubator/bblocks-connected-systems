<!-- generated -->
# TimeInstantOrNow

Time Instant

Converted from [`common/timeInstantOrNow.json`](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/common/timeInstantOrNow.json) in the OGC API - Connected Systems repository.

## Known issues in the source

This block is a faithful copy of the upstream file, which has the following mismatches with the examples of the specification (see `SCHEMA-FIXES.md`):

- Uses `oneOf`: the string `now` also matches the `date-time` branch unless `format` is asserted, so valid instances fail. Possible resolution: `anyOf`.

