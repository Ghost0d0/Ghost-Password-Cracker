import hashlib
import time
import os

def detect_hash_type(hash_str):
    hash_str = hash_str.strip().lower()
    length = len(hash_str)
    
    if not all(c in '0123456789abcdef' for c in hash_str):
        return 'Unknown'
    
    return {
        32: 'MD5',
        40: 'SHA1',
        56: 'SHA224',
        64: 'SHA256',
        96: 'SHA384',
        128: 'SHA512'
    }.get(length, 'Unknown')

def get_hash_function(name):
    return {
        'MD5': hashlib.md5,
        'SHA1': hashlib.sha1,
        'SHA224': hashlib.sha224,
        'SHA256': hashlib.sha256,
        'SHA384': hashlib.sha384,
        'SHA512': hashlib.sha512
    }.get(name, hashlib.sha256)

def crack_password(target_hash, hash_type, wordlist_path, progress_callback):
    start_time = time.time()
    target_hash = target_hash.lower()

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        return {"error": f"Error reading wordlist: {str(e)}"}

    total = len(passwords)
    hash_func = get_hash_function(hash_type)
    last_progress = -1

    for idx, pwd in enumerate(passwords, 1):
        try:
            hashed_pwd = hash_func(pwd.encode()).hexdigest()
            if hashed_pwd == target_hash:
                progress_callback(100)
                return {
                    "found": True,
                    "password": pwd,
                    "hash_type": hash_type,
                    "time": round(time.time() - start_time, 2)
                }
        except Exception:
            continue
            
        current_progress = (idx * 100) // total
        if current_progress != last_progress:
            progress_callback(current_progress)
            last_progress = current_progress

    progress_callback(100)
    return {
        "found": False,
        "hash_type": hash_type,
        "time": round(time.time() - start_time, 2)
    }