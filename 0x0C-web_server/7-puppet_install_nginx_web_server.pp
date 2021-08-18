# install ngnx whit puppet and configuration
package{ 'nginx':
ensure => installed,
}

file_line{ 'Add redirection':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'listen 80 default_server',
}

file{'/var/www/html/index.html':
content => 'Holberton School'
}

service{'nginx':
ensure  => running,
require => Package['nginx']
}
