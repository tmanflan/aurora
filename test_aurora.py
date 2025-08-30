import unittest
from aurora import Aurora

class TestAurora(unittest.TestCase):
    def setUp(self):
        self.aurora = Aurora()

    def test_fizzbuzz_generation(self):
        prompt = "Write a Python function for FizzBuzz."
        code = self.aurora.generate_code(prompt)
        # Check if the code contains the function
        self.assertIn("def fizzbuzz", code)
        self.assertIn("FizzBuzz", code)

    def test_security_audit(self):
        safe_code = "print('Hello')"
        self.assertEqual(self.aurora.security_auditor.audit(safe_code), "No security issues found.")
        unsafe_code = "eval('print(1)')"
        self.assertIn("Security warning", self.aurora.security_auditor.audit(unsafe_code))

    def test_optimizer_suggestion(self):
        code_with_print = "print('test')"
        self.assertIn("Suggestion", self.aurora.optimizer.optimize(code_with_print))
        optimized_code = "return 'test'"
        self.assertEqual(self.aurora.optimizer.optimize(optimized_code), "Code looks optimized.")

if __name__ == "__main__":
    unittest.main()