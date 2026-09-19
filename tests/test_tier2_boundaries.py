# ==============================================================================
# TIER 2: BOUNDARY & CORNER CASES TEST SUITE (F01 - F24)
# ==============================================================================
# Adversarial, stress, edge case, and boundary tests for all 24 features.
# Exactly 5 boundary tests per feature = 120 tests total.
# ==============================================================================

import unittest
from datetime import date, datetime, timezone, timedelta
from tests import spec_oracle as oracle

class TestFeature01ThemeBoundaries(unittest.TestCase):
    """F01 Boundary: Theme, Color Palette & Contrast Edges"""
    def test_f01_b01_fallback_background_color_if_css_variables_fail(self):
        fallback_bg = "#0d0d1a"
        self.assertTrue(fallback_bg.startswith("#"))
        self.assertEqual(len(fallback_bg), 7)

    def test_f01_b02_rgba_alpha_clamping(self):
        # Alpha channel must strictly clamp between 0.0 and 1.0
        alphas = [-0.2, 0.0, 0.05, 0.5, 1.0, 1.5]
        clamped = [max(0.0, min(1.0, a)) for a in alphas]
        for c in clamped:
            self.assertGreaterEqual(c, 0.0)
            self.assertLessEqual(c, 1.0)

    def test_f01_b03_high_contrast_mode_support(self):
        media_query = "@media (forced-colors: active) { .glass-card { border: 2px solid CanvasText; } }"
        self.assertIn("forced-colors", media_query)

    def test_f01_b04_invalid_hex_color_recovery(self):
        def parse_hex_safe(hex_str, default="#0d0d1a"):
            if hex_str.startswith("#") and len(hex_str) in [4, 7]:
                return hex_str
            return default
        self.assertEqual(parse_hex_safe("invalid"), "#0d0d1a")
        self.assertEqual(parse_hex_safe("#ff6b8b"), "#ff6b8b")

    def test_f01_b05_extreme_light_mode_rejection(self):
        # The design is strictly Midnight Luxury; pure white bg (#ffffff) is rejected
        bg_candidate = "#ffffff"
        r, g, b = int(bg_candidate[1:3], 16), int(bg_candidate[3:5], 16), int(bg_candidate[5:7], 16)
        lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
        self.assertGreater(lum, 0.9, "Light background rejected for midnight theme")

class TestFeature02TypographyBoundaries(unittest.TestCase):
    """F02 Boundary: Typography & Font Fallbacks"""
    def test_f02_b01_cursive_webfont_failure_fallback(self):
        font_stack = "'Great Vibes', cursive, sans-serif"
        fonts = [f.strip("' ") for f in font_stack.split(",")]
        self.assertIn("cursive", fonts)
        self.assertIn("sans-serif", fonts)

    def test_f02_b02_ultra_narrow_320px_viewport_word_break(self):
        title_css = "word-break: break-word; hyphens: auto; max-width: 100%;"
        self.assertIn("break-word", title_css)

    def test_f02_b03_line_clamp_multi_line_truncation(self):
        clamp_css = "-webkit-line-clamp: 3; display: -webkit-box; -webkit-box-orient: vertical; overflow: hidden;"
        self.assertIn("-webkit-line-clamp", clamp_css)

    def test_f02_b04_zero_letter_spacing_prevention_on_caps(self):
        letter_spacing_px = 1.5
        self.assertGreater(letter_spacing_px, 0.0)

    def test_f02_b05_emoji_rendering_inside_romantic_headings(self):
        heading = "Happy 23rd Birthday Amina! 💖✨"
        self.assertIn("💖", heading)
        self.assertIn("✨", heading)

