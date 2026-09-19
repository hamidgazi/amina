"""Authoritative Specification Reference Oracle for Version 2.0
Amina's 23rd Birthday Gift Web Application
Derived strictly from ORIGINAL_REQUEST.md (## 2026-09-17T11:23:00Z) and PROJECT_V2.md
Dataset: Extended 18,589 messages (July 06 – September 16, 2026)
"""

import hashlib
import math
import os
import re
from datetime import date, datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple

# Target Date & Timezones
BIRTHDAY_TARGET_DATE = date(2026, 9, 17)
IST_TZ = timezone(timedelta(hours=5, minutes=30))

# V1 Baseline Preservation Constants (Preserved in version_1_offline/)
V1_EXPECTED_SIZE = 270487
V1_EXPECTED_SHA256 = "4314E596BA3AC3B0D573DAF7845A08698033A006B63A6AA66ADD137901142D21"
V1_PRIMARY_FILE = os.path.join("version_1_offline", "Instagram_Chat_Analysis_Amina_Hamid.html")
V1_REPLICA_FILE = os.path.join("version_1_offline", "index.html")

# V2 Standalone & Primary Deployment Files
V2_PRIMARY_FILE = "Instagram_Chat_Analysis_Amina_Hamid_v2.html"
V2_REPLICA_FILE = "v2.html"
V2_MAIN_DEPLOYMENT = "index.html"

# Version 2.0 Extended Chat Metrics (Authoritative Ground Truth)
CHAT_METRICS_V2 = {
    'total_messages': 18589,
    'hamid_messages': 9301,
    'hamid_pct': 50.03,  # 50.03496%
    'amina_messages': 9288,
    'amina_pct': 49.97,  # 49.96503%
    'message_difference': 13,
    'total_calendar_days': 73,
    'active_days': 69,
    'offline_travel_days': 4,
    'start_date': '2026-07-06',
    'end_date': '2026-09-16',
    'start_timestamp_ms': 1783276789433,
    'end_timestamp_ms': 1789581944117,
    'first_message': {
        'sender': 'Amina Chamadiya',
        'content': 'Assalam walikum',
        'word': 'suno',
        'time_str': '00:09 AM',
        'date_str': '06 July 2026'
    },
    'text_messages': 18455,
    'total_words': 96358,
    'hamid_words': 57876,
    'amina_words': 38482,
    'total_chars': 461614,
    'hamid_chars': 276135,
    'amina_chars': 185479,
    'avg_words_per_msg': 5.18,
    'hamid_avg_words': 6.22,
    'amina_avg_words': 4.14,
    'photos_sent': 44,
    'hamid_photos': 43,
    'amina_photos': 1,
    'voice_notes': 14,
    'hamid_voice_notes': 14,
    'amina_voice_notes': 0,
    'reels_and_shares': 732,
    'hamid_reels': 504,
    'amina_reels': 228,
    'monthly_progression': {
        'july': {
            'total': 2610,
            'active_days': 23,
            'daily_avg': 113.5,  # 113.48
            'hamid': 1300,
            'amina': 1310
        },
        'august': {
            'total': 10489,
            'active_days': 31,
            'daily_avg': 338.4,  # 338.35
            'hamid': 5281,
            'amina': 5208
        },
        'september': {
            'total': 5490,
            'active_days': 15,
            'daily_avg': 366.0,  # 366.00 (all-time record velocity)
            'hamid': 2720,
            'amina': 2770
        }
    },
    'peak_day': {
        'date': '2026-08-17',
        'day_str': 'Monday, 17 August 2026',
        'total': 857,
        'hamid': 457,
        'amina': 400,
        'peak_hour': 16,
        'peak_hour_str': '04:00 PM – 04:59 PM',
        'peak_hour_msgs': 208
    },
    'midnight_chats': {
        'total': 8730,  # 23:00 - 03:00 IST
        'percentage': 46.96,  # 8730 / 18589
        'hamid_count': 4367,
        'hamid_pct': 50.02,
        'amina_count': 4363,
        'amina_pct': 49.98,
        'peak_hour': 0,
        'peak_hour_str': '00:00 – 01:00',
        'peak_hour_count': 3762
    },
    'reactions': {
        'total': 3368,
        'amina_count': 2604,
        'amina_pct': 77.32,  # 77.3%
        'hamid_count': 764,
        'hamid_pct': 22.68,  # 22.7%
        'queen': 'Amina Chamadiya',
        'top_emojis': {
            '👍': 1569,
            '❤️': 667,
            '😂': 269,
            '😅': 240,
            '😁': 231,
            '😘': 99,
            '😍': 79,
            '🫣': 32,
            '🤭': 30,
            '😤': 27
        }
    },
    'sweet_words': {
        'yaad': 96,
        'love': 48,
        'jaan': 40,
        'pyaar': 39,
        'khayal': 24,
        'baccha': 12,
        'cute': 5,
        'darling': 3,
        'baby': 3,
        'babu': 2,
        'miss_you': 2
    },
    'longest_break': {
        'duration_hours': 47.94,
        'duration_str': '47.94 Hours',
        'start': '2026-07-12T18:37:40+05:30',
        'end': '2026-07-14T18:34:07+05:30',
        'broken_by': 'Amina Chamadiya',
        'message_text': 'Aaj hamari raat ko 1 baje ki flight hai'
    }
}

