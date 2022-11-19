"""
kg = blocksmith.KeyGenerator()
kg.seed_input('Truly random string. I rolled a dice and got 4.')
key = kg.generate_key()
print(key)
#key = '7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00'

address = blocksmith.EthereumWallet.generate_address(key)
#print(address)


checksum_address = blocksmith.EthereumWallet.checksum_address(address)
print(checksum_address)
# 0x1269645a46A3e86c1a3C3De8447092D90f6F04ED
"""

    """kg = blocksmith.KeyGenerator()
    kg.seed_input('Truly random string. I rolled a dice and got 4.')
    key = kg.generate_key()
    #print(key)
    address = blocksmith.EthereumWallet.generate_address(key)
    #print(address)"""