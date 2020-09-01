provider "postgresql" {
  host            = "127.0.0.1"
  port            = 5432
  database        = "postgres"
  username        = "postgres"
  password        = "postgres"
  sslmode         = "require"
  connect_timeout = 15
}

resource "postgresql_role" "my_role" {
  name     = "user"
  login    = true
  password = "123456"
  superuser = true
}

resource "postgresql_database" "v0_back" {
  name              = "v0_back"
  owner             = "user"
  template          = "template0"
  lc_collate        = "C"
  connection_limit  = -1
  allow_connections = true

  depends_on = [postgresql_role.my_role]
}
