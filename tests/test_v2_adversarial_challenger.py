"""
================================================================================
VERSION 2.0 ADVERSARIAL & EMPIRICAL CHALLENGER TEST SUITE
================================================================================
Author: v2_challenger_1 (Empirical Challenger)
Scope:
  1. Parity & File Integrity: Byte-for-byte identity of primary and replica files.
  2. Zero Audio Policy: Static AST/DOM scan and dynamic runtime interception.
  3. Zero Prohibited Version Words: Full user-visible copy audit.
  4. Mobile Viewport Stress Testing: 320px, 360px, 375px, 390px, 412px, 430px
     verifying zero horizontal overflow, card clipping, and text collision.
  5. Secret Triple-Tap Timing & Security:
     - Rapid 3 taps (<1500ms) on wax seal, header title, and Surat node.
     - Slow taps (>1500ms timeout reset verification).
     - Wrong passcode vs correct '03072026'.
     - Dashboard opening and state transitions.
  6. Permanent Quiz Answer Locking & Storage:
     - Answer selection immutability (cannot change answer once chosen).
     - Persistence across page reload in localStorage ('amina_quiz_result').
     - WhatsApp score sharing button payload verification.
  7. Lightbox Full-Cycle & Boundary Navigation:
     - Sequential next/prev cycling across all 5 polaroids.
     - Boundary wrapping (4 -> 0 and 0 -> 4).
     - Counter pill display ('X / 5') synchronization.
     - Keyboard arrow key navigation and Escape key dismissal.
================================================================================
"""

import hashlib
import os
import re
import sys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2_PRIMARY_PATH = os.path.join(PROJECT_ROOT, "Instagram_Chat_Analysis_Amina_Hamid_v2.html")
V2_REPLICA_PATH = os.path.join(PROJECT_ROOT, "v2.html")


def get_chrome_driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--autoplay-policy=document-user-activation-required')
    options.add_argument('--window-size=1280,800')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    return driver


