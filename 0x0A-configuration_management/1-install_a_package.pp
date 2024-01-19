# File: install_flask.pp

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin',
  refreshonly => true,
}

package { 'python3-pip':
  ensure => present,
  before => Exec['install_flask'],
}
