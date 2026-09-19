"""Authoritative Specification Reference Oracle
Amina's 23rd Birthday Gift Web Application
Derived strictly from ORIGINAL_REQUEST.md and PROJECT.md
"""

import re
import math
import os
from datetime import datetime, date, timezone, timedelta
from typing import Dict, List, Any, Optional, Tuple

BIRTHDAY_TARGET_DATE = date(2026, 9, 17)
IST_TZ = timezone(timedelta(hours=5, minutes=30))

MILESTONES_DATA = [
    {
        'id': 'baat-pakki',
        'order': 1,
        'name': 'Baat Pakki (Relation Fixed)',
        'date_str': '14 April 2026',
        'date': date(2026, 4, 14),
        'iso_datetime': '2026-04-14T00:00:00+05:30',
        'elapsed_days': 156,
        'elapsed_birthday': '5 Months, 3 Days passed',
        'caption': 'The blessed day our families united and our beautiful destiny began.'
    },
    {
        'id': 'engagement',
        'order': 2,
        'name': 'Engagement',
        'date_str': '27 April 2026',
        'date': date(2026, 4, 27),
        'iso_datetime': '2026-04-27T00:00:00+05:30',
        'elapsed_days': 143,
        'elapsed_birthday': '4 Months, 21 Days passed',
        'caption': 'Two souls, one promise. The sparkle in your eyes lit up my whole universe.'
    },
    {
        'id': 'nikah',
        'order': 3,
        'name': 'Nikah',
        'date_str': '03 July 2026',
        'date': date(2026, 7, 3),
        'iso_datetime': '2026-07-03T00:00:00+05:30',
        'elapsed_days': 76,
        'elapsed_birthday': '2 Months, 14 Days passed',
        'caption': 'Qubool Hai. The most sacred, blessed, and happiest day of our lives.'
    },
    {
        'id': 'hand-hold',
        'order': 4,
        'name': 'Our First Hand Hold',
        'date_str': '04 July 2026',
        'date': date(2026, 7, 4),
        'iso_datetime': '2026-07-04T00:00:00+05:30',
        'elapsed_days': 75,
        'elapsed_birthday': '2 Months, 13 Days passed',
        'caption': 'When my fingers interlaced with yours, every racing thought found peace.'
    },
    {
        'id': 'first-hug-kiss-ride',
        'order': 5,
        'name': 'First Hug, First Kiss & Our First Ride',
        'date_str': '05 September 2026',
        'date': date(2026, 9, 5),
        'iso_datetime': '2026-09-05T00:00:00+05:30',
        'elapsed_days': 12,
        'elapsed_birthday': '12 Days passed',
        'caption': 'Holding you close, feeling your heartbeat, and that magical ride into the wind.'
    },
    {
        'id': 'first-good-kiss',
        'order': 6,
        'name': 'First Good Kiss',
        'date_str': '10 September 2026',
        'date': date(2026, 9, 10),
        'iso_datetime': '2026-09-10T00:00:00+05:30',
        'elapsed_days': 7,
        'elapsed_birthday': '7 Days passed',
        'caption': 'A timeless, perfect moment that took my breath away and sealed my heart to yours.'
    }
]

CHAT_METRICS = {
    'total_messages': 12980,
    'hamid_messages': 6561,
    'hamid_pct': 50.55,
    'amina_messages': 6419,
    'amina_pct': 49.45,
    'total_days': 57,
    'longest_streak_days': 57,
    'start_date': '2026-07-06',
    'end_date': '2026-08-31',
    'daily_avg': 227.7,
    'pre_nikah_messages': 0,
    'post_nikah_messages': 12980,
    'july_daily_avg': 100.0,
    'august_daily_avg': 334.5,
    'longest_break': {
        'duration_hours': 47.94,
        'duration_str': '47.94 Hours',
        'start': '2026-07-12T18:37:40+05:30',
        'end': '2026-07-14T18:34:07+05:30',
        'broken_by': 'Amina Chamadiya',
        'message_text': 'Aaj hamari raat ko 1 baje ki flight hai'
    },
    'midnight_chats': {
        'total': 6571,
        'percentage': 50.62,
        'hamid_count': 3306,
        'hamid_pct': 50.3,
        'amina_count': 3265,
        'amina_pct': 49.7,
        'peak_hour': 0,
        'peak_hour_count': 2652
    },
    'sweet_words': {
        'total': 219,
        'yaad': 75,
        'love': 42,
        'pyaar': 41,
        'miss': 18,
        'jaan': 16,
        'dil_heart': 18,
        'sweet_baby_cutie': 9,
        'jaanu': 78,
        'baby_babu': 54,
        'sweetheart': 28,
        'honey': 17
    },
    'reactions': {
        'total': 2187,
        'amina': 1669,
        'hamid': 518,
        'amina_pct': 76.3,
        'hamid_pct': 23.7,
        'ratio': 3.22,
        'reaction_queen': 'Amina Chamadiya',
        'top_reactions': [
            {'emoji': '👍', 'name': 'Thumbs Up', 'count': 1001},
            {'emoji': '❤️{', 'name': 'Red Heart', 'count': 430},
            {'emoji': '😂', 'name': 'Joy Laugh', 'count': 189}
        ]
    },
    'streak': {
        'days': 57,
        'start': '2026-07-06',
        'end': '2026-08-31',
        'unbroken': True
    },
    'peak_day': {
        'date': '2026-08-17',
        'day_name': 'Monday',
        'count': 857
    },
    'first_message': {
        'timestamp': '2026-07-06T00:09:49+05:30',
        'sender': 'Amina Chamadiya',
        'content': 'suno'
    }
}

