## Observatory logging daemon

`obslogd` is a Pyro daemon that exposes commands for writing to the log database.

### Software Setup

`obslogd` must be enabled after installation using
```
sudo systemctl enable --now obslogd
```

Next, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9016/tcp --permanent
sudo firewall-cmd --reload
```

`obslogd` requires a MySQL/MariaDB database on the same machine.  See the instructions in the [weather log daemon](https://github.com/rockit-astro/weatherlogd) (which runs on the same machine) for the instructions on how to create the database.

Logs are written to the `obslog` table, which should be created using:

```sql
CREATE TABLE `obslog` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `type` enum('error','warning','info') NOT NULL,
  `source` text NOT NULL,
  `message` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
