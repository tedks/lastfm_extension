"""Exercise the actual whitelist without loading Rhythmbox or API keys."""

from pathlib import Path
import unittest

from lastfmextension_genres import genre_from_tags


class GenreMatcherTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = Path(__file__).absolute().parent.parent / "genres.txt"
        cls.whitelist = {
            line.strip().lower()
            for line in source.read_text(encoding="utf-8").splitlines()
            if line.strip()
        }

    def test_first_matching_tag_wins_case_insensitively(self):
        self.assertIn("jazz", self.whitelist)
        self.assertIn("rock", self.whitelist)
        self.assertEqual(genre_from_tags(["unknown", "jAZZ", "ROCK"], self.whitelist), "Jazz")

    def test_no_match_returns_none(self):
        self.assertIsNone(genre_from_tags(["not-a-genre"], self.whitelist))

    def test_empty_tags_returns_none(self):
        self.assertIsNone(genre_from_tags([], self.whitelist))

    def test_title_case_and_no_whitespace_trimming_match_legacy_behavior(self):
        self.assertEqual(genre_from_tags(["hip hop"], {"hip hop"}), "Hip Hop")
        self.assertIsNone(genre_from_tags([" jazz "], self.whitelist))


if __name__ == "__main__":
    unittest.main()