# ==============================================================================
# SUITE 1: FILE INTEGRITY & ZERO AUDIO & ZERO PROHIBITED WORDS (STATIC)
# ==============================================================================
class TestV2StaticContracts(unittest.TestCase):
    """Static AST/Regex code audits across primary and replica files."""

    def setUp(self):
        self.assertTrue(os.path.exists(V2_PRIMARY_PATH), "V2 primary file missing")
        self.assertTrue(os.path.exists(V2_REPLICA_PATH), "V2 replica file missing")
        with open(V2_PRIMARY_PATH, "r", encoding="utf-8", errors="ignore") as f:
            self.primary_content = f.read()
        with open(V2_REPLICA_PATH, "r", encoding="utf-8", errors="ignore") as f:
            self.replica_content = f.read()

    def test_01_byte_for_byte_identical(self):
        """Primary and replica V2 files must be 100% byte identical."""
        with open(V2_PRIMARY_PATH, "rb") as f1, open(V2_REPLICA_PATH, "rb") as f2:
            b1 = f1.read()
            b2 = f2.read()
        self.assertEqual(len(b1), len(b2), f"Size mismatch: {len(b1)} vs {len(b2)}")
        self.assertEqual(b1, b2, "Byte content mismatch between primary and replica")

    def test_02_zero_audio_tags_and_files(self):
        """Zero <audio> tags, zero audio source tags, zero audio files (.mp3, .wav, etc.)."""
        for label, content in [("primary", self.primary_content), ("replica", self.replica_content)]:
            audio_tags = re.findall(r'<audio\b[^>]*>', content, re.IGNORECASE)
            self.assertEqual(len(audio_tags), 0, f"Found <audio> tag in {label}: {audio_tags}")

            source_audio = re.findall(r'<source\b[^>]*type=[\'"]audio/[^\'"]*[\'"]', content, re.IGNORECASE)
            self.assertEqual(len(source_audio), 0, f"Found audio source in {label}: {source_audio}")

            audio_files = re.findall(r'[\'"][^\'"]+\.(?:mp3|wav|ogg|m4a|aac|flac)[\'"]', content, re.IGNORECASE)
            self.assertEqual(len(audio_files), 0, f"Found audio file references in {label}: {audio_files}")

    def test_03_zero_active_audio_synthesis_calls(self):
        """Verify Web Audio API (AudioContext) or SpeechSynthesis are not invoked."""
        code_without_comments = re.sub(r'//.*?$|/\*.*?\*/', '', self.primary_content, flags=re.MULTILINE | re.DOTALL)
        self.assertNotIn("new AudioContext", code_without_comments)
        self.assertNotIn("new webkitAudioContext", code_without_comments)
        self.assertNotIn("new Audio(", code_without_comments)
        self.assertNotIn("speechSynthesis.speak", code_without_comments)

    def test_04_zero_prohibited_version_words_in_user_copy(self):
        """Zero prohibited version keywords in visible user copy."""
        body_match = re.search(r'<body\b[^>]*>(.*?)</body>', self.primary_content, re.DOTALL | re.IGNORECASE)
        self.assertTrue(body_match, "Could not find body tag")
        body_content = body_match.group(1)
        cleaned = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', body_content, flags=re.IGNORECASE)
        cleaned = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'<!--.*?-->', '', cleaned, flags=re.DOTALL)

        prohibited_patterns = [
            (r'\bv\d+\.\d+\b', "vX.X pattern"),
            (r'\bversion\s+\d+\b', "version X pattern"),
            (r'\bbuild\s*#?\s*\d+\b', "build # pattern"),
            (r'\bcommit\s+[0-9a-f]{7,40}\b', "git commit hash pattern"),
            (r'\bdebug\s+mode\b', "debug mode pattern"),
            (r'\bdeveloper\s+mode\b', "developer mode pattern"),
            (r'\(NEW\s*ANALYTICS\)', "(NEW ANALYTICS) pattern"),
            (r'\b(?:alpha|beta|rc\d*)\b', "alpha/beta release pattern"),
            (r'\btest_suite\b', "test_suite pattern")
        ]

        violations = []
        for pat, desc in prohibited_patterns:
            matches = re.findall(pat, cleaned, re.IGNORECASE)
            if matches:
                violations.append((desc, matches))
        self.assertEqual(len(violations), 0, f"Found prohibited version strings in user copy: {violations}")

    def test_05_strictly_allah_taala_and_zero_swt(self):
        """Reverent Allah Ta'ala strictly preserved with zero 'swt' abbreviations."""
        swt_matches = re.findall(r'\bswt\b|\(swt\)', self.primary_content, re.IGNORECASE)
        self.assertEqual(len(swt_matches), 0, f"Prohibited 'swt' found: {swt_matches}")
        self.assertTrue(
            "Allah Ta'ala" in self.primary_content or "Allah Ta’ala" in self.primary_content,
            "Missing required reverent phrase 'Allah Ta\\'ala'"
        )


# ==============================================================================
# SUITE 2: MOBILE VIEWPORT STRESS TESTING (RESPONSIVENESS & BOUNDARIES)
# ==============================================================================
class TestV2MobileViewports(unittest.TestCase):
    """Stress tests rendering at 320px, 360px, 375px, 390px, 412px, 430px viewports."""

    @classmethod
    def setUpClass(cls):
        cls.driver = get_chrome_driver()
        cls.file_url = f"file:///{V2_PRIMARY_PATH.replace(os.sep, '/')}"
        cls.driver.get(cls.file_url)
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass

    def _set_viewport(self, width, height=800):
        self.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': width,
            'height': height,
            'deviceScaleFactor': 2,
            'mobile': True
        })
        self.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        time.sleep(0.2)

    def test_viewports_horizontal_overflow(self):
        """Ensure document does not have horizontal scrollbar at mobile viewports."""
        viewports = [320, 360, 375, 390, 412, 430]
        for w in viewports:
            with self.subTest(viewport_width=w):
                self._set_viewport(w)
                scroll_w = self.driver.execute_script("return document.documentElement.scrollWidth;")
                client_w = self.driver.execute_script("return document.documentElement.clientWidth;")
                self.assertLessEqual(
                    scroll_w,
                    client_w + 1,
                    f"Horizontal overflow at {w}px viewport: scrollWidth={scroll_w} > clientWidth={client_w}"
                )

    def test_cards_bounding_box_within_viewport(self):
        """Ensure all primary glass cards fit within mobile viewport bounds."""
        viewports = [320, 375, 412]
        test_selectors = [
            '#two-cities-card',
            '#trivia-questions-container',
            '#polaroids-gallery-container'
        ]
        for w in viewports:
            self._set_viewport(w)
            for sel in test_selectors:
                with self.subTest(viewport=w, selector=sel):
                    rect = self.driver.execute_script(f"""
                        const el = document.querySelector('{sel}');
                        if (!el) return null;
                        const r = el.getBoundingClientRect();
                        return {{ left: r.left, right: r.right, width: r.width }};
                    """)
                    if rect is not None:
                        self.assertGreaterEqual(
                            rect['left'],
                            -1,
                            f"Element {sel} clipped on left at {w}px: left={rect['left']}"
                        )
                        self.assertLessEqual(
                            rect['right'],
                            w + 1,
                            f"Element {sel} clipped on right at {w}px: right={rect['right']} > width={w}"
                        )


