# Simple Tessera Container

A simple Docker container for [Tessera](http://urbanairship.github.io/tessera). Initially inspired by [aalpern/tessera-simple](https://hub.docker.com/r/aalpern/tessera-simple/) but completely reworked afterwards:
* Removed build tools used on build time to compile assets
* Do not load demo dashboards
* Build Tessera from [github.com/urbanairship/tessera](http://github.com/urbanairship/tessera)
* Use fixed revision instead of `master` branch to make builds reproducible.

Starting this container will bind the following ports by default:
* `80` — the Tessera user interface and API

You can get up and running with an existing graphite instance by setting the `GRAPHITE_URL` environment variable when running container:

```
docker run -P -e GRAPHITE_URL=http://graphite.host:port -it aalpern/tessera-simple
```
