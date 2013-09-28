
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
            "python-pip"
        ]:
            ensure  => "present",
            require => Exec["apt-update"];
    }

    file {
        "/home/vagrant/.bash_profile":
            ensure  => present,
            source => "/vagrant/file/.bash_profile";
    }

}
