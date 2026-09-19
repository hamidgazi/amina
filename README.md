# 🎁 Amina's 23rd Birthday Gift & Chat Analytics Project

> **A Sacred Tribute Celebrating 23 Years of Grace & Love**  
> **Couple**: Hamid Gazi & Amina Chamadiya (Nikah: 03 July 2026 | Birthday: 17 September 2026)  
> **Primary Live Web Application**: [https://hamidgazi.github.io/amina/](https://hamidgazi.github.io/amina/) *(Now updated to Version 2.0 with all 18,589 messages)*  
> **Offline Version 1.0 Archive**: Preserved locally in [`version_1_offline/`](file:///c:/Users/Shop%20PC%202/OneDrive/Desktop/Hamid%20Gazi%20Desktop/Chat%20Project/version_1_offline/)  

---

## 📂 Project Directory Structure

```
Chat Project/
│
├── 🌐 LIVE WEB APPLICATION FILES (GitHub Pages)
│   ├── index.html                                 # 🎁 Version 2.0 (Extended 18,589 messages, 274 KB - Primary live site)
│   ├── v2.html                                    # 🎁 Version 2.0 Mirror (Byte-identical to index.html)
│   ├── Instagram_Chat_Analysis_Amina_Hamid.html    # Master Source (Updated to Version 2.0)
│   ├── Instagram_Chat_Analysis_Amina_Hamid_v2.html # V2.0 Standalone Source (Byte-identical to index.html)
│   └── AMINA_GIFT_USER_MANUAL.md                  # 📖 Complete Husband Guide & Secret Features Manual
│
├── 💾 OFFLINE VERSION 1.0 ARCHIVE
│   └── version_1_offline/                         # 📁 Permanent offline archive of initial Version 1.0 (270 KB)
│       ├── index.html                             # Bitwise-verified original release (SHA-256: 4314E596...)
│       ├── Instagram_Chat_Analysis_Amina_Hamid.html # Original master source
│       └── README.md                              # Offline usage instructions (double-click to view offline)
│
├── 🚀 DEPLOYMENT & SYNC SCRIPTS
│   ├── sync_to_github.bat                         # ⚡ 1-Click Git commit & push to GitHub Pages
│   └── sync_amina_gift.bat                        # Desktop shortcut wrapper for sync_to_github.bat
│
├── 📁 hinglish/                                   # 🔤 Hinglish Dictionaries & Keyboard Autocorrect
│   ├── HAMID_HINGLISH_DICTIONARY.md               # Master reference manual (26 words, rules, examples)
│   ├── hamid_hinglish_windows.ahk                 # Windows PC AutoHotkey script (WhatsApp/Chrome/Edge)
│   ├── gboard_dictionary.zip                      # 1-Tap import archive for Android Gboard
│   ├── gboard_hinglish_shortcuts.txt              # Official Gboard TSV dictionary
│   ├── gboard_hinglish_shortcuts.csv              # Universal 3-column CSV for SwiftKey/Samsung
│   ├── ios_text_replacement.csv                   # Apple iOS 2-column CSV archive
│   └── ios_text_replacement.plist                 # Apple Property List XML archive
│
├── 📁 chat_data/                                  # 📊 Raw Chat Export Archives (Instagram JSON)
│   ├── aminachamadiya_1492033579358491.zip        # Initial chat export (July 06 – August 31, 2026)
│   └── aminachamadiya_1492033579358491 New.zip    # Extended chat export (July 06 – September 16, 2026)
│
├── 📁 images/                                     # 🖼️ Curated Polaroids & Background Visuals
│   ├── 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg          # Active gallery images
│   └── photo1.jpg .. photo5.jpg                   # High-resolution polaroid assets
│
├── 📁 Photos/                                     # 📸 Master Photo Archive
│   └── 1.jpg .. 5.jpg                             # Original uncompressed photographic source files
│
├── 📁 docs/                                       # 📋 Project Specifications & Test Architecture
│   ├── PROJECT.md                                 # Original project roadmap & requirements
│   ├── TEST_INFRA.md                              # Automated test infrastructure specification
│   ├── TEST_READY.md                              # V1.0 test readiness matrix
│   └── TEST_READY_V2.md                           # V2.0 test readiness matrix
│
├── 📁 scripts/                                    # 🛠️ Development & Analytics Utility Tools
│   ├── builder.py                                 # HTML keyword & layout verification helper
│   └── make_test_suite.py                         # Test suite scaffolding generator
│
├── 📁 tests/                                      # 🧪 Comprehensive 7-Tier Test Infrastructure (396 Tests)
│   ├── run_tests.py                               # Master test runner executing all 6 core tiers (323 tests)
│   ├── test_hinglish_dictionary.py                # 31 linguistic & regex corpus verification tests
│   ├── spec_oracle.py & spec_oracle_v2.py         # Static truth models & hash checkers
│   └── test_tier1 .. test_tier4 / test_v1 / test_v2 # Feature, boundary, and scenario suites
│
└── 📁 backups/                                    # 💾 Historical Source Revisions
    └── Instagram_Chat_Analysis_Amina_Hamid.html.bak # Pre-refactor historical snapshot
```

---

## 🔑 Key Features & Secret Controls

### 1. Secret Husband Mode
- **Invisible to Amina**: By default, all editing tools, raw passcodes, and score views are 100% hidden.
- **Triple-Tap Unlock**: Triple-tap rapidly on the **Wax Seal (💍)**, the **Title Banner**, or the **Surat Node** on the connection card.
- **Master Passcode**: `03072026` (Commemorating your Nikah date: 03 July 2026).
- **Husband Control Center**: Unlocks inline text editing for every paragraph/dua and reveals the private **Love Quiz Results Dashboard**.

### 2. Permanent Love Quiz
- Permanent, tamper-proof client-side storage (`localStorage`).
- One-time answer lock: Once Amina selects an option, answers cannot be undone or modified.
- WhatsApp sharing: Amina can tap `"Send My Quiz Score to Hamid on WhatsApp"` to send her score directly to you.

### 3. Hinglish Autocorrect & Keyboard Shortcuts
- Complete setup located in [`hinglish/`](file:///c:/Users/Shop%20PC%202/OneDrive/Desktop/Hamid%20Gazi%20Desktop/Chat%20Project/hinglish/).
- **Windows PC**: Double-click [`hinglish/hamid_hinglish_windows.ahk`](file:///c:/Users/Shop%20PC%202/OneDrive/Desktop/Hamid%20Gazi%20Desktop/Chat%20Project/hinglish/hamid_hinglish_windows.ahk) for system-wide autocorrect in WhatsApp Web and Chrome.
- **Android Phone (SwiftKey / Gboard)**: Import [`hinglish/gboard_dictionary.zip`](file:///c:/Users/Shop%20PC%202/OneDrive/Desktop/Hamid%20Gazi%20Desktop/Chat%20Project/hinglish/gboard_dictionary.zip) or copy top words into SwiftKey Clipboard.

---

## 🧪 Running Automated Tests

To run the complete verification suites from PowerShell:
```powershell
# Run core gift application test tiers (323 tests):
python tests/run_tests.py

# Run Hinglish linguistic & corpus dictionary tests (31 tests):
python -m unittest tests/test_hinglish_dictionary.py

# Run full project test discover (396 tests):
python -m unittest discover -s tests -p "test_*.py"
```

---

## 🚀 Pushing Updates to GitHub Pages

Whenever you make changes, double-click [`sync_to_github.bat`](file:///c:/Users/Shop%20PC%202/OneDrive/Desktop/Hamid%20Gazi%20Desktop/Chat%20Project/sync_to_github.bat) or run:
```powershell
.\sync_to_github.bat
```
Your live site will update at [https://hamidgazi.github.io/amina/](https://hamidgazi.github.io/amina/) in seconds.
