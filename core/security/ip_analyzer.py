from collections import defaultdict, deque
from datetime import datetime, timedelta

ACCESS_LOG = defaultdict(lambda: deque(maxlen=1000))
BANNED_IPS = set()

WINDOW_SECONDS = 60
THRESHOLD = 20
DECAY_MINUTES = 15

def log_ip_access(ip: str):
    if ip in BANNED_IPS:
        return
    now = datetime.utcnow()
    ACCESS_LOG[ip].append(now)

def is_ip_suspicious(ip: str) -> bool:
    if ip in BANNED_IPS:
        return True
    now = datetime.utcnow()
    recent_hits = [t for t in ACCESS_LOG[ip] if now - t <= timedelta(seconds=WINDOW_SECONDS)]
    if len(recent_hits) > THRESHOLD:
        BANNED_IPS.add(ip)
        return True
    return False

def clean_banlist():
    """ Optional: Clean IPs from banlist after DECAY_MINUTES """
    now = datetime.utcnow()
    for ip in list(BANNED_IPS):
        if all(now - t > timedelta(minutes=DECAY_MINUTES) for t in ACCESS_LOG[ip]):
            BANNED_IPS.remove(ip)
