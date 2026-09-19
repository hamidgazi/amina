"""
Dedicated Empirical Probe for Edge Cases and Race Conditions
Milestone 1 - Amina 23rd Birthday Web App
"""

import time
import json
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

HTML_PATH = Path(__file__).resolve().parent.parent / "Instagram_Chat_Analysis_Amina_Hamid.html"
FILE_URL = HTML_PATH.as_uri()

def get_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    opts.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    d = webdriver.Chrome(options=opts)
    d.get(FILE_URL)
    time.sleep(0.5)
    return d

def run_probe():
    results = {}

    # -------------------------------------------------------------
    # PROBE 1: BACKDROP CLICK ON LOVE LETTER MODAL
    # -------------------------------------------------------------
    d1 = get_driver()
    try:
        # Open love letter
        d1.execute_script("window.openLoveLetter();")
        time.sleep(0.3)

        overlay = d1.find_element(By.ID, "gift-reveal-overlay")
        card = d1.find_element(By.ID, "letter-card-container")

        # Click outside the card (e.g., coordinate (25, 25))
        actions = ActionChains(d1)
        actions.move_to_element_with_offset(overlay, 25, 25).click().perform()
        time.sleep(0.3)

        classes = d1.execute_script("return document.getElementById('gift-reveal-overlay').className;")
        results["backdrop_click_closed_modal"] = "overlay-hidden" in classes
        results["backdrop_click_classes"] = classes
    finally:
        d1.quit()

    # -------------------------------------------------------------
    # PROBE 2: ESCAPE KEY DURING OPENING ANIMATION
    # -------------------------------------------------------------
    d2 = get_driver()
    try:
        d2.execute_script("window.unwrapGift();")
        time.sleep(0.3) # mid opening animation

        # Press Escape key
        d2.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(0.2)
        classes_t500 = d2.execute_script("return document.getElementById('gift-reveal-overlay').className;")

        # Wait past 1300ms unwrap timer
        time.sleep(1.2)
        classes_t1700 = d2.execute_script("return document.getElementById('gift-reveal-overlay').className;")
        box_disp = d2.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
        letter_disp = d2.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")

        results["escape_during_animation"] = {
            "classes_immediately_after_escape": classes_t500,
            "classes_after_unwrap_timer_fires": classes_t1700,
            "box_display": box_disp,
            "letter_display": letter_disp
        }
    finally:
        d2.quit()

    # -------------------------------------------------------------
    # PROBE 3: REPLAY CALL DURING UNWRAP ANIMATION (TIMER HIJACK)
    # -------------------------------------------------------------
    d3 = get_driver()
    try:
        d3.execute_script("window.unwrapGift();")
        time.sleep(0.2) # 200ms

        # Trigger replay while unwrap timer is active
        d3.execute_script("window.replayGiftUnwrap();")
        time.sleep(0.4) # 600ms total

        box_disp_after_replay = d3.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
        letter_disp_after_replay = d3.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")

        # Wait for unwrap timer (1300ms) to fire
        time.sleep(1.0) # 1600ms total
        box_disp_after_lingering_timer = d3.execute_script("return window.getComputedStyle(document.getElementById('gift-box-stage')).display;")
        letter_disp_after_lingering_timer = d3.execute_script("return window.getComputedStyle(document.getElementById('gift-letter-stage')).display;")
        classes_after_lingering_timer = d3.execute_script("return document.getElementById('gift-reveal-overlay').className;")

        results["replay_unwrap_timer_hijack"] = {
            "box_disp_after_replay": box_disp_after_replay,
            "letter_disp_after_replay": letter_disp_after_replay,
            "box_disp_after_lingering_timer": box_disp_after_lingering_timer,
            "letter_disp_after_lingering_timer": letter_disp_after_lingering_timer,
            "classes_after_lingering_timer": classes_after_lingering_timer,
            "hijacked": (box_disp_after_lingering_timer == "none" and letter_disp_after_lingering_timer == "block")
        }
    finally:
        d3.quit()

    # -------------------------------------------------------------
    # PROBE 4: BTN-UNFOLD-MEMORIES STATE TRANSITION
    # -------------------------------------------------------------
    d4 = get_driver()
    try:
        d4.execute_script("window.unwrapGift();")
        time.sleep(1.6)

        btn = d4.find_element(By.ID, "btn-unfold-memories")
        btn.click()
        time.sleep(0.3)

        overlay_classes = d4.execute_script("return document.getElementById('gift-reveal-overlay').className;")
        milestones_hidden = d4.execute_script("return document.getElementById('view-milestones').classList.contains('hidden');")
        nav_milestones_active = d4.execute_script("return document.getElementById('nav-milestones').classList.contains('active');")
        step_btn_active = d4.execute_script("return document.getElementById('step-btn-milestones').classList.contains('active');")

        results["unfold_memories_transition"] = {
            "overlay_classes": overlay_classes,
            "modal_closed": "overlay-hidden" in overlay_classes,
            "milestones_revealed": not milestones_hidden,
            "milestones_nav_active": nav_milestones_active,
            "step_btn_active": step_btn_active
        }
    finally:
        d4.quit()

    # -------------------------------------------------------------
    # PROBE 5: CONSOLE INTERVENTIONS & ERRORS
    # -------------------------------------------------------------
    d5 = get_driver()
    try:
        d5.execute_script("window.unwrapGift();")
        time.sleep(1.6)
        logs = d5.get_log("browser")
        results["console_logs"] = [l for l in logs if l.get("level") in ["SEVERE", "ERROR", "WARNING"]]
    finally:
        d5.quit()

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    run_probe()