# ==============================================================================
# SUITE 3: SECRET TRIPLE-TAP GESTURE TIMING & HUSBAND DASHBOARD
# ==============================================================================
class TestV2SecretTripleTap(unittest.TestCase):
    """Adversarial stress testing of secret gesture timing, timeouts, and passcodes."""

    @classmethod
    def setUpClass(cls):
        cls.driver = get_chrome_driver()
        cls.file_url = f"file:///{V2_PRIMARY_PATH.replace(os.sep, '/')}"

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass

    def setUp(self):
        self.driver.get(self.file_url)
        time.sleep(0.3)
        self.driver.execute_script("""
            localStorage.clear();
            _secretTapCount = 0;
            if (_secretTapTimer) clearTimeout(_secretTapTimer);
            const m1 = document.getElementById('husband-unlock-modal');
            if (m1) m1.style.display = 'none';
            const m2 = document.getElementById('husband-dashboard-modal');
            if (m2) m2.style.display = 'none';
        """)

    def test_rapid_triple_tap_opens_unlock_modal(self):
        """Rapid 3 taps within 1500ms on wax seal opens husband unlock modal."""
        self.driver.execute_script("""
            const seal = document.getElementById('letter-wax-seal');
            seal.click();
            seal.click();
            seal.click();
        """)
        time.sleep(0.2)

        modal_display = self.driver.execute_script("""
            const m = document.getElementById('husband-unlock-modal');
            return m ? m.style.display : 'none';
        """)
        self.assertEqual(modal_display, 'flex', "3 rapid taps must open husband-unlock-modal")

    def test_slow_taps_exceeding_1500ms_do_not_unlock(self):
        """Taps separated by >1500ms must time out and NOT open unlock modal."""
        self.driver.execute_script("""
            const seal = document.getElementById('letter-wax-seal');
            seal.click();
            seal.click();
        """)
        # Wait 1.6 seconds for timeout
        time.sleep(1.6)

        # 3rd tap after timeout
        self.driver.execute_script("""
            const seal = document.getElementById('letter-wax-seal');
            seal.click();
        """)
        time.sleep(0.2)

        modal_display = self.driver.execute_script("""
            const m = document.getElementById('husband-unlock-modal');
            return m ? m.style.display : 'none';
        """)
        self.assertNotEqual(modal_display, 'flex', "Slow taps exceeding 1500ms must not trigger unlock modal")

    def test_header_title_and_surat_node_triggers(self):
        """Header title and Surat node both act as functional triple-tap triggers."""
        # Test Header title trigger
        self.driver.execute_script("""
            const t = document.getElementById('header-hamid-trigger');
            if (t) { t.click(); t.click(); t.click(); }
        """)
        time.sleep(0.2)
        opened = self.driver.execute_script("return document.getElementById('husband-unlock-modal').style.display === 'flex';")
        self.assertTrue(opened, "Header title trigger must open unlock modal")

        # Close modal and reset
        self.driver.execute_script("""
            closeHusbandUnlockModal();
            _secretTapCount = 0;
        """)
        time.sleep(0.2)

        # Test Surat node trigger
        self.driver.execute_script("""
            const s = document.querySelector('[title=\"Hamid\"]');
            if (s) { s.click(); s.click(); s.click(); }
        """)
        time.sleep(0.2)
        opened = self.driver.execute_script("return document.getElementById('husband-unlock-modal').style.display === 'flex';")
        self.assertTrue(opened, "Surat node trigger must open unlock modal")

    def test_wrong_passcode_rejected(self):
        """Entering incorrect passcode displays error and does NOT unlock."""
        self.driver.execute_script("openHusbandUnlockModal();")
        time.sleep(0.1)

        self.driver.execute_script("""
            document.getElementById('husband-passcode-input').value = '99999999';
            submitHusbandUnlock();
        """)
        time.sleep(0.1)

        err_hidden = self.driver.execute_script("""
            const err = document.getElementById('husband-unlock-error');
            return err ? err.classList.contains('hidden') : true;
        """)
        self.assertFalse(err_hidden, "Error message must be shown for wrong passcode")

        is_unlocked = self.driver.execute_script("return localStorage.getItem('amina_husband_mode');")
        self.assertNotEqual(is_unlocked, 'true', "Storage amina_husband_mode must not be set to true on wrong passcode")

    def test_correct_passcode_unlocks_and_opens_dashboard(self):
        """Entering correct passcode '03072026' unlocks and opens dashboard modal."""
        self.driver.execute_script("openHusbandUnlockModal();")
        time.sleep(0.1)

        self.driver.execute_script("""
            document.getElementById('husband-passcode-input').value = '03072026';
            submitHusbandUnlock();
        """)
        time.sleep(0.6)

        is_unlocked = self.driver.execute_script("return localStorage.getItem('amina_husband_mode');")
        self.assertEqual(is_unlocked, 'true', "Storage amina_husband_mode must be 'true'")

        dash_display = self.driver.execute_script("""
            const d = document.getElementById('husband-dashboard-modal');
            return d ? d.style.display : 'none';
        """)
        self.assertEqual(dash_display, 'flex', "Husband dashboard modal must open on correct passcode")


