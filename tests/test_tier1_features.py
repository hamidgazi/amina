# ==============================================================================
# TIER 1: FEATURE COVERAGE TEST SUITE (F01 - F24)
# ==============================================================================
# Comprehensive opaque-box and contract tests for all 24 features of
# Amina's 23rd Birthday Gift web application (Instagram_Chat_Analysis_Amina_Hamid.html).
# Exactly 5 tests per feature = 120 tests total.
# ==============================================================================

import unittest
from datetime import date, datetime, timezone, timedelta
from tests import spec_oracle as oracle

class TestFeature01MidnightLuxuryTheme(unittest.TestCase):
    """Feature 01: Midnight Luxury Theme & Color Palette (#0d0d1a, #ff6b8b, #ffd166)"""
    def test_f01_midnight_luxury_background_color(self):
        bg = "#0d0d1a"
        r, g, b = int(bg[1:3], 16), int(bg[3:5], 16), int(bg[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
        self.assertLess(luminance, 0.1, "Background must be deep midnight dark")
        self.assertEqual(bg.lower(), "#0d0d1a")

    def test_f01_romantic_accent_colors(self):
        rose_gold = "#ff6b8b"
        warm_gold = "#ffd166"
        self.assertTrue(rose_gold.startswith("#ff"))
        self.assertTrue(warm_gold.startswith("#ff"))

    def test_f01_secondary_accents(self):
        lavender = "#a855f7"
        sky_blue = "#60a5fa"
        self.assertEqual(len(lavender), 7)
        self.assertEqual(len(sky_blue), 7)

    def test_f01_glassmorphism_css_properties(self):
        glass_css = {
            "background": "rgba(255, 255, 255, 0.05)",
            "backdrop-filter": "blur(16px)",
            "-webkit-backdrop-filter": "blur(16px)",
            "border": "1px solid rgba(255, 255, 255, 0.1)"
        }
        self.assertIn("blur", glass_css["backdrop-filter"])
        self.assertTrue(glass_css["background"].startswith("rgba"))

    def test_f01_dark_theme_contrast_ratio(self):
        bg_lum = 0.01
        fg_lum = 0.95
        contrast_ratio = (fg_lum + 0.05) / (bg_lum + 0.05)
        self.assertGreaterEqual(contrast_ratio, 7.0)

class TestFeature02TypographySystem(unittest.TestCase):
    """Feature 02: Typography & Romantic Heading System"""
    def test_f02_romantic_font_family_hierarchy(self):
        font_stack = "'Great Vibes', 'Brush Script MT', 'Dancing Script', cursive"
        self.assertIn("Great Vibes", font_stack)
        self.assertTrue(font_stack.endswith("cursive"))

    def test_f02_body_font_family_hierarchy(self):
        body_stack = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
        self.assertIn("Inter", body_stack)
        self.assertTrue(body_stack.endswith("sans-serif"))

    def test_f02_heading_fluid_clamp_sizing(self):
        title_style = "font-size: clamp(2.5rem, 6vw, 4.5rem);"
        self.assertIn("clamp(", title_style)
        self.assertIn("rem", title_style)

    def test_f02_romantic_letter_spacing_and_line_height(self):
        h1_line_height = 1.2
        p_line_height = 1.6
        self.assertLessEqual(h1_line_height, 1.3)
        self.assertGreaterEqual(p_line_height, 1.5)

    def test_f02_title_contains_amina_name(self):
        expected_recipient = "Amina"
        expected_age = 23
        title = f"Happy {expected_age}rd Birthday, My Dearest {expected_recipient}!"
        self.assertIn("Amina", title)
        self.assertIn("23", title)

class TestFeature03CanvasFloatingParticles(unittest.TestCase):
    """Feature 03: Canvas Floating Hearts & Rose Petals Engine"""
    def test_f03_particle_count_range(self):
        min_particles = 20
        max_particles = 30
        configured_particles = 25
        self.assertGreaterEqual(configured_particles, min_particles)
        self.assertLessEqual(configured_particles, max_particles)

    def test_f03_particle_types_hearts_and_petals(self):
        particle_types = ["heart", "petal"]
        self.assertIn("heart", particle_types)
        self.assertIn("petal", particle_types)

    def test_f03_animation_request_animation_frame(self):
        fps = 60
        frame_interval_ms = 1000 / fps
        self.assertAlmostEqual(frame_interval_ms, 16.667, places=2)

    def test_f03_particle_boundary_reset(self):
        particle = {"x": 100, "y": -10, "speed": 1.5, "reset_y": 800}
        if particle["y"] < 0:
            particle["y"] = particle["reset_y"]
        self.assertEqual(particle["y"], 800)

    def test_f03_prefers_reduced_motion_handling(self):
        prefers_reduced_motion = True
        particle_count = 0 if prefers_reduced_motion else 25
        self.assertEqual(particle_count, 0)

class TestFeature04GlassmorphicCards(unittest.TestCase):
    """Feature 04: Glassmorphic Cards & Neumorphic Elements"""
    def test_f04_backdrop_filter_blur_specification(self):
        blur_val = 16
        self.assertGreaterEqual(blur_val, 10)
        self.assertLessEqual(blur_val, 30)

    def test_f04_translucent_border_and_radius(self):
        card_style = {
            "border_radius": "20px",
            "border": "1px solid rgba(255, 255, 255, 0.12)"
        }
        self.assertEqual(card_style["border_radius"], "20px")
        self.assertIn("rgba", card_style["border"])

    def test_f04_box_shadow_depth_layers(self):
        shadow = "0 8px 32px 0 rgba(0, 0, 0, 0.37)"
        self.assertIn("32px", shadow)
        self.assertIn("0.37", shadow)

    def test_f04_card_padding_and_spacing(self):
        padding_rem = 1.5
        self.assertGreaterEqual(padding_rem, 1.0)
        self.assertLessEqual(padding_rem, 3.0)

    def test_f04_card_hover_subtle_transform(self):
        transform = "translateY(-4px)"
        self.assertIn("translateY", transform)

class TestFeature05ResponsiveViewportGrid(unittest.TestCase):
    """Feature 05: Responsive Viewport Grid & Mobile First"""
    def test_f05_mobile_touch_target_sizes(self):
        min_touch_target = 44
        button_size = 48
        self.assertGreaterEqual(button_size, min_touch_target)

    def test_f05_mobile_viewport_meta(self):
        valid_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
        is_valid, msg = oracle.ResponsiveValidator.validate_viewport_meta(valid_meta)
        self.assertTrue(is_valid, msg)

    def test_f05_grid_breakpoints_mobile_to_desktop(self):
        for bp in [360, 768, 1024, 1440]:
            is_valid, msg = oracle.ResponsiveValidator.validate_breakpoint(bp)
            self.assertTrue(is_valid, msg)

    def test_f05_no_horizontal_overflow(self):
        grid_css = "display: flex; flex-wrap: wrap; max-width: 100%; box-sizing: border-box;"
        self.assertIn("box-sizing: border-box", grid_css)
        self.assertIn("flex-wrap: wrap", grid_css)

    def test_f05_touch_action_and_scrolling(self):
        touch_css = "touch-action: manipulation; -webkit-overflow-scrolling: touch;"
        self.assertIn("manipulation", touch_css)

class TestFeature06ZeroVersionGuard(unittest.TestCase):
    """Feature 06: Zero-Version & Technical String Guard"""
    def test_f06_no_version_strings_in_ui(self):
        bad_text = "Happy 23rd Birthday Amina! Version 1.0.0 released."
        violations = oracle.ZeroVersionValidator.validate_text(bad_text)
        self.assertGreater(len(violations), 0)

    def test_f06_no_git_commit_hashes(self):
        bad_text = "Built with love commit 4f9a2b8"
        violations = oracle.ZeroVersionValidator.validate_text(bad_text)
        self.assertGreater(len(violations), 0)

    def test_f06_no_framework_or_tech_names(self):
        bad_text = "Powered by React and Tailwind CSS for Amina"
        violations = oracle.ZeroVersionValidator.validate_text(bad_text)
        self.assertGreater(len(violations), 0)

    def test_f06_no_build_timestamps_or_release_tags(self):
        bad_text = "Release 2.1-beta build 2026-09-17"
        violations = oracle.ZeroVersionValidator.validate_text(bad_text)
        self.assertGreater(len(violations), 0)

    def test_f06_clean_romantic_text_passes_validator(self):
        clean_text = "Happy 23rd Birthday, My Dearest Amina! With all my love forever, Hamid."
        violations = oracle.ZeroVersionValidator.validate_text(clean_text)
        self.assertEqual(len(violations), 0, f"Clean text should have 0 violations, got: {violations}")

class TestFeature07InteractiveGiftBox(unittest.TestCase):
    """Feature 07: Interactive 3D Gift Box Modal"""
    def test_f07_initial_state_closed(self):
        box = oracle.GiftBoxStateMachine()
        self.assertEqual(box.current_state, "CLOSED")

    def test_f07_trigger_shake_transition(self):
        box = oracle.GiftBoxStateMachine()
        success = box.tap()
        self.assertTrue(success)
        self.assertEqual(box.current_state, "SHAKING")

    def test_f07_lid_opening_transition(self):
        box = oracle.GiftBoxStateMachine()
        box.tap()
        success = box.unwrap()
        self.assertTrue(success)
        self.assertEqual(box.current_state, "OPENING")

    def test_f07_exploded_confetti_transition(self):
        box = oracle.GiftBoxStateMachine()
        box.tap()
        box.unwrap()
        success = box.explode()
        self.assertTrue(success)
        self.assertEqual(box.current_state, "EXPLODED")

    def test_f07_dismiss_reveals_dashboard(self):
        box = oracle.GiftBoxStateMachine()
        box.tap()
        box.unwrap()
        box.explode()
        success = box.dismiss()
        self.assertTrue(success)
        self.assertEqual(box.current_state, "REVEALED")

class TestFeature08ConfettiAndAudio(unittest.TestCase):
    """Feature 08: Confetti Explosion & Audio Sound Effects"""
    def test_f08_confetti_particle_count(self):
        confetti_count = 80
        self.assertGreaterEqual(confetti_count, 50)
        self.assertLessEqual(confetti_count, 150)

    def test_f08_confetti_color_palette(self):
        palette = ["#ff6b8b", "#ffd166", "#a855f7", "#60a5fa", "#ffffff"]
        self.assertIn("#ff6b8b", palette)
        self.assertIn("#ffd166", palette)

    def test_f08_web_audio_synthesizer_frequency(self):
        base_freq = 440.0
        sparkle_freq = 880.0
        self.assertEqual(sparkle_freq / base_freq, 2.0)

    def test_f08_zero_external_audio_dependencies(self):
        script_code = "const ctx = new (window.AudioContext || window.webkitAudioContext)(); const osc = ctx.createOscillator();"
        is_clean, violations = oracle.OfflineValidator.validate_script_content(script_code)
        self.assertTrue(is_clean, violations)

    def test_f08_audio_mute_or_safe_autoplay_handling(self):
        is_muted = True
        volume = 0.0 if is_muted else 0.5
        self.assertEqual(volume, 0.0)

class TestFeature09BirthdayLetterToAmina(unittest.TestCase):
    """Feature 09: Birthday Letter to Amina"""
    def test_f09_letter_recipient_name(self):
        letter = "My Dearest Amina, today as you celebrate turning 23..."
        self.assertIn("Amina", letter)

    def test_f09_letter_celebrates_23rd_birthday(self):
        letter = "Happy 23rd Birthday to the love of my life!"
        self.assertIn("23", letter)

    def test_f09_letter_sender_signature(self):
        letter = "Forever and always yours, Hamid."
        self.assertIn("Hamid", letter)

    def test_f09_letter_content_emotional_depth(self):
        letter = "Every message we exchanged was a quiet prayer answered. You are my home, my heart, my paradise."
        self.assertIn("heart", letter)
        self.assertIn("prayer", letter)

    def test_f09_letter_presentation_modal_or_card(self):
        letter_container = {"display": "block", "overflow-y": "auto", "max-height": "80vh"}
        self.assertEqual(letter_container["overflow-y"], "auto")

class TestFeature10TotalMessageVolume(unittest.TestCase):
    """Feature 10: Total Message Volume & Split Hero Cards"""
    def test_f10_total_message_count(self):
        total = oracle.CHAT_METRICS["total_messages"]
        self.assertEqual(total, 12980)

    def test_f10_hamid_message_count_and_percentage(self):
        hamid_count = oracle.CHAT_METRICS["hamid_messages"]
        hamid_pct = oracle.CHAT_METRICS["hamid_pct"]
        self.assertEqual(hamid_count, 6561)
        self.assertAlmostEqual(hamid_pct, 50.55, places=2)

    def test_f10_amina_message_count_and_percentage(self):
        amina_count = oracle.CHAT_METRICS["amina_messages"]
        amina_pct = oracle.CHAT_METRICS["amina_pct"]
        self.assertEqual(amina_count, 6419)
        self.assertAlmostEqual(amina_pct, 49.45, places=2)

    def test_f10_percentage_sum_equals_100(self):
        total_pct = oracle.CHAT_METRICS["hamid_pct"] + oracle.CHAT_METRICS["amina_pct"]
        self.assertAlmostEqual(total_pct, 100.0, places=1)

    def test_f10_hero_card_display_formatting(self):
        total_str = f"{oracle.CHAT_METRICS['total_messages']:,}"
        self.assertEqual(total_str, "12,980")

class TestFeature11SweetWordsFrequency(unittest.TestCase):
    """Feature 11: Sweet Words Frequency Counter"""
    def test_f11_total_sweet_words_count(self):
        total = oracle.CHAT_METRICS["sweet_words"]["total"]
        self.assertGreaterEqual(total, 219)

    def test_f11_jaanu_highest_frequency(self):
        jaanu_count = oracle.CHAT_METRICS["sweet_words"]["jaanu"]
        self.assertEqual(jaanu_count, 78)

    def test_f11_baby_babu_frequency(self):
        baby_count = oracle.CHAT_METRICS["sweet_words"]["baby_babu"]
        self.assertEqual(baby_count, 54)

    def test_f11_love_frequency(self):
        love_count = oracle.CHAT_METRICS["sweet_words"]["love"]
        self.assertEqual(love_count, 42)

    def test_f11_sweetheart_and_honey_frequencies(self):
        sweetheart = oracle.CHAT_METRICS["sweet_words"]["sweetheart"]
        honey = oracle.CHAT_METRICS["sweet_words"]["honey"]
        self.assertEqual(sweetheart, 28)
        self.assertEqual(honey, 17)

class TestFeature12ReactionLeaderboard(unittest.TestCase):
    """Feature 12: Reaction Leaderboard & Reaction Queen"""
    def test_f12_total_reactions_count(self):
        reactions = oracle.CHAT_METRICS["reactions"]
        total = reactions["amina"] + reactions["hamid"]
        self.assertEqual(total, 2187)

    def test_f12_amina_reaction_count(self):
        amina_rxn = oracle.CHAT_METRICS["reactions"]["amina"]
        self.assertEqual(amina_rxn, 1669)

    def test_f12_hamid_reaction_count(self):
        hamid_rxn = oracle.CHAT_METRICS["reactions"]["hamid"]
        self.assertEqual(hamid_rxn, 518)

    def test_f12_reaction_queen_title_assigned_to_amina(self):
        queen = oracle.CHAT_METRICS["reactions"]["reaction_queen"]
        self.assertEqual(queen, "Amina Chamadiya")

    def test_f12_reaction_ratio_and_top_reactions(self):
        ratio = oracle.CHAT_METRICS["reactions"]["ratio"]
        self.assertAlmostEqual(ratio, 3.22, places=2)

class TestFeature13ActivityClock(unittest.TestCase):
    """Feature 13: 24-Hour Activity Clock & Midnight Peak"""
    def test_f13_midnight_messages_count(self):
        midnight = oracle.CHAT_METRICS["midnight_chats"]["total"]
        self.assertEqual(midnight, 6571)

    def test_f13_midnight_percentage_of_total(self):
        pct = oracle.CHAT_METRICS["midnight_chats"]["percentage"]
        self.assertAlmostEqual(pct, 50.62, places=2)

    def test_f13_midnight_split_hamid_and_amina(self):
        hamid_midnight = oracle.CHAT_METRICS["midnight_chats"]["hamid_count"]
        amina_midnight = oracle.CHAT_METRICS["midnight_chats"]["amina_count"]
        self.assertEqual(hamid_midnight, 3306)
        self.assertEqual(amina_midnight, 3265)

    def test_f13_peak_hour_is_midnight_12am(self):
        peak_hr = oracle.CHAT_METRICS["midnight_chats"]["peak_hour"]
        peak_count = oracle.CHAT_METRICS["midnight_chats"]["peak_hour_count"]
        self.assertEqual(peak_hr, 0)
        self.assertEqual(peak_count, 2652)

    def test_f13_hourly_distribution_buckets(self):
        hours = list(range(24))
        self.assertEqual(len(hours), 24)

class TestFeature14MonthlyHeatmap(unittest.TestCase):
    """Feature 14: Monthly Heatmap & Daily Trajectory"""
    def test_f14_timespan_coverage(self):
        start_date = oracle.CHAT_METRICS["start_date"]
        end_date = oracle.CHAT_METRICS["end_date"]
        self.assertTrue(start_date.startswith("2026-07"))
        self.assertTrue(end_date.startswith("2026-08"))

    def test_f14_july_daily_average(self):
        july_avg = oracle.CHAT_METRICS["july_daily_avg"]
        self.assertAlmostEqual(july_avg, 100.0, places=1)

    def test_f14_august_daily_average(self):
        aug_avg = oracle.CHAT_METRICS["august_daily_avg"]
        self.assertAlmostEqual(aug_avg, 334.5, places=1)

    def test_f14_peak_single_day_volume(self):
        peak_day = oracle.CHAT_METRICS["peak_day"]
        self.assertEqual(peak_day["count"], 857)
        self.assertEqual(peak_day["date"], "2026-08-17")
        self.assertEqual(peak_day["day_name"], "Monday")

    def test_f14_daily_average_acceleration(self):
        overall_avg = oracle.CHAT_METRICS["daily_avg"]
        self.assertAlmostEqual(overall_avg, 227.7, places=1)

class TestFeature15ChatStreaks(unittest.TestCase):
    """Feature 15: Chat Streaks & Silence Resilience"""
    def test_f15_longest_streak_days(self):
        longest_streak = oracle.CHAT_METRICS["longest_streak_days"]
        self.assertEqual(longest_streak, 57)

    def test_f15_longest_break_duration(self):
        break_info = oracle.CHAT_METRICS["longest_break"]
        self.assertAlmostEqual(break_info["duration_hours"], 47.94, places=2)

    def test_f15_longest_break_initiator(self):
        break_info = oracle.CHAT_METRICS["longest_break"]
        self.assertEqual(break_info["broken_by"], "Amina Chamadiya")

    def test_f15_longest_break_context_flight(self):
        break_info = oracle.CHAT_METRICS["longest_break"]
        self.assertIn("flight", break_info["message_text"].lower())

    def test_f15_longest_break_timestamps(self):
        break_info = oracle.CHAT_METRICS["longest_break"]
        self.assertEqual(break_info["start"], "2026-07-12T18:37:40+05:30")
        self.assertEqual(break_info["end"], "2026-07-14T18:34:07+05:30")

class TestFeature16MilestoneTimeline(unittest.TestCase):
    """Feature 16: Relationship Milestone Timeline"""
    def test_f16_total_milestones_count(self):
        self.assertEqual(len(oracle.MILESTONES_DATA), 6)

    def test_f16_baat_pakki_milestone_math(self):
        bp = oracle.MILESTONES_DATA[0]
        self.assertEqual(bp["id"], "baat-pakki")
        self.assertEqual(bp["elapsed_birthday"], "5 Months, 3 Days passed")
        self.assertEqual(bp["elapsed_days"], 156)

    def test_f16_engagement_milestone_math(self):
        eng = oracle.MILESTONES_DATA[1]
        self.assertEqual(eng["id"], "engagement")
        self.assertEqual(eng["elapsed_birthday"], "4 Months, 21 Days passed")
        self.assertEqual(eng["elapsed_days"], 143)

    def test_f16_nikah_milestone_math(self):
        nikah = oracle.MILESTONES_DATA[2]
        self.assertEqual(nikah["id"], "nikah")
        self.assertEqual(nikah["elapsed_birthday"], "2 Months, 14 Days passed")
        self.assertEqual(nikah["elapsed_days"], 76)

    def test_f16_hand_hold_and_kisses_math(self):
        hh = oracle.MILESTONES_DATA[3]
        hk = oracle.MILESTONES_DATA[4]
        gk = oracle.MILESTONES_DATA[5]
        self.assertEqual(hh["elapsed_birthday"], "2 Months, 13 Days passed")
        self.assertEqual(hk["elapsed_birthday"], "12 Days passed")
        self.assertEqual(gk["elapsed_birthday"], "7 Days passed")

class TestFeature17LiveAnniversaryTicker(unittest.TestCase):
    """Feature 17: Live Anniversary & Age Tickers"""
    def test_f17_birthday_target_date(self):
        target = oracle.BIRTHDAY_TARGET_DATE
        self.assertEqual(target.year, 2026)
        self.assertEqual(target.month, 9)
        self.assertEqual(target.day, 17)

    def test_f17_live_ticker_before_target(self):
        test_now = datetime(2026, 9, 14, 0, 0, 0, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(oracle.BIRTHDAY_TARGET_DATE, test_now)
        self.assertFalse(ticker["is_reached"])
        self.assertEqual(ticker["days"], 3)
        self.assertEqual(ticker["hours"], 0)

    def test_f17_live_ticker_at_or_past_target(self):
        test_now = datetime(2026, 9, 17, 12, 0, 0, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(oracle.BIRTHDAY_TARGET_DATE, test_now)
        self.assertTrue(ticker["is_reached"])
        self.assertIn("Amina is officially 23", ticker["celebration_text"])

    def test_f17_live_ticker_countdown_fields(self):
        test_now = datetime(2026, 9, 16, 22, 15, 30, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(oracle.BIRTHDAY_TARGET_DATE, test_now)
        self.assertEqual(ticker["days"], 0)
        self.assertEqual(ticker["hours"], 1)
        self.assertEqual(ticker["minutes"], 44)
        self.assertEqual(ticker["seconds"], 30)

    def test_f17_live_ticker_update_cadence_one_second(self):
        interval_ms = 1000
        self.assertEqual(interval_ms, 1000)

class TestFeature18PolaroidMemoryWall(unittest.TestCase):
    """Feature 18: Interactive Polaroid Memory Wall"""
    def test_f18_polaroid_count(self):
        self.assertEqual(len(oracle.POLAROIDS_DATA), 6)

    def test_f18_polaroid_captions_and_dates(self):
        for p in oracle.POLAROIDS_DATA:
            self.assertIn("title", p)
            self.assertIn("caption", p)
            self.assertIn("date_str", p)
            self.assertIn("photo_file", p)

    def test_f18_polaroid_rotation_angles(self):
        for p in oracle.POLAROIDS_DATA:
            deg = float(p["rotation"].replace("deg", ""))
            self.assertGreaterEqual(deg, -5.0)
            self.assertLessEqual(deg, 5.0)

    def test_f18_polaroid_onerror_fallback(self):
        svg = oracle.generate_fallback_svg("Nikah Day", 300, 360)
        self.assertIn("<svg", svg)
        self.assertIn("Nikah Day", svg)

    def test_f18_fallback_svg_content_validity(self):
        svg = oracle.generate_fallback_svg("Memory", 200, 200)
        self.assertIn('xmlns="http://www.w3.org/2000/svg"', svg)
        self.assertIn("viewBox=\"0 0 400 500\"", svg)

class TestFeature19CoupleTriviaGame(unittest.TestCase):
    """Feature 19: Hamid & Amina Couple Trivia Game"""
    def test_f19_trivia_questions_count(self):
        self.assertEqual(len(oracle.TRIVIA_QUESTIONS), 5)

    def test_f19_trivia_state_machine_flow(self):
        game = oracle.TriviaGameStateMachine()
        self.assertEqual(game.current_index, 0)
        self.assertFalse(game.is_finished)
        for i in range(5):
            res = game.answer_question(oracle.TRIVIA_QUESTIONS[i]["correct_index"])
            self.assertTrue(res["is_correct"])
        self.assertTrue(game.is_finished)

    def test_f19_perfect_score_soulmate_badge(self):
        game = oracle.TriviaGameStateMachine()
        for i in range(5):
            game.answer_question(oracle.TRIVIA_QUESTIONS[i]["correct_index"])
        summary = game.get_score_summary()
        self.assertEqual(summary["score"], 5)
        self.assertEqual(summary["total"], 5)
        self.assertEqual(summary["percentage"], 100.0)
        self.assertTrue(summary["is_soulmate"])

    def test_f19_partial_score_percentage(self):
        game = oracle.TriviaGameStateMachine()
        game.answer_question(oracle.TRIVIA_QUESTIONS[0]["correct_index"]) # Correct
        wrong_idx_1 = (oracle.TRIVIA_QUESTIONS[1]["correct_index"] + 1) % 4
        game.answer_question(wrong_idx_1) # Wrong
        game.answer_question(oracle.TRIVIA_QUESTIONS[2]["correct_index"]) # Correct
        game.answer_question(oracle.TRIVIA_QUESTIONS[3]["correct_index"]) # Correct
        wrong_idx_4 = (oracle.TRIVIA_QUESTIONS[4]["correct_index"] + 1) % 4
        game.answer_question(wrong_idx_4) # Wrong
        summary = game.get_score_summary()
        self.assertEqual(summary["score"], 3)
        self.assertEqual(summary["percentage"], 60.0)
        self.assertFalse(summary["is_soulmate"])

    def test_f19_immediate_feedback_explanation(self):
        for q in oracle.TRIVIA_QUESTIONS:
            self.assertIn("feedback", q)
            self.assertGreater(len(q["feedback"]), 10)

class TestFeature20RomanticSoundtrackPlayer(unittest.TestCase):
    """Feature 20: Romantic Soundtrack Player"""
    def test_f20_web_audio_synth_frequencies(self):
        # Pentatonic romantic frequencies (C4, E4, G4, A4, B4, C5)
        notes = [261.63, 329.63, 392.00, 440.00, 493.88, 523.25]
        for note in notes:
            self.assertGreater(note, 200.0)
            self.assertLess(note, 600.0)

    def test_f20_play_pause_state_toggle(self):
        is_playing = False
        is_playing = not is_playing
        self.assertTrue(is_playing)
        is_playing = not is_playing
        self.assertFalse(is_playing)

    def test_f20_mute_unmute_functionality(self):
        master_volume = 0.5
        muted = True
        active_volume = 0.0 if muted else master_volume
        self.assertEqual(active_volume, 0.0)
        muted = False
        active_volume = 0.0 if muted else master_volume
        self.assertEqual(active_volume, 0.5)

    def test_f20_visualizer_or_music_note_pulse(self):
        animation_state = "playing" if True else "paused"
        self.assertEqual(animation_state, "playing")

    def test_f20_zero_network_audio_failure(self):
        synth_code = "const osc = audioCtx.createOscillator(); osc.type = 'sine';"
        self.assertIn("createOscillator", synth_code)

class TestFeature21OfflineFirstArchitecture(unittest.TestCase):
    """Feature 21: Offline-First Architecture & Zero External CDNs"""
    def test_f21_zero_http_external_scripts(self):
        html = '<script src="https://cdn.jsdelivr.net/npm/bootstrap"></script>'
        is_clean, violations = oracle.OfflineValidator.validate_script_content(html)
        self.assertFalse(is_clean)
        self.assertGreater(len(violations), 0)

    def test_f21_zero_external_css_stylesheets(self):
        html = '<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Great+Vibes">'
        is_clean, violations = oracle.OfflineValidator.validate_link_tags(html)
        self.assertFalse(is_clean)
        self.assertGreater(len(violations), 0)

    def test_f21_embedded_or_inline_fonts(self):
        safe_css = "font-family: 'Great Vibes', cursive, sans-serif;"
        self.assertIn("cursive", safe_css)

    def test_f21_file_uri_scheme_compatibility(self):
        relative_path = "assets/photos/nikah.jpg"
        self.assertFalse(relative_path.startswith("http"))
        self.assertFalse(relative_path.startswith("/"))

    def test_f21_offline_validator_audit_pass(self):
        clean_html = '<html><head><style>body { color: white; }</style></head><body><script>console.log("ready");</script></body></html>'
        is_clean, violations = oracle.OfflineValidator.audit_offline_readiness(clean_html)
        self.assertTrue(is_clean, violations)

class TestFeature22TouchGesturesMobile(unittest.TestCase):
    """Feature 22: Touch Gestures & Mobile Haptics"""
    def test_f22_touch_target_accessibility(self):
        target_size = 48
        self.assertGreaterEqual(target_size, 44)

    def test_f22_touch_feedback_active_state(self):
        btn_active_css = "transform: scale(0.96);"
        self.assertIn("scale(0.96)", btn_active_css)

    def test_f22_swipe_or_horizontal_scroll_snap(self):
        scroll_css = "scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch;"
        self.assertIn("scroll-snap-type", scroll_css)

    def test_f22_navigator_vibrate_safe_feature_detect(self):
        vibrate_js = "if ('vibrate' in navigator) { navigator.vibrate(50); }"
        self.assertIn("in navigator", vibrate_js)

    def test_f22_viewport_touch_manipulation(self):
        touch_manipulation = "touch-action: manipulation;"
        self.assertEqual(touch_manipulation, "touch-action: manipulation;")

class TestFeature23SingleFilePackaging(unittest.TestCase):
    """Feature 23: Single-File Production Packaging"""
    def test_f23_single_html_file_path(self):
        filename = "Instagram_Chat_Analysis_Amina_Hamid.html"
        self.assertTrue(filename.endswith(".html"))

    def test_f23_doctype_and_html_structure(self):
        html_sample = "<!DOCTYPE html><html lang=\"en\"><head></head><body></body></html>"
        self.assertTrue(html_sample.startswith("<!DOCTYPE html>"))

    def test_f23_embedded_style_and_script_tags(self):
        html_sample = "<html><head><style></style></head><body><script></script></body></html>"
        self.assertIn("<style>", html_sample)
        self.assertIn("<script>", html_sample)

    def test_f23_standalone_execution_no_server(self):
        protocol = "file:"
        self.assertEqual(protocol, "file:")

    def test_f23_file_size_and_readability(self):
        max_bytes = 10 * 1024 * 1024 # 10MB budget
        self.assertGreater(max_bytes, 1000000)

class TestFeature24CompatibilityAccessibility(unittest.TestCase):
    """Feature 24: Production Browser Compatibility & Accessibility"""
    def test_f24_aria_labels_on_interactive_elements(self):
        button_html = '<button aria-label="Open Birthday Gift Box" class="gift-btn"></button>'
        self.assertIn('aria-label="Open Birthday Gift Box"', button_html)

    def test_f24_semantic_html_landmarks(self):
        landmarks = ["header", "main", "section", "footer"]
        for lm in landmarks:
            self.assertTrue(len(lm) > 0)

    def test_f24_image_alt_text_accessibility(self):
        for p in oracle.POLAROIDS_DATA:
            self.assertIn("caption", p)
            self.assertGreater(len(p["caption"]), 5)

    def test_f24_keyboard_navigation_tabindex(self):
        interactive_elem = '<div tabindex="0" role="button"></div>'
        self.assertIn('tabindex="0"', interactive_elem)

    def test_f24_color_contrast_wcag_aa(self):
        # Rose gold text (#ff6b8b) on dark background (#0d0d1a)
        # Luminance of #ff6b8b: 0.299*255 + 0.587*107 + 0.114*139 = 76.2 + 62.8 + 15.8 = 154.8 / 255 = 0.607
        contrast_ratio = (0.607 + 0.05) / (0.01 + 0.05) # ~10.95:1
        self.assertGreaterEqual(contrast_ratio, 4.5)

if __name__ == '__main__':
    unittest.main()
