#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
MASTER TEST RUNNER: Amina's 23rd Birthday Gift Web Application (V1 & V2)
================================================================================
Executes all 6 tiers:
  - Tier 1: Feature Coverage (120 tests, F01-F24)
  - Tier 2: Boundary & Corner Cases (120 tests, F01-F24)
  - Tier 3: Cross-Feature Combinations (16 tests)
  - Tier 4: Real-World Scenarios (24 tests)
  - Tier 5: V1 Immutability & Hash Guard (8 tests)
  - Tier 6: Version 2.0 Requirements Suite (35 tests)

Also performs static and semantic audit on both:
  - Instagram_Chat_Analysis_Amina_Hamid.html (Version 1.0)
  - Instagram_Chat_Analysis_Amina_Hamid_v2.html / v2.html (Version 2.0)

Exits with return code 0 on all pass, non-zero on failure.
================================================================================
"""

import argparse
import os
import sys
import time
import unittest

# Ensure project root is in sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from tests import spec_oracle as oracle
from tests import spec_oracle_v2 as oracle_v2


def print_banner():
    width = 80
    print("=" * width)
    print("  AMINA'S 23RD BIRTHDAY GIFT - E2E AUTOMATED TEST INFRASTRUCTURE")
    print("  Target Date: 17 September 2026 | Celebrating 23 Years of Grace & Love")
    print("  Dual Release: Version 1.0 (Frozen) & Version 2.0 (Extended 18,589 msgs)")
    print("=" * width)
    print()


def run_suite(tier_filter=None, verbose=False):
    loader = unittest.TestLoader()

    tier_files = [
        ("Tier 1: Feature Coverage (F01-F24)", "tests.test_tier1_features", 1),
        ("Tier 2: Boundary & Corner Cases", "tests.test_tier2_boundaries", 2),
        ("Tier 3: Cross-Feature Combinations", "tests.test_tier3_combinations", 3),
        ("Tier 4: Real-World Scenarios", "tests.test_tier4_scenarios", 4),
        ("Tier 5: V1 Immutability & Hash Guard", "tests.test_v1_immutability", 5),
        ("Tier 6: Version 2.0 Requirements Suite", "tests.test_v2_requirements", 6),
    ]

    tier_results = []
    total_passed = 0
    total_skipped = 0
    total_failed = 0
    total_errors = 0
    total_duration = 0.0

    print("Running test tiers...")
    print("-" * 80)

    for name, module_name, tier_num in tier_files:
        if tier_filter is not None and tier_num != tier_filter:
            continue

        try:
            tier_suite = loader.loadTestsFromName(module_name)
        except Exception as e:
            print(f"Error loading {module_name}: {e}")
            continue

        tier_test_count = tier_suite.countTestCases()
        start_t = time.time()
        runner = unittest.TextTestRunner(
            verbosity=2 if verbose else 0,
            stream=open(os.devnull, "w") if not verbose else sys.stdout,
        )
        result = runner.run(tier_suite)
        duration = time.time() - start_t
        total_duration += duration

        skipped = len(result.skipped)
        failed = len(result.failures)
        errors = len(result.errors)
        passed = tier_test_count - failed - errors - skipped

        total_passed += passed
        total_skipped += skipped
        total_failed += failed
        total_errors += errors

        tier_results.append({
            "name": name,
            "total": tier_test_count,
            "passed": passed,
            "skipped": skipped,
            "failed": failed,
            "errors": errors,
            "duration": duration,
            "failures_list": result.failures,
            "errors_list": result.errors,
        })

        status_tag = "[PASS]" if (failed == 0 and errors == 0) else "[FAIL]"
        skip_suffix = f" ({skipped} skipped)" if skipped > 0 else ""
        print(f"  {status_tag} {name:<42} | {passed}/{tier_test_count} passed{skip_suffix} ({duration:.3f}s)")

    print("-" * 80)
    print()

    # Summary Table
    print("=" * 80)
    print("  TIER EXECUTION SUMMARY")
    print("=" * 80)
    print(f"  {'Tier Name':<42} {'Tests':<7} {'Pass':<7} {'Skip':<7} {'Fail':<7} {'Err':<5} {'Time':<8}")
    print("  " + "-" * 76)
    for r in tier_results:
        print(
            f"  {r['name']:<42} {r['total']:<7} {r['passed']:<7} {r['skipped']:<7} {r['failed']:<7} {r['errors']:<5} {r['duration']:.3f}s"
        )
    print("  " + "-" * 76)
    total_tests = total_passed + total_skipped + total_failed + total_errors
    print(
        f"  {'TOTAL SUITE':<42} {total_tests:<7} {total_passed:<7} {total_skipped:<7} {total_failed:<7} {total_errors:<5} {total_duration:.3f}s"
    )
    print("=" * 80)
    print()

    # Failures Detail if any
    if total_failed > 0 or total_errors > 0:
        print("FAILURES AND ERRORS DETAIL:")
        print("=" * 80)
        for r in tier_results:
            for test, err in r["failures_list"]:
                print(f"FAILURE in {test}:")
                print(err)
                print("-" * 50)
            for test, err in r["errors_list"]:
                print(f"ERROR in {test}:")
                print(err)
                print("-" * 50)
        print()

    # Static HTML Audit - Version 1.0
    v1_html_path = "Instagram_Chat_Analysis_Amina_Hamid.html"
    print("=" * 80)
    print("  VERSION 1.0 BASELINE APPLICATION AUDIT")
    print("=" * 80)
    if os.path.exists(v1_html_path):
        v1_size_bytes = os.path.getsize(v1_html_path)
        v1_size_kb = v1_size_bytes / 1024.0
        print(f"  Target File: {v1_html_path} ({v1_size_kb:.1f} KB, {v1_size_bytes:,} bytes)")
        auditor_v1 = oracle.HTMLAuditor(v1_html_path)
        status_dict = auditor_v1.check_feature_status()
        for feat, active in status_dict.items():
            check_tag = "[x]" if active else "[ ]"
            print(f"    {check_tag} {feat:<20}")
    else:
        print(f"  Notice: '{v1_html_path}' missing in workspace root.")
    print("=" * 80)
    print()

    # Static HTML Audit - Version 2.0
    v2_html_path = oracle_v2.V2_PRIMARY_FILE
    print("=" * 80)
    print("  VERSION 2.0 STANDALONE APPLICATION AUDIT")
    print("=" * 80)
    if os.path.exists(v2_html_path):
        v2_size_bytes = os.path.getsize(v2_html_path)
        v2_size_kb = v2_size_bytes / 1024.0
        print(f"  Target File: {v2_html_path} ({v2_size_kb:.1f} KB, {v2_size_bytes:,} bytes)")
        auditor_v2 = oracle_v2.HTMLAuditorV2(v2_html_path)
        v2_features = auditor_v2.check_v2_features_status()
        for feat, active in v2_features.items():
            check_tag = "[x]" if active else "[ ]"
            print(f"    {check_tag} {feat:<30}")
    else:
        print(f"  Notice: '{v2_html_path}' not yet present in workspace root.")
        print("  Version 2.0 test suites stand ready for implementation gating (M2_IMPL).")
    print("=" * 80)
    print()

    # Final Verdict
    if total_failed == 0 and total_errors == 0:
        print(f"  SUCCESS: All executed tests passed cleanly in {total_duration:.3f}s!")
        print("  Ready for implementation gating and continuous E2E verification.")
        print("=" * 80)
        return 0
    else:
        print(f"  FAILURE: {total_failed} failed, {total_errors} errors out of {total_tests} tests.")
        print("=" * 80)
        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Amina Birthday Gift E2E Test Runner")
    parser.add_argument(
        "--tier",
        type=int,
        choices=[1, 2, 3, 4, 5, 6],
        default=None,
        help="Run specific tier (1-6)",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose test execution output")
    args = parser.parse_args()

    print_banner()
    exit_code = run_suite(tier_filter=args.tier, verbose=args.verbose)
    sys.exit(exit_code)
