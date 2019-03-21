# ysoserial-wrapper

Python wrapper for [ysoserial](https://github.com/frohoff/ysoserial)

A sample for `config.py`:

```python
"""
The below configuration variables will be used in the encryption mechanism.
param: mode can take 0 or 1.
        0 for ECB
        1 for CBC
parma: padmode can take 1 or 2.
        1 for normal padding.
        2 for PCKS5 padding.
"""
ENCRYPTION_CONFIG = {
    'key': 'SecretKey',
    'mode': 0,
    'padmode': 1
}
```