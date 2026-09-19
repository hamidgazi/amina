import os

TEST_CODE = '''"""Milestone 1 Empirical Stress Test Suite
Author: m1_challenger_2
Scope:
  - Canvas confetti particle array limits, memory footprint, and RAF animation loop termination.
  - Audio context safety and browser autoplay policy resilience.
  - Viewport boundary testing (320px, 375px, 414px) and love letter header/footer pinning.
  - Text verification of exact required 23rd birthday greeting.
"""

import unittest
import os
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HTML_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Instagram_Chat_Analysis_Amina_Hamid.html'))

class BaseSeleniumTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--autoplay-policy=document-user-activation-required')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(f'file:///{HTML_FILE_PATH}')
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass

class TestM1ExactGreetingVerification(BaseSeleniumTest):
    """Verification of exact required greeting string"""
    
    def test_greeting_exact_string_in_source(self):
        with open(HTML_FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        target = 'Happy 23rd Birthday My Love, Amina! • 17 September 2026'
        self.assertIn(target, content, f'Exact greeting string "{target}" must be present in HTML source')

    def test_greeting_rendered_in_modal_dom(self):
        el = self.driver.find_element('id', 'modal-birthday-greeting')
        self.assertIsNotNone(el, 'modal-birthday-greeting element must exist in DOM')
        text = el.text.strip()
        target = 'Happy 23rd Birthday My Love, Amina! • 17 September 2026'
        self.assertIn(target, text, f'modal-birthday-greeting must contain exact string "{target}"')

    def test_greeting_in_letter_header(self):
        with open(HTML_FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('On Your 23rd Birthday • 17 September 2026', content)
        self.assertIn('Meri Pyaari Amina', content)
        self.assertIn('Happy 23rd Birthday, my love. As the sun rises on this blessed 17th of September', content)

class TestM1ConfettiStress(BaseSeleniumTest):
    """Confetti particle array limits, memory footprint, and RAF animation loop termination"""

    def test_confetti_constant_cap_in_source(self):
        with open(HTML_FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('MAX_CONCURRENT_PARTICLES = 250', content)
        self.assertIn('confettiParticles.shift()', content)
        self.assertIn('cancelAnimationFrame(confettiAnimation)', content)
        self.assertIn('confettiAnimation = null', content)

    def test_confetti_lifecycle_loop_termination(self):
        # Verify that after confetti settles, RAF stops
        res = self.driver.execute_script('''
            return new Promise((resolve) => {
                const originalRAF = window.requestAnimationFrame;
                let activeRafs = 0;
                
                window.requestAnimationFrame = function(cb) {
                    activeRafs++;
                    return originalRAF.call(window, function(timestamp) {
                        activeRafs--;
                        cb(timestamp);
                    });
                };
                
                // Launch confetti
                window.triggerCelebrationConfetti();
                
                // Check after 3.5 seconds (all particles should have fallen and faded)
                setTimeout(() => {
                    window.requestAnimationFrame = originalRAF;
                    resolve({ activeRafs: activeRafs });
                }, 3500);
            });
        ''')
        self.assertEqual(res.get('activeRafs', 0), 0, 'Animation loop must stop when particles settle (zero CPU usage)')

class TestM1AudioFallback(BaseSeleniumTest):
    """Audio context safety and browser autoplay policy resilience"""

    def test_audio_autoplay_unhandled_rejections(self):
        errors = self.driver.execute_script('''
            window._audioErrors = [];
            const errHandler = (e) => window._audioErrors.push('err: ' + e.message);
            const rejHandler = (e) => window._audioErrors.push('rej: ' + (e.reason ? (e.reason.message || e.reason) : e));
            
            window.addEventListener('error', errHandler);
            window.addEventListener('unhandledrejection', rejHandler);
            
            try {
                playCelebrationChime();
            } catch(e) {
                window._audioErrors.push('sync: ' + e.message);
            }
            
            return new Promise((resolve) => {
                setTimeout(() => {
                    window.removeEventListener('error', errHandler);
                    window.removeEventListener('unhandledrejection', rejHandler);
                    resolve(window._audioErrors);
                }, 500);
            });
        ''')
        self.assertEqual(len(errors), 0, f'Audio execution threw unhandled errors: {errors}')

    def test_audio_context_missing_graceful_noop(self):
        res = self.driver.execute_script('''
            const origAudio = window.AudioContext;
            const origWebkit = window.webkitAudioContext;
            let crashed = false;
            try {
                window.AudioContext = undefined;
                window.webkitAudioContext = undefined;
                playCelebrationChime();
            } catch(e) {
                crashed = true;
            } finally {
                window.AudioContext = origAudio;
                window.webkitAudioContext = origWebkit;
            }
            return crashed;
        ''')
        self.assertFalse(res, 'playCelebrationChime must gracefully no-op when AudioContext is undefined')

    def test_audio_context_throwing_constructor_graceful_catch(self):
        res = self.driver.execute_script('''
            const origAudio = window.AudioContext;
            let crashed = false;
            try {
                window.AudioContext = function() {
                    throw new Error('NotAllowedError: Security policy blocked audio context creation');
                };
                playCelebrationChime();
            } catch(e) {
                crashed = true;
            } finally {
                window.AudioContext = origAudio;
            }
            return crashed;
        ''')
        self.assertFalse(res, 'playCelebrationChime must catch constructor errors gracefully without bubbling')

class TestM1ViewportResponsiveness(BaseSeleniumTest):
    """Viewport boundary testing and love letter pinning"""

    def test_viewport_375px_no_horizontal_overflow(self):
        self.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': 375, 'height': 667, 'deviceScaleFactor': 2, 'mobile': True
        })
        self.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        time.sleep(0.3)
        scroll_w = self.driver.execute_script('return document.documentElement.scrollWidth;')
        client_w = self.driver.execute_script('return document.documentElement.clientWidth;')
        self.assertLessEqual(scroll_w, client_w, f'Viewport 375px: scrollWidth ({scroll_w}) > clientWidth ({client_w})')

    def test_viewport_414px_no_horizontal_overflow(self):
        self.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': 414, 'height': 896, 'deviceScaleFactor': 2, 'mobile': True
        })
        self.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        time.sleep(0.3)
        scroll_w = self.driver.execute_script('return document.documentElement.scrollWidth;')
        client_w = self.driver.execute_script('return document.documentElement.clientWidth;')
        self.assertLessEqual(scroll_w, client_w, f'Viewport 414px: scrollWidth ({scroll_w}) > clientWidth ({client_w})')

    def test_viewport_320px_horizontal_overflow_check(self):
        self.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': 320, 'height': 568, 'deviceScaleFactor': 2, 'mobile': True
        })
        self.driver.execute_script("window.dispatchEvent(new Event('resize'));")
        time.sleep(0.3)
        doc_scroll = self.driver.execute_script('return document.documentElement.scrollWidth;')
        doc_client = self.driver.execute_script('return document.documentElement.clientWidth;')
        self.assertLessEqual(doc_scroll, doc_client, f'Viewport 320px: scrollWidth ({doc_scroll}) > clientWidth ({doc_client})')

    def test_love_letter_header_and_footer_remain_pinned(self):
        self.driver.execute_script('openLoveLetter();')
        time.sleep(0.5)
        
        info = self.driver.execute_script('''
            const card = document.getElementById('letter-card-container');
            const header = card.querySelector('.shrink-0:first-child');
            const footer = card.querySelector('.shrink-0:last-child');
            const body = card.querySelector('.overflow-y-auto');
            
            const initialHeaderRect = header.getBoundingClientRect();
            const initialFooterRect = footer.getBoundingClientRect();
            const initialBodyScrollTop = body.scrollTop;
            
            body.scrollTop = 300;
            
            const scrolledHeaderRect = header.getBoundingClientRect();
            const scrolledFooterRect = footer.getBoundingClientRect();
            const newBodyScrollTop = body.scrollTop;
            
            return {
                initialHeaderTop: initialHeaderRect.top,
                scrolledHeaderTop: scrolledHeaderRect.top,
                initialFooterBottom: initialFooterRect.bottom,
                scrolledFooterBottom: scrolledFooterRect.bottom,
                initialBodyScrollTop: initialBodyScrollTop,
                newBodyScrollTop: newBodyScrollTop,
                scrollHeight: body.scrollHeight,
                clientHeight: body.clientHeight,
                overflowY: window.getComputedStyle(body).overflowY
            };
        ''')
        
        self.assertAlmostEqual(info['initialHeaderTop'], info['scrolledHeaderTop'], delta=1.0,
                               msg='Love letter header must remain pinned at top during body scroll')
        self.assertAlmostEqual(info['initialFooterBottom'], info['scrolledFooterBottom'], delta=1.0,
                               msg='Love letter footer must remain pinned at bottom during body scroll')
        self.assertGreater(info['newBodyScrollTop'], info['initialBodyScrollTop'],
                           msg='Letter body must actually scroll')
        self.assertGreater(info['scrollHeight'], info['clientHeight'],
                           msg='Letter body content must exceed container height for scrollability')
        self.assertIn(info['overflowY'], ['auto', 'scroll'],
                      msg='Letter body must have overflow-y auto or scroll')

if __name__ == '__main__':
    unittest.main()
'''

with open('tests/test_m1_challenger_2_stress.py', 'w', encoding='utf-8') as f:
    f.write(TEST_CODE.strip())
print('Generated tests/test_m1_challenger_2_stress.py successfully')

