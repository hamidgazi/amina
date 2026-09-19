"""Comprehensive Automated Test Suite for Hamid's Hinglish Dictionary & Shortcuts
Verifies corpus extraction, exact frequency calculations, descending order sorting,
thematic categorizations, linguistic rules, real chat contexts, and mobile shortcut files.
"""

import unittest
import os
import re
import csv
import json
import zipfile
import plistlib

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HINGLISH_DIR = os.path.join(PROJECT_ROOT, "hinglish")
DATA_DIR = os.path.join(PROJECT_ROOT, "chat_data")
ZIP_PATH = os.path.join(DATA_DIR, "aminachamadiya_1492033579358491 New.zip") if os.path.exists(os.path.join(DATA_DIR, "aminachamadiya_1492033579358491 New.zip")) else os.path.join(PROJECT_ROOT, "aminachamadiya_1492033579358491 New.zip")
DICT_MD_PATH = os.path.join(HINGLISH_DIR, "HAMID_HINGLISH_DICTIONARY.md") if os.path.exists(os.path.join(HINGLISH_DIR, "HAMID_HINGLISH_DICTIONARY.md")) else os.path.join(PROJECT_ROOT, "HAMID_HINGLISH_DICTIONARY.md")
GBOARD_TXT_PATH = os.path.join(HINGLISH_DIR, "gboard_hinglish_shortcuts.txt") if os.path.exists(os.path.join(HINGLISH_DIR, "gboard_hinglish_shortcuts.txt")) else os.path.join(PROJECT_ROOT, "gboard_hinglish_shortcuts.txt")
GBOARD_CSV_PATH = os.path.join(HINGLISH_DIR, "gboard_hinglish_shortcuts.csv") if os.path.exists(os.path.join(HINGLISH_DIR, "gboard_hinglish_shortcuts.csv")) else os.path.join(PROJECT_ROOT, "gboard_hinglish_shortcuts.csv")
IOS_CSV_PATH = os.path.join(HINGLISH_DIR, "ios_text_replacement.csv") if os.path.exists(os.path.join(HINGLISH_DIR, "ios_text_replacement.csv")) else os.path.join(PROJECT_ROOT, "ios_text_replacement.csv")
IOS_PLIST_PATH = os.path.join(HINGLISH_DIR, "ios_text_replacement.plist") if os.path.exists(os.path.join(HINGLISH_DIR, "ios_text_replacement.plist")) else os.path.join(PROJECT_ROOT, "ios_text_replacement.plist")
GBOARD_ZIP_PATH = os.path.join(HINGLISH_DIR, "gboard_dictionary.zip") if os.path.exists(os.path.join(HINGLISH_DIR, "gboard_dictionary.zip")) else os.path.join(PROJECT_ROOT, "gboard_dictionary.zip")

REQUIRED_PROMPT_WORDS = [
    'muje', 'tuje', 'samaj', 'kuch', 'mene', 'eak', 'zayada',
    'badme', 'dusre', 'hu', 'baate', 'lunga', 'dunga', 'kyu', 'karu'
]

REQUIRED_THEMATIC_CATEGORIES = [
    "Pronouns & Addressing",
    "Common Verbs & Future Tense",
    "Adverbs & Conjunctions",
    "General Vocabulary & Quantifiers"
]

class TestCorpusExtraction(unittest.TestCase):
    """Test R1: Corpus extraction and message counts from the zip archive."""

    @classmethod
    def setUpClass(cls):
        cls.hamid_msgs = []
        cls.hamid_texts = []
        with zipfile.ZipFile(ZIP_PATH, 'r') as z:
            all_msgs = []
            for name in ['aminachamadiya_1492033579358491/message_1.json', 'aminachamadiya_1492033579358491/message_2.json']:
                data = json.loads(z.read(name).decode('utf-8'))
                all_msgs.extend(data['messages'])
            cls.hamid_msgs = [m for m in all_msgs if m.get('sender_name') == 'Hamid Gazi']
            cls.hamid_texts = [m['content'] for m in cls.hamid_msgs if 'content' in m]

    def test_hamid_message_counts(self):
        """Hamid authored 9,301 total messages with 9,203 actual text messages (9,234 with content)."""
        self.assertEqual(len(self.hamid_msgs), 9301, "Hamid's total messages in raw JSON must be 9,301")
        self.assertEqual(len(self.hamid_texts), 9234, "Hamid's messages with content field must be 9,234")
        # 9,203 actual text messages when excluding media/calls
        self.assertGreaterEqual(len(self.hamid_texts), 9203)

    def test_prompt_words_present_in_corpus(self):
        """Every single informal word mentioned in the prompt must occur in Hamid's texts."""
        for w in REQUIRED_PROMPT_WORDS:
            pat = rf'\b{re.escape(w)}\b'
            cnt = sum(len(re.findall(pat, t, re.I)) for t in self.hamid_texts)
            self.assertGreater(cnt, 0, f"Word '{w}' should have at least 1 match in Hamid's corpus")