# Love Quiz 2.0 Contract
LOVE_QUIZ_2_CONTRACT = {
    'total_questions': 5,
    'distribution': ['B', 'D', 'A', 'C', 'B'],
    'correct_indices': [1, 3, 0, 2, 1],
    'questions': [
        {
            'index': 0,
            'topic': 'Icebreaker First Message',
            'question_snippet': 'suno',
            'date': '06 July 2026',
            'time': '00:09 AM',
            'correct_option': 'B',
            'correct_index': 1
        },
        {
            'index': 1,
            'topic': 'Record Peak Chat Day',
            'question_snippet': '857',
            'date': '17 August 2026',
            'day': 'Monday',
            'correct_option': 'D',
            'correct_index': 3
        },
        {
            'index': 2,
            'topic': 'Midnight Peak Hour',
            'question_snippet': '3,762',
            'window': '00:00 – 01:00',
            'correct_option': 'A',
            'correct_index': 0
        },
        {
            'index': 3,
            'topic': 'Reaction Queen & Top Emoji',
            'question_snippet': '👍',
            'count': 1569,
            'total_reactions': 3368,
            'correct_option': 'C',
            'correct_index': 2
        },
        {
            'index': 4,
            'topic': 'Sacred Baat Pakki Milestone',
            'question_snippet': '14 April 2026',
            'correct_option': 'B',
            'correct_index': 1
        }
    ]
}

# Relationship Sacred Milestones (Full 10 Milestones spanning Pre-Nikah to Birthday)
MILESTONES_V2 = [
    {
        'id': 'baat-pakki',
        'name': 'Baat Pakki',
        'date_str': '14 April 2026',
        'caption': 'The blessed day our families united and our beautiful destiny began.'
    },
    {
        'id': 'engagement',
        'name': 'Engagement',
        'date_str': '27 April 2026',
        'caption': 'Two souls, one promise. The sparkle in your eyes lit up my whole universe.'
    },
    {
        'id': 'nikah',
        'name': 'Sacred Nikah',
        'date_str': '03 July 2026',
        'caption': 'Qubool Hai. The most sacred, blessed, and happiest day of our lives.'
    },
    {
        'id': 'hand-hold',
        'name': 'Our First Hand Hold',
        'date_str': '04 July 2026',
        'caption': 'When my fingers interlaced with yours, every racing thought found peace.'
    },
    {
        'id': 'first-chat',
        'name': 'First Chat on Instagram',
        'date_str': '06 July 2026',
        'caption': 'Assalam walikum... suno. The very beginning of our 18,589 whispers.'
    },
    {
        'id': 'peak-day',
        'name': 'All-Time Record Chat Marathon',
        'date_str': '17 August 2026',
        'caption': '857 messages in a single day — pouring our hearts into every second.'
    },
    {
        'id': 'first-hug-kiss-ride',
        'name': 'First Hug, First Kiss & Our First Ride',
        'date_str': '05 September 2026',
        'caption': 'Holding you close, feeling your heartbeat, and that magical ride into the wind.'
    },
    {
        'id': 'first-good-kiss',
        'name': 'First Good Kiss',
        'date_str': '10 September 2026',
        'caption': 'A timeless, perfect moment that took my breath away and sealed my heart to yours.'
    },
    {
        'id': 'birthday-eve',
        'name': "Amina's 23rd Birthday Eve",
        'date_str': '16 September 2026',
        'caption': 'The countdown begins to celebrate the most precious soul Allah Ta\'ala gave me.'
    },
    {
        'id': 'birthday',
        'name': "Amina's 23rd Birthday",
        'date_str': '17 September 2026',
        'caption': 'Happy 23rd Birthday my soulmate, my wife, my forever Jannah partner.'
    }
]

