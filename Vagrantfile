Vagrant.configure(2) do |config|
  config.vm.box = "CumulusCommunity/cumulus-vx"
  config.vm.box_version = "3.2.0"

  config.vm.network :forwarded_port, guest: 22, host: 65022, id: 'ssh'
  config.ssh.port = 65022
end