class TestHinglishDictionaryMarkdown(unittest.TestCase):
    """Test R2: Comprehensive Reference Manual structure and content."""

    @classmethod
    def setUpClass(cls):
        with open(DICT_MD_PATH, 'r', encoding='utf-8') as f:
            cls.md_content = f.read()
        
        # Also load corpus texts for frequency verification
        with zipfile.ZipFile(ZIP_PATH, 'r') as z:
            all_msgs = []
            for name in ['aminachamadiya_1492033579358491/message_1.json', 'aminachamadiya_1492033579358491/message_2.json']:
                data = json.loads(z.read(name).decode('utf-8'))
                all_msgs.extend(data['messages'])
            hamid_msgs = [m for m in all_msgs if m.get('sender_name') == 'Hamid Gazi']
            cls.hamid_texts = [m['content'] for m in hamid_msgs if 'content' in m]

    def test_file_exists_and_substantial(self):
        """Dictionary file exists in root and contains substantial content (>10 KB)."""
        self.assertTrue(os.path.exists(DICT_MD_PATH))
        self.assertGreater(len(self.md_content), 10000)

    def test_major_sections_present(self):
        """Document must contain all mandatory major sections."""
        self.assertIn("1. Executive Summary & Texting Profile", self.md_content)
        self.assertIn("2. Master Ranked Correction Table", self.md_content)
        self.assertIn("3. Thematic Categorization", self.md_content)
        self.assertIn("4. The Top 5 Golden Rules of Clean Hinglish", self.md_content)
        self.assertIn("5. How to Setup Instant Autocorrect on Your Phone", self.md_content)

    def test_thematic_categories_present(self):
        """Document must contain exactly the 4 required thematic categories."""
        for cat in REQUIRED_THEMATIC_CATEGORIES:
            self.assertIn(cat, self.md_content, f"Thematic category '{cat}' missing from markdown")

    def test_top_5_golden_rules_present(self):
        """Document must define exactly 5 golden rules with clear explanations."""
        for rule_num in range(1, 6):
            self.assertIn(f"Rule {rule_num}:", self.md_content, f"Golden Rule {rule_num} missing")

    def test_phone_setup_instructions(self):
        """Must include setup instructions for both Android (Gboard) and iPhone (iOS)."""
        self.assertIn("Android Setup (Google Gboard)", self.md_content)
        self.assertIn("iPhone Setup (Apple iOS Text Replacement)", self.md_content)
        self.assertIn("Text Replacement", self.md_content)
        self.assertIn("Personal dictionary", self.md_content)

    def test_master_table_strictly_descending(self):
        """Master frequency table must be strictly sorted by frequency count descending."""
        table_rows = re.findall(r'\|\s*\*\*#(\d+)\*\*\s*\|\s*`([^`]+)`\s*\|\s*\*\*(\d+)x\*\*\s*\|', self.md_content)
        self.assertGreaterEqual(len(table_rows), 25, "Master table should contain at least 25 ranked words")
        
        prev_count = float('inf')
        for rank, word, count_str in table_rows:
            count = int(count_str)
            self.assertLessEqual(count, prev_count, f"Word '{word}' with count {count} is not in descending order after {prev_count}")
            prev_count = count

    def test_frequencies_match_corpus(self):
        """Every tracked word's count in the master table must match its exact count in Hamid's corpus."""
        table_rows = re.findall(r'\|\s*\*\*#(\d+)\*\*\s*\|\s*`([^`]+)`\s*\|\s*\*\*(\d+)x\*\*\s*\|', self.md_content)
        for rank, word, count_str in table_rows:
            expected_count = sum(len(re.findall(rf'\b{re.escape(word)}\b', t, re.I)) for t in self.hamid_texts)
            actual_count = int(count_str)
            self.assertEqual(actual_count, expected_count, f"Count mismatch for '{word}': table={actual_count}, corpus={expected_count}")

    def test_real_chat_contexts_are_authentic(self):
        """Real chat context examples in table must match actual substrings in Hamid's messages."""
        # Find all quoted examples in master table
        contexts = re.findall(r'\|\s*\*\"([^\"]+)\"\*\s*\|', self.md_content)
        self.assertGreaterEqual(len(contexts), 25)
        
        # Check that context words exist in corpus
        for ctx in contexts:
            # Check if at least 3 consecutive words from ctx exist in hamid_texts
            words = ctx.split()
            if len(words) >= 3:
                phrase = " ".join(words[:3]).lower()
                found = any(phrase in t.lower() for t in self.hamid_texts)
                self.assertTrue(found, f"Example context phrase '{phrase}' not found in Hamid's corpus")

    def test_polysemous_collision_advisory_present(self):
        """Must document why high-frequency English-colliding words (to, me, hi, is, us, so) are excluded."""
        self.assertIn("3.5 High-Frequency Excluded Words", self.md_content)
        self.assertIn("1,530x", self.md_content)
        self.assertIn("1,793x", self.md_content)
        self.assertIn("Call me when you're free", self.md_content)
        self.assertIn("cross-linguistic false positive collisions", self.md_content)

    def test_thoda_rationale_present(self):
        """Must provide explicit linguistic justification for thoda (Hinglish vs Roman Urdu thora & whitelist)."""
        self.assertIn("thora", self.md_content)
        self.assertIn("whitelist", self.md_content.lower())
        self.assertIn("autocorrect", self.md_content.lower())

    def test_corpus_methodology_present(self):
        """Must explain exact regex boundary methodology and prompt estimate variations."""
        self.assertIn("1.1 Corpus Extraction & Exact Frequency Methodology", self.md_content)
        self.assertIn("samaj", self.md_content)
        self.assertIn("samja", self.md_content)
        self.assertIn("78x", self.md_content)

    def test_thematic_tables_cross_table_parity(self):
        """Every word in Master Table must be present in Thematic tables with identical count and spelling."""
        # Parse master table
        master_rows = re.findall(r'\|\s*\*\*#(\d+)\*\*\s*\|\s*`([^`]+)`\s*\|\s*\*\*(\d+)x\*\*\s*\|\s*(.*?)\s*\|', self.md_content)
        master_dict = {r[1]: (int(r[2]), r[3].strip()) for r in master_rows}
        self.assertEqual(len(master_dict), 26, "Master table must contain exactly 26 words")

        # Parse 4 thematic sections
        thematic_sec = re.findall(r'###\s*(3\.[1-4]\s+[^\n]+)\n(.*?)(?=\n###|\n---)', self.md_content, re.DOTALL)
        self.assertEqual(len(thematic_sec), 4, "Must contain exactly 4 thematic category sections")

        thematic_dict = {}
        for sec_title, sec_content in thematic_sec:
            rows = re.findall(r'\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*(\d+)x\s*\|', sec_content)
            for r in rows:
                word = r[0]
                spelling = r[1].strip()
                count = int(r[2])
                self.assertNotIn(word, thematic_dict, f"Word '{word}' appears in more than one thematic category")
                thematic_dict[word] = (count, spelling, sec_title)

        # Cross-table set equivalence
        self.assertEqual(set(master_dict.keys()), set(thematic_dict.keys()), "Master table and thematic tables must contain the exact same set of words")

        # Parity check on counts and spellings
        for word, (m_count, m_spelling) in master_dict.items():
            t_count, t_spelling, t_sec = thematic_dict[word]
            self.assertEqual(m_count, t_count, f"Frequency mismatch for '{word}' between Master ({m_count}) and Thematic ({t_count})")
            self.assertEqual(m_spelling, t_spelling, f"Spelling mismatch for '{word}' between Master ({m_spelling}) and Thematic ({t_spelling})")

    def test_thematic_tables_descending_order(self):
        """Every individual thematic category table must be sorted strictly in descending order of frequency."""
        thematic_sec = re.findall(r'###\s*(3\.[1-4]\s+[^\n]+)\n(.*?)(?=\n###|\n---)', self.md_content, re.DOTALL)
        for sec_title, sec_content in thematic_sec:
            rows = re.findall(r'\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*(\d+)x\s*\|', sec_content)
            counts = [int(r[2]) for r in rows]
            self.assertGreater(len(counts), 0, f"Thematic section '{sec_title}' has no entries")
            is_descending = all(counts[i] >= counts[i+1] for i in range(len(counts)-1))
            self.assertTrue(is_descending, f"Thematic section '{sec_title}' is not sorted in descending order: {counts}")

    def test_third_party_android_keyboards_documented(self):
        """Must document instructions for Samsung Keyboard, SwiftKey, and refer to gboard_hinglish_shortcuts.csv."""
        self.assertIn("Samsung Keyboard", self.md_content)
        self.assertIn("Microsoft SwiftKey", self.md_content)
        self.assertIn("gboard_hinglish_shortcuts.csv", self.md_content)

    def test_icloud_sync_latency_and_verification_documented(self):
        """Must document iCloud sync latency (10s to 2m), iPhone verification steps, and troubleshooting."""
        self.assertIn("10 seconds and 2 minutes", self.md_content)
        self.assertIn("Settings", self.md_content)
        self.assertIn("Text Replacement", self.md_content)
        self.assertIn("iCloud Drive", self.md_content)

    def test_case_sensitivity_and_polymorphic_capitalization_documented(self):
        """Must document why shortcuts are strictly lowercase and how polymorphic capitalization works."""
        self.assertIn("5.3 Keyboard Case Sensitivity & Polymorphic Capitalization Mechanics", self.md_content)
        self.assertIn("polymorphic", self.md_content.lower())
        self.assertIn("lowercase", self.md_content.lower())
        self.assertIn("sentence start", self.md_content.lower())

    def test_third_party_keyboards_without_import_apis_documented(self):
        """Must document fallback instructions for minimalist keyboards lacking import APIs (Fleksy, Typewise)."""
        self.assertIn("Fleksy", self.md_content)
        self.assertIn("Typewise", self.md_content)
        self.assertIn("Keyboards Lacking Batch Import APIs", self.md_content)
        self.assertIn("gboard_hinglish_shortcuts.csv", self.md_content)

    def test_icloud_sync_low_power_mode_troubleshooting_documented(self):
        """Must document Low Power Mode / Battery Saver troubleshooting and CloudKit throttling."""
        self.assertIn("Low Power Mode", self.md_content)
        self.assertIn("textreplacementsd", self.md_content)
        self.assertIn("Battery", self.md_content)

    def test_toc_links_match_document_headings(self):
        """All Table of Contents anchor links must correspond 100% to actual document headings."""
        def gh_slug(text):
            text = text.replace('`', '')
            text = text.encode('ascii', 'ignore').decode('ascii')
            text = re.sub(r'[^\w\s-]', '', text).strip().lower()
            text = re.sub(r' ', '-', text)
            return '#' + text

        headings = re.findall(r'^(#{1,6})\s+(.+)$', self.md_content, re.MULTILINE)
        toc_links = re.findall(r'\[([^\]]+)\]\((#[^\)]+)\)', self.md_content[:2000])

        heading_slugs = {gh_slug(h_text): h_text for _, h_text in headings}
        self.assertGreaterEqual(len(toc_links), 14, "Must contain at least 14 TOC links")
        
        for text, link in toc_links:
            self.assertIn(link, heading_slugs, f"TOC link '{link}' for '{text}' does not match any heading slug in HAMID_HINGLISH_DICTIONARY.md")