# ==============================================================================
# SUITE 4: PERMANENT QUIZ ANSWER LOCKING & LOCALSTORAGE PERSISTENCE
# ==============================================================================
class TestV2QuizLocking(unittest.TestCase):
    """Verify answers cannot be changed once chosen and persist across reloads."""

    @classmethod
    def setUpClass(cls):
        cls.driver = get_chrome_driver()
        cls.file_url = f"file:///{V2_PRIMARY_PATH.replace(os.sep, '/')}"

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass

    def setUp(self):
        self.driver.get(self.file_url)
        time.sleep(0.3)
        self.driver.execute_script("localStorage.clear(); renderTriviaGame();")
        time.sleep(0.2)

    def test_quiz_answers_cannot_be_overridden_in_session(self):
        """Once an answer is selected for Q0, subsequent clicks on other options are rejected."""
        self.driver.execute_script("selectTriviaAnswer(0, 1);")
        time.sleep(0.1)

        # Attempt to change to option 0
        self.driver.execute_script("selectTriviaAnswer(0, 0);")
        time.sleep(0.1)

        # Verify answeredTrivia[0] is still 1
        ans = self.driver.execute_script("return answeredTrivia[0];")
        self.assertEqual(ans, 1, "Question 0 answer must remain locked to initial pick 1")

        # Verify buttons for Q0 are disabled
        btns_disabled = self.driver.execute_script("""
            const btns = document.querySelectorAll('#trivia-q-0 .trivia-opt-btn');
            return Array.from(btns).map(b => b.disabled);
        """)
        self.assertTrue(all(btns_disabled), f"All options for answered question must be disabled: {btns_disabled}")

    def test_quiz_answers_persist_across_page_reload(self):
        """Answers stored in localStorage are restored upon page refresh and remain locked."""
        self.driver.execute_script("selectTriviaAnswer(0, 1);")
        self.driver.execute_script("selectTriviaAnswer(1, 3);")
        time.sleep(0.2)

        storage_raw = self.driver.execute_script("return localStorage.getItem('amina_quiz_result');")
        self.assertIsNotNone(storage_raw, "amina_quiz_result must be in localStorage")
        self.assertIn('"0":1', storage_raw)
        self.assertIn('"1":3', storage_raw)

        # Refresh page
        self.driver.refresh()
        time.sleep(0.8)

        saved_ans = self.driver.execute_script("return answeredTrivia;")
        self.assertEqual(saved_ans.get('0'), 1, "Q0 must persist answer 1 after reload")
        self.assertEqual(saved_ans.get('1'), 3, "Q1 must persist answer 3 after reload")

        is_disabled_q0 = self.driver.execute_script("""
            const btn = document.getElementById('trivia-opt-0-1');
            return btn ? btn.disabled : false;
        """)
        self.assertTrue(is_disabled_q0, "Option button must remain disabled after reload")

    def test_all_5_questions_completion_and_whatsapp_link(self):
        """Completing all 5 questions generates valid WhatsApp score link."""
        self.driver.execute_script("""
            selectTriviaAnswer(0, 1);
            selectTriviaAnswer(1, 3);
            selectTriviaAnswer(2, 0);
            selectTriviaAnswer(3, 2);
            selectTriviaAnswer(4, 1);
        """)
        time.sleep(0.3)

        score = self.driver.execute_script("return triviaScore;")
        self.assertEqual(score, 5, "Score should be 5/5 for all correct answers")

        wa_href = self.driver.execute_script("""
            const btn = document.getElementById('whatsapp-quiz-share-btn');
            return btn ? btn.getAttribute('href') : '';
        """)
        self.assertIn("wa.me", wa_href, "WhatsApp share link must target wa.me")
        import urllib.parse
        decoded_href = urllib.parse.unquote(wa_href)
        self.assertIn("5/5", decoded_href, "WhatsApp share link message must include 5/5 score")