POLAROIDS_DATA = [
    {
        'id': 1,
        'photo_file': 'images/photo1.jpg',
        'milestone_id': 'baat-pakki',
        'title': 'Baat Pakki (Relation Fixed)',
        'date_str': '14 April 2026',
        'caption': 'The blessed day our families united and our beautiful destiny began.',
        'rotation': '-2.5deg'
    },
    {
        'id': 2,
        'photo_file': 'images/photo2.jpg',
        'milestone_id': 'engagement',
        'title': 'Engagement Celebration',
        'date_str': '27 April 2026',
        'caption': 'Two souls, one promise. The sparkle in your eyes lit up my whole universe.',
        'rotation': '2.0deg'
    },
    {
        'id': 3,
        'photo_file': 'images/photo3.jpg',
        'milestone_id': 'nikah',
        'title': 'Our Sacred Nikah',
        'date_str': '03 July 2026',
        'caption': 'Qubool Hai. The most sacred, blessed, and happiest day of our lives.',
        'rotation': '-1.8deg'
    },
    {
        'id': 4,
        'photo_file': 'images/photo4.jpg',
        'milestone_id': 'hand-hold',
        'title': 'Our First Hand Hold',
        'date_str': '04 July 2026',
        'caption': 'When my fingers interlaced with yours, every racing thought found peace.',
        'rotation': '3.2deg'
    },
    {
        'id': 5,
        'photo_file': 'images/photo5.jpg',
        'milestone_id': 'first-hug-kiss-ride',
        'title': 'First Hug, First Kiss & Our First Ride',
        'date_str': '05 September 2026',
        'caption': 'Holding you close, feeling your heartbeat, and that magical ride into the wind.',
        'rotation': '-3.0deg'
    },
    {
        'id': 6,
        'photo_file': 'images/photo6.jpg',
        'milestone_id': 'first-good-kiss',
        'title': 'Our First Good Kiss',
        'date_str': '10 September 2026',
        'caption': 'A timeless, perfect moment that took my breath away and sealed my heart to yours.',
        'rotation': '2.2deg'
    }
]

