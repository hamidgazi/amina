"""
================================================================================
VERSION 1.0 IMMUTABILITY & INTEGRITY TEST SUITE
================================================================================
Strict, bit-level tests asserting that Version 1.0 files:
  - Instagram_Chat_Analysis_Amina_Hamid.html
  - index.html
retain exact file size 270,487 bytes and SHA-256:
  4314E596BA3AC3B0D573DAF7845A08698033A006B63A6AA66ADD137901142D21.

Guarantees Version 1.0 is 100% frozen, untouched, and uncorrupted.
================================================================================
"""

import hashlib
import os
import unittest
from tests import spec_oracle_v2 as oracle_v2


class TestV1Immutability(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.v1_primary_path = os.path.join(cls.project_root, oracle_v2.V1_PRIMARY_FILE)
        cls.v1_replica_path = os.path.join(cls.project_root, oracle_v2.V1_REPLICA_FILE)

    def _compute_sha256(self, file_path: str) -> str:
        self.assertTrue(os.path.exists(file_path), f"File missing: {file_path}")
        h = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                h.update(chunk)
        return h.hexdigest().upper()

    def test_v1_primary_file_exists(self):
        """Verify Instagram_Chat_Analysis_Amina_Hamid.html exists in project root."""
        self.assertTrue(
            os.path.isfile(self.v1_primary_path),
            f"V1 primary file not found at {self.v1_primary_path}"
        )

    def test_v1_replica_file_exists(self):
        """Verify index.html exists in project root."""
        self.assertTrue(
            os.path.isfile(self.v1_replica_path),
            f"V1 replica file not found at {self.v1_replica_path}"
        )

    def test_v1_primary_file_exact_size(self):
        """Verify Instagram_Chat_Analysis_Amina_Hamid.html is exactly 270,487 bytes."""
        actual_size = os.path.getsize(self.v1_primary_path)
        self.assertEqual(
            actual_size,
            oracle_v2.V1_EXPECTED_SIZE,
            f"V1 primary size modified! Expected {oracle_v2.V1_EXPECTED_SIZE} bytes, got {actual_size} bytes"
        )

    def test_v1_replica_file_exact_size(self):
        """Verify index.html is exactly 270,487 bytes."""
        actual_size = os.path.getsize(self.v1_replica_path)
        self.assertEqual(
            actual_size,
            oracle_v2.V1_EXPECTED_SIZE,
            f"V1 replica size modified! Expected {oracle_v2.V1_EXPECTED_SIZE} bytes, got {actual_size} bytes"
        )

    def test_v1_primary_sha256_hash(self):
        """Verify Instagram_Chat_Analysis_Amina_Hamid.html SHA-256 hash matches authoritative baseline."""
        actual_hash = self._compute_sha256(self.v1_primary_path)
        self.assertEqual(
            actual_hash,
            oracle_v2.V1_EXPECTED_SHA256,
            f"V1 primary hash corrupted! Expected {oracle_v2.V1_EXPECTED_SHA256}, got {actual_hash}"
        )

    def test_v1_replica_sha256_hash(self):
        """Verify index.html SHA-256 hash matches authoritative baseline."""
        actual_hash = self._compute_sha256(self.v1_replica_path)
        self.assertEqual(
            actual_hash,
            oracle_v2.V1_EXPECTED_SHA256,
            f"V1 replica hash corrupted! Expected {oracle_v2.V1_EXPECTED_SHA256}, got {actual_hash}"
        )

    def test_v1_files_byte_for_byte_identical(self):
        """Verify Instagram_Chat_Analysis_Amina_Hamid.html and index.html are 100% bitwise identical."""
        with open(self.v1_primary_path, "rb") as f1, open(self.v1_replica_path, "rb") as f2:
            chunk1 = f1.read()
            chunk2 = f2.read()
        self.assertEqual(len(chunk1), len(chunk2), "File sizes differ between primary and replica")
        self.assertEqual(chunk1, chunk2, "Byte contents differ between V1 primary and replica files")

    def test_v1_preserves_v1_chat_baseline_content(self):
        """Verify V1 content still reflects the 12,980 baseline messages and is not contaminated with V2 data."""
        with open(self.v1_primary_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # V1 baseline markers
        self.assertIn('"total_messages": 12980', content, "V1 must contain original 12,980 message count in CHAT constant")
        self.assertIn('"total_days": 57', content, "V1 must contain original 57 total days in CHAT constant")
        self.assertIn('"end_date": "Aug 31, 2026"', content, "V1 must have Aug 31, 2026 end date in CHAT constant")
        # Must not contain V2 message count
        self.assertNotIn("18,589", content, "V1 must not contain formatted V2 message count")
        self.assertNotIn("18589", content, "V1 must not contain raw V2 message count")


if __name__ == "__main__":
    unittest.main()