# ==============================================================================
# SUITE 5: PHOTO LIGHTBOX NAVIGATION, CYCLING & BOUNDARY WRAP
# ==============================================================================
class TestV2LightboxNavigation(unittest.TestCase):
    """Verify Lightbox next/prev cycling, boundary wrap, counter pill, and keyboard."""

    @classmethod
    def setUpClass(cls):
        cls.driver = get_chrome_driver()
        cls.file_url = f"file:///{V2_PRIMARY_PATH.replace(os.sep, '/')}"
        cls.driver.get(cls.file_url)
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass

    def setUp(self):
        self.driver.execute_script("""
            closePhotoLightbox();
            currentLightboxIndex = 0;
        """)
        time.sleep(0.1)

    def test_lightbox_open_and_initial_counter(self):
        """Opening first photo sets index 0 and counter text '1 / 5'."""
        self.driver.execute_script("openPhotoLightbox(1);")
        time.sleep(0.2)

        idx = self.driver.execute_script("return currentLightboxIndex;")
        self.assertEqual(idx, 0, "Initial index should be 0")

        counter_text = self.driver.execute_script("""
            const el = document.getElementById('lightbox-counter-text');
            return el ? el.textContent.trim() : '';
        """)
        self.assertEqual(counter_text, "1 / 5", "Counter text must show '1 / 5'")

    def test_lightbox_forward_cycling_and_boundary_wrap(self):
        """Clicking Next cycles through 0->1->2->3->4 and wraps back to 0."""
        self.driver.execute_script("openPhotoLightbox(1);")
        time.sleep(0.1)

        expected_sequence = [
            (1, "2 / 5"),
            (2, "3 / 5"),
            (3, "4 / 5"),
            (4, "5 / 5"),
            (0, "1 / 5"),  # Boundary wrap!
            (1, "2 / 5")
        ]

        for exp_idx, exp_counter in expected_sequence:
            self.driver.execute_script("nextLightboxPhoto();")
            idx = self.driver.execute_script("return currentLightboxIndex;")
            counter = self.driver.execute_script("return document.getElementById('lightbox-counter-text').textContent.trim();")
            self.assertEqual(idx, exp_idx, f"Expected index {exp_idx}, got {idx}")
            self.assertEqual(counter, exp_counter, f"Expected counter {exp_counter}, got {counter}")

    def test_lightbox_reverse_cycling_and_boundary_wrap(self):
        """Clicking Prev on index 0 wraps backward to 4 ('5 / 5')."""
        self.driver.execute_script("openPhotoLightbox(1);")  # index 0
        time.sleep(0.1)

        self.driver.execute_script("prevLightboxPhoto();")  # wraps to index 4
        idx = self.driver.execute_script("return currentLightboxIndex;")
        counter = self.driver.execute_script("return document.getElementById('lightbox-counter-text').textContent.trim();")
        self.assertEqual(idx, 4, "Prev on index 0 must wrap to index 4")
        self.assertEqual(counter, "5 / 5", "Counter text must show '5 / 5'")

    def test_lightbox_keyboard_navigation(self):
        """ArrowRight, ArrowLeft, and Escape keys control the lightbox via document keydown."""
        self.driver.execute_script("openPhotoLightbox(1);")
        time.sleep(0.1)

        # Dispatch ArrowRight on document
        self.driver.execute_script("""
            document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
        """)
        idx = self.driver.execute_script("return currentLightboxIndex;")
        self.assertEqual(idx, 1, "ArrowRight must increment index to 1")

        # Dispatch ArrowLeft on document
        self.driver.execute_script("""
            document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowLeft', bubbles: true }));
        """)
        idx = self.driver.execute_script("return currentLightboxIndex;")
        self.assertEqual(idx, 0, "ArrowLeft must decrement index back to 0")

        # Dispatch Escape on document
        self.driver.execute_script("""
            document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
        """)
        time.sleep(0.2)
        display = self.driver.execute_script("""
            const m = document.getElementById('photo-lightbox-modal');
            return m ? m.style.display : '';
        """)
        self.assertEqual(display, "none", "Escape key must close lightbox modal")


