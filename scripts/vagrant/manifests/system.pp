
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
            "build-essential",
            "python-pip",
            "python-dev"
        ]:
            ensure  => "present",
            require => Exec["apt-update"];
    }

    file {
        "/home/vagrant/.bash_profile":
            ensure  => present,
            source => "/vagrant/files/bash_profile";
    }

}
