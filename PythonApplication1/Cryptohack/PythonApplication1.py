import base64
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
print(base64.b64encode(
    "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"))
key1 = 268011609358571820305085369857896955256986936039734864838603539
key4 = b2l(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))
key4 = key4 ^ key1
key3 = b2l(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"))
key4 = key4 ^ key3
print(base64.b64encode(l2b(key4)))
print(l2b(key4))
