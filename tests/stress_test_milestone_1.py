"""
Milestone 1 Empirical Stress Test Suite & Oracle
Author: m1_challenger_1 (Empirical Challenger)
Target: Instagram_Chat_Analysis_Amina_Hamid.html

Probes:
1. Rapid multi-clicks on 3D gift box (race conditions / animation glitches).
2. Replay functionality: calling window.replayGiftUnwrap() repeatedly and during animations.
3. Love letter modal lifecycle: window.openLoveLetter(), window.closeLoveLetter(), backdrop clicks, Escape key.
4. State transition to main chapters via "#btn-unfold-memories".
5. Browser console error telemetry and race condition detection.
"""

import os
import sys
import time
import json
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait

HTML_PATH = Path(__file__).resolve().parent.parent / "Instagram_Chat_Analysis_Amina_Hamid.html"
FILE_URL = HTML_PATH.as_uri()

# Browser security interventions that are expected under synthetic automation
BROWSER_SECURITY_INTERVENTIONS = [
    "Blocked call to navigator.vibrate",
    "AudioContext was not allowed to start",
    "autoplay"
]

def create_driver():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    driver = webdriver.Chrome(options=options)
    driver.get(FILE_URL)
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return typeof window.unwrapGift === 'function';")
    )
    return driver

def check_browser_errors(driver):
    """Retrieve uncaught application errors, ignoring standard browser security interventions."""
    try:
        logs = driver.get_log("browser")
        severe = [l for l in logs if l.get("level") in ["SEVERE", "ERROR"]]
        real_errors = [
            l for l in severe 
            if not any(interv in l.get("message", "") for interv in BROWSER_SECURITY_INTERVENTIONS)
        ]
        return real_errors
    except Exception:
        return []

