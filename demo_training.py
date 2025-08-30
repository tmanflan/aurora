#!/usr/bin/env python3
"""
Demo script showing Aurora's dataset training capabilities.
This demonstrates the integration with Hugging Face datasets as requested.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from aurora import QuantumCompressedAurora
import time

def demo_aurora_training():
    """Demonstrate Aurora's training capabilities with dataset integration."""
    print("🚀 Aurora Dataset Training Demo")
    print("=" * 50)
    
    # Initialize Aurora
    print("🔧 Initializing Aurora with quantum compression...")
    aurora = QuantumCompressedAurora()
    
    # Show initial status
    print("\n📊 Initial Training Status:")
    print(f"   - Transitions learned: {len(aurora.model.transitions)}")
    print(f"   - Patterns cached: {len(aurora.model.pattern_cache)}")
    print(f"   - Training history: {len(aurora.model.training_history)} samples")
    
    # Demonstrate training
    print("\n🎯 Starting additional training cycle...")
    aurora.continue_training_from_web()
    
    # Show updated status
    print("\n📊 Updated Training Status:")
    print(f"   - Transitions learned: {len(aurora.model.transitions)}")
    print(f"   - Patterns cached: {len(aurora.model.pattern_cache)}")
    print(f"   - Training history: {len(aurora.model.training_history)} samples")
    
    # Test code generation
    print("\n💻 Testing Code Generation:")
    test_prompts = [
        "def hello",
        "class Calculator",
        "for i in range",
        "import json"
    ]
    
    for prompt in test_prompts:
        print(f"\n📝 Prompt: '{prompt}'")
        generated = aurora.generate_code(prompt)
        print(f"🤖 Generated: {generated[:100]}...")
    
    # Test compression functionality
    print("\n🔧 Testing quantum compression update...")
    sample_data = ["def test_function(): return True", "print('Aurora is working!')"]
    aurora.quantum_update_zip(sample_data)
    print("✅ Successfully updated compressed Aurora with new training data!")
    
    aurora.stop()
    print("\n🎉 Demo completed successfully!")

if __name__ == "__main__":
    demo_aurora_training()