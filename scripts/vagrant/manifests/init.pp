
import 'system.pp'

node default {

    include system

    class { 'mysql::bindings::python': }
    class { 'mysql::server':
        config_hash => { 'root_password' => '' }
    }
    mysql::db {
        'db':
            user     => 'db_user',
            password => 'db_pwd',
            host     => 'localhost',
            grant    => ['ALL'];
    }


    class { 'nginx': }
    nginx::resource::vhost { 'www.localdev.com':
        ensure   => present,
        proxy  => 'http://127.0.0.1:8000';
    }

    exec {
        "pip-install":
            command => "/usr/bin/pip install -r /vagrant/requirements.txt",
            require => Package[python-pip, python-mysqldb];
    }

}
