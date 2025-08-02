############### API KEYS & CREDENTIALS ###############
# Add your API keys and credentials here
# ⚠️ CRITICAL: Replace these with your actual values and keep them secure!
SOLANA_PRIVATE_KEY = 'your_solana_private_key_here_base58_encoded'
BIRDEYE_API_KEY = 'your_birdeye_api_key_here'
SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com'  # Or your preferred RPC endpoint

############### PERFORMANCE & DELAYS ###############
# Optimized delay settings for faster bot performance
API_DELAY = 0.5  # Delay between API calls (reduced from 2s)
ERROR_RETRY_DELAY = 5  # Delay when API errors occur (reduced from 30s)
MAIN_LOOP_DELAY = 10  # Main bot loop delay (reduced from 30s)
WALLET_CHECK_DELAY = 5  # Delay for wallet operations (reduced from 10s)
PORTFOLIO_DISPLAY_DELAY = 3  # Portfolio display delay (reduced from 7s)
TRADING_DELAY = 2  # Delay between trading operations (reduced from 15s)
SOL_BALANCE_RETRY_DELAY = 10  # Delay between SOL balance check retries (reduced from 30s)

### FILE DIRECTORIES ####
# Update these paths to match your project directory
PROJECT_ROOT = '/path/to/your/solana-sniper-bot'  # UPDATE THIS PATH!

CLOSED_POSITIONS_TXT = f'{PROJECT_ROOT}/data/closed_positions.txt'
FILTERED_PRICECHANGE_URLS_CSV = f'{PROJECT_ROOT}/data/filtered_pricechange_with_urls.csv'
FINAL_SORTED_CSV = f'{PROJECT_ROOT}/data/final-sorted.csv'
HYPER_SORTED_CSV = f'{PROJECT_ROOT}/data/hyper-sorted-sol.csv'
NEW_LAUNCHED_CSV = f'{PROJECT_ROOT}/data/new_launches.csv'
READY_TO_BUY_CSV = f'{PROJECT_ROOT}/data/ready_to_buy.csv'
TOKEN_PER_ADDY_CSV = f'{PROJECT_ROOT}/data/token_per_addy.csv'
VIBE_CHECKED_CSV = f'{PROJECT_ROOT}/data/vibe_checked.csv'
FILTERED_WALLET_HOLDINGS = f'{PROJECT_ROOT}/data/filtered_wallet_holdings.csv'
PRE_MCAP_FILTER_CSV = f'{PROJECT_ROOT}/data/pre_mcap_filter.csv'
ALL_NEW_TOKENS = f'{PROJECT_ROOT}/data/all_new_tokens.csv'
PERMANENT_BLACKLIST = f'{PROJECT_ROOT}/data/permanent_blacklist.txt'


# Blacklist reasons that will cause permanent blacklisting
PERMANENT_BLACKLIST_REASONS = [
    'token_2022_program',  # Token uses 2022 program
    'mutable_metadata',    # Token has mutable metadata
    'top_holder_percent',  # Top holders own too much
    'freezable',          # Token can be frozen
    'min_liquidity',      # Below minimum liquidity
    'security_check'      # Failed security check
]

# Minute marks to run token scanning (00, 15, 30, 45)
SCAN_MINUTE_MARKS = [0, 15, 30, 45]

# below are all of the variables we can change in the bot, change them here opposed to in the files
# this bot trades USDC / token on solana 
# keep a little SOL in your wallet to pay for fees and USDC is the trading token

############### main.py configurations ###############

EXIT_ALL_POSITIONS = False # when this is set to true, we are exiting all positions in FULL

# Tokens to never trade (includes SOL, USDC, and known problematic tokens)
DO_NOT_TRADE_LIST = [
    'So11111111111111111111111111111111111111111',  # SOL
    'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',  # USDC
    'cf8CqpDqTy8NURoyiJer7Ri42XyxMuWVirNQ5E6pump',
    'DsfwbGtT2pSFaFTZUe6hwwir2wQvFvXsYahC4uv6T85y',
    'Q1BaFmfN8TXdMVS98RYMhFZWRzVTCp8tUDhqM9CgcAL',
    'HiZZAjSHf8W53QPtWYzj1y9wqhdirg124fiEHFGiUpQh',
    'AuabGXArmR3QwuKxT3jvSViVPscQASkFAvnGDQCE8tfm',
    'rxkExwV2Gay2Bf1so4chsZj7f4MiLKTx45bd9hQy6dK',
    'BmDXugmfBhqKE7S2KVdDnVSNGER5LXhZfPkRmsDfVuov',
    '423scBCY2bzX6YyqwkjCfWN114JY3xvyNNZ1WsWytZbF',
    '7S6i87ZY29bWNbkviR2hyEgRUdojjMzs1fqMSXoe3HHy',
    '8nBNfJsvtVmZXhbyLCBg3ndVW2Zwef7oHuCPjQVbRqfc',
    'FqW3CJYF3TfR49WXRusxqCbJMNSjnay1A51sqP34ZxcB',
    'EwsHNUuAtPc6SHkhMu8sQoyL6R4jnWYUU1ugstHXo5qQ',
    '9Y9yqdNUL76v1ybpkQnVUj35traGEHXTBJB2b1iszFVv',
    'Fd1hzhprThxCwz2tv5rTKyFeVCyEKRHaGqhT7hDh4fsW',
    '83227N9Fq4h1HMNnuKut61beYcB7fsCnRbzuFDCt2rRQ',
    'J1oqg1WphZaiRDTfq7gAXho6K1xLoRMxVvVG5BBva3fh',
    'GEvQuL9DT2UDtuTCCyjxm6KXEc7B5oguTHecPhKad8Dr'
] 

