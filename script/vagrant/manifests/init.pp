
import 'system.pp'

node default {

    include system

    class { 'mysql::php': }
    class { 'mysql::python': }
    class { 'mysql::server':
        config_hash => { 'root_password' => '' }
    }
    mysql::db {
        'db':
            user     => 'db_user',
            password => 'db_pwd',
            host     => 'localhost',
            grant    => ['all'],
    }


    class { 'nginx': }
    nginx::resource::vhost { 'www.localdev.com':
        ensure   => present,
        proxy  => 'http://127.0.0.1:8000',
    }

}
