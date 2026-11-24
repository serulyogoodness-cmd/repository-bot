# SIMPLE FOREX BOT FOR DERIV - $1 ACCOUNT
# Strategy: MA 5 crosses MA 20 on EUR/USD

import asyncio
from deriv_api import DerivAPI

API_TOKEN = "PASTE_YOUR_DEMO_TOKEN_HERE" # Get it from Deriv > Account Settings > API Token
APP_ID = 1089
SYMBOL = "frxEURUSD" # EUR/USD on Deriv
STAKE = 0.35
MAX_LOSS = 1.0
MAX_PROFIT = 2.0

balance = 0
prices = []

async def main():
    api = DerivAPI(app_id=APP_ID)
    await api.authorize(API_TOKEN)
    print("Bot Connected!")

    # Get live ticks
    source = await api.subscribe_ticks(SYMBOL)

    async for tick in source:
        price = tick['tick']['quote']
        prices.append(price)
        if len(prices) > 20:
            prices.pop(0)

        if len(prices) == 20:
            fast_ma = sum(prices[-5:]) / 5
            slow_ma = sum(prices) / 20

            print(f"Price: {price} | Fast MA: {fast_ma:.5f} | Slow MA: {slow_ma:.5f}")

            if fast_ma > slow_ma:
                print(">>> SIGNAL: BUY / RISE")
                # Here you would place a Multiplier UP trade
            elif fast_ma < slow_ma:
                print(">>> SIGNAL: SELL / FALL")
                # Here you would place a Multiplier DOWN trade

asyncio.run(main())