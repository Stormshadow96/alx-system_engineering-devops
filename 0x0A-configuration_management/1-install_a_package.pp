# A manifest to istall flask v2.1.0 on puppet-agent
package { 'flask':
  ensure   => '2.1.0',
  provider =>  pip3,
}

