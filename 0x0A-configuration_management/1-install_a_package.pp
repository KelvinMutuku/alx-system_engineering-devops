exec { 'install_flask':
  command  => '/usr/bin/pip3 install flask==2.1.0',
  creates  => '/usr/local/lib/python3.x/dist-packages/flask',
  provider => 'shell',
}

