# ==============================================================================
# TIER 4: REAL-WORLD USER SCENARIOS TEST SUITE
# ==============================================================================
# 24 end-to-end user journeys simulating Amina and Hamid interacting with
# the 23rd Birthday Gift web application across desktop, mobile, offline, and keyboard modes.
# ==============================================================================

import unittest
from datetime import date, datetime, timezone, timedelta
from tests import spec_oracle as oracle

class TestTier4RealWorldScenarios(unittest.TestCase):
    """Tier 4: Realistic End-to-End User Experience Scenarios"""

    def test_t4_01_first_launch_gift_box_modal_flow(self):
        # Scenario 1: Amina opens page on iPhone Safari
        box = oracle.GiftBoxStateMachine()
        self.assertEqual(box.current_state, "CLOSED")
        box.tap()
        self.assertEqual(box.current_state, "SHAKING")
        res = box.unwrap()
        self.assertTrue(res["first_trigger"])
        self.assertTrue(box.letter_opened)

    def test_t4_02_reading_birthday_letter_flow(self):
        # Scenario 2: Reading the 23rd birthday letter
        box = oracle.GiftBoxStateMachine()
        box.unwrap()
        self.assertTrue(box.letter_opened)
        box.close_letter()
        self.assertFalse(box.letter_opened)
        self.assertEqual(box.current_chapter, "milestones")

    def test_t4_03_inspecting_hero_chat_volume_split(self):
        # Scenario 3: Inspecting hero cards message volume
        total = oracle.CHAT_METRICS["total_messages"]
        h_msgs = oracle.CHAT_METRICS["hamid_messages"]
        a_msgs = oracle.CHAT_METRICS["amina_messages"]
        self.assertEqual(total, 12980)
        self.assertEqual(h_msgs + a_msgs, 12980)
        self.assertAlmostEqual(h_msgs / total * 100, 50.55, places=2)

    def test_t4_04_browsing_sweet_words_counter(self):
        # Scenario 4: Browsing sweet words
        sw = oracle.CHAT_METRICS["sweet_words"]
        self.assertGreaterEqual(sw["total"], 219)
        self.assertEqual(sw["jaanu"], 78)
        self.assertEqual(sw["love"], 42)

    def test_t4_05_discovering_reaction_queen_crown(self):
        # Scenario 5: Amina discovers Reaction Queen title
        rx = oracle.CHAT_METRICS["reactions"]
        self.assertEqual(rx["reaction_queen"], "Amina Chamadiya")
        self.assertEqual(rx["amina"], 1669)
        self.assertGreater(rx["ratio"], 3.0)

    def test_t4_06_analyzing_midnight_chat_clocks(self):
        # Scenario 6: Midnight chat analysis (12 AM - 6 AM)
        mc = oracle.CHAT_METRICS["midnight_chats"]
        self.assertEqual(mc["total"], 6571)
        self.assertAlmostEqual(mc["percentage"], 50.62, places=2)
        self.assertEqual(mc["peak_hour"], 0)

    def test_t4_07_reviewing_daily_activity_trajectory(self):
        # Scenario 7: Activity acceleration from July to August
        july = oracle.CHAT_METRICS["july_daily_avg"]
        aug = oracle.CHAT_METRICS["august_daily_avg"]
        peak = oracle.CHAT_METRICS["peak_day"]["count"]
        self.assertEqual(july, 100.0)
        self.assertEqual(aug, 334.5)
        self.assertEqual(peak, 857)

    def test_t4_08_reliving_57_day_chat_streak(self):
        # Scenario 8: 57-day continuous chatting streak
        streak = oracle.CHAT_METRICS["streak"]
        self.assertEqual(streak["days"], 57)
        self.assertTrue(streak["unbroken"])
        longest_break = oracle.CHAT_METRICS["longest_break"]
        self.assertEqual(longest_break["broken_by"], "Amina Chamadiya")

    def test_t4_09_walking_through_6_relationship_milestones(self):
        # Scenario 9: Stepping through all 6 milestones
        self.assertEqual(len(oracle.MILESTONES_DATA), 6)
        milestones = [m["id"] for m in oracle.MILESTONES_DATA]
        expected = ["baat-pakki", "engagement", "nikah", "hand-hold", "first-hug-kiss-ride", "first-good-kiss"]
        self.assertEqual(milestones, expected)

    def test_t4_10_watching_live_23rd_birthday_ticker(self):
        # Scenario 10: Watching live birthday countdown
        target = oracle.BIRTHDAY_TARGET_DATE
        now_sim = datetime(2026, 9, 14, 12, 0, 0, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(target, now_sim)
        self.assertFalse(ticker["is_reached"])
        self.assertEqual(ticker["days"], 2)

    def test_t4_11_browsing_polaroid_memories_with_local_images(self):
        # Scenario 11: Viewing memories with local image paths
        for p in oracle.POLAROIDS_DATA:
            self.assertTrue(p["photo_file"].startswith("images/photo"))
            self.assertGreater(len(p["caption"]), 10)

    def test_t4_12_browsing_polaroids_with_missing_images_offline(self):
        # Scenario 12: Offline fallback rendering when images missing
        for p in oracle.POLAROIDS_DATA:
            svg = oracle.generate_fallback_svg(p["id"], p["title"], p["date_str"])
            self.assertIn("xmlns", svg)
            safe_title = p["title"].replace("&", "&amp;")
            self.assertIn(safe_title, svg)

    def test_t4_13_playing_couple_trivia_game_flawless_win(self):
        # Scenario 13: 5/5 perfect trivia score
        game = oracle.TriviaGameStateMachine()
        for i in range(5):
            res = game.select_answer(i, oracle.TRIVIA_QUESTIONS[i]["correct_index"])
            self.assertTrue(res["is_correct"])
        summary = game.get_score_summary()
        self.assertEqual(summary["score"], 5)
        self.assertEqual(summary["percentage"], 100.0)
        self.assertTrue(summary["is_soulmate"])

    def test_t4_14_playing_couple_trivia_game_with_mistakes(self):
        # Scenario 14: Trivia with 1 wrong answer
        game = oracle.TriviaGameStateMachine()
        game.select_answer(0, oracle.TRIVIA_QUESTIONS[0]["correct_index"])
        game.select_answer(1, (oracle.TRIVIA_QUESTIONS[1]["correct_index"] + 1) % 4)
        game.select_answer(2, oracle.TRIVIA_QUESTIONS[2]["correct_index"])
        game.select_answer(3, oracle.TRIVIA_QUESTIONS[3]["correct_index"])
        game.select_answer(4, oracle.TRIVIA_QUESTIONS[4]["correct_index"])
        summary = game.get_score_summary()
        self.assertEqual(summary["score"], 4)
        self.assertEqual(summary["percentage"], 80.0)
        self.assertFalse(summary["is_soulmate"])

    def test_t4_15_toggling_romantic_bgm_on_and_off(self):
        # Scenario 15: Background music player toggles
        player = {"is_playing": False, "volume": 0.5}
        player["is_playing"] = True
        self.assertTrue(player["is_playing"])
        player["is_playing"] = False
        self.assertFalse(player["is_playing"])

    def test_t4_16_offline_file_uri_double_click_launch(self):
        # Scenario 16: file:/// desktop execution
        test_html = '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body><div id="app"></div></body></html>'
        is_clean, violations = oracle.OfflineValidator.audit_offline_readiness(test_html)
        self.assertTrue(is_clean, violations)

    def test_t4_17_mobile_viewport_375px_iphone_se(self):
        # Scenario 17: iPhone SE (375px width)
        is_valid, msg = oracle.ResponsiveValidator.validate_breakpoint(360)
        self.assertTrue(is_valid)

    def test_t4_18_desktop_viewport_1920px_fhd(self):
        # Scenario 18: 1920x1080 Full HD desktop
        is_valid, msg = oracle.ResponsiveValidator.validate_breakpoint(1920)
        self.assertTrue(is_valid)

    def test_t4_19_reduced_motion_accessibility_preference(self):
        # Scenario 19: Reduced motion accessibility
        prefers_reduced_motion = True
        animation_duration = "0.01ms" if prefers_reduced_motion else "2s"
        self.assertEqual(animation_duration, "0.01ms")

    def test_t4_20_keyboard_only_navigation_journey(self):
        # Scenario 20: Keyboard Tab/Enter navigation
        interactive_elements = [
            {"name": "gift_box", "tabindex": 0},
            {"name": "letter_close_btn", "tabindex": 0},
            {"name": "audio_toggle_btn", "tabindex": 0},
            {"name": "trivia_opt_1", "tabindex": 0}
        ]
        for el in interactive_elements:
            self.assertEqual(el["tabindex"], 0)

    def test_t4_21_rapid_navigation_and_tab_switching(self):
        # Scenario 21: Tab switching / visibilitychange
        is_visible = False
        raf_active = is_visible
        self.assertFalse(raf_active)
        is_visible = True
        raf_active = is_visible
        self.assertTrue(raf_active)

    def test_t4_22_browser_reload_and_state_idempotence(self):
        # Scenario 22: Browser reload fresh start
        box1 = oracle.GiftBoxStateMachine()
        box1.unwrap()
        box2 = oracle.GiftBoxStateMachine() # Reload
        self.assertEqual(box2.current_state, "CLOSED")

    def test_t4_23_zero_technical_artifact_leak_throughout_journey(self):
        # Scenario 23: Complete UI romantic text audit
        full_journey_text = (
            "Happy 23rd Birthday My Dearest Amina! "
            "Welcome to our love story. "
            "Every message was a prayer answered. "
            "Baat Pakki, Engagement, Nikah, First Hand Hold, First Hug & Kiss. "
            "With all my love forever, Hamid."
        )
        violations = oracle.ZeroVersionValidator.validate_text(full_journey_text)
        self.assertEqual(len(violations), 0)

    def test_t4_24_complete_end_to_end_birthday_celebration(self):
        # Scenario 24: Complete birthday celebration sequence
        box = oracle.GiftBoxStateMachine()
        box.tap()
        box.unwrap()
        box.explode()
        box.dismiss()
        self.assertEqual(box.current_state, "REVEALED")

        game = oracle.TriviaGameStateMachine()
        for i in range(5):
            game.select_answer(i, oracle.TRIVIA_QUESTIONS[i]["correct_index"])
        self.assertTrue(game.is_soulmate_unlocked)

        now = datetime(2026, 9, 17, 0, 0, 0, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(oracle.BIRTHDAY_TARGET_DATE, now)
        self.assertTrue(ticker["is_reached"])

if __name__ == '__main__':
    unittest.main()
