import pyotp

secret = 'mgxinby4glinbo2y5aypdioh7qk2bvnl5zupayw3dk2pdkt66jvq===='
secret_matt= 'zduuebtqqbs5a5cbjmhwq4yuttdisqcawczow5jyaisha25ulyla===='
secret_xinya = 'ppt5ypt4m36sdchjbpnlhv3g6vzuufmfuarn4tclsyt5nujinwgq===='

def get_hotp():
    totp = pyotp.TOTP(secret_matt)
    return totp.now()

print(get_hotp())