TRIVIA_QUESTIONS = [
    {
        'id': 1,
        'prompt': "On 06 July 2026 at 00:09 AM, who broke the ice on Instagram and what was the very first word sent?",
        'options': [
            "Hamid Gazi — 'Assalamu Alaikum'",
            "Amina Chamadiya — 'suno'",
            "Amina Chamadiya — 'Hii Hamid'",
            "Hamid Gazi — 'Mubarak ho'"
        ],
        'correct_index': 1,
        'correct_text': "Amina Chamadiya — 'suno'",
        'feedback': "Bingo! At 00:09 AM on 06 July, Amina broke the ice with that iconic single word 'suno' — and our beautiful story began! ✨"
    },
    {
        'id': 2,
        'prompt': "What was our all-time record chat day when we sent an astonishing 857 messages in 24 hours?",
        'options': [
            "Friday, August 14, 2026",
            "Sunday, August 16, 2026",
            "Tuesday, August 18, 2026",
            "Monday, August 17, 2026"
        ],
        'correct_index': 3,
        'correct_text': "Monday, August 17, 2026",
        'feedback': "SubhanAllah! Monday, August 17, 2026 was our record-shattering day — we exchanged 857 messages because we simply could not stop talking! 🔥"
    },
    {
        'id': 3,
        'prompt': "Over 50.6% of our chat (6,571 messages) happened late at night. Which exact 1-hour window had our highest message volume (2,652 msgs)?",
        'options': [
            "12:00 AM – 1:00 AM (Midnight Hour)",
            "1:00 AM – 2:00 AM (Deep Night)",
            "11:00 PM – 12:00 AM (Late Evening)",
            "2:00 AM – 3:00 AM (Before Sleep)"
        ],
        'correct_index': 0,
        'correct_text': "12:00 AM – 1:00 AM (Midnight Hour)",
        'feedback': "Spot on! 12:00 AM to 1:00 AM is our true soulmate peak hour with 2,652 messages exchanged under the quiet stars 🌙"
    },
    {
        'id': 4,
        'prompt': "Out of 2,187 total emoji reactions in our chat, what was our mutual #1 most reacted emoji (used over 1,000 times)?",
        'options': [
            "❤️ Red Heart",
            "😂 Tears of Joy",
            "👍 Thumbs Up",
            "🔥 Fire"
        ],
        'correct_index': 2,
        'correct_text': "👍 Thumbs Up",
        'feedback': "Incredible memory! While ❤️ had 430 uses, our signature 👍 Thumbs Up took the #1 crown with 1,001 reactions! 👍✨"
    },
    {
        'id': 5,
        'prompt': "Our love story is anchored by monumental milestones in 2026. On which exact date was our sacred Baat Pakki celebrated?",
        'options': [
            "Friday, 03 July 2026",
            "Sunday, 14 April 2026",
            "Monday, 06 July 2026",
            "Monday, 27 April 2026"
        ],
        'correct_index': 1,
        'correct_text': "Sunday, 14 April 2026",
        'feedback': "Alhamdulillah! 14 April 2026 was the blessed Sunday of our Baat Pakki that united our families and set our sacred destiny into motion 💍❤️"
    }
]

def calculate_calendar_elapsed(m_date: date, b_date: date = BIRTHDAY_TARGET_DATE) -> Tuple[int, int, str]:
    if m_date > b_date:
        return (0, 0, '0 Days passed')
    m_month, m_day = m_date.month, m_date.day
    b_month, b_day = b_date.month, b_date.day
    if b_day >= m_day:
        months = b_month - m_month
        days = b_day - m_day
    else:
        months = (b_month - m_month) - 1
        days = (b_day - m_day) + 31
    if months > 0 and days > 0:
        elapsed_str = f'{months} Month{"s" if months != 1 else ""}, {days} Day{"s" if days != 1 else ""} passed'
    elif months > 0:
        elapsed_str = f'{months} Month{"s" if months != 1 else ""} passed'
    else:
        elapsed_str = f'{days} Day{"s" if days != 1 else ""} passed'
    return (months, days, elapsed_str)


def calculate_live_ticker(milestone_dt: Any, current_dt: datetime) -> Dict[str, Any]:
    if isinstance(milestone_dt, date) and not isinstance(milestone_dt, datetime):
        milestone_dt = datetime.combine(milestone_dt, datetime.min.time(), tzinfo=current_dt.tzinfo)
    elif milestone_dt.tzinfo is None and current_dt.tzinfo is not None:
        milestone_dt = milestone_dt.replace(tzinfo=current_dt.tzinfo)
    
    is_reached = (current_dt >= milestone_dt)
    if is_reached:
        delta_seconds = int((current_dt - milestone_dt).total_seconds())
        celebration_text = "Happy 23rd Birthday! Amina is officially 23!"
    else:
        delta_seconds = int((milestone_dt - current_dt).total_seconds())
        celebration_text = ""
        
    days = delta_seconds // 86400
    rem = delta_seconds % 86400
    hours = rem // 3600
    rem = rem % 3600
    minutes = rem // 60
    seconds = rem % 60
    return {
        'is_reached': is_reached,
        'celebration_text': celebration_text,
        'total_seconds': delta_seconds,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'formatted': f'{days}d {hours}h {minutes}m {seconds}s'
    }


