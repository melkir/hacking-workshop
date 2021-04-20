# Security Workshop

This workshop is inspired from [Complete Ethical Hacking Bootcamp 2021: Zero to Mastery](https://www.udemy.com/course/complete-ethical-hacking-bootcamp-zero-to-mastery/).

> Learn Ethical Hacking + Penetration Testing! Use real techniques by black hat hackers then learn to defend against them!

## Requirements

- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Metasploitable](https://github.com/rapid7/metasploitable3)

## Installation

- [Kali Linux VirtualBox 64-Bit (OVA)](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/#1572305786534-030ce714-cc3b)

Double click on the `kali-linux-2021.1-vbox-amd64.ova` file, this should open VirtualBox and create your first virtual machine. You can keep the default options.

- [metasploitable3#quick-start](https://github.com/rapid7/metasploitable3#quick-start)

Follow the quick-start instructions that correspond to your operating system. For simplicity, we'll use the prebuit images.

## Configuration

> VirtualBox

In order to enable the communication between your virtual machines we'll configure a NAT Network.

`Virtual Box` >> `Preferences...` >> `Network` >> `[+] Adds new NAT network` >> `OK`

> Kali Linux

`Kali-Linux-2021.1-vbox-amd64` >> `Settings` >> `Network` >> `Attached to: NAT Network` >> `OK`

Click on the `Show` button, on the login screen enter the following credentials:

```
login: kali
password: kali
```

From a terminal, you can also configure the keyboard to `azerty` if you're using a French keyboard

```sh
$ sudo loadkeys fr
$ sudo dpkg-reconfigure keyboard-configuration
```

Choose the following options:

- Generic 105-key (Intl) PC
- French
- French
- The default for the keyboard layout
- No compose key

To retrieve the IP address of the machine use the following command:

```
$ ip -4 addr
...
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.4/24 brd 10.0.2.255 scope global dynamic
```

> Metasploitable 3

`Metasploitable3-ub1404` >> `Settings` >> `Network` >> `Attached to: NAT Network`

You might also want to increase the display scale factor:

`Settings` >> `Display` >> `Scale Factor: 300%` >> `OK`

Once this is done you can click on the `Show` button

```sh
metasploitable3-ub1404 login: vagrant
password: vagrant
```

You can repeat the steps above in order to configure the keyboard to `azerty` if needed.

As previously, to retrieve the IP address of the machine use the following command:

```
$ ip -4 addr
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global eth0
```

You are ready to take up the challenge, head over to the [Wiki](https://github.com/melkir/hacking-workshop/wiki/1.-Information-Gathering) 💻

**SSH (Optionnal)**

You can configure port-forwarding (only required over NAT Network) in order to access to access remotly to the virtual machine terminal using your host machine.

`Virtual Box` >> `Preferences...` >> `Network` >> `NatNetwork` >> `Port Forwarding`

| Name       | Protocol | Host IP   | Host Port | Guest IP  | Guest Port |
| ---------- | -------- | --------- | --------- | --------- | ---------- |
| SSH Kali   | TCP      | 127.0.0.1 | 2522      | 10.0.2.4  | 22         |
| SSH Ubuntu | TCP      | 127.0.0.1 | 2523      | 10.0.2.15 | 22         |

<br />

Open **Kali Linux** and access to the terminal

```
$ sudo systemctl start ssh.socket
$ sudo systemctl enable ssh.socket
```

Open a terminal of your **HOST** machine:

> Kali Linux

```
$ ssh -p 2522 kali@127.0.0.1
```

> Metasploit

```
$ ssh -p 2523 vagrant@127.0.0.1
```
