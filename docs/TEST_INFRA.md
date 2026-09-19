# Test Infrastructure & Specification Document

## 1. Test Philosophy & Principles

The E2E test infrastructure for Amina's 23rd Birthday Gift Web Application (Instagram_Chat_Analysis_Amina_Hamid.html) is built on strict, opaque-box, requirement-driven verification principles:

1. **Requirement-Driven & Opaque-Box**:
   Tests are authored strictly against the authoritative requirements specified in ORIGINAL_REQUEST.md and PROJECT.md. Tests treat the application as a black box, validating state transitions, calendar arithmetic, live counter algorithms, data analytics integrity, user interaction flows, and DOM/styling contracts.
2. **Authoritative Expected Output Derivation**:
   Every test derives its expected output from documented mathematical formulas, empirical chat data extracted from minachamadiya_1492033579358491.zip, and explicit milestones established in PROJECT.md. No test relies on arbitrary hardcoded guesses.
3. **Zero-Facade Policy**:
   No test is allowed to pass trivially. Every test executes real functional logic, evaluates state assertions, verifies mathematical invariants, and checks error handling.
4. **Progressive Testability & Dual Verification**:
   The test harness features a decoupled reference oracle (	ests/spec_oracle.py) and a physical asset/HTML inspector (Instagram_Chat_Analysis_Amina_Hamid.html and images/). The test runner verifies the comprehensive requirement specification across all 4 tiers, while providing milestone gating (--milestone M1..M4) and HTML integration audit matrix for active milestone workers.
5. **Adversarial & Boundary Hardening**:
   Extensive boundary testing covers extreme time offsets, clock drift, future milestone timestamps, empty data structures, missing photo assets, rapid click debouncing, small viewport constraints (iPhone SE/14), and zero-version string regex purging.

---

## 2. Feature Inventory Coverage Mapping

The application encompasses 24 core features mapped across milestones M1 to M4:

| Feature # | Feature Name | Milestone | Tier 1 Tests | Tier 2 Tests | Tier 3 Tests | Tier 4 Tests | Total Coverage |
|---|---|---|---|---|---|---|---|
| F1 | Interactive Gift-Box Opening Screen | M1 | T1_F01_1..5 | T2_F01_1..5 | Included | Included | >=10 tests |
| F2 | Celebration Confetti Blast | M1 | T1_F02_1..5 | T2_F02_1..5 | Included | Included | >=10 tests |
| F3 | Ambient 23rd Birthday Greeting | M1 | T1_F03_1..5 | T2_F03_1..5 | Included | Included | >=10 tests |
| F4 | Hamid's Heartfelt Love Letter | M1 | T1_F04_1..5 | T2_F04_1..5 | Included | Included | >=10 tests |
| F5 | Love Letter Re-read Access | M1 | T1_F05_1..5 | T2_F05_1..5 | Included | Included | >=10 tests |
| F6 | 6 Chronological Relationship Milestones | M2 | T1_F06_1..5 | T2_F06_1..5 | Included | Included | >=10 tests |
| F7 | Static 23rd Birthday Elapsed Time | M2 | T1_F07_1..5 | T2_F07_1..5 | Included | Included | >=10 tests |
| F8 | Dynamic Real-Time Live Tickers | M2 | T1_F08_1..5 | T2_F08_1..5 | Included | Included | >=10 tests |
| F9 | Polaroid Photo Memories Carousel/Grid | M2 | T1_F09_1..5 | T2_F09_1..5 | Included | Included | >=10 tests |
| F10 | images/ Directory & File Structure | M2 | T1_F10_1..5 | T2_F10_1..5 | Included | Included | >=10 tests |
| F11 | Dual-Layer Image Fallback System | M2 | T1_F11_1..5 | T2_F11_1..5 | Included | Included | >=10 tests |
| F12 | Longest Conversation Silence Card | M3 | T1_F12_1..5 | T2_F12_1..5 | Included | Included | >=10 tests |
| F13 | Pre-Nikah vs Post-Nikah Narrative | M3 | T1_F13_1..5 | T2_F13_1..5 | Included | Included | >=10 tests |
| F14 | Sweet Words & Affection Counter | M3 | T1_F14_1..5 | T2_F14_1..5 | Included | Included | >=10 tests |
| F15 | Midnight Heart-to-Hearts Showcase | M3 | T1_F15_1..5 | T2_F15_1..5 | Included | Included | >=10 tests |
| F16 | Milestone-Day Chat Spikes & Peak Days | M3 | T1_F16_1..5 | T2_F16_1..5 | Included | Included | >=10 tests |
| F17 | Reaction Queen Feature | M3 | T1_F17_1..5 | T2_F17_1..5 | Included | Included | >=10 tests |
| F18 | 100% Unbroken 57-Day Streak Badge | M3 | T1_F18_1..5 | T2_F18_1..5 | Included | Included | >=10 tests |
| F19 | 5-Question 'Our Love Trivia' Quiz | M4 | T1_F19_1..5 | T2_F19_1..5 | Included | Included | >=10 tests |
| F20 | Instant Quiz Feedback & Mini-Confetti | M4 | T1_F20_1..5 | T2_F20_1..5 | Included | Included | >=10 tests |
| F21 | 100% Soulmate Compatibility Card | M4 | T1_F21_1..5 | T2_F21_1..5 | Included | Included | >=10 tests |
| F22 | Zero-Version & Zero-Technical Purge | M4 | T1_F22_1..5 | T2_F22_1..5 | Included | Included | >=10 tests |
| F23 | Cross-Platform Responsive Polish | M4 | T1_F23_1..5 | T2_F23_1..5 | Included | Included | >=10 tests |
| F24 | Complete Offline & Static Readiness | M4 | T1_F24_1..5 | T2_F24_1..5 | Included | Included | >=10 tests |