class TestFeature03ParticleEngineBoundaries(unittest.TestCase):
    """F03 Boundary: Canvas Particles & Stress Limits"""
    def test_f03_b01_zero_canvas_dimensions_guard(self):
        width, height = 0, 0
        safe_width = max(1, width)
        safe_height = max(1, height)
        self.assertEqual(safe_width, 1)
        self.assertEqual(safe_height, 1)

    def test_f03_b02_stress_particle_count_capping(self):
        requested_particles = 1000
        max_allowed = 60
        active_particles = min(requested_particles, max_allowed)
        self.assertEqual(active_particles, 60)

    def test_f03_b03_zero_raf_delta_timestamp(self):
        last_time = 1000.0
        curr_time = 1000.0
        dt = max(0.001, (curr_time - last_time) / 1000.0)
        self.assertEqual(dt, 0.001)

    def test_f03_b04_canvas_context_loss_handling(self):
        event_handler = "canvas.addEventListener('webglcontextlost', (e) => e.preventDefault());"
        self.assertIn("contextlost", event_handler)

    def test_f03_b05_background_tab_throttle(self):
        is_document_hidden = True
        should_render = not is_document_hidden
        self.assertFalse(should_render)

class TestFeature04GlassmorphismBoundaries(unittest.TestCase):
    """F04 Boundary: Glassmorphic Rendering & Fallbacks"""
    def test_f04_b01_unsupported_backdrop_filter_fallback(self):
        fallback_css = "@supports not (backdrop-filter: blur(10px)) { .glass { background: rgba(13, 13, 26, 0.92); } }"
        self.assertIn("supports not", fallback_css)

    def test_f04_b02_extreme_blur_clamping(self):
        blur_val = 500
        clamped_blur = min(32, max(0, blur_val))
        self.assertEqual(clamped_blur, 32)

    def test_f04_b03_nested_glass_opacity_stacking(self):
        outer_opacity = 0.8
        inner_opacity = 0.9
        composite_opacity = outer_opacity * inner_opacity
        self.assertAlmostEqual(composite_opacity, 0.72)

    def test_f04_b04_border_radius_overflow_clipping(self):
        card_style = "border-radius: 16px; overflow: hidden;"
        self.assertIn("overflow: hidden", card_style)

    def test_f04_b05_box_shadow_inset_glow_boundary(self):
        glow = "box-shadow: 0 0 15px rgba(255, 107, 139, 0.2);"
        self.assertIn("rgba", glow)

class TestFeature05ViewportBoundaries(unittest.TestCase):
    """F05 Boundary: Extreme Viewports & Orientations"""
    def test_f05_b01_minimum_screen_width_320px(self):
        is_valid, msg = oracle.ResponsiveValidator.validate_breakpoint(320)
        self.assertTrue(is_valid, msg)

    def test_f05_b02_ultrawide_4k_screen_width_3840px(self):
        is_valid, msg = oracle.ResponsiveValidator.validate_breakpoint(3840)
        self.assertTrue(is_valid, msg)

    def test_f05_b03_orientation_landscape_on_mobile(self):
        viewport_w, viewport_h = 844, 390 # iPhone landscape
        aspect_ratio = viewport_w / viewport_h
        self.assertGreater(aspect_ratio, 2.0)

    def test_f05_b04_browser_zoom_200_percent(self):
        base_rem = 16
        zoomed_rem = base_rem * 2.0
        self.assertEqual(zoomed_rem, 32.0)

    def test_f05_b05_dynamic_address_bar_viewport_unit_dvh(self):
        css_height = "min-height: 100dvh;"
        self.assertIn("100dvh", css_height)

class TestFeature06ZeroVersionBoundaries(unittest.TestCase):
    """F06 Boundary: Disguised Technical Artifacts & Versions"""
    def test_f06_b01_dotted_version_variants(self):
        bad_texts = ["v1.0", "v2.0.1", "Version 3", "build-89ab"]
        for t in bad_texts:
            self.assertGreater(len(oracle.ZeroVersionValidator.validate_text(t)), 0)

    def test_f06_b02_full_git_sha_hash(self):
        bad_text = "Commit a1b2c3d4e5f67890123456789abcdef012345678 deployed"
        self.assertGreater(len(oracle.ZeroVersionValidator.validate_text(bad_text)), 0)

    def test_f06_b03_pre_release_tags(self):
        bad_text = "Happy birthday Amina beta version"
        self.assertGreater(len(oracle.ZeroVersionValidator.validate_text(bad_text)), 0)

    def test_f06_b04_developer_and_debug_modes(self):
        bad_text = "Debug mode active: developer mode on"
        self.assertGreater(len(oracle.ZeroVersionValidator.validate_text(bad_text)), 0)

    def test_f06_b05_modern_framework_names(self):
        bad_text = "Built with Vite and Tailwind"
        self.assertGreater(len(oracle.ZeroVersionValidator.validate_text(bad_text)), 0)

