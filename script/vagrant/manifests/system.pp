
class system {

    exec {
        "apt-update":
            command => "/usr/bin/apt-get update";
    }

    package {
        [
            "vim",
            "curl",
            "git-core",
            "php5-common",
            "php5-cgi",
            "php5-curl",
            "php5-gd",
            "build-essential",
            "python-pip"
        ]:
            ensure  => "present";
    }

    exec {
        "pip-install":
            command => "/usr/bin/pip install -r /vagrant/requirements.txt",
            require => Package[python-pip];
    }

}