---

## 3. Test Architecture & Tier Structure

`
tests/
|-- spec_oracle.py              # Reference Specification Oracle & Mathematical Models
|-- test_tier1_features.py      # Tier 1: Feature Coverage (120 tests: 24 features x 5 tests)
|-- test_tier2_boundaries.py    # Tier 2: Boundary & Corner Cases (120 tests: 24 features x 5 tests)
|-- test_tier3_combinations.py  # Tier 3: Cross-Feature Pairwise Interactions (16 tests)
|-- test_tier4_scenarios.py     # Tier 4: Real-World E2E User Scenarios (24 tests)
-- run_tests.py                # Automated Test Runner & HTML Integration Scanner
`

### Tier Breakdown & Minimum Threshold Formula
According to project test guidelines, the required minimum test count is:
Min Tests = 11 * N + max(5, floor(N / 2))
With N = 24:
Min Tests = 11 * 24 + max(5, 12) = 264 + 12 = 276 tests

Our test suite implements **280 tests**:
- **Tier 1 (Feature Coverage)**: **120 tests** (5 tests per feature for all 24 features).
- **Tier 2 (Boundary & Corner Cases)**: **120 tests** (5 edge/boundary tests per feature for all 24 features).
- **Tier 3 (Cross-Feature Combinations)**: **16 tests** (Pairwise chapter transitions, multi-state navigation, modal interruptions, concurrent confetti triggers).
- **Tier 4 (Real-World Scenarios)**: **24 tests** (Mobile walkthrough, desktop walkthrough, offline gift opening, static CDN deployment, missing images fallback, trivia journey to 100% Soulmate card, midnight re-reading).

---

## 4. Test Execution Commands

### Running All Tests
To execute the complete 4-tier test suite (280 tests):
`powershell
python tests/run_tests.py
`

### Running Specific Tiers
To isolate execution to an individual tier:
`powershell
python tests/run_tests.py --tier 1     # Tier 1 only (120 tests)
python tests/run_tests.py --tier 2     # Tier 2 only (120 tests)
python tests/run_tests.py --tier 3     # Tier 3 only (16 tests)
python tests/run_tests.py --tier 4     # Tier 4 only (24 tests)
`

### Milestone-Filtered Testing
To test features mapped to a specific milestone:
`powershell
python tests/run_tests.py --milestone M1   # Milestone 1 tests
python tests/run_tests.py --milestone M2   # Milestone 2 tests
python tests/run_tests.py --milestone M3   # Milestone 3 tests
python tests/run_tests.py --milestone M4   # Milestone 4 tests
`

### Verbose Output
`powershell
python tests/run_tests.py -v
`

### Standard Python Unittest Execution
The test files are completely compatible with the standard library unittest runner:
`powershell
python -m unittest discover -s tests -p  test_*.py
`

---

## 5. Verification & Exit Code Conventions

- **Exit Code 0**: All executed test assertions passed successfully.
- **Exit Code 1**: One or more assertions failed or unhandled exception occurred.
- **Reporting Output**: Formatted console output detailing test counts per tier, pass/fail totals, execution duration, and an HTML Integration Audit status matrix.
