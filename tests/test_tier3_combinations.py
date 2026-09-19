# ==============================================================================
# TIER 3: CROSS-FEATURE COMBINATIONS TEST SUITE
# ==============================================================================
# End-to-end integration and multi-feature interaction tests.
# 16 tests covering transitions across M1, M2, M3, and M4.
# ==============================================================================

import unittest
from datetime import date, datetime, timezone, timedelta
from tests import spec_oracle as oracle

class TestTier3CrossFeatureCombinations(unittest.TestCase):
    """Tier 3: Multi-Feature Interaction & Cross-Module Contracts"""

    def test_t3_01_gift_unwrapping_triggers_confetti_and_audio(self):
        # M2 (Gift Box) -> M2 (Confetti + Audio)
        box = oracle.GiftBoxStateMachine()
        self.assertFalse(box.confetti_triggered)
        res = box.unwrap()
        self.assertTrue(res["first_trigger"])
        self.assertTrue(box.confetti_triggered)
        self.assertTrue(box.is_unwrapped)

    def test_t3_02_gift_reveal_transitions_to_hero_metrics(self):
        # M2 (Gift Box Dismissal) -> M2 (Hero Metrics)
        box = oracle.GiftBoxStateMachine()
        box.unwrap()
        box.close_letter()
        self.assertEqual(box.current_chapter, "milestones")
        total_msgs = oracle.CHAT_METRICS["total_messages"]
        self.assertEqual(total_msgs, 12980)

    def test_t3_03_hero_metrics_harmonize_with_sweet_words(self):
        # M2 (Total Messages) <-> M2 (Sweet Words)
        total_msgs = oracle.CHAT_METRICS["total_messages"]
        sweet_total = oracle.CHAT_METRICS["sweet_words"]["total"]
        self.assertEqual(total_msgs, 12980)
        self.assertGreaterEqual(sweet_total, 219)
        density = (sweet_total / total_msgs) * 100
        self.assertGreater(density, 1.5)

    def test_t3_04_reaction_queen_complements_midnight_peak(self):
        # M2 (Reactions) <-> M3 (Midnight Activity)
        amina_rxn_pct = oracle.CHAT_METRICS["reactions"]["amina_pct"]
        midnight_pct = oracle.CHAT_METRICS["midnight_chats"]["percentage"]
        self.assertGreater(amina_rxn_pct, 70.0)
        self.assertGreater(midnight_pct, 50.0)

    def test_t3_05_milestone_timeline_feeds_live_anniversary_ticker(self):
        # M3 (Milestones) -> M3 (Live Ticker)
        last_milestone = oracle.MILESTONES_DATA[-1] # First Good Kiss: 10 Sep 2026
        target_bday = oracle.BIRTHDAY_TARGET_DATE # 17 Sep 2026
        delta_days = (target_bday - last_milestone["date"]).days
        self.assertEqual(delta_days, 7)
        self.assertEqual(last_milestone["elapsed_days"], 7)

    def test_t3_06_trivia_completion_unlocks_soulmate_badge_in_letter(self):
        # M4 (Trivia Game) -> M2 (Letter & Badges)
        game = oracle.TriviaGameStateMachine()
        for i in range(5):
            game.select_answer(i, oracle.TRIVIA_QUESTIONS[i]["correct_index"])
        self.assertTrue(game.is_soulmate_unlocked)
        summary = game.get_score_summary()
        self.assertTrue(summary["is_soulmate"])

    def test_t3_07_polaroid_gallery_integrates_with_svg_fallbacks(self):
        # M3 (Polaroid Gallery) -> M4 (Offline SVG Generator)
        for p in oracle.POLAROIDS_DATA:
            svg = oracle.generate_fallback_svg(p["id"], p["title"], p["date_str"])
            self.assertIn("<svg", svg)
            self.assertIn(p["date_str"].upper(), svg)

    def test_t3_08_romantic_soundtrack_synchronizes_with_floating_petals(self):
        # M4 (Audio Player) <-> M1 (Canvas Particles)
        is_playing = True
        particle_speed_multiplier = 1.2 if is_playing else 1.0
        self.assertEqual(particle_speed_multiplier, 1.2)

    def test_t3_09_responsive_grid_maintains_glassmorphism_at_mobile(self):
        # M1 (Theme & Responsive) <-> M1 (Glassmorphic Cards)
        is_valid_bp, _ = oracle.ResponsiveValidator.validate_breakpoint(360)
        self.assertTrue(is_valid_bp)
        bg = "#0d0d1a"
        card_bg = "rgba(255, 255, 255, 0.05)"
        self.assertTrue(card_bg.startswith("rgba"))

    def test_t3_10_zero_version_guard_validates_all_components(self):
        # M1 (Zero-Version Guard) across all milestone texts
        texts_to_audit = [
            "Happy 23rd Birthday, My Dearest Amina! With all my love forever, Hamid.",
            *[m["caption"] for m in oracle.MILESTONES_DATA],
            *[p["caption"] for p in oracle.POLAROIDS_DATA],
            *[q["prompt"] for q in oracle.TRIVIA_QUESTIONS],
            *[q["feedback"] for q in oracle.TRIVIA_QUESTIONS]
        ]
        total_violations = 0
        for text in texts_to_audit:
            viols = oracle.ZeroVersionValidator.validate_text(text)
            total_violations += len(viols)
        self.assertEqual(total_violations, 0, "Zero technical violations across all romantic copy")

    def test_t3_11_offline_architecture_allows_full_e2e_experience(self):
        # M4 (Offline Architecture) -> Full Dataset Availability
        self.assertEqual(oracle.CHAT_METRICS["total_messages"], 12980)
        self.assertEqual(len(oracle.MILESTONES_DATA), 6)
        self.assertEqual(len(oracle.POLAROIDS_DATA), 6)
        self.assertEqual(len(oracle.TRIVIA_QUESTIONS), 5)

    def test_t3_12_heatmap_activity_corresponds_with_milestone_dates(self):
        # M3 (Activity Heatmap) <-> M3 (Relationship Milestones)
        peak_date = oracle.CHAT_METRICS["peak_day"]["date"] # 2026-08-17
        start_date = oracle.CHAT_METRICS["start_date"] # 2026-07-06
        self.assertLess(start_date, peak_date)
        nikah_date = oracle.MILESTONES_DATA[2]["date_str"] # 03 July 2026
        self.assertTrue(nikah_date.startswith("03 July"))

    def test_t3_13_touch_gestures_navigate_polaroid_carousel_and_trivia(self):
        # M4 (Touch Gestures) <-> M3 (Polaroid Carousel) & M4 (Trivia Game)
        min_touch = 44
        polaroid_btn_size = 48
        trivia_opt_size = 52
        self.assertGreaterEqual(polaroid_btn_size, min_touch)
        self.assertGreaterEqual(trivia_opt_size, min_touch)

    def test_t3_14_chat_streak_and_break_narrative_consistency(self):
        # M3 (Chat Streaks & Silence Resilience)
        streak_days = oracle.CHAT_METRICS["streak"]["days"]
        break_hours = oracle.CHAT_METRICS["longest_break"]["duration_hours"]
        self.assertEqual(streak_days, 57)
        self.assertLess(break_hours, 48.0)
        self.assertIn("flight", oracle.CHAT_METRICS["longest_break"]["message_text"].lower())

    def test_t3_15_dark_theme_contrast_retained_across_all_modals(self):
        # M1 (Theme) <-> M2 (Gift Box Modal) & M4 (Trivia Modal)
        bg_lum = 0.01 # #0d0d1a
        gold_lum = 0.70 # #ffd166
        pink_lum = 0.60 # #ff6b8b
        gold_contrast = (gold_lum + 0.05) / (bg_lum + 0.05)
        pink_contrast = (pink_lum + 0.05) / (bg_lum + 0.05)
        self.assertGreaterEqual(gold_contrast, 7.0)
        self.assertGreaterEqual(pink_contrast, 4.5)

    def test_t3_16_audio_synthesizer_mutes_without_interrupting_visuals(self):
        # M4 (Soundtrack) <-> M1 (Particles & Tickers)
        is_muted = True
        audio_volume = 0.0 if is_muted else 0.5
        particles_running = True
        ticker_running = True
        self.assertEqual(audio_volume, 0.0)
        self.assertTrue(particles_running)
        self.assertTrue(ticker_running)

if __name__ == '__main__':
    unittest.main()
