# ysoserial-wrapper

Python wrapper for [ysoserial](https://github.com/frohoff/ysoserial)

In order to encrypt the payload, set the KEY environment variable to be your encryption key.

```bash
export KEY="SecretEncryptionKey"
python3 ysoserial-wrapper.py -t CommonsCollection6 -c "ping 127.0.0.1"
```
