Skip to content
 
Search…
All gists
Back to GitHub
@hyperhorus 
@LondonAppDev
LondonAppDev/Vagrantfile Secret
Last active 2 hours ago • Report abuse
18
11
 Code
 Revisions 6
 Stars 18
 Forks 11
<script src="https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682.js"></script>
C1 Vagrantfile
Vagrantfile
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 config.vm.box = "ubuntu/bionic64"
 config.vm.box_version = "~> 20200304.0.0"

 config.vm.network "forwarded_port", guest: 8000, host: 8000

 config.vm.provision "shell", inline: <<-SHELL
   systemctl disable apt-daily.service
   systemctl disable apt-daily.timer
 
   sudo apt-get update
   sudo apt-get install -y python3-venv zip
   touch /home/vagrant/.bash_aliases
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
 SHELL
end
@LondonAppDev
Author
LondonAppDev commented on 3 Nov 2020
Please submit any course-related questions to the Udemy Q&A

This is so we have one central location where all of the knowledge about the course is located (questions asked and answered by students and instructors). This helps us address students’ questions faster and more efficiently - plus it helps students learn from each other.

@petter-jyslabra
petter-jyslabra commented on 22 Jun 2021
When trying to run vagrant init ... the Vagrantfile where not made. I have c-drive with program installed and f:/prosjekt where all my projects is, including profiles-rest-api. What do I miss? I copied the resourcefile, but shouldn't this file be made?
this is what happend:
C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/childprocess-4.0.0/lib/childprocess/windows/process_builder.rb:44:in encode!': "\xC3" to UTF-8 in conversion from ASCII-8BIT to UTF-8 to UTF-16LE (Encoding::UndefinedConversionError) from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/childprocess-4.0.0/lib/childprocess/windows/process_builder.rb:44:in to_wide_string'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/childprocess-4.0.0/lib/childprocess/windows/process_builder.rb:67:in create_environment_pointer' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/childprocess-4.0.0/lib/childprocess/windows/process_builder.rb:28:in start'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/childprocess-4.0.0/lib/childprocess/windows/process.rb:70:in launch_process' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/childprocess-4.0.0/lib/childprocess/abstract_process.rb:81:in start'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/subprocess.rb:155:in block in execute' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/safe_chdir.rb:26:in block (2 levels) in safe_chdir'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/safe_chdir.rb:25:in chdir' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/safe_chdir.rb:25:in block in safe_chdir'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/safe_chdir.rb:24:in synchronize' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/safe_chdir.rb:24:in safe_chdir'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/subprocess.rb:154:in execute' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/subprocess.rb:22:in execute'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/powershell.rb:190:in version' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/powershell.rb:211:in validate_install!'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/powershell.rb:112:in execute_cmd' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/platform.rb:82:in block in windows_admin?'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/util/platform.rb:84:in windows_admin?' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/plugins/providers/hyperv/provider.rb:20:in usable?'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/environment.rb:361:in block in default_provider' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/registry.rb:49:in block in each'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/registry.rb:48:in each' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/registry.rb:48:in each'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/environment.rb:347:in default_provider' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/environment.rb:944:in guess_provider'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/environment.rb:956:in find_configured_plugins' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/environment.rb:984:in process_configured_plugins'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/lib/vagrant/environment.rb:178:in initialize' from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/bin/vagrant:194:in new'
from C:/HashiCorp/Vagrant/embedded/gems/2.2.16/gems/vagrant-2.2.16/bin/vagrant:194:in `

'
@AbdulahadDev1121
AbdulahadDev1121 commented on 1 Oct 2021
what is this vagrant file in Windows?

@namiqi
namiqi commented on 4 Nov 2021
what is this vagrant file in Windows?

same question here

@Clint258
Clint258 commented 4 days ago
C:\Users\Clint Pereira\Desktop\Workspace\profiles-rest-api>vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'ubuntu/bionic64' could not be found. Attempting to find and install...
default: Box Provider: virtualbox
default: Box Version: ~> 20200304.0.0
The box 'ubuntu/bionic64' could not be found or
could not be accessed in the remote catalog. If this is a private
box on HashiCorp's Vagrant Cloud, please verify you're logged in via
vagrant login. Also, please double-check the name. The expanded
URL and error message are shown below:

URL: ["https://vagrantcloud.com/ubuntu/bionic64"]
Error: schannel: next InitializeSecurityContext failed: Unknown error (0x80092012) - The revocation function was unable to check revocation for the certificate.

@hyperhorus
 
Leave a comment
Ninguno archivo selec.
Attach files by dragging & dropping, selecting or pasting them.
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
