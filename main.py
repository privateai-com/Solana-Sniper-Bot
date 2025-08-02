from termcolor import colored, cprint
from config import * 
import warnings
warnings.filterwarnings('ignore')
import math, os
import requests
import pandas as pd
import time 
import json
import nice_funcs as n
import schedule
from datetime import datetime 
from get_new_tokens import scan_bot  # Import scan_bot instead of ohlcv_filter



def bot():
    # Get the current time
    now = datetime.now()
    cprint(f'🌙 PrivateAI live bot running at {now}',  'black', 'on_green')

    # checking if need to kill all positions
    while EXIT_ALL_POSITIONS:
        cprint(f'exiting all positions bc EXIT_ALL_POSITIONS is set to {EXIT_ALL_POSITIONS}', 'white', 'on_magenta')
        n.close_all_positions()
        open_positions_df = n.fetch_wallet_holdings_og(MY_SOLANA_ADDERESS)

    time.sleep(1)
    # PNL CLOSE FIRST
    open_positions_df = n.fetch_wallet_holdings_og(MY_SOLANA_ADDERESS)

    # Check SOL balance with retries
    retry_count = 0
    sol_amount = None
    sol_value = None

    cprint("\n🔍 PrivateAI: Checking SOL Balance", 'white', 'on_blue')
    
    while retry_count < 3 and (sol_amount is None or sol_value is None):
        retry_count += 1
        cprint(f"\n💫 PrivateAI: SOL Balance Check Attempt {retry_count}/3", 'white', 'on_cyan')
        sol_amount, sol_value = n.get_sol_balance(MY_SOLANA_ADDERESS)
        
        if sol_amount is not None:
            cprint(f"✅ SOL Balance: {sol_amount} SOL (${sol_value:.2f})",  'black', 'on_green')
            break
        else:
            cprint(f"⚠️ Attempt {retry_count} failed to get SOL balance", 'white', 'on_red')
            time.sleep(SOL_BALANCE_RETRY_DELAY)

    # If we still don't have SOL balance after retries, exit
    if sol_amount is None:
        cprint("🚨 CRITICAL: Failed to get SOL balance after 3 attempts. Exiting bot...", 'white', 'on_red')
        return  # Exit the bot function gracefully

    # Check if SOL balance is too low
    if float(sol_amount) < 0.005:
        cprint(f"🚨 PrivateAI: SOL BALANCE CRITICAL! Only {sol_amount} SOL remaining", 'white', 'on_red')
        cprint(f"Need at least: 0.005 SOL", 'white', 'on_red')
        cprint(f"Current value: ${sol_value:.2f}", 'white', 'on_red')
        return

    # Print final SOL balance info
    cprint("\n💰 PrivateAI SOL BALANCE INFO:", 'white', 'on_light_blue')
    cprint(f"Amount: {sol_amount} SOL", 'white', 'on_light_blue')


####### 🚨🚨🚨🚨🚨🚨🚨🚨🚨 BELOW SECTION I MARKED OUT CUZ IM HANDLING RISK AND TAKE PROFIT IN COPY BOT

    # open_positions_count = open_positions_df.shape[0]
    # winning_positions_df = open_positions_df[open_positions_df['USD Value'] > SELL_AT_MULTIPLE * USDC_SIZE]

    # for index, row in winning_positions_df.iterrows():
    #     token_mint_address = row['Mint Address']
    #     if token_mint_address not in DO_NOT_TRADE_LIST:
    #         cprint(f'🌙 PrivateAI: Winning Position - Token: {token_mint_address}',  'black', 'on_green')
    #         n.pnl_close(token_mint_address)
    #         #print('i am handling pnl close in copy bot so marked the above out for now..')
    #     cprint('✨ PrivateAI: Done closing winning positions...', 'white', 'on_magenta')

    # sl_size = ((1+STOP_LOSS_PERCENTAGE) * USDC_SIZE)
    # losing_positions_df = open_positions_df[open_positions_df['USD Value'] < sl_size]
    # losing_positions_df = losing_positions_df[losing_positions_df['USD Value'] != 0]
 
    # for index, row in losing_positions_df.iterrows():
    #     token_mint_address = row['Mint Address']
    #     if token_mint_address in DO_NOT_TRADE_LIST:
    #         cprint(f'🚫 PrivateAI: Skipping trade for {token_mint_address} (in DO_NOT_TRADE_LIST)', 'white', 'on_red')
    #         continue
    #     if token_mint_address != USDC_CA:
    #         n.pnl_close(token_mint_address)
           
    # cprint('🌙 PrivateAI: Done closing losing positions.. keep swimming ❤️ 🙏', 'white', 'on_magenta')


####### 🚨🚨🚨🚨🚨🚨🚨🚨🚨 ABOVE SECTION I MARKED OUT CUZ IM HANDLING RISK AND TAKE PROFIT IN COPY BOT

    # Run token scan every time
    cprint(f'🔍 PrivateAI: Running token scan...', 'white', 'on_cyan')
    scan_bot()  # Run the scan_bot from get_new_tokens.py
        
    try:
        df = pd.read_csv(FINAL_SORTED_CSV)
    except Exception as e:
        cprint(f"❌ PrivateAI: Error reading {FINAL_SORTED_CSV}: {str(e)}", 'white', 'on_red')
        return

    # look at closed_positions.txt and if the token is there, then remove that row from the df
    with open(CLOSED_POSITIONS_TXT, 'r') as f:
        closed_positions = [line.strip() for line in f.readlines()]
    df = df[~df['address'].isin(closed_positions)]
    df.to_csv(READY_TO_BUY_CSV, index=False)

    df = n.get_names(df)

# 🍀 THIS IS WHERE THE BUYING STARTS
    for index, row in df.iterrows():
        usdc_holdings = n.get_position(USDC_CA)
        usdc_holdings = float(usdc_holdings)
        token_mint_address = row['address']
        
        if usdc_holdings > USDC_SIZE:
            cprint(f'💰 PrivateAI: USDC Balance {usdc_holdings} > {USDC_SIZE}, opening position...', 'white', 'on_blue')
            cprint(f'📝 Token Address: {token_mint_address}', 'white', 'on_blue')
            n.open_position(token_mint_address)
        else:
            cprint(f'⚠️ PrivateAI: Insufficient USDC ({usdc_holdings}), skipping position', 'white', 'on_red')
    
    time.sleep(5)

bot()
cprint('🌙 PrivateAI: Done with 1st run, now looping...',  'black', 'on_green')

# Schedule bot to run every 120 seconds
schedule.every(600).seconds.do(bot)

while True:
    try:
        schedule.run_pending()
        time.sleep(MAIN_LOOP_DELAY)  # Check schedule every 10 seconds
    except Exception as e:
        cprint('❌ PrivateAI: Connection error!', 'white', 'on_red')
        cprint(str(e), 'white', 'on_red')
        time.sleep(ERROR_RETRY_DELAY)

