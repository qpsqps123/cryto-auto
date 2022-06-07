import pyupbit

access = "SdkOvxw5FTVgieJn61xKtPc1BN5YNMhJ9xUl6JeF"          # 본인 값으로 변경
secret = "45zxgciXmZYInG6RqGxr1tEkFP2E3ai8y60V4tOd"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회