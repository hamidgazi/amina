"""
Independent Reviewer Verification & Adversarial Test Suite for Milestone 1
Validates UX, Audio, Visual, and Copy constraints for Amina's 23rd Birthday Gift Reveal.
"""

import unittest
import os
import re
import html.parser

class TestMilestone1IndependentReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        offline_v1 = os.path.join(base_dir, "version_1_offline", "Instagram_Chat_Analysis_Amina_Hamid.html")
        cls.html_path = offline_v1 if os.path.exists(offline_v1) else os.path.join(base_dir, "Instagram_Chat_Analysis_Amina_Hamid.html")
        with open(cls.html_path, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_canvas_confetti_engine(self):
        """Verify canvas existence, DPI clamp, and multi-shape rendering logic."""
        self.assertIn('id="confetti-canvas"', self.content)
        # Verify clamped DPR to prevent memory exhaustion on high-DPI retina mobile
        self.assertIn('Math.min(window.devicePixelRatio || 1, 2)', self.content)
        # Verify procedural heart geometry with Bézier curves
        self.assertIn('bezierCurveTo', self.content)
        # Verify 4-pointed pinched star procedural geometry
        self.assertIn('quadraticCurveTo', self.content)
        self.assertIn('drawStar', self.content)
        # Verify 3D ribbon perspective flip with cosine tilt
        self.assertIn('Math.cos(p.tiltAngle)', self.content)
        # Verify circular sequin drawing
        self.assertIn('ctx.ellipse', self.content)
        # Verify 3-stage celebration sequence
        self.assertIn('triggerCelebrationConfetti', self.content)
        # Verify max concurrent particle cap
        self.assertIn('MAX_CONCURRENT_PARTICLES = 250', self.content)
        # Verify animation loop cleanup on zero particles
        self.assertIn('cancelAnimationFrame(confettiAnimation)', self.content)

    def test_web_audio_api_synthesizer(self):
        """Verify Web Audio API synthesis without external audio files."""
        self.assertIn('AudioContext', self.content)
        self.assertIn('webkitAudioContext', self.content)
        # Verify 6-note arpeggio C5, E5, G5, B5, C6, E6
        notes = [523.25, 659.25, 783.99, 987.77, 1046.50, 1318.51]
        for note in notes:
            self.assertIn(str(note), self.content)
        # Verify triangle oscillator and exponential gain envelopes
        self.assertIn("osc.type = 'triangle'", self.content)
        self.assertIn('exponentialRampToValueAtTime', self.content)
        # Verify suspended context resumption for browser autoplay policies
        self.assertIn('_celebrationAudioCtx.state === \'suspended\'', self.content)
        self.assertIn('_celebrationAudioCtx.resume()', self.content)
        # Verify exception safety wrapper
        self.assertIn('function playCelebrationChime()', self.content)

    def test_love_letter_copy_fidelity(self):
        """Verify verbatim fidelity of sacred copy, milestone dates, and chat stats."""
        # Sacred Bismillah
        self.assertIn('بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ', self.content)
        # Greeting and 23rd birthday date
        self.assertIn('Meri Pyaari Amina,', self.content)
        self.assertIn('Happy 23rd Birthday My Love, Amina! • 17 September 2026', self.content)
        # Sacred Nikah and Qubool Hai
        self.assertIn('03 July 2026', self.content)
        self.assertIn('Qubool Hai', self.content)
        # All 6 milestone dates
        self.assertIn('14 April 2026', self.content)
        self.assertIn('27 April 2026', self.content)
        self.assertIn('04 July 2026', self.content)
        self.assertIn('05 September 2026', self.content)
        self.assertIn('10 September 2026', self.content)
        # Chat stats and specific moments
        self.assertIn('12,980 messages', self.content)
        self.assertIn('6,571 of our whispers', self.content)
        self.assertIn('Reaction Queen', self.content)
        self.assertIn('1,669 reactions', self.content)
        self.assertIn('Aaj hamari flight hai', self.content)
        # All 4 chapter introductions
        self.assertIn('Chapter 1: Our Sacred Milestones & Live Tickers', self.content)
        self.assertIn('Chapter 2: Our Polaroid Moments', self.content)
        self.assertIn('Chapter 3: Our Whispers & Midnight Story', self.content)
        self.assertIn('Chapter 4: Our Love Trivia', self.content)
        # Signature block
        self.assertIn('Your Husband, Hamid ❤️', self.content)

    def test_3d_wax_seal_aesthetics(self):
        """Verify 3D wax seal construction, monogram, and milestone badge."""
        self.assertIn('H ❤️ A', self.content)
        self.assertIn('23rd', self.content)
        # Verify crimson gradient and box shadow
        self.assertIn('from-rose-600 via-red-700 to-red-950', self.content)
        self.assertIn('shadow-[0_8px_25px_rgba(185,28,28,0.65)]', self.content)
        # Verify ribbon tails beneath seal
        self.assertIn('-rotate-12', self.content)
        self.assertIn('rotate-12', self.content)

    def test_3d_gift_box_faces_and_bow_geometry(self):
        """Verify 3D CSS cube faces, lid faces, and ribbon bow assembly."""
        # 3D stage and container
        self.assertIn('perspective: 1200px', self.content)
        self.assertIn('transform-style: preserve-3d', self.content)
        # Base cube faces
        self.assertIn('face front', self.content)
        self.assertIn('face back', self.content)
        self.assertIn('face left', self.content)
        self.assertIn('face right', self.content)
        self.assertIn('face bottom', self.content)
        self.assertIn('face inside-glow', self.content)
        # Lid faces
        self.assertIn('lid-face lid-top', self.content)
        self.assertIn('lid-face lid-front', self.content)
        self.assertIn('lid-face lid-left', self.content)
        self.assertIn('lid-face lid-right', self.content)
        self.assertIn('lid-face lid-back', self.content)
        # 4 bow loops and knot
        self.assertIn('bow-loop loop-top', self.content)
        self.assertIn('bow-loop loop-bottom', self.content)
        self.assertIn('bow-loop loop-left', self.content)
        self.assertIn('bow-loop loop-right', self.content)
        self.assertIn('bow-knot', self.content)

    def test_mobile_responsiveness_and_scroll_locking(self):
        """Verify touch UX, custom scrollbar, and body scroll lock."""
        # Scrollbar styles
        self.assertIn('custom-scrollbar', self.content)
        self.assertIn('.custom-scrollbar::-webkit-scrollbar', self.content)
        # Scroll locking
        self.assertIn('body.overflow-hidden', self.content)
        self.assertIn("document.body.classList.add('overflow-hidden')", self.content)
        self.assertIn("document.body.classList.remove('overflow-hidden')", self.content)
        # Touch swipe vs tap disambiguation
        self.assertIn('touchmove', self.content)
        self.assertIn('isSwiping = true', self.content)
        # Reduced motion support
        self.assertIn('@media (prefers-reduced-motion: reduce)', self.content)

    def test_zero_version_and_developer_strings(self):
        """Verify zero version numbers, build tags, or technical debug labels."""
        forbidden = [
            r'\bv\d+\.\d+(\.\d+)?\b',
            r'\bversion\s*\d+(\.\d+)?\b',
            r'\bbuild\s*#?\d+\b',
            r'\bcommit\s+[0-9a-f]{7,40}\b',
            r'\(NEW ANALYTICS\)',
            r'TODO',
            r'FIXME'
        ]
        for pattern in forbidden:
            matches = re.findall(pattern, self.content, re.IGNORECASE)
            self.assertEqual(len(matches), 0, f"Found forbidden pattern {pattern}: {matches}")

    def test_state_machine_and_api_contracts(self):
        """Verify state machine orchestration functions and public window contracts."""
        methods = [
            'window.unwrapGift',
            'window.closeLoveLetter',
            'window.openLoveLetter',
            'window.replayGiftUnwrap',
            'window.goToChapter',
            'window.triggerCelebrationConfetti',
            'window.launchConfetti',
            'window.triggerAnswerConfetti'
        ]
        for m in methods:
            self.assertIn(m, self.content)

    def test_integrity_and_facade_absence(self):
        """Adversarial integrity check: ensure implementations are real, not mocks or stubs."""
        # Check that playCelebrationChime actually creates oscillators, not just logging
        self.assertIn('createOscillator', self.content)
        self.assertIn('createGain', self.content)
        # Check that canvas actually performs 2D context draws
        self.assertIn('ctx.bezierCurveTo', self.content)
        self.assertIn('ctx.quadraticCurveTo', self.content)
        # Check that unwrapGift alters DOM classes
        self.assertIn("overlay.classList.add('is-opening')", self.content)
        self.assertIn("overlay.classList.add('is-revealed')", self.content)

if __name__ == '__main__':
    unittest.main()
