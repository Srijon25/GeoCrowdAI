import unittest
from geocrowdai.processor import GeoTextProcessor
from geocrowdai.geoextractor import GeoEntityExtractor
from geocrowdai.visualizer import MapVisualizer

class TestGeoCrowdAI(unittest.TestCase):

    def setUp(self):
        self.sample_texts = [
            "Earthquake reported near San Francisco, stay safe!",
            "Flooding in Dhaka after heavy rain.",
            "Forest fire spreading outside Melbourne."
        ]
        self.keywords = ["earthquake", "flood", "fire"]
        self.processor = GeoTextProcessor(self.keywords)
        self.extractor = GeoEntityExtractor()
        self.visualizer = MapVisualizer()

    def test_keyword_filtering(self):
        filtered = self.processor.filter_by_keywords(self.sample_texts)
        self.assertEqual(len(filtered), 3)
        self.assertTrue(any("earthquake" in text.lower() for text in filtered))

    def test_location_extraction(self):
        locations = [self.extractor.extract_location(text) for text in self.sample_texts]
        self.assertTrue(any(loc is not None for loc in locations))
        self.assertIn("San Francisco", str(locations[0]))

    def test_map_creation(self):
        locations = [
            {"text": "Earthquake in San Francisco", "lat": 37.7749, "lon": -122.4194},
            {"text": "Flooding in Dhaka", "lat": 23.8103, "lon": 90.4125}
        ]
        map_file = self.visualizer.plot_locations(locations, output_file="test_map.html")
        self.assertTrue(map_file.endswith(".html"))

if __name__ == '__main__':
    unittest.main()
