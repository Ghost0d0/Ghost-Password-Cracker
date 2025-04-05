# GhostCracker 🔐

![Banner](https://static.vecteezy.com/system/resources/thumbnails/028/781/942/small_2x/ghost-covered-in-white-cloth-shrouded-in-darkness-ambiguous-symbolism-ai-generated-photo.jpg)

A user-friendly GUI password recovery tool for educational purposes and authorized security testing.

```bash
# Quick Install
git clone https://github.com/yourusername/GhostCracker.git
cd GhostCracker
pip install -r requirements.txt
python main.py
```

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 Hash Detection | Auto-detects MD5, SHA1, SHA256, SHA384, SHA512 |
| 📚 Dictionary Attacks | Supports custom wordlist files |
| 🖥️ Clean Interface | Dark-themed GUI built with CustomTkinter |
| 📊 Progress Tracking | Real-time progress bar |
| ⏱️ Performance Stats | Tracks time taken per attempt |

## 📦 Installation

### For End Users
1. Download the latest release from [Releases page](#)
2. Extract the ZIP file
3. Run `ghost_password_cracker.exe`

### For Developers
```bash
git clone https://github.com/yourusername/GhostCracker.git
cd GhostCracker
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

## 🚀 Usage

1. **Enter Target Hash**  
   Try these test hashes:
   ```
   MD5: 5f4dcc3b5aa765d61d8327deb882cf99 (password: "password")
   SHA256: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 (password: "password")
   ```

2. **Select Wordlist**  
   [Download sample wordlists](#recommended-wordlists)

3. **Start Cracking**  

## 📚 Recommended Wordlists

- [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) (14M common passwords)
- [SecLists](https://github.com/danielmiessler/SecLists) (Comprehensive security testing list)
- [CrackStation](https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm) (1.5B password corpus)

## ⚠️ Legal & Ethical Notice

> **Warning**  
> This tool is for **legal, authorized use only**:
> - Educational purposes
> - Security research with permission
> - Password recovery on owned systems

**By using this software, you agree to:**
1. Not use it for illegal activities
2. Comply with all applicable laws
3. Only test systems you own or have explicit permission to test

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Current Roadmap
- [ ] Add brute-force mode
- [ ] Implement rule-based attacks
- [ ] Support more hash types
- [ ] Improve multi-threading

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

👻 GhostCracker - Because even ghosts leave traces