def generate_fallback_svg(arg1: Any = 1, arg2: Any = "Memory", arg3: Any = "17 September 2026") -> str:
    if isinstance(arg1, int):
        photo_id = arg1
        title = str(arg2)
        date_str = str(arg3)
    else:
        photo_id = 1
        title = str(arg1)
        date_str = str(arg3) if isinstance(arg3, str) and not arg3.isdigit() else "17 September 2026"
    safe_title = (title.replace('&', '&amp;')
                       .replace('<', '&lt;')
                       .replace('>', '&gt;')
                       .replace('"', '&quot;'))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="100%" height="100%">'
        f'<defs><linearGradient id="grad-{photo_id}" x1="0%" y1="0%" x2="100%" y2="100%">'
        f'<stop offset="0%" stop-color="#4a1525"/><stop offset="50%" stop-color="#2e1065"/><stop offset="100%" stop-color="#1e1b4b"/>'
        f'</linearGradient></defs>'
        f'<rect width="400" height="500" fill="url(#grad-{photo_id})" rx="12"/>'
        f'<circle cx="200" cy="180" r="50" fill="#f43f5e" fill-opacity="0.2"/>'
        f'<path d="M175 180 C175 160 200 160 200 175 C200 160 225 160 225 180 C225 200 200 215 200 215 C200 215 175 200 175 180 Z" fill="#f43f5e"/>'
        f'<text x="200" y="280" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold" letter-spacing="2">{date_str.upper()}</text>'
        f'<text x="200" y="320" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="18" font-weight="bold">{safe_title}</text>'
        f'<text x="200" y="420" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Drop photo in images/photo{photo_id}.jpg</text>'
        '</svg>'
    )


class GiftBoxStateMachine:
    def __init__(self):
        self.is_unwrapped = False
        self.confetti_triggered = False
        self.letter_opened = False
        self.current_chapter = 'reveal'
        self.unwrap_count = 0
        self._shaking = False
        self._exploded = False
        self._revealed = False

    @property
    def current_state(self) -> str:
        if self._revealed:
            return 'REVEALED'
        if self._exploded:
            return 'EXPLODED'
        if self.is_unwrapped:
            return 'OPENING'
        if self._shaking:
            return 'SHAKING'
        return 'CLOSED'

    def tap(self) -> bool:
        self._shaking = True
        return True

    def explode(self) -> bool:
        self._exploded = True
        self.confetti_triggered = True
        return True

    def dismiss(self) -> bool:
        self._revealed = True
        return True
    
    def unwrap(self) -> Dict[str, Any]:
        self.unwrap_count += 1
        if not self.is_unwrapped:
            self.is_unwrapped = True
            self.confetti_triggered = True
            self.letter_opened = True
            return {'status': 'unwrapped', 'first_trigger': True}
        return {'status': 'unwrapped', 'first_trigger': False}
    
    def open_letter(self):
        self.letter_opened = True
    
    def close_letter(self):
        self.letter_opened = False
        if self.current_chapter == 'reveal':
            self.current_chapter = 'milestones'
    
    def go_to_chapter(self, chapter_id: str) -> bool:
        valid = ['reveal', 'milestones', 'polaroids', 'chat', 'trivia']
        if chapter_id in valid:
            self.current_chapter = chapter_id
            return True
        return False


class TriviaGameStateMachine:
    def __init__(self):
        self.current_question = 0
        self.score = 0
        self.answered_questions = {}
        self.is_soulmate_unlocked = False
        self.confetti_bursts = 0
    
    @property
    def current_index(self) -> int:
        return self.current_question

    @property
    def is_finished(self) -> bool:
        return self.is_soulmate_unlocked or (len(self.answered_questions) >= len(TRIVIA_QUESTIONS))

    def answer_question(self, opt_index: int) -> Dict[str, Any]:
        idx = self.current_question
        res = self.select_answer(idx, opt_index)
        self.current_question += 1
        return res

    def select_answer(self, q_index: int, opt_index: int) -> Dict[str, Any]:
        if q_index < 0 or q_index >= len(TRIVIA_QUESTIONS):
            raise ValueError('invalid question index')
        if opt_index < 0 or opt_index > 3:
            raise ValueError('invalid option index')
        
        if q_index in self.answered_questions:
            return {'status': 'already_answered', 'q_index': q_index}
        
        q = TRIVIA_QUESTIONS[q_index]
        is_correct = (opt_index == q['correct_index'])
        if is_correct:
            self.score += 1
            self.confetti_bursts += 1
        
        self.answered_questions[q_index] = {
            'selected_index': opt_index,
            'is_correct': is_correct,
            'feedback': q['feedback']
        }
        
        if len(self.answered_questions) == len(TRIVIA_QUESTIONS): 
            self.is_soulmate_unlocked = True
        
        return {
            'status': 'answered',
            'q_index': q_index,
            'is_correct': is_correct,
            'feedback': q['feedback'],
            'all_completed': self.is_soulmate_unlocked
        }
    
    def get_score_summary(self) -> Dict[str, Any]:
        total = len(TRIVIA_QUESTIONS)
        pct = (self.score / total) * 100.0 if total > 0 else 0.0
        return {
            'score': self.score,
            'total': total,
            'percentage': pct,
            'is_soulmate': (self.score == total)
        }

    def restart(self):
        self.current_question = 0
        self.score = 0
        self.answered_questions = {}
        self.is_soulmate_unlocked = False