# Husband Mode Contract
HUSBAND_MODE_CONFIG = {
    'passcode': '03072026',
    'triple_tap_timeout_ms': 1500,
    'trigger_selectors': [
        '#wax-seal-btn',
        '#nav-title',
        '#surat-node'
    ],
    'modal_id': 'husband-dashboard-modal',
    'storage_key_quiz': 'amina_quiz_result'
}

# Two Cities One Heart Card Contract
TWO_CITIES_CONFIG = {
    'card_id': 'two-cities-card',
    'surat_title': 'Surat',
    'bhiwandi_title': 'Bhiwandi',
    'distance_km': 280,
    'nikah_date_str': '03 July 2026',
    'heartbeat_btn_id': 'heartbeat-btn'
}

# Photo Lightbox Contract
PHOTO_LIGHTBOX_CONFIG = {
    'modal_id': 'photo-lightbox-modal',
    'total_photos': 5,
    'photo_paths': [
        'images/1.jpg',
        'images/2.jpg',
        'images/3.jpg',
        'images/4.jpg',
        'images/5.jpg'
    ],
    'prev_btn_id': 'lightbox-prev-btn',
    'next_btn_id': 'lightbox-next-btn',
    'counter_id': 'lightbox-counter'
}

# Ambient Petals Contract
AMBIENT_PETALS_CONFIG = {
    'container_id': 'ambient-rose-petals',
    'toggle_id': 'ambient-petals-toggle',
    'icon': '🌸'
}


# ==============================================================================
# VALIDATORS & AUDITORS
# ==============================================================================

class ZeroVersionValidatorV2:
    """Detects prohibited version words and debugging labels in romantic user copy."""
    PROHIBITED_PATTERNS = [
        r'\bv\d+\.\d+(\.\d+)?\b',
        r'\bversion\s+\d+\b',
        r'\bbuild-[a-f0-9]+\b',
        r'\bbuild\s*#\s*\d+\b',
        r'\bcommit\s+[a-f0-9]{7,40}\b',
        r'\bdeveloper\s+mode\b',
        r'\bdebug\s+mode\b',
        r'\(NEW\s*ANALYTICS\)',
        r'\btest_suite\b',
        r'\b(?:React|Vue|Angular|Tailwind|Webpack|Vite)\b',
        r'\b(?:build|release)\s+[\w\.\-]+',
        r'\b(?:alpha|beta|rc\d*)\b'
    ]

    @classmethod
    def scan(cls, text: str) -> List[Tuple[str, str]]:
        violations = []
        for pat in cls.PROHIBITED_PATTERNS:
            matches = re.finditer(pat, text, re.IGNORECASE)
            for m in matches:
                violations.append((pat, m.group(0)))
        return violations


class AudioSilenceValidatorV2:
    """Verifies complete absence of audio elements, players, and audio media."""
    @classmethod
    def audit_silence(cls, html_content: str) -> Tuple[bool, List[str]]:
        violations = []
        # Check for <audio> tags
        audio_tags = re.findall(r'<audio\b[^>]*>', html_content, re.IGNORECASE)
        if audio_tags:
            violations.append(f"Found {len(audio_tags)} <audio> tag(s) in HTML")

        # Check for sound player elements or audio controls
        if re.search(r'<source\b[^>]*type=[\'"]audio/', html_content, re.IGNORECASE):
            violations.append("Found audio <source> tag in HTML")

        if re.search(r'\bcontrols\b[^>]*\baudio\b', html_content, re.IGNORECASE):
            violations.append("Found audio controls in HTML")

        # Check for external audio files (.mp3, .wav, .ogg, .m4a)
        audio_files = re.findall(r'[\'"][^\'"]+\.(?:mp3|wav|ogg|m4a|aac)[\'"]', html_content, re.IGNORECASE)
        if audio_files:
            violations.append(f"Found audio file references: {audio_files}")

        return len(violations) == 0, violations


class IslamicNamingValidatorV2:
    """Ensures exclusive and respectful usage of Allah Ta'ala and absence of abbreviations."""
    @classmethod
    def audit_islamic_naming(cls, text: str) -> Tuple[bool, List[str]]:
        violations = []
        # Check for forbidden abbreviation 'swt' or '(swt)'
        swt_matches = re.findall(r'\bswt\b|\(swt\)', text, re.IGNORECASE)
        if swt_matches:
            violations.append(f"Found forbidden abbreviation 'swt': {swt_matches}")

        # Check for presence of 'Allah Ta\'ala'
        if "Allah Ta'ala" not in text and 'Allah Ta’ala' not in text:
            violations.append("Expected reverent 'Allah Ta'ala' in text")

        return len(violations) == 0, violations


