### 说明
create_rsa.py创建公钥和私钥<br>
public_key.py加密文本<br>
private_key.py解密文本<br>
为了方便使用，创建了一个main.py来管理<br>
因为python2不能直接使用中文，为了兼容python2，所以提示都是用英文<br>
但是因为我英语不好，所以是用百度翻译的<br>
如果有语法错误或者bug，可以提交一个issues<br>
### 用法
create_rsa.py可以用来生成公钥id_rsa_pub.txt和私钥id_rsa.txt<br>
首先输入两个质数p、q，建议使用两个大质数，质数大小影响加密长度<br>
我是加密单个字符的，ascii有128个字符，unicode有65536个字符<br>
想要正确加密解密，p、q的乘积需要大于字符集的数量<br>
加密解密的公式：<br>
c ≡ m ^ e (mod n)<br>
m ≡ c ^ d (mod n)<br>
余数的范围是大于等于0且小于除数，除数n是p、q的乘积<br>
如果n小于128，余数自然小于128，ascii字符集也就不能正确加密解密了，更不用提unicode字符集了<br>
如果p取11，q取13，乘积大于128，就可以正确加密解密ascii字符集了，但对于unicode字符集还是不够<br>
p、q的乘积应大于65536才可以正确加密解密unicode字符集，如257和263<br>
<br>
public_key.py用来加密文本<br>
寻找到公钥id_rsa_pub.txt后，只要输入想要加密的字符串就可以了，然后会生成secret.txt来存放密文<br>
<br>
private_key.py用来解密文本<br>
寻找到私钥id_rsa.txt和密文secret.txt后，就会输出明文了<br>
### 应用
A和B想要建立一个私密的通讯，A创建了自己的公钥A_rsa_pub和私钥A_rsa后，将公钥A_rsa_pub发送给B<br>
B也创建自己的公钥B_rsa_pub私钥B_rsa后，将公钥B_rsa_pub发送给A<br>
这样A向B发送消息时，用B_rsa_pub生成密文后发送给B，B就可以用B_rsa解密了<br>
同样B向A发送消息时，用A_rsa_pub生成密文后发送给A，A就可以用A_rsa解密了<br>
这样，即使被别人获取了B_rsa_pub和密文，没有B_rsa也没法解密<br>
同样的被别人获取了A_rsa_pub和密文，没有A_rsa也没法解密<br>
因为两个大的质数相乘，很难将其因式分解，这也是rsa难以被破解的原因了