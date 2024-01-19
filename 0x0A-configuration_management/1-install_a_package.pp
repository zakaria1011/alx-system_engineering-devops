# 1-install_a_package.pp

# Define package resource for Flask with version 2.1.0 and specify Werkzeug version
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'],
}

package { 'Werkzeug':
  ensure   => '2.1.1',  # Specify the version of Werkzeug
  provider => 'pip3',
}

# End of Puppet manifest