# USDC contract address
USDC_CA = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'

# Your Solana wallet address (public key)
MY_SOLANA_ADDERESS = "your_wallet_address_here"  # PUT YOUR ADDRESS HERE

############### TRADING PARAMETERS ###############
USDC_SIZE = 1  # Position size in USDC per trade
MAX_POSITIONS = 100  # Maximum number of concurrent positions
SELL_AT_MULTIPLE = 49  # Take profit multiplier (49x gain)
STOP_LOSS_PERCENTAGE = -0.6  # Stop loss (-0.6 = down 60%, set to -0.99 to disable)
SELL_AMOUNT_PERCENTAGE = 0.7  # Percentage to sell when taking profit
orders_per_open = 1  # Number of orders per position opening

# Trading execution settings
SLIPPAGE = 499  # Slippage tolerance (499 = 4.99%, 5000 = 50%)
PRIORITY_FEE = 20000  # Priority fee in lamports for faster execution

############### SECURITY & FILTERING ###############
MAX_TOP10_HOLDER_PERCENT = 0.7  # Maximum top 10 holder percentage (if over, reject)
DROP_IF_MUTABLE_METADATA = False  # Drop tokens with mutable metadata
DROP_IF_2022_TOKEN_PROGRAM = True  # Drop Token 2022 program tokens

############### TIMING SETTINGS ###############
# Token scanning time windows (minutes of each hour)
scan_start_min = 10  # Start scanning at minute 10
scan_end_min = 22    # Stop scanning at minute 22

# PnL management time windows (offset from scanning)
pnl_start_min = 40   # Start PnL management at minute 40
pnl_end_min = 58     # Stop PnL management at minute 58

# How many hours back to look for new token launches
HOURS_TO_LOOK_AT_NEW_LAUNCHES = 0.2  # 0.2 hours = 12 minutes

############### TOKEN FILTERING PARAMETERS ###############
MAX_SELL_PERCENTAGE = 70  # Maximum sell percentage for security check
MIN_TRADES_LAST_HOUR = 9  # Minimum trades in last hour
MIN_UNQ_WALLETS2HR = 30   # Minimum unique wallets in 2 hours
MIN_VIEW24H = 15          # Minimum views in 24 hours
MIN_LIQUIDITY = 400       # Minimum liquidity in USD
BASE_URL = "https://api.birdeye.so/v1"  # Birdeye API base URL
MAX_MARKET_CAP = 30000    # Maximum market cap to consider

############### TECHNICAL ANALYSIS SETTINGS ###############
TIMEFRAME = '3m'  # Candlestick timeframe: 1m, 3m, 5m, 15m, 1h, 4h, 1d

# Token age filtering
max_amount_of_bars_before_dropping = 120  # Max bars before dropping (120 * 3m = 6 hours)
# Example: 5m timeframe with 10 bars = 50 minutes max age

# Price trend filtering
only_keep_if_above_avg_close = True  # Only keep if current price > average close

############### ADVANCED SCANNING SETTINGS ###############
get_new_data = True  # Whether to fetch new data
max_market_cap_to_scan_for = 30000    # Maximum market cap to scan
min_market_cap_to_scan_for = 50       # Minimum market cap to scan
number_of_tokens_to_search_through = 50000  # Number of tokens to search through
minimum_24hour_volume_of_tokens = 1000      # Minimum 24h volume requirement

############### SETUP INSTRUCTIONS ###############
"""
SETUP CHECKLIST:
1. Replace SOLANA_PRIVATE_KEY with your actual private key
2. Replace BIRDEYE_API_KEY with your Birdeye API key
3. Replace MY_SOLANA_ADDERESS with your wallet address
4. Update PROJECT_ROOT to your actual project path
5. Ensure you have SOL for gas fees and USDC for trading
6. Create the data/ directory if it doesn't exist
7. Test with small USDC_SIZE values first

SECURITY REMINDERS:
- Never commit your actual config.py to version control
- Keep your private key secure and never share it
- Start with small position sizes for testing
- Monitor your bot's performance regularly
"""