class ZeroVersionValidator:
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
                matched_str = m.group(0)
                violations.append((pat, matched_str))
        return violations

    @classmethod
    def validate_text(cls, text: str) -> List[Tuple[str, str]]:
        return cls.scan(text)


class ResponsiveValidator:
    @classmethod
    def validate_viewport(cls, html: str) -> bool:
        return bool(re.search(r'<meta[^>]*name=["\']viewport["\'][^>]*content=["\'][^"\']*width=device-width', html, re.IGNORECASE))
    
    @classmethod
    def validate_viewport_meta(cls, meta: str) -> Tuple[bool, str]:
        if cls.validate_viewport(meta):
            return True, "Valid viewport meta tag"
        return False, "Missing or invalid viewport meta tag"

    @classmethod
    def validate_breakpoint(cls, bp: int) -> Tuple[bool, str]:
        if bp in [320, 360, 480, 768, 1024, 1280, 1440, 1920, 2560, 3840]:
            return True, f"Standard responsive breakpoint: {bp}px"
        return False, f"Non-standard breakpoint: {bp}px"

    @classmethod
    def validate_max_width_containers(cls, html: str) -> bool:
        return bool(re.search(r'[^ w]*max-w-(?:xl|2xl|3xl|4xl|5xl|screen)', html))


class OfflineValidator:
    @classmethod
    def validate_no_hardcoded_absolute_server_apis(cls, html: str) -> bool:
        return not bool(re.search(r'fetch\(["\']http://localhost|axios\.get\(["\']http', html, re.IGNORECASE))

    @classmethod
    def validate_script_content(cls, content: str) -> Tuple[bool, List[str]]:
        violations = []
        matches = re.findall(r'<script[^>]*src=["\'](https?://[^"\']+)["\']', content, re.IGNORECASE)
        for m in matches:
            violations.append(f"External script dependency: {m}")
        return len(violations) == 0, violations

    @classmethod
    def validate_link_tags(cls, content: str) -> Tuple[bool, List[str]]:
        violations = []
        matches = re.findall(r'<link[^>]*href=["\'](https?://[^"\']+)["\']', content, re.IGNORECASE)
        for m in matches:
            violations.append(f"External link dependency: {m}")
        return len(violations) == 0, violations

    @classmethod
    def audit_offline_readiness(cls, html: str) -> Tuple[bool, List[str]]:
        violations = []
        clean_scripts, s_viol = cls.validate_script_content(html)
        clean_links, l_viol = cls.validate_link_tags(html)
        violations.extend(s_viol)
        violations.extend(l_viol)
        if not cls.validate_no_hardcoded_absolute_server_apis(html):
            violations.append("Found hardcoded localhost or absolute server API calls")
        return len(violations) == 0, violations


class HTMLAuditor:
    def __init__(self, html_path: str):
        self.html_path = html_path
        self.content = ''
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                self.content = f.read()

    def has_element_id(self, elem_id: str) -> bool:
        return bool(re.search(rf'id=[\"\']{re.escape(elem_id)}[\"\']', self.content))

    def has_text(self, text: str) -> bool:
        return text in self.content

    def check_feature_status(self) -> Dict[str, bool]:
        return {
            'gift_box': self.has_element_id('gift-reveal-overlay') or 'gift' in self.content.lower(),
            'milestones': 'Baat Pakki' in self.content and 'Nikah' in self.content,
            'tickers': 'ticker-' in self.content,
            'polaroids': 'photo1.jpg' in self.content or 'polaroid' in self.content.lower(),
            'chat_break': 'flight' in self.content.lower() or '47.94' in self.content,
            'trivia': 'trivia' in self.content.lower() or 'soulmate' in self.content.lower(),
            'zero_version': len(ZeroVersionValidator.scan(self.content)) == 0,
            'responsive': ResponsiveValidator.validate_viewport(self.content)
        }