class StandaloneValidatorV2:
    """Verifies that the file is standalone with no broken local script or stylesheet links."""
    @classmethod
    def audit_standalone(cls, html_content: str) -> Tuple[bool, List[str]]:
        violations = []
        # Check for local script tags like <script src="app.js"></script>
        scripts = re.findall(r'<script\b[^>]*src=[\'"]([^\'"]+)[\'"]', html_content, re.IGNORECASE)
        for s in scripts:
            if not s.startswith("http://") and not s.startswith("https://"):
                violations.append(f"Broken local script import: {s}")

        # Check for local style links like <link rel="stylesheet" href="style.css">
        css_links = re.findall(r'<link\b[^>]*rel=[\'"]stylesheet[\'"][^>]*href=[\'"]([^\'"]+)[\'"]', html_content, re.IGNORECASE)
        for c in css_links:
            if not c.startswith("http://") and not c.startswith("https://"):
                violations.append(f"Broken local stylesheet import: {c}")

        return len(violations) == 0, violations


class HTMLAuditorV2:
    """Comprehensive parser and auditor for Version 2.0 HTML documents."""
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content = ""
        self.exists = os.path.exists(file_path)
        if self.exists:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                self.content = f.read()

    def get_sha256(self) -> str:
        if not self.exists:
            return ""
        with open(self.file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest().upper()

    def get_size(self) -> int:
        if not self.exists:
            return 0
        return os.path.getsize(self.file_path)

    def has_element_id(self, elem_id: str) -> bool:
        return bool(re.search(rf'id=[\"\']{re.escape(elem_id)}[\"\']', self.content))

    def has_text(self, snippet: str) -> bool:
        return snippet in self.content

    def has_regex(self, pattern: str, flags: int = 0) -> bool:
        return bool(re.search(pattern, self.content, flags))

    def check_v2_features_status(self) -> Dict[str, bool]:
        """Audit status of key Version 2.0 features."""
        if not self.exists:
            return {}

        return {
            'extended_messages_18589': '18,589' in self.content or '18589' in self.content,
            'partner_balance_50_50': ('9,301' in self.content or '9301' in self.content) and ('9,288' in self.content or '9288' in self.content),
            'monthly_velocity_july': '113.5' in self.content or '2,610' in self.content or '2610' in self.content,
            'monthly_velocity_aug': '338.4' in self.content or '10,489' in self.content or '10489' in self.content,
            'monthly_velocity_sept': '366.0' in self.content or '366' in self.content or '5,490' in self.content,
            'peak_day_aug17': '857' in self.content and ('17 August' in self.content or 'August 17' in self.content),
            'midnight_window_8730': '8,730' in self.content or '8730' in self.content,
            'midnight_peak_hour_3762': '3,762' in self.content or '3762' in self.content,
            'reactions_queen_amina': '2,604' in self.content or '2604' in self.content or 'Reaction Queen' in self.content,
            'reactions_top_thumbs_up': '1,569' in self.content or '1569' in self.content,
            'reactions_top_heart': '667' in self.content,
            'sweet_words_yaad_96': '96' in self.content and 'yaad' in self.content.lower(),
            'sweet_words_love_48': '48' in self.content and 'love' in self.content.lower(),
            'longest_break_47_94h': '47.94' in self.content,
            'two_cities_card': self.has_element_id('two-cities-card') or 'Bhiwandi' in self.content,
            'husband_dashboard_modal': self.has_element_id('husband-dashboard-modal'),
            'husband_passcode_03072026': '03072026' in self.content,
            'permanent_quiz_storage': 'amina_quiz_result' in self.content or 'localStorage' in self.content,
            'whatsapp_sharing': 'wa.me' in self.content,
            'photo_lightbox_modal': self.has_element_id('photo-lightbox-modal') or 'lightbox' in self.content.lower(),
            'ambient_rose_petals': self.has_element_id('ambient-rose-petals') or '🌸' in self.content,
            'zero_audio': AudioSilenceValidatorV2.audit_silence(self.content)[0],
            'strict_allah_taala': IslamicNamingValidatorV2.audit_islamic_naming(self.content)[0],
            'standalone_validity': StandaloneValidatorV2.audit_standalone(self.content)[0]
        }
