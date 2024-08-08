# syncthing

Running on wyf9's Serv00 server (#7)

expire: `2034-07-28`

---

## Use

Configure:

- Discover server (`全局发现服务器`):

```url
https://s7.serv00.com:58443/?id=QE7S4FD-WOKL73H-5JVOMHD-XSV2OAB-GLCMSTT-L4GCC73-MJPPSYS-L6HCCQI
```

- Relay server (`协议监听地址`):

```
relay://s7.serv00.com:22067/?id=WBP6NSN-O5HGNDT-B6P2PIV-ET3J5NH-3O7ERQ3-6C36CVI-R4DOAAB-HE5JSA3&networkTimeout=2m0s&pingInterval=1m0s
```

- Discover server:

---

Or keep `default`:

```url
default,https://s7.serv00.com:58443/?id=QE7S4FD-WOKL73H-5JVOMHD-XSV2OAB-GLCMSTT-L4GCC73-MJPPSYS-L6HCCQI
```

- Relay server:

```url
default,relay://s7.serv00.com:22067/?id=WBP6NSN-O5HGNDT-B6P2PIV-ET3J5NH-3O7ERQ3-6C36CVI-R4DOAAB-HE5JSA3&networkTimeout=2m0s&pingInterval=1m0s
```