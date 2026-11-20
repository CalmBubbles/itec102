# MODULE 11: FUNCTIONS
# 8: Mini library of babel
# Diff: Hard

# this was a bad idea...

# Just update these

# 0: check
# 1: find
mode = 0
inputText = "2clt69fq9cmjc6j9b4ik6avz33gpvfbyr7ty47z6zn3ph4iantyp46cwf3krsgu8u0ht89jqtk3ro9gk7f1ygj0dp1u0kluswzm03yc2w5nzvjktc9wag1d5c1g78t554tbedd51rgxm0wjtwch3pn6ssuqx4wg40jnvbpmpls6iwm6p3ys8who7eoq5f1l1w30fc4gj8htxtj81wd9vggnuoq8ponw3ziu40j0o769ayfkh4euecsfyyyfeipx5hmbhhov2o8m4bii4suyzm1qvhjo3rsq6193740ibaupiyp2ndp8lh2se2c94k321gtusmqddyhxhks0q4xh2swaizydf4smtt3rfwe9jq9a63u4ldg77d9ntsdjzqvdm1w0ys9yaqttmnf3yv7nrkcdcb3m5eli9cpf3x8qpamtlcof8om7k38zo6kjqsxw3z842ics8zwx0jkk3joqegrcb2gifit6xk0mto94xyyuovns9sda4pfi7zg2a25d72a30rrkh3uptkbch7o3953v1jn6xwrutfjb1rvj8hy9edqc417icw59953p9ac5036sg5qrhtk6f737kcoqm2bzktdvq8qk517zvzhdg3ia4in8vimqvik5fhva6q6s3y3vr0yikog9tl35w02g9uw1759cj3stuxpmviy0uez39od21ycva3p2cbglqba8z53qo5xa4y4zkfwspaigmg1iwh5muexl7e05wz2y8lidk16whxqq7u8w9rrn3680jc1a8718hfm0x44eyaimwzeuqhhzmwmcd5ycz6z0emlmcwk9esq90l6gelb86a7or5yk96l5hk56zn55a9x69equ1mgjl6o2l17j6dftvubga8y9nr9cmw1tmor2m6xhua7xc3hi1t33ypiubcqo07rmwx8ug69t7i59d1t5jr8rr86ikdtzaoxmw7c45co0mtvwz5d8xhnnzkssj7jggrwj6hnrtymgtgto0skihupthmetsvycu52vgdrabn34e0zfmkxqzlio92gq29mtwy8hofj3ze6qzibgpeai2rdw5ft52j87hw4ocr2o17fstwd9jcmx9fh7c2c9a2o738765yu1p6fm1fvab6l9bl2q314vl8thpb2v9im7td0qnwbajozq2qqqle6hohukac284pz7h4uxelu83xzbd9jaopulq1ry90zusbvgb2r7eos9nofyh0bonm6zouzi511rvz7hctkfolivi8127aesmst2wt7oiywn3csbkxed1g6hh9l7u2f2sogyczcc3za4epyqn5zrsj5btg71wflmwo0xhjfynrv03sin1ijrhmf7pgy7iido1tpj86cpj3f2uz729toarqrng8l9k7n9vs0ezysp06cucsd3ncovt5zk1xb63j3w7wkze33vq68ofymxo0lwhh1vwyjpkoo92u9t0vrq41lsu8d6z0p8h7ui06zpkcn2107qs5z051ew7msm0pobd"
# inputText = ""

import random

length = 1600
chars = "abcdefghijklmnopqrstuvwxyz,. "
charsLength = len(chars)
b36 = "0123456789abcdefghijklmnopqrstuvwxyz"

def char2dec (text: str):
    output = 0

    for c in text: output = chars.index(c) + charsLength * output

    return output

def dec2base36 (no: int):
    if no == 0: return "0"

    output = []

    while no > 0:
        no, re = divmod(no, 36)
        output.append(b36[re])

    return "".join(reversed(output))

def find (text: str):
    safeText = text.lower()
    safeText = "".join([c if c in chars else " " for c in safeText])
    safeText = safeText.ljust(length)
    print(safeText)

    return dec2base36(char2dec(safeText))

def placeholdertext (address: str):
    safeAddress = "".join([c for c in address if c in b36])
    safeAddress = safeAddress.lower().ljust(length)

    no = int(safeAddress, 36)
    
    output = []

    for i in range(length):
        no, re = divmod(no, charsLength)
        output.append(chars[re])
    
    return "".join(reversed(output))



if mode == 0: print(placeholdertext(inputText).strip())
else: print(find(inputText).strip())