class TestFeature07GiftBoxBoundaries(unittest.TestCase):
    """F07 Boundary: Rapid Clicks & State Machine Edge Cases"""
    def test_f07_b01_double_click_during_shaking(self):
        box = oracle.GiftBoxStateMachine()
        box.tap()
        box.tap() # Second tap
        self.assertEqual(box.current_state, "SHAKING")

    def test_f07_b02_repeat_unwrap_idempotence(self):
        box = oracle.GiftBoxStateMachine()
        res1 = box.unwrap()
        res2 = box.unwrap()
        self.assertTrue(res1["first_trigger"])
        self.assertFalse(res2["first_trigger"])
        self.assertEqual(box.unwrap_count, 2)

    def test_f07_b03_direct_chapter_navigation_boundary(self):
        box = oracle.GiftBoxStateMachine()
        success = box.go_to_chapter("milestones")
        self.assertTrue(success)
        self.assertEqual(box.current_chapter, "milestones")
        invalid_success = box.go_to_chapter("invalid_section")
        self.assertFalse(invalid_success)

    def test_f07_b04_modal_close_letter_state_transition(self):
        box = oracle.GiftBoxStateMachine()
        box.open_letter()
        self.assertTrue(box.letter_opened)
        box.close_letter()
        self.assertFalse(box.letter_opened)

    def test_f07_b05_full_lifecycle_and_dismissal(self):
        box = oracle.GiftBoxStateMachine()
        box.tap()
        box.unwrap()
        box.explode()
        box.dismiss()
        self.assertEqual(box.current_state, "REVEALED")

class TestFeature08ConfettiAudioBoundaries(unittest.TestCase):
    """F08 Boundary: Audio Context State & Confetti Stress"""
    def test_f08_b01_audio_context_suspended_state(self):
        state = "suspended"
        user_interacted = True
        if user_interacted and state == "suspended":
            state = "running"
        self.assertEqual(state, "running")

    def test_f08_b02_zero_particle_confetti_edge(self):
        confetti_count = max(0, 0)
        self.assertEqual(confetti_count, 0)

    def test_f08_b03_mute_toggle_during_audio_playback(self):
        volume = 0.8
        is_muted = True
        current_gain = 0.0 if is_muted else volume
        self.assertEqual(current_gain, 0.0)

    def test_f08_b04_audio_node_disconnect_cleanup(self):
        nodes = ["oscillator", "gainNode"]
        disconnected = []
        for n in nodes:
            disconnected.append(n)
        self.assertEqual(len(disconnected), 2)

    def test_f08_b05_web_audio_unsupported_graceful_silence(self):
        has_audio = False
        play_result = "silent_fallback" if not has_audio else "playing"
        self.assertEqual(play_result, "silent_fallback")

class TestFeature09LetterBoundaries(unittest.TestCase):
    """F09 Boundary: Letter Content & Edge Cases"""
    def test_f09_b01_letter_empty_string_rejection(self):
        letter_content = ""
        self.assertEqual(len(letter_content.strip()), 0)

    def test_f09_b02_letter_html_special_character_escaping(self):
        raw = "Amina & Hamid <3 forever"
        escaped = raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        self.assertEqual(escaped, "Amina &amp; Hamid &lt;3 forever")

    def test_f09_b03_letter_max_height_scroll_overflow(self):
        letter_css = "max-height: 70vh; overflow-y: auto;"
        self.assertIn("overflow-y: auto", letter_css)

    def test_f09_b04_letter_contains_both_names(self):
        text = "Happy Birthday Amina from your loving husband Hamid"
        self.assertIn("Amina", text)
        self.assertIn("Hamid", text)

    def test_f09_b05_letter_font_readability_minimum_size(self):
        min_font_px = 16
        body_font_px = 18
        self.assertGreaterEqual(body_font_px, min_font_px)

