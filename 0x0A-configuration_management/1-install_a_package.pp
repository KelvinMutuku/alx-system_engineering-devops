package { 'flask':
  ensure => '2.1.0',
}

exec { 'install_puppet_lint':
  command => '/usr/bin/apt-get -y install puppet-lint',
}

exec { 'puppet_apply':
  command => 'puppet apply 1-install_a_package.pp',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  require => [Package['flask'], Exec['install_puppet_lint']],
  logoutput => true,
}

exec { 'check_flask_version':
  command => 'flask --version',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  require => Exec['puppet_apply'],
  logoutput => true,
}