class StressTestMilestone1:
    def __init__(self):
        self.results = []

    def record(self, test_name, category, passed, details, empirical_evidence):
        status = "PASS" if passed else "FAIL"
        entry = {
            "test": test_name,
            "category": category,
            "status": status,
            "details": details,
            "evidence": empirical_evidence
        }
        self.results.append(entry)
        print(f"[{status}] {category} :: {test_name}")
        if not passed:
            print(f"       Details: {details}")
            print(f"       Evidence: {empirical_evidence}")

    # =========================================================================
    # SUITE 1: RAPID CLICKS ON 3D GIFT BOX
    # =========================================================================
    def test_rapid_double_click(self):
        driver = create_driver()
        try:
            box = driver.find_element(By.ID, "gift-box-container")
            actions = ActionChains(driver)
            actions.click(box).pause(0.02).click(box).perform()

            classes_t0 = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            time.sleep(1.6)

            classes_final = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            letter_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            box_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
            has_unwrapped = driver.execute_script("return window._hasUnwrappedGift;")
            errors = check_browser_errors(driver)

            passed = (
                "is-revealed" in classes_final and
                "is-opening" not in classes_final and
                letter_display != "none" and
                box_display == "none" and
                has_unwrapped is True and
                len(errors) == 0
            )
            evidence = {
                "classes_t0": classes_t0,
                "classes_final": classes_final,
                "letter_display": letter_display,
                "box_display": box_display,
                "has_unwrapped": has_unwrapped,
                "errors": errors
            }
            self.record("Rapid Double-Click Protection", "Gift Box Clicks", passed,
                        "Verify double-click does not corrupt state or trigger duplicate transitions", evidence)
        finally:
            driver.quit()

    def test_rapid_burst_clicks(self):
        driver = create_driver()
        try:
            res = driver.execute_script("""
                const overlay = document.getElementById('gift-reveal-overlay');
                let calls = 0;
                for (let i = 0; i < 20; i++) {
                    try {
                        window.unwrapGift();
                        calls++;
                    } catch (e) {
                        return { calls, error: e.message };
                    }
                }
                return { calls, classes: overlay.className, error: null };
            """)

            time.sleep(1.6)
            classes_final = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            letter_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            errors = check_browser_errors(driver)

            passed = (
                res["calls"] == 20 and
                res["error"] is None and
                "is-revealed" in classes_final and
                letter_display == "block" and
                len(errors) == 0
            )
            self.record("20x Burst Click Stress", "Gift Box Clicks", passed,
                        "Verify 20 rapid programmatic clicks in tight loop do not throw exceptions or corrupt state",
                        {"burst_res": res, "classes_final": classes_final, "letter_display": letter_display, "errors": errors})
        finally:
            driver.quit()

    def test_click_during_opening_transition(self):
        driver = create_driver()
        try:
            box = driver.find_element(By.ID, "gift-box-container")
            box.click()

            time.sleep(0.3)
            driver.execute_script("window.unwrapGift();")

            time.sleep(1.4)
            classes_final = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            letter_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            box_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
            errors = check_browser_errors(driver)

            passed = (
                "is-revealed" in classes_final and
                box_display == "none" and
                letter_display == "block" and
                len(errors) == 0
            )
            self.record("Mid-Transition Click Rejection", "Gift Box Clicks", passed,
                        "Verify click during active 1300ms transition is safely ignored",
                        {"classes_final": classes_final, "box_display": box_display, "letter_display": letter_display, "errors": errors})
        finally:
            driver.quit()

    # =========================================================================
    # SUITE 2: REPLAY FUNCTIONALITY
    # =========================================================================
    def test_single_replay_cycle(self):
        driver = create_driver()
        try:
            driver.execute_script("window.unwrapGift();")
            time.sleep(1.6)

            driver.execute_script("window.replayGiftUnwrap();")
            time.sleep(0.4)

            box_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
            letter_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            classes = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            is_floating = driver.execute_script("return document.getElementById('gift-box-container').classList.contains('floating');")
            errors = check_browser_errors(driver)

            passed = (
                box_display == "flex" and
                letter_display == "none" and
                "is-revealed" not in classes and
                "is-opening" not in classes and
                is_floating is True and
                len(errors) == 0
            )
            self.record("Standard Replay Reset", "Replay Functionality", passed,
                        "Verify replayGiftUnwrap() smoothly restores box stage and hides letter",
                        {"box_display": box_display, "letter_display": letter_display, "classes": classes, "is_floating": is_floating, "errors": errors})
        finally:
            driver.quit()

    def test_repeated_rapid_replay_calls(self):
        driver = create_driver()
        try:
            driver.execute_script("window.unwrapGift();")
            time.sleep(1.6)

            res = driver.execute_script("""
                let err = null;
                try {
                    for (let i = 0; i < 15; i++) {
                        window.replayGiftUnwrap();
                    }
                } catch(e) {
                    err = e.message;
                }
                return { error: err };
            """)

            time.sleep(0.5)
            box_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
            letter_display = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            errors = check_browser_errors(driver)

            passed = (
                res["error"] is None and
                box_display == "flex" and
                letter_display == "none" and
                len(errors) == 0
            )
            self.record("15x Rapid Replay Burst", "Replay Functionality", passed,
                        "Verify rapid back-to-back replay calls settle cleanly into box stage",
                        {"error": res["error"], "box_display": box_display, "letter_display": letter_display, "errors": errors})
        finally:
            driver.quit()

    def test_replay_during_active_unwrap_race(self):
        """CRITICAL RACE CONDITION TEST:
        Unwrap initiates at t=0 with a 1300ms transition timer.
        If user calls replayGiftUnwrap() at t=200ms, does the lingering unwrap
        timer clobber the replay and force-open the letter at t=1300ms?
        """
        driver = create_driver()
        try:
            driver.execute_script("window.unwrapGift();")
            time.sleep(0.2) # t = 200ms

            driver.execute_script("window.replayGiftUnwrap();")
            time.sleep(0.4) # t = 600ms; replay completed into box stage
            
            box_disp_t600 = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")

            # Wait past t = 1300ms (where unwrapGift's setTimeout fires)
            time.sleep(1.0) # total elapsed > 1600ms

            box_disp_t1600 = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
            letter_disp_t1600 = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            classes_t1600 = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")

            # If lingering timer fired, box_disp_t1600 would be 'none', letter_disp_t1600 would be 'block', classes would have 'is-revealed'
            race_condition_detected = (box_disp_t1600 == "none" or letter_disp_t1600 == "block" or "is-revealed" in classes_t1600)
            passed = not race_condition_detected

            evidence = {
                "box_disp_t600": box_disp_t600,
                "box_disp_t1600": box_disp_t1600,
                "letter_disp_t1600": letter_disp_t1600,
                "classes_t1600": classes_t1600,
                "race_hijacked_by_timer": race_condition_detected
            }
            self.record("Replay During Active Unwrap Race Condition", "Replay Functionality", passed,
                        "Checks if lingering setTimeout(..., 1300) from unwrapGift hijacks replay state",
                        evidence)
        finally:
            driver.quit()

    def test_multi_cycle_unwrap_replay(self):
        driver = create_driver()
        try:
            cycles = 5
            all_clean = True
            log_steps = []

            for i in range(cycles):
                driver.execute_script("window.unwrapGift();")
                time.sleep(1.5)
                is_rev = driver.execute_script("return document.getElementById('gift-reveal-overlay').classList.contains('is-revealed');")
                
                driver.execute_script("window.replayGiftUnwrap();")
                time.sleep(0.4)
                is_box = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display === 'flex';")

                step_ok = is_rev and is_box
                log_steps.append({"cycle": i+1, "revealed": is_rev, "replayed_to_box": is_box})
                if not step_ok:
                    all_clean = False
                    break

            errors = check_browser_errors(driver)
            passed = all_clean and len(errors) == 0
            self.record("5-Cycle Unwrap-Replay Stability", "Replay Functionality", passed,
                        "Verify 5 continuous unwrap-to-replay cycles maintain consistent DOM state",
                        {"cycles_log": log_steps, "errors": errors})
        finally:
            driver.quit()

    # =========================================================================
    # SUITE 3: LOVE LETTER MODAL LIFECYCLE
    # =========================================================================
    def test_open_and_close_love_letter_api(self):
        driver = create_driver()
        try:
            driver.execute_script("window.closeLoveLetter();")
            c1 = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            body_overflow_c1 = driver.execute_script("return document.body.style.overflow;")
            body_class_c1 = driver.execute_script("return document.body.className;")

            driver.execute_script("window.openLoveLetter();")
            c2 = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            letter_display_c2 = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            body_overflow_c2 = driver.execute_script("return document.body.style.overflow;")

            passed = (
                "overlay-hidden" in c1 and
                "overflow-hidden" not in body_class_c1 and
                body_overflow_c1 != "hidden" and
                "overlay-hidden" not in c2 and
                "is-revealed" in c2 and
                letter_display_c2 == "block" and
                body_overflow_c2 == "hidden"
            )
            self.record("Programmatic Open/Close API", "Modal Lifecycle", passed,
                        "Verify window.openLoveLetter() and window.closeLoveLetter() manage overlay and scroll lock",
                        {"close_state": {"classes": c1, "overflow": body_overflow_c1},
                         "open_state": {"classes": c2, "display": letter_display_c2, "overflow": body_overflow_c2}})
        finally:
            driver.quit()

    def test_escape_key_dismissal(self):
        driver = create_driver()
        try:
            driver.execute_script("window.openLoveLetter();")
            time.sleep(0.1)

            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(0.2)

            classes = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            body_overflow = driver.execute_script("return document.body.style.overflow;")
            passed = "overlay-hidden" in classes and body_overflow != "hidden"

            self.record("Keyboard Escape Key Dismissal", "Modal Lifecycle", passed,
                        "Verify Escape key press closes the love letter modal and unfreezes body scroll",
                        {"classes": classes, "body_overflow": body_overflow})
        finally:
            driver.quit()

    def test_backdrop_click_dismissal(self):
        """BACKDROP CLICK TEST:
        When the love letter modal is open, clicking on the backdrop area
        (outside the letter card) should close the modal.
        """
        driver = create_driver()
        try:
            driver.execute_script("window.openLoveLetter();")
            time.sleep(0.2)

            overlay = driver.find_element(By.ID, "gift-reveal-overlay")

            actions = ActionChains(driver)
            actions.w3c_actions.pointer_action.move_to_location(20, 20)
            actions.w3c_actions.pointer_action.click()
            actions.perform()
            time.sleep(0.3)

            classes = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            has_hidden = "overlay-hidden" in classes
            passed = has_hidden

            evidence = {
                "classes_after_backdrop_click": classes,
                "overlay_hidden_present": has_hidden
            }
            self.record("Backdrop Click Dismissal", "Modal Lifecycle", passed,
                        "Verify clicking backdrop outside letter card closes the modal",
                        evidence)
        finally:
            driver.quit()

    def test_rapid_modal_toggling(self):
        driver = create_driver()
        try:
            res = driver.execute_script("""
                let err = null;
                try {
                    for (let i = 0; i < 20; i++) {
                        if (i % 2 === 0) window.closeLoveLetter();
                        else window.openLoveLetter();
                    }
                } catch(e) {
                    err = e.message;
                }
                return { error: err };
            """)

            classes = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            errors = check_browser_errors(driver)

            passed = res["error"] is None and len(errors) == 0
            self.record("20x Rapid Modal Toggle", "Modal Lifecycle", passed,
                        "Verify 20 rapid toggles between openLoveLetter() and closeLoveLetter() execute without error",
                        {"res": res, "final_classes": classes, "errors": errors})
        finally:
            driver.quit()

    # =========================================================================
    # SUITE 4: STATE TRANSITION TO MAIN CHAPTERS
    # =========================================================================
    def test_btn_unfold_memories_transition(self):
        driver = create_driver()
        try:
            driver.execute_script("window.unwrapGift();")
            time.sleep(1.6)

            btn = driver.find_element(By.ID, "btn-unfold-memories")
            btn.click()
            time.sleep(0.3)

            overlay_classes = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            body_overflow = driver.execute_script("return document.body.style.overflow;")
            milestones_hidden = driver.execute_script("return document.getElementById('view-milestones').classList.contains('hidden');")
            milestones_nav_active = driver.execute_script("return document.getElementById('nav-milestones').classList.contains('active');")
            milestones_pill_active = driver.execute_script("return document.getElementById('step-btn-milestones').classList.contains('active');")
            story_hidden = driver.execute_script("return document.getElementById('view-story').classList.contains('hidden');")
            matchup_hidden = driver.execute_script("return document.getElementById('view-matchup').classList.contains('hidden');")
            errors = check_browser_errors(driver)

            passed = (
                "overlay-hidden" in overlay_classes and
                body_overflow != "hidden" and
                milestones_hidden is False and
                milestones_nav_active is True and
                milestones_pill_active is True and
                story_hidden is True and
                matchup_hidden is True and
                len(errors) == 0
            )
            evidence = {
                "overlay_classes": overlay_classes,
                "body_overflow": body_overflow,
                "view_milestones_hidden": milestones_hidden,
                "nav_milestones_active": milestones_nav_active,
                "step_btn_milestones_active": milestones_pill_active,
                "view_story_hidden": story_hidden,
                "view_matchup_hidden": matchup_hidden,
                "errors": errors
            }
            self.record("Unfold Memories Transition to Milestones", "Chapter Transitions", passed,
                        "Verify #btn-unfold-memories closes modal and activates Milestones view and navigation indicators",
                        evidence)
        finally:
            driver.quit()

    def test_go_to_chapter_contract(self):
        driver = create_driver()
        try:
            routes = ['milestones', 'polaroids', 'chat', 'trivia', 'reveal']
            results = {}

            for r in routes:
                driver.execute_script(f"window.goToChapter('{r}');")
                time.sleep(0.2)
                ov_classes = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
                if r == 'reveal':
                    results[r] = ("is-revealed" in ov_classes and "overlay-hidden" not in ov_classes)
                else:
                    results[r] = ("overlay-hidden" in ov_classes)

            passed = all(results.values())
            errors = check_browser_errors(driver)

            self.record("window.goToChapter Interface Contract", "Chapter Transitions", passed and len(errors) == 0,
                        "Verify window.goToChapter switches views and opens/closes reveal overlay according to PROJECT.md",
                        {"results": results, "errors": errors})
        finally:
            driver.quit()

    # =========================================================================
    # SUITE 5: AUDIO & HAPTIC RESILIENCE UNDER RESTRICTIONS
    # =========================================================================
    def test_celebration_effects_without_audio_haptics(self):
        driver = create_driver()
        try:
            driver.execute_script("""
                window.AudioContext = undefined;
                window.webkitAudioContext = undefined;
                window.unwrapGift();
            """)
            time.sleep(1.6)

            classes = driver.execute_script("return document.getElementById('gift-reveal-overlay').className;")
            letter_disp = driver.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
            errors = check_browser_errors(driver)

            passed = (
                "is-revealed" in classes and
                letter_disp == "block" and
                len(errors) == 0
            )
            self.record("Audio/Haptic Fallback Safety", "Hardware Fallback", passed,
                        "Verify unwrapGift completes smoothly even when AudioContext and navigator.vibrate are unavailable",
                        {"classes": classes, "letter_disp": letter_disp, "errors": errors})
        finally:
            driver.quit()

    # =========================================================================
    # SUMMARY
    # =========================================================================
    def run_all(self):
        print("=" * 70)
        print("STARTING MILSTONE 1 EMPIRICAL STRESS TESTS")
        print("=" * 70)
        self.test_rapid_double_click()
        self.test_rapid_burst_clicks()
        self.test_click_during_opening_transition()
        self.test_single_replay_cycle()
        self.test_repeated_rapid_replay_calls()
        self.test_replay_during_active_unwrap_race()
        self.test_multi_cycle_unwrap_replay()
        self.test_open_and_close_love_letter_api()
        self.test_escape_key_dismissal()
        self.test_backdrop_click_dismissal()
        self.test_rapid_modal_toggling()
        self.test_btn_unfold_memories_transition()
        self.test_go_to_chapter_contract()
        self.test_celebration_effects_without_audio_haptics()

        print("=" * 70)
        passes = sum(1 for r in self.results if r["status"] == "PASS")
        fails = sum(1 for r in self.results if r["status"] == "FAIL")
        print(f"RESULTS: Total: {len(self.results)}, Passed: {passes}, Failed: {fails}")
        print("=" * 70)

        out_path = Path(__file__).resolve().parent / "stress_test_results.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2)
        print(f"Results written to: {out_path}")
        return fails

if __name__ == "__main__":
    runner = StressTestMilestone1()
    sys.exit(runner.run_all())
