from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import base64

# 密钥
key = b'YzM5ODY3MjEtNTU2MC00YTEw'

# 待加密的明文
plaintext = b'Firewall1!'

# 使用PKCS5填充
padded_plaintext = pad(plaintext, DES3.block_size)

# 创建DES3加密器
cipher = DES3.new(key, DES3.MODE_ECB)

# 加密
ciphertext = cipher.encrypt(padded_plaintext)

# 将加密结果转为base64编码
base64_ciphertext = base64.b64encode(ciphertext).decode('utf-8')

st.write(base64_ciphertext )