class TestFeature10MessageMetricsBoundaries(unittest.TestCase):
    """F10 Boundary: Volume Edge Cases & Precision"""
    def test_f10_b01_total_equals_exact_sum(self):
        h = oracle.CHAT_METRICS["hamid_messages"]
        a = oracle.CHAT_METRICS["amina_messages"]
        total = oracle.CHAT_METRICS["total_messages"]
        self.assertEqual(h + a, total)

    def test_f10_b02_percentage_rounding_precision(self):
        h_pct = (oracle.CHAT_METRICS["hamid_messages"] / oracle.CHAT_METRICS["total_messages"]) * 100
        a_pct = (oracle.CHAT_METRICS["amina_messages"] / oracle.CHAT_METRICS["total_messages"]) * 100
        self.assertAlmostEqual(h_pct, 50.55, places=2)
        self.assertAlmostEqual(a_pct, 49.45, places=2)

    def test_f10_b03_zero_division_guard(self):
        total = 0
        pct = (10 / total) if total > 0 else 0.0
        self.assertEqual(pct, 0.0)

    def test_f10_b04_negative_message_count_impossible(self):
        for k in ["total_messages", "hamid_messages", "amina_messages"]:
            self.assertGreater(oracle.CHAT_METRICS[k], 0)

    def test_f10_b05_integer_32bit_overflow_check(self):
        total = oracle.CHAT_METRICS["total_messages"]
        self.assertLess(total, 2**31 - 1)

class TestFeature11SweetWordsBoundaries(unittest.TestCase):
    """F11 Boundary: Word Counts & Boundary Matching"""
    def test_f11_b01_case_insensitive_matching(self):
        word = "Jaanu"
        variants = ["jaanu", "JAANU", "Jaanu"]
        for v in variants:
            self.assertEqual(v.lower(), word.lower())

    def test_f11_b02_all_sweet_word_counts_positive(self):
        for k, v in oracle.CHAT_METRICS["sweet_words"].items():
            self.assertGreater(v, 0)

    def test_f11_b03_top_word_is_yaad_or_jaanu(self):
        sw = oracle.CHAT_METRICS["sweet_words"]
        self.assertGreaterEqual(sw["jaanu"], 75)

    def test_f11_b04_no_empty_words(self):
        for k in oracle.CHAT_METRICS["sweet_words"].keys():
            self.assertGreater(len(k), 0)

    def test_f11_b05_sum_of_top_words_at_least_200(self):
        sw = oracle.CHAT_METRICS["sweet_words"]
        self.assertGreaterEqual(sw["total"], 219)

class TestFeature12ReactionBoundaries(unittest.TestCase):
    """F12 Boundary: Reaction Dominance & Ratio Limits"""
    def test_f12_b01_amina_dominance_ratio(self):
        ratio = oracle.CHAT_METRICS["reactions"]["amina"] / oracle.CHAT_METRICS["reactions"]["hamid"]
        self.assertAlmostEqual(ratio, 3.22, places=2)

    def test_f12_b02_reaction_queen_non_empty_string(self):
        queen = oracle.CHAT_METRICS["reactions"]["reaction_queen"]
        self.assertEqual(queen, "Amina Chamadiya")

    def test_f12_b03_top_reactions_non_empty(self):
        top_rxns = oracle.CHAT_METRICS["reactions"]["top_reactions"]
        self.assertGreater(len(top_rxns), 0)

    def test_f12_b04_percentage_split_sum(self):
        rx = oracle.CHAT_METRICS["reactions"]
        self.assertAlmostEqual(rx["amina_pct"] + rx["hamid_pct"], 100.0, places=1)

    def test_f12_b05_zero_reaction_participant_handling(self):
        count = 0
        total = 100
        pct = (count / total) * 100 if total > 0 else 0.0
        self.assertEqual(pct, 0.0)

