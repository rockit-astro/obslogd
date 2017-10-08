## Warwick common observatory logging code [![Travis CI build status](https://travis-ci.org/warwick-one-metre/obslogd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/obslogd)

Part of the observatory software for the Warwick one-meter telescope.

`obslogd` is a Pyro daemon that exposes commands for reading and writing from the log database.

`obslog` is a utility for writing messages into the log database from the commandline.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

`obslogd` must be enabled after installation using
```
sudo systemctl enable obslogd
sudo systemctl start obslogd
```

The first command enables it to start automatically after a reboot, and the second tells it to start immediately (can be omitted if you plan to reboot).

`obslogd` requires a MySQL/MariaDB database on the same machine.  It will attempt to connect to the `ops` database as user `ops` with no password.
Logs are written to the `obslog` table, which has a schema:

```sql
CREATE TABLE `obslog` (
  `id` int(10) UNSIGNED NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `type` enum('error','warning','info') NOT NULL,
  `source` text NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `obslog`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `obslog`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
```