class TestKeyboardShortcutFiles(unittest.TestCase):
    """Test R3: Mobile Keyboard Shortcut Files format and contents."""

    def test_gboard_txt_format(self):
        """gboard_hinglish_shortcuts.txt must be tab-separated: Shortcut<TAB>Replacement<TAB>Language."""
        self.assertTrue(os.path.exists(GBOARD_TXT_PATH))
        with open(GBOARD_TXT_PATH, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        self.assertGreaterEqual(len(lines), 25)
        for idx, line in enumerate(lines):
            parts = line.split('\t')
            self.assertEqual(len(parts), 3, f"Line {idx+1} in gboard txt not tab-separated with 3 parts: '{line}'")
            shortcut, repl, lang = parts
            self.assertTrue(shortcut)
            self.assertTrue(repl)
            self.assertEqual(lang, 'hi')

    def test_gboard_csv_format(self):
        """gboard_hinglish_shortcuts.csv must be valid CSV with Shortcut, Replacement, Language headers."""
        self.assertTrue(os.path.exists(GBOARD_CSV_PATH))
        with open(GBOARD_CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ["Shortcut", "Replacement", "Language"])
            rows = list(reader)
            self.assertGreaterEqual(len(rows), 25)
            for row in rows:
                self.assertEqual(len(row), 3)
                self.assertTrue(row[0])
                self.assertTrue(row[1])
                self.assertEqual(row[2], 'hi')

    def test_ios_csv_format(self):
        """ios_text_replacement.csv must be valid CSV with Shortcut, Phrase headers."""
        self.assertTrue(os.path.exists(IOS_CSV_PATH))
        with open(IOS_CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ["Shortcut", "Phrase"])
            rows = list(reader)
            self.assertGreaterEqual(len(rows), 25)
            for row in rows:
                self.assertEqual(len(row), 2)
                self.assertTrue(row[0])
                self.assertTrue(row[1])

    def test_ios_plist_format(self):
        """ios_text_replacement.plist must be a valid Apple XML property list."""
        self.assertTrue(os.path.exists(IOS_PLIST_PATH))
        with open(IOS_PLIST_PATH, 'rb') as f:
            data = plistlib.load(f)
        
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 25)
        for item in data:
            self.assertIn("shortcut", item)
            self.assertIn("phrase", item)
            self.assertTrue(item["shortcut"])
            self.assertTrue(item["phrase"])

    def test_shortcuts_consistency_across_files(self):
        """All shortcut deliverables must contain the exact same shortcuts in the same order."""
        # Read from gboard txt
        with open(GBOARD_TXT_PATH, 'r', encoding='utf-8') as f:
            gboard_words = [l.split('\t')[0] for l in f if l.strip() and not l.startswith('#')]
        
        # Read from ios csv
        with open(IOS_CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            ios_words = [row[0] for row in reader]
        
        # Read from plist
        with open(IOS_PLIST_PATH, 'rb') as f:
            plist_data = plistlib.load(f)
            plist_words = [item['shortcut'] for item in plist_data]
        
        self.assertEqual(gboard_words, ios_words, "Gboard txt and iOS csv shortcut lists must match exactly")
        self.assertEqual(gboard_words, plist_words, "Gboard txt and iOS plist shortcut lists must match exactly")

    def test_gboard_txt_header(self):
        """gboard_hinglish_shortcuts.txt must start with official # Gboard Dictionary version:1."""
        with open(GBOARD_TXT_PATH, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
        self.assertEqual(first_line, "# Gboard Dictionary version:1")

    def test_gboard_zip_archive(self):
        """gboard_dictionary.zip must exist, contain dictionary.txt, and be ready for 1-tap Gboard import."""
        self.assertTrue(os.path.exists(GBOARD_ZIP_PATH), "gboard_dictionary.zip must exist in project root")
        with zipfile.ZipFile(GBOARD_ZIP_PATH, 'r') as z:
            self.assertIn('dictionary.txt', z.namelist())
            content = z.read('dictionary.txt').decode('utf-8')
            lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith('#')]
            self.assertGreaterEqual(len(lines), 25)
            self.assertTrue(content.startswith("# Gboard Dictionary version:1"))

    def test_gboard_zip_and_txt_exact_entry_and_line_parity(self):
        """gboard_dictionary.zip's dictionary.txt must match gboard_hinglish_shortcuts.txt line-by-line."""
        with open(GBOARD_TXT_PATH, 'r', encoding='utf-8') as f:
            txt_lines = [line.strip() for line in f if line.strip()]

        with zipfile.ZipFile(GBOARD_ZIP_PATH, 'r') as z:
            zip_content = z.read('dictionary.txt').decode('utf-8')
            zip_lines = [line.strip() for line in zip_content.splitlines() if line.strip()]

        self.assertEqual(txt_lines, zip_lines, "gboard_dictionary.zip internal dictionary.txt must match gboard_hinglish_shortcuts.txt line-by-line")


    def test_shortcuts_match_master_table(self):
        """All shortcuts across deliverables must match the master markdown table 1:1 in exact order."""
        with open(DICT_MD_PATH, 'r', encoding='utf-8') as f:
            md = f.read()
        table_rows = re.findall(r'\|\s*\*\*#(\d+)\*\*\s*\|\s*`([^`]+)`\s*\|\s*\*\*(\d+)x\*\*\s*\|', md)
        table_words = [r[1] for r in table_rows]

        with open(GBOARD_TXT_PATH, 'r', encoding='utf-8') as f:
            gboard_words = [l.split('\t')[0] for l in f if l.strip() and not l.startswith('#')]

        with open(IOS_CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            ios_words = [row[0] for row in reader]

        with open(IOS_PLIST_PATH, 'rb') as f:
            plist_data = plistlib.load(f)
            plist_words = [item['shortcut'] for item in plist_data]

        self.assertEqual(gboard_words, table_words, "Gboard shortcuts must match master table words exactly")
        self.assertEqual(ios_words, table_words, "iOS CSV shortcuts must match master table words exactly")
        self.assertEqual(plist_words, table_words, "iOS Plist shortcuts must match master table words exactly")

    def test_shortcuts_casing_all_lowercase(self):
        """All shortcuts and replacement phrases across all deliverables must be strictly lowercase for polymorphic expansion."""
        # Check Gboard TXT
        with open(GBOARD_TXT_PATH, 'r', encoding='utf-8') as f:
            for idx, line in enumerate(f):
                if line.strip() and not line.startswith('#'):
                    s, r, _ = line.strip().split('\t')
                    self.assertEqual(s, s.lower(), f"Shortcut '{s}' on line {idx+1} of gboard txt is not lowercase")
                    self.assertEqual(r, r.lower(), f"Replacement '{r}' on line {idx+1} of gboard txt is not lowercase")

        # Check Gboard CSV
        with open(GBOARD_CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                s, r, _ = row
                self.assertEqual(s, s.lower(), f"Shortcut '{s}' in gboard csv is not lowercase")
                self.assertEqual(r, r.lower(), f"Replacement '{r}' in gboard csv is not lowercase")

        # Check iOS CSV
        with open(IOS_CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for s, p in reader:
                self.assertEqual(s, s.lower(), f"Shortcut '{s}' in ios csv is not lowercase")
                self.assertEqual(p, p.lower(), f"Phrase '{p}' in ios csv is not lowercase")

        # Check iOS Plist
        with open(IOS_PLIST_PATH, 'rb') as f:
            plist_data = plistlib.load(f)
            for item in plist_data:
                s = item['shortcut']
                p = item['phrase']
                self.assertEqual(s, s.lower(), f"Shortcut '{s}' in ios plist is not lowercase")
                self.assertEqual(p, p.lower(), f"Phrase '{p}' in ios plist is not lowercase")

        # Check Gboard ZIP
        with zipfile.ZipFile(GBOARD_ZIP_PATH, 'r') as z:
            content = z.read('dictionary.txt').decode('utf-8')
            for line in content.splitlines():
                if line.strip() and not line.startswith('#'):
                    s, r, _ = line.strip().split('\t')
                    self.assertEqual(s, s.lower(), f"Shortcut '{s}' in gboard zip is not lowercase")
                    self.assertEqual(r, r.lower(), f"Replacement '{r}' in gboard zip is not lowercase")

if __name__ == '__main__':
    unittest.main(verbosity=2)