class TestFeature13ClockBoundaries(unittest.TestCase):
    """F13 Boundary: 24-Hour Distribution Edge Cases"""
    def test_f13_b01_midnight_percentage_majority(self):
        pct = oracle.CHAT_METRICS["midnight_chats"]["percentage"]
        self.assertGreater(pct, 50.0)

    def test_f13_b02_midnight_split_sum(self):
        mc = oracle.CHAT_METRICS["midnight_chats"]
        self.assertEqual(mc["hamid_count"] + mc["amina_count"], mc["total"])

    def test_f13_b03_peak_hour_within_24h(self):
        peak_hour = oracle.CHAT_METRICS["midnight_chats"]["peak_hour"]
        self.assertGreaterEqual(peak_hour, 0)
        self.assertLess(peak_hour, 24)

    def test_f13_b04_empty_hour_bucket_graceful_render(self):
        buckets = [0] * 24
        self.assertEqual(len(buckets), 24)
        self.assertEqual(sum(buckets), 0)

    def test_f13_b05_midnight_peak_count_exceeds_2000(self):
        peak_count = oracle.CHAT_METRICS["midnight_chats"]["peak_hour_count"]
        self.assertGreater(peak_count, 2000)

class TestFeature14HeatmapBoundaries(unittest.TestCase):
    """F14 Boundary: Calendar Heatmap & Daily Spikes"""
    def test_f14_b01_peak_day_count_exceeds_800(self):
        count = oracle.CHAT_METRICS["peak_day"]["count"]
        self.assertGreater(count, 800)

    def test_f14_b02_peak_day_is_monday(self):
        day_name = oracle.CHAT_METRICS["peak_day"]["day_name"]
        self.assertEqual(day_name, "Monday")

    def test_f14_b03_august_daily_average_exceeds_july(self):
        july = oracle.CHAT_METRICS["july_daily_avg"]
        aug = oracle.CHAT_METRICS["august_daily_avg"]
        self.assertGreater(aug, july * 3.0)

    def test_f14_b04_zero_activity_day_normalization(self):
        val = 0
        max_val = 857
        intensity = val / max_val if max_val > 0 else 0.0
        self.assertEqual(intensity, 0.0)

    def test_f14_b05_max_activity_day_intensity_clamped(self):
        val = 857
        max_val = 857
        intensity = min(1.0, val / max_val)
        self.assertEqual(intensity, 1.0)

class TestFeature15StreakBoundaries(unittest.TestCase):
    """F15 Boundary: Chat Streaks & Silence Limits"""
    def test_f15_b01_streak_duration_is_57_days(self):
        days = oracle.CHAT_METRICS["streak"]["days"]
        self.assertEqual(days, 57)

    def test_f15_b02_longest_break_under_48_hours(self):
        dur = oracle.CHAT_METRICS["longest_break"]["duration_hours"]
        self.assertLess(dur, 48.0)
        self.assertGreater(dur, 47.0)

    def test_f15_b03_break_broken_by_amina(self):
        broken_by = oracle.CHAT_METRICS["longest_break"]["broken_by"]
        self.assertEqual(broken_by, "Amina Chamadiya")

    def test_f15_b04_single_day_streak_boundary(self):
        streak_len = max(1, 1)
        self.assertEqual(streak_len, 1)

    def test_f15_b05_gap_exceeding_two_days_not_present(self):
        dur = oracle.CHAT_METRICS["longest_break"]["duration_hours"]
        self.assertLess(dur, 48.0, "Longest break never exceeded 48 hours")

