import requests
import time
import string
import urllib3

# Hide connection errors and red warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- SETTINGS ---
TOKEN = "YOUR_TOKEN_HERE"
MY_SERVER_ID = "YOUR_SERVER_ID_HERE"
DELAY = 1.0  
# ---------------

HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}

def pull_url(code):
    url = f"https://discord.com/api/v9/guilds/{MY_SERVER_ID}/vanity-url"
    try:
        # verify=False is used to bypass SSL errors
        response = requests.patch(url, headers=HEADERS, json={"code": code}, verify=False)
        
        if response.status_code == 200:
            print(f"SUCCESS! {code} IS NOW OURS!")
            return True
        else:
            # Status codes like 401, 403, 400 are treated as 'banned' or 'no permission'
            print(f"FAILED: {code} could not be taken (Banned or No Permission). Continuing...")
            return False
    except:
        return False

def start_sniper():
    chars = string.ascii_lowercase + string.digits
    combinations = [a + b for a in chars for b in chars]
    
    print(f"--- KUZEY SNIPER 2.0 ACTIVE DISCORD @Z6VB ---")
    
    while True:
        for code in combinations:
            try:
                check_url = f"https://discord.com/api/v9/invites/{code}"
                # verify=False is used to avoid SSL errors
                r = requests.get(check_url, verify=False)
                
                if r.status_code == 404:
                    print(f"AVAILABLE: {code} FOUND! Attempting to pull...")
                    pull_url(code)
                else:
                    print(f"OCCUPIED: {code} is full.")
                
                time.sleep(DELAY)
            except Exception as e:
                # If connection drops, wait 5 seconds and continue without closing
                print(f"Connection error, sleeping and continuing...")
                time.sleep(5)

start_sniper()