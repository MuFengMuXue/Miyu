You need to have a PostgreSQL cluster and database already created. The test suite will not do it for you.

The cluster does not need to be on the same machine that\'s running the tests.

Then, create the /etc/libpqxx_test_env file with the following content:

[FILE] **`/etc/libpqxx_test_env`**

    PGUSER="postgres"
    PGDATABASE="libpqxx_test"
    # PGHOST="example.com"
    # PGPORT="2345"

Only PGUSER and PGDATABASE are required.