# ==============================================================================
# SUITE 6: RUNTIME ZERO-AUDIO INTERCEPTION
# ==============================================================================
class TestV2RuntimeZeroAudio(unittest.TestCase):
    """Intercept all Web Audio and HTMLAudioElement calls during full app interactions."""

    @classmethod
    def setUpClass(cls):
        cls.driver = get_chrome_driver()
        cls.file_url = f"file:///{V2_PRIMARY_PATH.replace(os.sep, '/')}"

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass

    def setUp(self):
        self.driver.get(self.file_url)
        time.sleep(0.3)

        self.driver.execute_script("""
            window._audioCallCount = 0;
            window._audioViolations = [];

            if (window.Audio) {
                const OrigAudio = window.Audio;
                window.Audio = function(...args) {
                    window._audioCallCount++;
                    window._audioViolations.push('new Audio(' + args.join(',') + ')');
                    return new OrigAudio(...args);
                };
            }

            if (window.AudioContext || window.webkitAudioContext) {
                const AC = window.AudioContext || window.webkitAudioContext;
                window.AudioContext = function() {
                    window._audioCallCount++;
                    window._audioViolations.push('new AudioContext()');
                    return new AC();
                };
            }
        """)

    def test_zero_audio_invocations_during_app_flows(self):
        """Execute reveal, trivia answers, petals toggle, lightbox and verify zero audio calls."""
        self.driver.execute_script("playCelebrationChime(); triggerCelebrationHaptic([10]);")

        self.driver.execute_script("""
            selectTriviaAnswer(0, 1);
            selectTriviaAnswer(1, 3);
            selectTriviaAnswer(2, 0);
            selectTriviaAnswer(3, 2);
            selectTriviaAnswer(4, 1);
        """)

        self.driver.execute_script("""
            const btn = document.getElementById('ambient-petals-toggle');
            if (btn) { btn.click(); btn.click(); }
        """)

        self.driver.execute_script("""
            openPhotoLightbox(1);
            nextLightboxPhoto();
            prevLightboxPhoto();
            closePhotoLightbox();
        """)

        violations = self.driver.execute_script("return window._audioViolations;")
        call_count = self.driver.execute_script("return window._audioCallCount;")
        self.assertEqual(call_count, 0, f"Runtime audio calls detected: {violations}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