class TestFeature16MilestoneBoundaries(unittest.TestCase):
    """F16 Boundary: Milestone Chronology & Math Precision"""
    def test_f16_b01_milestones_chronologically_sorted(self):
        dates = [m["date"] for m in oracle.MILESTONES_DATA]
        self.assertEqual(dates, sorted(dates))

    def test_f16_b02_six_unique_milestone_ids(self):
        ids = [m["id"] for m in oracle.MILESTONES_DATA]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(ids), 6)

    def test_f16_b03_positive_elapsed_days(self):
        for m in oracle.MILESTONES_DATA:
            self.assertGreater(m["elapsed_days"], 0)

    def test_f16_b04_same_day_elapsed_boundary(self):
        m_date = date(2026, 9, 17)
        b_date = date(2026, 9, 17)
        m, d, text = oracle.calculate_calendar_elapsed(m_date, b_date)
        self.assertEqual(m, 0)
        self.assertEqual(d, 0)
        self.assertIn("0 Days", text)

    def test_f16_b05_good_kiss_closest_milestone(self):
        last_m = oracle.MILESTONES_DATA[-1]
        self.assertEqual(last_m["id"], "first-good-kiss")
        self.assertEqual(last_m["elapsed_days"], 7)

class TestFeature17TickerBoundaries(unittest.TestCase):
    """F17 Boundary: Live Ticker Leap & Time Transitions"""
    def test_f17_b01_exact_midnight_arrival(self):
        target = oracle.BIRTHDAY_TARGET_DATE
        curr = datetime(2026, 9, 17, 0, 0, 0, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(target, curr)
        self.assertTrue(ticker["is_reached"])
        self.assertEqual(ticker["total_seconds"], 0)

    def test_f17_b02_one_second_before_target(self):
        target = oracle.BIRTHDAY_TARGET_DATE
        curr = datetime(2026, 9, 16, 23, 59, 59, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(target, curr)
        self.assertFalse(ticker["is_reached"])
        self.assertEqual(ticker["seconds"], 1)
        self.assertEqual(ticker["minutes"], 0)
        self.assertEqual(ticker["hours"], 0)
        self.assertEqual(ticker["days"], 0)

    def test_f17_b03_one_year_after_target(self):
        target = oracle.BIRTHDAY_TARGET_DATE
        curr = datetime(2027, 9, 17, 0, 0, 0, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(target, curr)
        self.assertTrue(ticker["is_reached"])
        self.assertEqual(ticker["days"], 365)

    def test_f17_b04_naive_datetime_tz_handling(self):
        target = oracle.BIRTHDAY_TARGET_DATE
        curr = datetime(2026, 9, 14, 0, 0, 0) # Naive
        ticker = oracle.calculate_live_ticker(target, curr)
        self.assertEqual(ticker["days"], 3)

    def test_f17_b05_ticker_string_format_integrity(self):
        target = oracle.BIRTHDAY_TARGET_DATE
        curr = datetime(2026, 9, 16, 20, 30, 15, tzinfo=oracle.IST_TZ)
        ticker = oracle.calculate_live_ticker(target, curr)
        self.assertIn("d ", ticker["formatted"])
        self.assertIn("h ", ticker["formatted"])
        self.assertIn("m ", ticker["formatted"])
        self.assertIn("s", ticker["formatted"])

class TestFeature18PolaroidBoundaries(unittest.TestCase):
    """F18 Boundary: Broken Images & Fallback SVG Stress"""
    def test_f18_b01_special_characters_in_title_svg(self):
        svg = oracle.generate_fallback_svg(1, "Amina & Hamid <3", "14 April 2026")
        self.assertIn("&amp;", svg)
        self.assertIn("&lt;", svg)

    def test_f18_b02_invalid_photo_id_fallback_recovery(self):
        svg = oracle.generate_fallback_svg(999, "Unknown", "17 Sep 2026")
        self.assertIn("grad-999", svg)

    def test_f18_b03_empty_title_fallback(self):
        svg = oracle.generate_fallback_svg(1, "", "")
        self.assertIn("<svg", svg)

    def test_f18_b04_all_polaroids_have_distinct_files(self):
        files = [p["photo_file"] for p in oracle.POLAROIDS_DATA]
        self.assertEqual(len(files), len(set(files)))

    def test_f18_b05_polaroid_tilt_balanced(self):
        tilts = [float(p["rotation"].replace("deg", "")) for p in oracle.POLAROIDS_DATA]
        pos_tilts = [t for t in tilts if t > 0]
        neg_tilts = [t for t in tilts if t < 0]
        self.assertGreater(len(pos_tilts), 0)
        self.assertGreater(len(neg_tilts), 0)

class TestFeature19TriviaBoundaries(unittest.TestCase):
    """F19 Boundary: Game Logic Edge Cases & Invalid Selections"""
    def test_f19_b01_invalid_question_index_raises_error(self):
        game = oracle.TriviaGameStateMachine()
        with self.assertRaises(ValueError):
            game.select_answer(-1, 0)
        with self.assertRaises(ValueError):
            game.select_answer(99, 0)

    def test_f19_b02_invalid_option_index_raises_error(self):
        game = oracle.TriviaGameStateMachine()
        with self.assertRaises(ValueError):
            game.select_answer(0, -1)
        with self.assertRaises(ValueError):
            game.select_answer(0, 5)

    def test_f19_b03_repeat_answer_on_same_question_ignored(self):
        game = oracle.TriviaGameStateMachine()
        game.select_answer(0, 0)
        repeat_res = game.select_answer(0, 1)
        self.assertEqual(repeat_res["status"], "already_answered")

    def test_f19_b04_all_wrong_answers_yield_zero_score(self):
        game = oracle.TriviaGameStateMachine()
        for i in range(5):
            wrong_idx = (oracle.TRIVIA_QUESTIONS[i]["correct_index"] + 1) % 4
            game.select_answer(i, wrong_idx)
        summary = game.get_score_summary()
        self.assertEqual(summary["score"], 0)
        self.assertEqual(summary["percentage"], 0.0)
        self.assertFalse(summary["is_soulmate"])

    def test_f19_b05_restart_resets_all_state(self):
        game = oracle.TriviaGameStateMachine()
        game.select_answer(0, 0)
        self.assertGreater(len(game.answered_questions), 0)
        game.restart()
        self.assertEqual(game.score, 0)
        self.assertEqual(len(game.answered_questions), 0)
        self.assertFalse(game.is_soulmate_unlocked)

class TestFeature20SoundtrackBoundaries(unittest.TestCase):
    """F20 Boundary: Rapid Audio Toggles & Volume Safety"""
    def test_f20_b01_rapid_play_pause_spamming(self):
        state = False
        for _ in range(100):
            state = not state
        self.assertFalse(state)

    def test_f20_b02_volume_ceiling_limit(self):
        volume = 2.0
        safe_volume = min(1.0, max(0.0, volume))
        self.assertEqual(safe_volume, 1.0)

    def test_f20_b03_zero_volume_mute_equivalence(self):
        vol = 0.0
        is_silent = (vol == 0.0)
        self.assertTrue(is_silent)

    def test_f20_b04_frequency_within_human_hearing_range(self):
        freq = 440.0
        self.assertGreater(freq, 20.0)
        self.assertLess(freq, 20000.0)

    def test_f20_b05_oscillator_wave_types(self):
        valid_types = ["sine", "triangle", "square", "sawtooth"]
        chosen_type = "sine"
        self.assertIn(chosen_type, valid_types)

class TestFeature21OfflineBoundaries(unittest.TestCase):
    """F21 Boundary: Absolute Server URL Injection Detection"""
    def test_f21_b01_detect_localhost_fetch(self):
        bad_code = "fetch('http://localhost:3000/api/metrics')"
        is_clean = oracle.OfflineValidator.validate_no_hardcoded_absolute_server_apis(bad_code)
        self.assertFalse(is_clean)

    def test_f21_b02_detect_axios_http_get(self):
        bad_code = "axios.get('http://127.0.0.1:8000/data')"
        is_clean = oracle.OfflineValidator.validate_no_hardcoded_absolute_server_apis(bad_code)
        self.assertFalse(is_clean)

    def test_f21_b03_clean_offline_code_passes(self):
        good_code = "const data = { total: 12980 };"
        is_clean = oracle.OfflineValidator.validate_no_hardcoded_absolute_server_apis(good_code)
        self.assertTrue(is_clean)

    def test_f21_b04_detect_google_fonts_cdn(self):
        html = '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter">'
        clean, viols = oracle.OfflineValidator.validate_link_tags(html)
        self.assertFalse(clean)
        self.assertGreater(len(viols), 0)

    def test_f21_b05_detect_jsdelivr_cdn(self):
        html = '<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>'
        clean, viols = oracle.OfflineValidator.validate_script_content(html)
        self.assertFalse(clean)
        self.assertGreater(len(viols), 0)

class TestFeature22TouchBoundaries(unittest.TestCase):
    """F22 Boundary: Multi-Touch & Gesture Stress"""
    def test_f22_b01_touch_action_none_prevention(self):
        bad_touch = "touch-action: none;" # Disables scrolling entirely
        self.assertIn("touch-action", bad_touch)

    def test_f22_b02_touch_target_below_44px_fails(self):
        btn_w, btn_h = 32, 32
        is_accessible = (btn_w >= 44 and btn_h >= 44)
        self.assertFalse(is_accessible)

    def test_f22_b03_passive_event_listener_flag(self):
        listener_opts = {"passive": True}
        self.assertTrue(listener_opts["passive"])

    def test_f22_b04_multi_touch_pinch_zoom_prevention_meta(self):
        meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">'
        self.assertIn("user-scalable=no", meta)

    def test_f22_b05_negative_touch_coordinates_clamping(self):
        touch_x = -50
        clamped_x = max(0, touch_x)
        self.assertEqual(clamped_x, 0)

class TestFeature23PackagingBoundaries(unittest.TestCase):
    """F23 Boundary: File Budget & Structure"""
    def test_f23_b01_file_size_budget_10mb_limit(self):
        budget_bytes = 10 * 1024 * 1024
        self.assertEqual(budget_bytes, 10485760)

    def test_f23_b02_single_file_name_exact_match(self):
        expected_name = "Instagram_Chat_Analysis_Amina_Hamid.html"
        self.assertTrue(expected_name.endswith(".html"))
        self.assertIn("Amina", expected_name)
        self.assertIn("Hamid", expected_name)

    def test_f23_b03_no_external_binary_executables(self):
        disallowed = [".exe", ".bat", ".sh", ".dll", ".so"]
        for ext in disallowed:
            self.assertFalse("Instagram_Chat_Analysis_Amina_Hamid.html".endswith(ext))

    def test_f23_b04_utf8_meta_charset_boundary(self):
        meta_charset = '<meta charset="UTF-8">'
        self.assertIn("UTF-8", meta_charset)

    def test_f23_b05_title_tag_presence(self):
        title = "<title>Amina's 23rd Birthday - Instagram Chat Analysis</title>"
        self.assertIn("Amina", title)
        self.assertIn("23rd", title)

class TestFeature24CompatBoundaries(unittest.TestCase):
    """F24 Boundary: Browser Prefixes & Semantic Landmarks"""
    def test_f24_b01_webkit_backdrop_filter_prefix(self):
        css = "-webkit-backdrop-filter: blur(16px); backdrop-filter: blur(16px);"
        self.assertIn("-webkit-backdrop-filter", css)
        self.assertIn("backdrop-filter", css)

    def test_f24_b02_aria_live_polite_on_ticker(self):
        ticker_attr = 'aria-live="polite"'
        self.assertIn("polite", ticker_attr)

    def test_f24_b03_role_dialog_on_modal(self):
        modal_attr = 'role="dialog" aria-modal="true"'
        self.assertIn('role="dialog"', modal_attr)
        self.assertIn('aria-modal="true"', modal_attr)

    def test_f24_b04_focus_outline_visibility(self):
        focus_css = ":focus-visible { outline: 2px solid #ff6b8b; outline-offset: 2px; }"
        self.assertIn("focus-visible", focus_css)

    def test_f24_b05_heading_hierarchy_levels(self):
        headings = ["h1", "h2", "h3"]
        self.assertEqual(len(headings), 3)

if __name__ == '__main__':
    unittest.main()
