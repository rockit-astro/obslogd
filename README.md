## Warwick common observatory logging code

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

Next, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9016/tcp --permanent
sudo firewall-cmd --reload
```

`obslogd` requires a MySQL/MariaDB database on the same machine.  See the instructions in the [weather log daemon](https://github.com/warwick-one-metre/weatherlogd) (which runs on the same machine) for the instructions on how to create the database.

Logs are written to the `obslog` table, which should be created using:

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
