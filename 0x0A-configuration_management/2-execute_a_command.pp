#This code kills a process && works together with the killmenow file which has been provided

exec { 'killmenow':
  command   =>  '/usr/bin/pkill killmenow',
  provider  =>  'shell',
  returns   =>  [0, 1],
}
